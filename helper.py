# نسخه جدید دیباگ : 3
# صفر تا صد توسط @U3erZX دیباگ شده 
# اگه ننت خراب نیست اسکی میری منبع بزن
from pyrogram import Client, filters, idle, errors
from pyrogram.types import *
from pyrogram.raw import functions, base, types
from colorama import Fore
import requests
import pymysql
import json
import sys
import os
#================= Config =================#
owner = 6508600903 # ایدی عددی مالک سلف ساز
api_id = 29042268 # ایپی ایدی مالک سلف ساز 
api_hash = "54a7b377dd4a04a58108639febe2f443" # ایپی هش مالک سلف ساز
bot_token = "8156078217:AAE-iIBpwWBXE3XhyVy24uHduTB5CKNOXME" # توکن ربات هلپر 
DBName = "" # نام دیتابیس هلپر 
DBUser = "" # یوزر دیتابیس هلپر 
DBPass = "" # پسورد دیتابیس هلپر 
#==========================================#

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

update_data("""
CREATE TABLE IF NOT EXISTS user(
id bigint PRIMARY KEY,
step varchar(150) DEFAULT 'none'
) default charset=utf8mb4;
""")
update_data("""
CREATE TABLE IF NOT EXISTS ownerlist(
id bigint PRIMARY KEY
) default charset=utf8mb4;
""")
update_data("""
CREATE TABLE IF NOT EXISTS adminlist(
id bigint PRIMARY KEY
) default charset=utf8mb4;
""")

OwnerUser = get_data(f"SELECT * FROM ownerlist WHERE id = '{owner}' LIMIT 1")
if OwnerUser is None:
     update_data(f"INSERT INTO ownerlist(id) VALUES({owner})")

AdminUser = get_data(f"SELECT * FROM adminlist WHERE id = '{owner}' LIMIT 1")
if AdminUser is None:
     update_data(f"INSERT INTO adminlist(id) VALUES({owner})")

app = Client("Helper", api_id, api_hash, bot_token=bot_token)

@app.on_message(filters.private, group=-1)
async def update(c, m):
     OwnerUser = get_data(f"SELECT * FROM ownerlist WHERE id = '{m.chat.id}' LIMIT 1")
     AdminUser = get_data(f"SELECT * FROM adminlist WHERE id = '{m.chat.id}' LIMIT 1")
     if OwnerUser is not None or AdminUser is not None:
          user = get_data(f"SELECT * FROM user WHERE id = '{m.chat.id}' LIMIT 1")
          if user is None:
               update_data(f"INSERT INTO user(id) VALUES({m.chat.id})")
  
fahelp1 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ سراسری - شخصی ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
سکوت کاربر
➤ [ `.mute` ]
———————————————
حذف سکوت کاربر
➤ [ `.unmute` ]
———————————————
پاکسازی لیست سکوت
➤ [ `.allunmute` ]
———————————————
بلاک کاربر
➤ [ `.block` ]
———————————————
آنبلاک کاربر
➤ [ `.unblock` ]
———————————————
افزودن کاربر به لیست دشمنان
➤ [ `.setenemy` ]
———————————————
حذف کاربر از لیست دشمنان
➤ [ `.delenemy` ]
———————————————
پاکسازی لیست دشمنان
➤ [ `.clearenemy` ]
———————————————
افزودن کاربر به لیست عشق
➤ [ `.setlove` ]
———————————————
حذف کاربر از لیست عشق
➤ [ `.dellove` ]
———————————————
پاکسازی لیست عشق
➤ [ `.clearlove` ]
———————————————
تنظیم متن منشی خودکار
➤ [ `.monshi` ] **⤳** (TEXT)
———————————————
غیرفعال کردن منشی خودکار
➤ [ `.monshioff` ]
———————————————
تنظیم متن حالت آفلاینی
➤ [ `.afk` ] **⤳** (TEXT)
———————————————
غیرفعال کردن حالت آفلاینی
➤ [ `.unafk` ]
———————————————
دریافت هشدار تگ شدن
➤ [ `.tagalert` ] **⤳** (on OR off)
———————————————
ساخت کانال
➤ [ `.creatchannel` ] **⤳** (Name)
———————————————
ساخت گروه
➤ [ `.creatgroup` ] **⤳** (Name)
———————————————
ساخت سوپر گروه
➤ [ `.creatsupergroup` ] **⤳** (Name)
———————————————
اسپم متن معمولی
➤ [ `.spam` ] **⤳** (NUM TEXT)
———————————————
اسپم متن آرام
➤ [ `.slowspam` ] **⤳** (NUM TEXT)
———————————————
اسپم متن و حذف
➤ [ `.statspam` ] **⤳** (NUM TEXT)
———————————————
اسپم متن سریع
➤ [ `.fastspam` ] **⤳** (NUM TEXT)
———————————————
فعال کردن کامنت اول
➤ [ `.firstcom` ] **⤳** (on OR off)
———————————————
تنظیم متن کامنت اول
➤ [ `.first_message` ] **⤳** (TEXT) (Reply)
———————————————
تنظیم زمان ارسال خودکار متن
➤ [ `.text_time` ] **⤳** (HH:MM)
———————————————
تنظیم زمان ارسال خودکار عکس
➤ [ `.photo_time` ] **⤳** (HH:MM)
———————————————
تنظیم متن ارسال خودکار متن
➤ [ `.text_send_time` ] **⤳** (TEXT) (Reply)
———————————————
تنظیم عکس ارسال خودکار عکس
➤ [ `.photo_send_time` ] **⤳** (Reply)
———————————————
فعال یا غیرفعال کردن پاسخ خودکار
➤ [ `.answer` ] **⤳** (on OR off)
———————————————
تنظیم سوال جواب برای پاسخ خودکار
➤ [ `.addan` ] **⤳** (Question:Answer)
———————————————
حذف یک سوال جواب
➤ [ `.delan` ] **⤳** (Answer)
———————————————
مشاهده لیست سوال جواب ها
➤ [ `.anlist` ]
———————————————
پاکسازی لیست پاسخ خودکار
➤ [ `.anclear` ]
———————————————
فعال یا غیرفعال کردن حالت خوش آمد گویی
➤ [ `.welcome` ] **⤳** (on OR off)
———————————————
تنظیم متن خوش آمد گویی
➤ [ `.welcome_add` ] **⤳** (TEXT)
———————————————
نمایش متن خوش آمد گویی
➤ [ `.welcome_show` ]
———————————————
ریست متن خوش آمد گویی
➤ [ `.welcome_reset` ]
———————————————
**توجه! برای استفاده از دستورات زیر باید مالک یا ادمین گروه مورد نظر با دسترسی های لازم باشید**

بن کاربر در گروه
➤ [ `.ban` ] **⤳** (ID) (Reply)
———————————————
آنبن کاربر در گروه
➤ [ `.unban` ] **⤳** (ID) (Reply)
———————————————
سکوت کاربر در گروه
➤ [ `.setmute` ] **⤳** (ID) (Reply)
———————————————
حذف سکوت کاربر در گروه
➤ [ `.delmute` ] **⤳** (ID) (Reply)
———————————————
تنظیم عکس گروه
➤ [ `.setchatphoto` ] **⤳** (Reply)
———————————————
تنظیم نام گروه
➤ [ `.setchattitle` ] **⤳** (TEXT)
———————————————
تنظیم بیوگرافی گروه
➤ [ `.setchatbio` ] **⤳** (TEXT)
———————————————
تنظیم نام کاربری گروه
➤ [ `.setchatusername` ] **⤳** (Username)
———————————————
سنجاق پیام در گروه
➤ [ `.pin` ] **⤳** (Reply)
———————————————
حذف سنجاق پیام در گروه
➤ [ `.unpin` ] **⤳** (Reply)
———————————————
حذف همه سنجاق های گروه
➤ [ `.unpinall` ]
———————————————
حذف کانال
➤ [ `.deletechannel` ] **⤳** (Username)
———————————————
حذف گروه
➤ [ `.deletegroup` ] **⤳** (Username)
———————————————
حذف همه پیام های کاربر در گروه
➤ [ `.delallmsguser` ] **⤳** (Reply)
———————————————
تنظیم زمان بین ارسال هر پیام برای اعضای گروه برحسب ثانیه
➤ [ `.slowmod` ] **⤳** (NUM)
———————————————
حذف تعدادی از پیام ها
➤ [ `.delete` ] **⤳** (NUM)
———————————————
تگ ادمین های گروه
➤ [ `.tadmin` ]
———————————————
تگ همه کاربران گروه
➤ [ `.tagall` ] **⤳** (TEXT) (Reply)
———————————————
لغو تگ کاربران گروه
➤ [ `.cancel` ]
———————————————
پاکسازی تاریخچه
➤ [ `.delethistory` ]
———————————————
حذف یک پیام
➤ [ `.del` ] **⤳** (Reply)
———————————————
"""

fahelp2 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ پروفایل ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
تنظیم نام اکانت
➤ [ `.setname` ] **⤳** (TEXT)
———————————————
تنظیم نام خانوادگی اکانت
➤ [ `.setlastname` ] **⤳** (TEXT)
———————————————
تنظیم بیوگرافی اکانت
➤ [ `.setbio` ] **⤳** (TEXT)
———————————————
تنظیم فونت خودکار نام
➤ [ `.fontname` ] **⤳** (on OR off)
———————————————
تنظیم ساعت روی نام
➤ [ `.timename` ] **⤳** (on OR off)
———————————————
تنظیم ساعت روی نام 2
➤ [ `.2timename` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی ساده
➤ [ `.timebio` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی رندوم
➤ [ `.2timebio` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی با خورشید و ماه
➤ [ `.3timebio` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی با خورشید و ماه و روز
➤ [ `.4timebio` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی با قلب رنگی
➤ [ `.5timebio` ] **⤳** (on OR off)
———————————————
تنظیم ساعت در بیوگرافی با ثبت فضولی
➤ [ `.6timebio` ] **⤳** (on OR off)
———————————————
تنظیم عکس پروفایل اکانت
➤ [ `.setprofile` ] **⤳** (Reply)
———————————————
حذف عکس پروفایل اکانت
➤ [ `.delprofile` ]
———————————————
تنظیم ساعت روی عکس پروفایل
➤ [ `.autopic` ]
———————————————
تنظیم ساعت روی عکس پروفایل 2
➤ [ `.2autopic` ]
———————————————
تنظیم ساعت روی عکس پروفایل 3
➤ [ `.3autopic` ]
———————————————
تنظیم ساعت روی عکس پروفایل 4
➤ [ `.4autopic` ]
———————————————
"""

fahelp3 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ دانلودر ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
دریافت اطلاعات پیج اینستاگرام
➤ [ `.iginfo` ] **⤳** (Username)
———————————————
دانلود از اینستاگرام
➤ [ `.igdl` ] **⤳** (URL)
———————————————
دانلود از اینستاگرام & یوتیوب &  فیسبوک & تیک تاک
➤ [ `.down` ] **⤳** (URL)
———————————————
جستجو و دانلود از یوتیوب با متن
➤ [ `.youtube` ] **⤳** (TEXT)
———————————————
جستجوی اپلیکیشن
➤ [ `.app` ] **⤳** (TEXT)
———————————————
جستجوی اپلیکیشن 2
➤ [ `.apk` ] **⤳** (TEXT)
———————————————
"""

fahelp4 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ آپلودر ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
آپلود متن
➤ [ `.neko` ] **⤳** (Reply)
———————————————
آپلود عکس
➤ [ `.telegraph` ] **⤳** (Reply)
———————————————
"""

fahelp5 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ حالت متن ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
حالت بولد
➤ [ `.bold` ] **⤳** (on OR off)
———————————————
حالت اسپویلر
➤ [ `.spoiler` ] **⤳** (on OR off)
———————————————
حالت کج نویس
➤ [ `.italic` ] **⤳** (on OR off)
———————————————
حالت کد نویس
➤ [ `.code` ] **⤳** (on OR off)
———————————————
حالت زیر خط
➤ [ `.underline` ] **⤳** (on OR off)
———————————————
حالت خط خوردگی
➤ [ `.strike` ] **⤳** (on OR off)
———————————————
حالت ایموجی
➤ [ `.emoji` ] **⤳** (on OR off)
———————————————
حالت نقل قول
➤ [ `.quote` ] **⤳** (on OR off)
———————————————
حالت منشن
➤ [ `.mention` ] **⤳** (on OR off)
———————————————
تنظیم ری اکشن روی کاربر
➤ [ `.setreact` ] **⤳** (Emoji) (Reply)
———————————————
حذف ری اکشن
➤ [ `.delreact` ] **⤳** (Reply)
———————————————
لیست ری اکشن ها
➤ [ `.reactlist` ]
———————————————
ارسال متن به صورت پله ای
➤ [ `.lad` ] **⤳** (TEXT)
———————————————
"""

fahelp6 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ حالت اکشن ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
حالت نوشتن
➤ [ `.typing` ] **⤳** (on OR off)
———————————————
حالت بازی کردن
➤ [ `.playing` ] **⤳** (on OR off)
———————————————
حالت ضبط ویدیو
➤ [ `.record_vid` ] **⤳** (on OR off)
———————————————
حالت انتخاب استیکر
➤ [ `.choose_sticker` ] **⤳** (on OR off)
———————————————
حالت آپلود ویدیو
➤ [ `.upload_vid` ] **⤳** (on OR off)
———————————————
حالت آپلود فایل
➤ [ `.upload_doc` ] **⤳** (on OR off)
———————————————
حالت آپلود فایل صوتی
➤ [ `.upload_audio` ] **⤳** (on OR off)
———————————————
حالت صحبت کردن
➤ [ `.speaking` ] **⤳** (on OR off)
———————————————
حالت آنلاین بودن اکانت
➤ [ `.online` ] **⤳** (on OR off)
———————————————
حالت آفلاین بودن اکانت
➤ [ `.offline` ] **⤳** (on OR off)
———————————————
"""

fahelp7 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ وبهوک ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
تنظیم وبهوک
➤ [ `.setwebhook` ] **⤳** (Token URL)
———————————————
حذف وبهوک
➤ [ `.delwebhook` ] **⤳** (Token)
———————————————
پاکسازی آپدیت های در انتظار
➤ [ `.delupdate` ] **⤳** (Token)
———————————————
دریافت اطلاعات وبهوک
➤ [ `.webhookinfo` ] **⤳** (Token)
———————————————
دریافت اطلاعات ربات
➤ [ `.botinfo` ] **⤳** (Token)
———————————————
"""

fahelp8 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ قفل ها ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
فعال یا غیرفعال کردن قفل پیوی
➤ [ `.pvlock` ] **⤳** (on OR off)
———————————————
فعال یا غیرفعال کردن جوین اجباری پیوی
➤ [ `.monshi2` ] **⤳** (on OR off)
———————————————
لیست نام قفل ها
➤ [ `.hlock` ]
———————————————
وضعیت قفل گروه
➤ [ `.locks` ]
———————————————
قفل یک ویژگی
➤ [ `.lock` ] **⤳** (Name)
———————————————
بازکردن قفل یک ویژگی
➤ [ `.unlock` ] **⤳** (Name)
———————————————
قفل همه ویژگی ها
➤ [ `.lock all` ]
———————————————
بازکردن قفل همه ویژگی ها
➤ [ `.unlock all` ]
———————————————
"""

fahelp9 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ کرون جاب ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
تنظیم کرون جاب برحسب دقیقه
➤ [ `.cron` ] **⤳** (URL Time)
Time: 1, 2, 5, 10, 15, 30 ...
———————————————
"""

fahelp10 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ آنتی لاگین ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
فعال یا غیرفعال کردن آنتی لاگین اکانت
➤ [ `.antilog` ] **⤳** (on OR off)
———————————————
"""

fahelp11 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ تبچی ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
وضعیت تبچی
➤ [ `.tabchi status` ]
———————————————
فعال یا غیرفعال کردن ارسال خودکار به پیوی ها
➤ [ `.tabchipv` ] **⤳** (on OR off)
———————————————
فعال یا غیرفعال کردن ارسال خودکار به گروه ها
➤ [ `.tabchigp` ] **⤳** (on OR off)
———————————————
تنظیم بنر ارسال خودکار به پیوی ها
➤ [ `.setbannerpv` ] **⤳** (TEXT) (Reply)
———————————————
تنظیم بنر ارسال خودکار به گروه ها
➤ [ `.setbannergp` ] **⤳** (TEXT) (Reply)
———————————————
تنظیم زمان ارسال خودکار به پیوی ها برحسب ثانیه
➤ [ `.settimerpv` ] **⤳** (NUM)
———————————————
تنظیم زمان ارسال خودکار به گروه ها برحسب ثانیه
➤ [ `.settimergp` ] **⤳** (NUM)
———————————————
ارسال همگانی به پیوی ها
➤ [ `.sendpv` ] **⤳** (TEXT) (Reply)
———————————————
ارسال همگانی به گروه ها
➤ [ `.sendgp` ] **⤳** (TEXT) (Reply)
———————————————
تنظیم بنر ارسال به پیوی اعضای گروه
➤ [ `.setbannersender` ] **⤳** (TEXT) (Reply)
———————————————
ارسال به پیوی اعضای گروه مورد نظر
➤ [ `.sendall` ] **⤳** (Username)
———————————————
دریافت لینک گروه
➤ [ `.invitelink` ]
———————————————
پیوستن به گروه
➤ [ `.join` ] **⤳** (Link)
———————————————
خروج از گروه
➤ [ `.leave` ] **⤳** (Link)
———————————————
خروج از تمام گروه ها
➤ [ `.leaveallgc` ]
———————————————
خروج از تمام کانال ها
➤ [ `.leaveallch` ]
———————————————
"""

fahelp12 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ ویرایشگر عکس ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**با دستورات زیر می‌توانید متن مورد نظر خود را روی عکس طرح کنید**

➤ [ `.kanna` ] **⤳** (TEXT)
———————————————
➤ [ `.clyde` ] **⤳** (TEXT)
———————————————
➤ [ `.write` ] **⤳** (TEXT)
———————————————
➤ [ `.mind` ] **⤳** (TEXT)
———————————————
➤ [ `.trump` ] **⤳** (TEXT)
———————————————
➤ [ `.o` ] **⤳** (TEXT)
———————————————
➤ [ `.o2` ] **⤳** (TEXT)
———————————————
➤ [ `.bish` ] **⤳** (TEXT)
———————————————
➤ [ `.latex` ] **⤳** (TEXT)
———————————————
**با دستورات زیر می‌توانید روی عکس مورد نظر خود فیلتر های مختلف ست کنید**

➤ [ `.blue` ] **⤳** (Reply)
———————————————
➤ [ `.green` ] **⤳** (Reply)
———————————————
➤ [ `.red` ] **⤳** (Reply)
———————————————
➤ [ `.grey` ] **⤳** (Reply)
———————————————
➤ [ `.grey2` ] **⤳** (Reply)
———————————————
➤ [ `.sepia` ] **⤳** (Reply)
———————————————
➤ [ `.threshold` ] **⤳** (Reply)
———————————————
➤ [ `.blurple` ] **⤳** (Reply)
———————————————
➤ [ `.filter` ] **⤳** (Reply)
———————————————
**با دستورات زیر می‌توانید استایل و ابعاد عکس مورد نظر خود را تغییر دهید**

➤ [ `.bisexual` ] **⤳** (Reply)
———————————————
➤ [ `.blur` ] **⤳** (Reply)
———————————————
➤ [ `.horny` ] **⤳** (Reply)
———————————————
➤ [ `.stupid` ] **⤳** (Reply)
———————————————
➤ [ `.lesbian` ] **⤳** (Reply)
———————————————
➤ [ `.lgbt` ] **⤳** (Reply)
———————————————
➤ [ `.lolice` ] **⤳** (Reply)
———————————————
➤ [ `.non` ] **⤳** (Reply)
———————————————
➤ [ `.psexual` ] **⤳** (Reply)
———————————————
➤ [ `.pixel` ] **⤳** (Reply)
———————————————
➤ [ `.simp` ] **⤳** (Reply)
———————————————
➤ [ `.spin` ] **⤳** (Reply)
———————————————
➤ [ `.toni` ] **⤳** (Reply)
———————————————
**با دستورات زیر می‌توانید روی عکس مورد نظر خود فیلتر ها و تغییرات فان ست کنید**

➤ [ `.comrade` ] **⤳** (Reply)
———————————————
➤ [ `.gay` ] **⤳** (Reply)
———————————————
➤ [ `.glass` ] **⤳** (Reply)
———————————————
➤ [ `.jail` ] **⤳** (Reply)
———————————————
➤ [ `.wasted` ] **⤳** (Reply)
———————————————
➤ [ `.pass` ] **⤳** (Reply)
———————————————
"""

fahelp13 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ گیف و لوگو ساز ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
ساخت لوگو با متن
➤ [ `.logo` ] **⤳** (TEXT)
———————————————
ساخت لوگو با متن 2
➤ [ `.logo2` ] **⤳** (TEXT)
———————————————
ساخت لوگو با متن و طرح دلخواه
➤ [ `.lg` ] **⤳** (TEXT Mode)
Mode: 1-138
———————————————
ساخت گیف با متن
➤ [ `.gif` ] **⤳** (TEXT)
———————————————
ساخت گیف با متن 2
➤ [ `.giff` ] **⤳** (TEXT)
———————————————
"""

fahelp14 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ کامپایلر ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➤ [ `.py` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.js` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.php` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.kotlin` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.go` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.java` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.lua` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.exec` ] **⤳** (Code)
———————————————
"""

fahelp15 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ ابزار ها ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
استخراج فایل از حالت فشرده
➤ [ `.unzip` ] **⤳** (Reply)
———————————————
تغییر نام فایل
➤ [ `.rname` ] **⤳** (TEXT) (Reply)
———————————————
چکر شماره مجازی
➤ [ `.check` ] **⤳** (Number)
———————————————
اسکرین شات از متن
➤ [ `.q` ] **⤳** (Reply)
———————————————
اسکرین شات از متن دلخواه
➤ [ `.qq` ] **⤳** (TEXT)
———————————————
دریافت نتایج بازی های Cricket
➤ [ `.cricket` ] **⤳**
———————————————
وضعیت آب و هوا
➤ [ `.weather` ] **⤳** (City Name)
———————————————
زمان اذان
➤ [ `.azan` ] **⤳** (City Name)
———————————————
تبدیل کننده دما
➤ [ `.t` ] **⤳** (NUM c OR f)
eg: .t 25 c
———————————————
تبدیل کننده ارز دیجیتال
➤ [ `.c` ] **⤳** (NUM Currency1 Currency2)
eg: .c 100 usdt eur
———————————————
ماشین حساب ریاضی
➤ [ `.e` ] **⤳** (Match)
eg: .e 2+2
———————————————
دریافت آیپی سایت
➤ [ `.ip` ] **⤳** (Domain)
———————————————
دریافت اطلاعات آیپی
➤ [ `.whoisip` ] **⤳** (IP)
———————————————
کوتاه کننده لینک
➤ [ `.link` ] **⤳** (URL)
———————————————
کوتاه کننده لینک 2
➤ [ `.link2` ] **⤳** (URL)
———————————————
دریافت پینگ سایت
➤ [ `.p` ] **⤳** (Domain)
———————————————
اسکرین شات از سایت
➤ [ `.screenshot` ] **⤳** (Domain)
———————————————
اسکرین شات از سایت 2
➤ [ `.screenshot2` ] **⤳** (Domain)
———————————————
اسکرین شات از سایت 3
➤ [ `.screenshot3` ] **⤳** (Domain)
———————————————
اسکرین شات از سایت 4
➤ [ `.screenshot4` ] **⤳** (Domain)
———————————————
اسکرین شات از سایت 5
➤ [ `.shot` ] **⤳** (Domain)
———————————————
دریافت اطلاعات اکانت گیت هاب
➤ [ `.github` ] **⤳** (Username)
———————————————
دریافت اطلاعات پروژه
➤ [ `.git` ] **⤳** (TEXT)
———————————————
جستجو در دیکشنری
➤ [ `.dict` ] **⤳** (Word)
———————————————
کپی کردن پروفایل یک اکانت
➤ [ `.clone` ] **⤳** (ID) (Reply)
———————————————
دریافت تاریخ ساخت اکانت
➤ [ `.i` ] **⤳** (ID) (Reply)
———————————————
دریافت تاریخ ساخت اکانت سلف
➤ [ `.creation` ]
———————————————
وضعیت محدودیت اکانت سلف
➤ [ `.limit` ]
———————————————
دریافت اطلاعات کشور
➤ [ `.country` ] **⤳** (Name)
———————————————
تبدیل استیکر به عکس
➤ [ `.tp` ] **⤳** (Reply)
———————————————
تبدیل عکس به استیکر
➤ [ `.ts` ] **⤳** (Reply)
———————————————
ساخت گیف
➤ [ `.tg` ] **⤳** (Reply)
———————————————
ترجمه به فارسی
➤ [ `.fa` ] **⤳** (TEXT)
———————————————
ترجمه به انگلیسی
➤ [ `.en` ] **⤳** (TEXT)
———————————————
دریافت فیلم
➤ [ `.movie` ] **⤳** (TEXT)
———————————————
دریافت انیمه
➤ [ `.anim` ] **⤳** (TEXT)
———————————————
ساخت پسورد با تعداد کاراکتر دلخواه
➤ [ `.pass` ] **⤳** (NUM)
———————————————
تبدیل متن به کد مورس
➤ [ `.morset` ] **⤳** (TEXT)
———————————————
تبدیل کد مورس به متن
➤ [ `.unmorset` ] **⤳** (Code)
———————————————
دریافت تاریخ
➤ [ `.date` ]
———————————————
دریافت اطلاعات یک اکانت
➤ [ `.id` ] **⤳** (ID) (Reply)
———————————————
دریافت اطلاعات یک پیام
➤ [ `.get_message` ] **⤳** (Reply)
———————————————
منشن کردن یک کاربر
➤ [ `.mention` ] **⤳** (ID) (Reply)
———————————————
بررسی صحت کد ملی
➤ [ `.meli` ] **⤳** (Number)
———————————————
استعلام کارت بانکی
➤ [ `.estelam` ] **⤳** (Number)
———————————————
دریافت اخبار روز
➤ [ `.news` ] **⤳** (Category)
Category: business, entertainment, general, health, science, sports, technology
———————————————
دریافت کارت بین
➤ [ `.ccgen` ]
———————————————
دریافت اخبار روز
➤ [ `.yjc` ]
———————————————
استخراج متن از عکس
➤ [ `.ocr` ] **⤳** (Reply)
———————————————
دانلود عکس زمان دار
➤ [ `.dl` ] **⤳** (Reply)
———————————————
ذخیره محتوا در پیام های ذخیره شده
➤ [ `.waitt` ] **⤳** (Reply)
———————————————
دریافت ساعت
➤ [ `.time` ]
———————————————
"""

fahelp16 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ اکانت ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
افزودن ادمین به سلف
➤ [ `.addadmin` ] **⤳** (ID) (Reply)
———————————————
حذف ادمین سلف
➤ [ `.deladmin` ] **⤳** (ID) (Reply)
———————————————
لیست ادمین های سلف
➤ [ `.adminlist` ]
———————————————
پاکسازی لیست ادمین های سلف
➤ [ `.clearadminlist` ]
———————————————
دریافت آیدی عددی اکانت سلف
➤ [ `id` ]
———————————————
وضعیت محدودیت اکانت سلف
➤ [ `.limit` ]
———————————————
دریافت تاریخ ساخت اکانت سلف
➤ [ `.creation` ]
———————————————
دریافت اطلاعات سشن اکانت سلف
➤ [ `.session` ]
———————————————
"""

fahelp17 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ کتاب ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
دریافت جوک
➤ [ `.joke` ]
———————————————
دریافت شعر
➤ [ `.poem` ]
———————————————
دریافت دانستنی
➤ [ `.know` ]
———————————————
دریافت نقل قول
➤ [ `.quote` ]
———————————————
جستجو در ویکی پدیا
➤ [ `.wiki` ] **⤳** (TEXT)
———————————————
جستجو در گوگل
➤ [ `.google` ] **⤳** (TEXT)
———————————————
تبدیل عدد به حروف
➤ [ `.num` ] **⤳** (NUM)
———————————————
دریافت اطلاعات نام
➤ [ `.name` ] **⤳** (Name)
———————————————
دریافت بیوگرافی
➤ [ `.bio` ]
———————————————
دریافت خاطره
➤ [ `.memo` ]
———————————————
دریافت پ ن پ
➤ [ `.pnp` ]
———————————————
دریافت الکی
➤ [ `.alaki` ]
———————————————
دریافت حدیث
➤ [ `.hadis` ]
———————————————
دریافت داستان
➤ [ `.dastan` ]
———————————————
دریافت نام رندوم
➤ [ `.rname` ]
———————————————
دریافت فال
➤ [ `.fal` ]
———————————————
دریافت استخاره
➤ [ `.estekhare` ]
———————————————
دریافت ذکر
➤ [ `.zekr` ]
———————————————
"""

fahelp18 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ سرگرمی ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
تقلب در تاس
➤ [ `.tas` ] **⤳** (1-6)
———————————————
تقلب در دارت
➤ [ `.dart` ]
———————————————
تقلب در بولینگ
➤ [ `.bowling` ]
———————————————
تقلب در بسکتبال
➤ [ `.basketball` ]
———————————————
تقلب در فوتبال
➤ [ `.football` ] **⤳** (1 OR 6)
1: Fail
4: Goal
———————————————
دریافت بازی رندوم 1
➤ [ `.game` ]
———————————————
دریافت بازی رندوم 2
➤ [ `.bazi` ]
———————————————
دریافت بازی رندوم 3
➤ [ `.hehe` ]
———————————————
**سایر سرگرمی ها**

➤ [ `.moon` ]
———————————————
➤ [ `.clock` ]
———————————————
➤ [ `.thunder` ]
———————————————
➤ [ `.earth` ]
———————————————
➤ [ `.heart` ]
———————————————
➤ [ `.love` ]
———————————————
➤ [ `.santet` ]
———————————————
➤ [ `.nah` ]
———————————————
➤ [ `.ajg` ]
———————————————
➤ [ `.babi` ]
———————————————
➤ [ `.tank` ]
———————————————
➤ [ `.y` ]
———————————————
➤ [ `.awk` ]
———————————————
➤ [ `.tembak` ]
———————————————
➤ [ `.heli` ]
———————————————
➤ [ `.gabut` ]
———————————————
➤ [ `.syg` ]
———————————————
➤ [ `.dino` ]
———————————————
➤ [ `.hack` ]
———————————————
➤ [ `.fuck` ]
———————————————
➤ [ `.koc` ]
———————————————
➤ [ `.charging` ]
———————————————
➤ [ `.gang` ]
———————————————
➤ [ `.hypo` ]
———————————————
➤ [ `.ding` ]
———————————————
➤ [ `.wtf` ]
———————————————
➤ [ `.call` ]
———————————————
➤ [ `.bomb` ]
———————————————
➤ [ `.brain` ]
———————————————
➤ [ `.ahh` ]
———————————————
➤ [ `.hmm` ]
———————————————
"""

fahelp19 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ بازار ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
قیمت کالا در بازار ایران (باسلام)
➤ [ `.price` ] **⤳** (TEXT)
———————————————
قیمت کالا در بازار ایران (ترب)
➤ [ `.qeymat` ] **⤳** (TEXT)
———————————————
لیست نماد ارز های دیجیتال
➤ [ `.cryptolist` ]
———————————————
قیمت ارز دیجیتال
➤ [ `.crypto` ] **⤳** (Name)
———————————————
تبدیل کننده ارز دیجیتال
➤ [ `.c` ] **⤳** (NUM Currency1 Currency2)
eg: .c 100 usdt eur
———————————————
قیمت ترون
➤ [ `.trx` ]
———————————————
لیست قیمت ارز ها
➤ [ `.arz` ]
———————————————
استعلام کارت بانکی
➤ [ `.estelam` ] **⤳** (Number)
———————————————
دریافت اطلاعات تراکنش ارز دیجیتال
➤ [ `.tara` ] **⤳** (TransLink)
———————————————
"""

fahelp20 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ استیکر - گیف ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
ساخت استیکر با متن
➤ [ `.sticker` ] **⤳** (TEXT)
———————————————
دریافت اطلاعات استیکر
➤ [ `.stickerinfo` ] **⤳** (Reply)
———————————————
ساخت استیکر با کد ارور
➤ [ `.error` ] **⤳** (Code)
eg: .error 404
———————————————
کوچک کردن استیکر و عکس
➤ [ `.tiny` ] **⤳** (Reply)
———————————————
تبدیل عکس به استیکر
➤ [ `.ts` ] **⤳** (Reply)
———————————————
ساخت گیف
➤ [ `.tg` ] **⤳** (Reply)
———————————————
**دریافت گیف رندوم**

➤ [ `.palm` ]
———————————————
➤ [ `.wink` ]
———————————————
➤ [ `.hug` ]
———————————————
➤ [ `.pat` ]
———————————————
"""

fahelp21 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ هوش مصنوعی ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**هوش مصنوعی متنی**

➤ [ `.gpt3` ] **⤳** (TEXT)
———————————————
➤ [ `.gpt4` ] **⤳** (TEXT)
———————————————
➤ [ `.bard` ] **⤳** (TEXT)
———————————————
➤ [ `.asq` ] **⤳** (TEXT)
———————————————
➤ [ `.messi` ] **⤳** (TEXT)
———————————————
➤ [ `.ronaldo` ] **⤳** (TEXT)
———————————————
➤ [ `.ilon` ] **⤳** (TEXT)
———————————————
**هوش مصنوعی صوتی**

➤ [ `.` ] **⤳** (TEXT) زن
———————————————
➤ [ `/` ] **⤳** (TEXT) مرد
———————————————
➤ [ `.voice` ] **⤳** (TEXT)
———————————————
➤ [ `.crush` ] **⤳** (TEXT)
———————————————
➤ [ `.wo` ] **⤳** (TEXT) زن
———————————————
➤ [ `.ma` ] **⤳** (TEXT) مرد
———————————————
➤ [ `.v` ] **⤳** (TEXT)
———————————————
دریافت لیست آیدی ها
➤ [ `.vl` ]
———————————————
تنظیم لهجه مورد نظر با آیدی
➤ [ `.sv` ] **⤳** (Mode)
———————————————
**هوش مصنوعی تصویری**

➤ [ `.pgpt` ] **⤳** (TEXT)
———————————————
"""

fahelp22 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ عکس ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
ساخت رنگ
➤ [ `.color` ] **⤳** (Color)
———————————————
**دریافت عکس رندوم حیوانات**

➤ [ `.pikachu` ]
———————————————
➤ [ `.whale` 
———————————————
➤ [ `.foxx` ]
———————————————
➤ [ `.doggg` ]
———————————————
➤ [ `.rpanda` ]
———————————————
➤ [ `.raccoon` ]
———————————————
➤ [ `.panda` ]
———————————————
➤ [ `.koala` ]
———————————————
➤ [ `.kangroo` ]
———————————————
➤ [ `.fox` ]
———————————————
➤ [ `.dogg` ]
———————————————
➤ [ `.birdd` ]
———————————————
➤ [ `.catt` ]
———————————————
➤ [ `.bird` ]
———————————————
➤ [ `.dog` ]
———————————————
➤ [ `.cat` ]
———————————————
➤ [ `.robo` ] **⤳** (1-999999)
———————————————
**دریافت عکس رندوم +18**

➤ [ `.couple` ]
———————————————
➤ [ `.ayang` ]
———————————————
➤ [ `.boob` ]
———————————————
➤ [ `.nude` ]
———————————————
➤ [ `.nude2` ]
———————————————
**جستجوی عکس**

➤ [ `.pic` ]
———————————————
➤ [ `.bing` ]
———————————————
➤ [ `.uns` ]
———————————————
➤ [ `.photo` ]
———————————————
➤ [ `.photos` ]
———————————————
"""

fahelp23 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ موزیک ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**جستجو و دریافت موزیک با دستورات زیر**

➤ [ `.music` ] **⤳** (TEXT)
———————————————
➤ [ `.youtube` ] **⤳** (TEXT)
———————————————
➤ [ `.musicc` ] **⤳** (TEXT)
———————————————
➤ [ `.remix` ] **⤳** (TEXT)
———————————————
➤ [ `.demo` ] **⤳** (TEXT)
———————————————
➤ [ `.classic` ] **⤳** (TEXT)
———————————————
➤ [ `.ahang` ] **⤳** (TEXT)
———————————————
➤ [ `.melo` ] **⤳** (TEXT)
———————————————
➤ [ `.global` ] **⤳** (TEXT)
———————————————
"""

fahelp24 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                                                   **[ تنظیمات سیستم ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
روشن کردن سلف
[ ➤ `.on` ]
———————————————
خاموش کردن سلف
[ ➤ `.off` ]
———————————————
راه اندازی مجدد سلف
➤ [ `.restart` ]
———————————————
غیرفعال کردن اضطراری سلف
➤ [ `.shutdown` ]
———————————————
دریافت پینگ سلف
➤ [ `.ping` ]
———————————————
وضعیت سلف
➤ [ `self` ]
———————————————
دریافت آمار سلف
➤ [ `.on_off_status` ]
———————————————
اطلاعات پردازشگر
➤ [ `.cpu` ]
———————————————
اطلاعات مموری
➤ [ `.memory` ]
———————————————
اطلاعات سیستم
➤ [ `.system-inf` ]
———————————————
"""

enhelp1 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Global - Personal ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
User mute
➤ [ `.mute` ]
———————————————
User unmute
➤ [ `.unmute` ]
———————————————
Clear mute list
➤ [ `.allunmute` ]
———————————————
User block
➤ [ `.block` ]
———————————————
User unblock
➤ [ `.unblock` ]
———————————————
Add User to enemy list
➤ [ `.setenemy` ]
———————————————
Remove User from the enemy list
➤ [ `.delenemy` ]
———————————————
Clear enemy list
➤ [ `.clearenemy` ]
———————————————
Add User to love list
➤ [ `.setlove` ]
———————————————
Remove User from the love list
➤ [ `.dellove` ]
———————————————
Clear love list
➤ [ `.clearlove` ]
———————————————
Set Auto monshi text
➤ [ `.monshi` ] **⤳** (TEXT)
———————————————
Disable Auto monshi
➤ [ `.monshioff` ]
———————————————
Set Offline mode text
➤ [ `.afk` ] **⤳** (TEXT)
———————————————
Disable Offline mode
➤ [ `.unafk` ]
———————————————
Receive Tagalert
➤ [ `.tagalert` ] **⤳** (on OR off)
———————————————
Create Channel
➤ [ `.creatchannel` ] **⤳** (Name)
———————————————
Create Group
➤ [ `.creatgroup` ] **⤳** (Name)
———————————————
Create Supergroup
➤ [ `.creatsupergroup` ] **⤳** (Name)
———————————————
Normal Spam text
➤ [ `.spam` ] **⤳** (NUM TEXT)
———————————————
Slow Spam text
➤ [ `.slowspam` ] **⤳** (NUM TEXT)
———————————————
Spam Text and delete
➤ [ `.statspam` ] **⤳** (NUM TEXT)
———————————————
Fast Spam text
➤ [ `.fastspam` ] **⤳** (NUM TEXT)
———————————————
Enable first comment
➤ [ `.firstcom` ] **⤳** (on OR off)
———————————————
Set first comment text
➤ [ `.first_message` ] **⤳** (TEXT) (Reply)
———————————————
Set time for Auto send text
➤ [ `.text_time` ] **⤳** (HH:MM)
———————————————
Set time for Auto send photo
➤ [ `.photo_time` ] **⤳** (HH:MM)
———————————————
Set Text for Auto send text
➤ [ `.text_send_time` ] **⤳** (TEXT) (Reply)
———————————————
Set Photo for Auto send photo
➤ [ `.photo_send_time` ] **⤳** (Reply)
———————————————
Auto answer
➤ [ `.answer` ] **⤳** (on OR off)
———————————————
Set Question and Answer for Auto answer
➤ [ `.addan` ] **⤳** (Question:Answer)
———————————————
Delete an answer
➤ [ `.delan` ] **⤳** (Answer)
———————————————
Answer list
➤ [ `.anlist` ]
———————————————
Clear Auto answer list
➤ [ `.anclear` ]
———————————————
Welcome Mode
➤ [ `.welcome` ] **⤳** (on OR off)
———————————————
Set Welcome text
➤ [ `.welcome_add` ] **⤳** (TEXT)
———————————————
Show Welcome text
➤ [ `.welcome_show` ]
———————————————
Reset Welcome text
➤ [ `.welcome_reset` ]
———————————————
**Attention! To use the following commands, you must be the owner or administrator of the desired group with the necessary permissions**

Ban a User in the group
➤ [ `.ban` ] **⤳** (ID) (Reply)
———————————————
Unban a User in the group
➤ [ `.unban` ] **⤳** (ID) (Reply)
———————————————
Mute a User in the group
➤ [ `.setmute` ] **⤳** (ID) (Reply)
———————————————
Unmute a User in the group
➤ [ `.delmute` ] **⤳** (ID) (Reply)
———————————————
Set Chat photo
➤ [ `.setchatphoto` ] **⤳** (Reply)
———————————————
Set Chat title
➤ [ `.setchattitle` ] **⤳** (TEXT)
———————————————
Set Chat bio
➤ [ `.setchatbio` ] **⤳** (TEXT)
———————————————
Set Chat Username
➤ [ `.setchatusername` ] **⤳** (Username)
———————————————
Pin a Message in the group
➤ [ `.pin` ] **⤳** (Reply)
———————————————
Unpin a Message in the group
➤ [ `.unpin` ] **⤳** (Reply)
———————————————
Unpin All messages
➤ [ `.unpinall` ]
———————————————
Delete Channel
➤ [ `.deletechannel` ] **⤳** (Username)
———————————————
Delete Group
➤ [ `.deletegroup` ] **⤳** (Username)
———————————————
Delete All messages from a User in the group
➤ [ `.delallmsguser` ] **⤳** (Reply)
———————————————
Set time between sending each message for group members (Second)
➤ [ `.slowmod` ] **⤳** (NUM)
———————————————
Delete some messages
➤ [ `.delete` ] **⤳** (NUM)
———————————————
Tag Group admins
➤ [ `.tadmin` ]
———————————————
Tag All members group
➤ [ `.tagall` ] **⤳** (TEXT) (Reply)
———————————————
Cancel Group members tag
➤ [ `.cancel` ]
———————————————
Clear history
➤ [ `.delethistory` ]
———————————————
Delete a message
➤ [ `.del` ] **⤳** (Reply)
———————————————
"""

enhelp2 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Profile ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Set Account name
➤ [ `.setname` ] **⤳** (TEXT)
———————————————
Set Account lastname
➤ [ `.setlastname` ] **⤳** (TEXT)
———————————————
Set Account bio
➤ [ `.setbio` ] **⤳** (TEXT)
———————————————
Auto Font name
➤ [ `.fontname` ] **⤳** (on OR off)
———————————————
Set Time name
➤ [ `.timename` ] **⤳** (on OR off)
———————————————
Set Time name 2
➤ [ `.2timename` ] **⤳** (on OR off)
———————————————
Set Time bio
➤ [ `.timebio` ] **⤳** (on OR off)
———————————————
Set Time bio 2
➤ [ `.2timebio` ] **⤳** (on OR off)
———————————————
Set Time bio 3
➤ [ `.3timebio` ] **⤳** (on OR off)
———————————————
Set Time bio 4
➤ [ `.4timebio` ] **⤳** (on OR off)
———————————————
Set Time bio 5
➤ [ `.5timebio` ] **⤳** (on OR off)
———————————————
Set Time bio 6
➤ [ `.6timebio` ] **⤳** (on OR off)
———————————————
Set Account profile photo
➤ [ `.setprofile` ] **⤳** (Reply)
———————————————
Delete Account profile photo
➤ [ `.delprofile` ]
———————————————
Set Time on profile photo
➤ [ `.autopic` ]
———————————————
Set Time on profile photo 2
➤ [ `.2autopic` ]
———————————————
Set Time on profile photo 3
➤ [ `.3autopic` ]
———————————————
Set Time on profile photo 4
➤ [ `.4autopic` ]
———————————————
"""

enhelp3 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Downloader ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Get Instagram page information
➤ [ `.iginfo` ] **⤳** (Username)
———————————————
Download from Instagram
➤ [ `.igdl` ] **⤳** (URL)
———————————————
Download from Instagram, YouTube, Facebook & TikTok
➤ [ `.down` ] **⤳** (URL)
———————————————
Search and download from YouTube with text
➤ [ `.youtube` ] **⤳** (TEXT)
———————————————
Application Search
➤ [ `.app` ] **⤳** (TEXT)
———————————————
Application Search 2
➤ [ `.apk` ] **⤳** (TEXT)
———————————————
"""

enhelp4 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Uploader ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Upload Text
➤ [ `.neko` ] **⤳** (Reply)
———————————————
Upload Photo
➤ [ `.telegraph` ] **⤳** (Reply)
———————————————
"""

enhelp5 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Text Mode ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Bold Mode
➤ [ `.bold` ] **⤳** (on OR off)
———————————————
Spoiler Mode
➤ [ `.spoiler` ] **⤳** (on OR off)
———————————————
Italic Mode
➤ [ `.italic` ] **⤳** (on OR off)
———————————————
Code Mode
➤ [ `.code` ] **⤳** (on OR off)
———————————————
Underline Mode
➤ [ `.underline` ] **⤳** (on OR off)
———————————————
Strike Mode
➤ [ `.strike` ] **⤳** (on OR off)
———————————————
Emoji Mode
➤ [ `.emoji` ] **⤳** (on OR off)
———————————————
Quote Mode
➤ [ `.quote` ] **⤳** (on OR off)
———————————————
Mention Mode
➤ [ `.mention` ] **⤳** (on OR off)
———————————————
Set Reaction
➤ [ `.setreact` ] **⤳** (Emoji) (Reply)
———————————————
Delete Reaction
➤ [ `.delreact` ] **⤳** (Reply)
———————————————
Reaction List
➤ [ `.reactlist` ]
———————————————
Send ladder text
➤ [ `.lad` ] **⤳** (TEXT)
———————————————
"""

enhelp6 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Action Mode ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Typing Mode
➤ [ `.typing` ] **⤳** (on OR off)
———————————————
Playing Mode
➤ [ `.playing` ] **⤳** (on OR off)
———————————————
Recording Mode
➤ [ `.record_vid` ] **⤳** (on OR off)
———————————————
Sticker Selection Mode
➤ [ `.choose_sticker` ] **⤳** (on OR off)
———————————————
Video Uploading Mode
➤ [ `.upload_vid` ] **⤳** (on OR off)
———————————————
Document Uploading Mode
➤ [ `.upload_doc` ] **⤳** (on OR off)
———————————————
Audio Uploading Mode
➤ [ `.upload_audio` ] **⤳** (on OR off)
———————————————
Speaking Mode
➤ [ `.speaking` ] **⤳** (on OR off)
———————————————
Account Online Mode
➤ [ `.online` ] **⤳** (on OR off)
———————————————
Account Offline Mode
➤ [ `.offline` ] **⤳** (on OR off)
———————————————
"""

enhelp7 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Webhook ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Set Webhook
➤ [ `.setwebhook` ] **⤳** (Token URL)
———————————————
Delete Webhook
➤ [ `.delwebhook` ] **⤳** (Token)
———————————————
Clear Pending Updates
➤ [ `.delupdate` ] **⤳** (Token)
———————————————
Get Webhook information
➤ [ `.webhookinfo` ] **⤳** (Token)
———————————————
Get Bot information
➤ [ `.botinfo` ] **⤳** (Token)
———————————————
"""

enhelp8 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Locks ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
PV Lock Mode
➤ [ `.pvlock` ] **⤳** (on OR off)
———————————————
Mandatory join
➤ [ `.monshi2` ] **⤳** (on OR off)
———————————————
Lock Name list
➤ [ `.hlock` ]
———————————————
Group Lock status
➤ [ `.locks` ]
———————————————
Lock a option
➤ [ `.lock` ] **⤳** (Name)
———————————————
Unlock a option
➤ [ `.unlock` ] **⤳** (Name)
———————————————
Lock All options
➤ [ `.lock all` ]
———————————————
Unlock All options
➤ [ `.unlock all` ]
———————————————
"""

enhelp9 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Cron Job ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Set Cron Job (Minute)
➤ [ `.cron` ] **⤳** (URL Time)
Time: 1, 2, 5, 10, 15, 30 ...
———————————————
"""

enhelp10 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Anti Login ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Anti Login Account
➤ [ `.antilog` ] **⤳** (on OR off)
———————————————
"""

enhelp11 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Tabchi ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Tabchi Status
➤ [ `.tabchi status` ]
———————————————
Auto Send to PVs
➤ [ `.tabchipv` ] **⤳** (on OR off)
———————————————
Auto Send to Groups
➤ [ `.tabchigp` ] **⤳** (on OR off)
———————————————
Set Banner for Auto Send to PVs
➤ [ `.setbannerpv` ] **⤳** (TEXT) (Reply)
———————————————
Set Banner for Auto Send to Groups
➤ [ `.setbannergp` ] **⤳** (TEXT) (Reply)
———————————————
Set Timer for Auto Send to PVs (Second)
➤ [ `.settimerpv` ] **⤳** (NUM)
———————————————
Set Timer for Auto Send to Groups (Second)
➤ [ `.settimergp` ] **⤳** (NUM)
———————————————
Send to PVs
➤ [ `.sendpv` ] **⤳** (TEXT) (Reply)
———————————————
Send to Groups
➤ [ `.sendgp` ] **⤳** (TEXT) (Reply)
———————————————
Set Banner for Send to Group members
➤ [ `.setbannersender` ] **⤳** (TEXT) (Reply)
———————————————
Send to Group membes
➤ [ `.sendall` ] **⤳** (Username)
———————————————
Get the group invitation link
➤ [ `.invitelink` ]
———————————————
Join the Group
➤ [ `.join` ] **⤳** (Link)
———————————————
Leave the Group
➤ [ `.leave` ] **⤳** (Link)
———————————————
Leave All Groups
➤ [ `.leaveallgc` ]
———————————————
Leave All Channels
➤ [ `.leaveallch` ]
———————————————
"""

enhelp12 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Photo Editor ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**With the following commands, you can design the text you want on the photo**

➤ [ `.kanna` ] **⤳** (TEXT)
———————————————
➤ [ `.clyde` ] **⤳** (TEXT)
———————————————
➤ [ `.write` ] **⤳** (TEXT)
———————————————
➤ [ `.mind` ] **⤳** (TEXT)
———————————————
➤ [ `.trump` ] **⤳** (TEXT)
———————————————
➤ [ `.o` ] **⤳** (TEXT)
———————————————
➤ [ `.o2` ] **⤳** (TEXT)
———————————————
➤ [ `.bish` ] **⤳** (TEXT)
———————————————
➤ [ `.latex` ] **⤳** (TEXT)
———————————————
**With the following commands, you can set different filters on the photo you want**

➤ [ `.blue` ] **⤳** (Reply)
———————————————
➤ [ `.green` ] **⤳** (Reply)
———————————————
➤ [ `.red` ] **⤳** (Reply)
———————————————
➤ [ `.grey` ] **⤳** (Reply)
———————————————
➤ [ `.grey2` ] **⤳** (Reply)
———————————————
➤ [ `.sepia` ] **⤳** (Reply)
———————————————
➤ [ `.threshold` ] **⤳** (Reply)
———————————————
➤ [ `.blurple` ] **⤳** (Reply)
———————————————
➤ [ `.filter` ] **⤳** (Reply)
———————————————
**With the following commands, you can change the style and dimensions of the photo you want**

➤ [ `.bisexual` ] **⤳** (Reply)
———————————————
➤ [ `.blur` ] **⤳** (Reply)
———————————————
➤ [ `.horny` ] **⤳** (Reply)
———————————————
➤ [ `.stupid` ] **⤳** (Reply)
———————————————
➤ [ `.lesbian` ] **⤳** (Reply)
———————————————
➤ [ `.lgbt` ] **⤳** (Reply)
———————————————
➤ [ `.lolice` ] **⤳** (Reply)
———————————————
➤ [ `.non` ] **⤳** (Reply)
———————————————
➤ [ `.psexual` ] **⤳** (Reply)
———————————————
➤ [ `.pixel` ] **⤳** (Reply)
———————————————
➤ [ `.simp` ] **⤳** (Reply)
———————————————
➤ [ `.spin` ] **⤳** (Reply)
———————————————
➤ [ `.toni` ] **⤳** (Reply)
———————————————
**With the commands below, you can apply filters and fun changes to your desired photo**

➤ [ `.comrade` ] **⤳** (Reply)
———————————————
➤ [ `.gay` ] **⤳** (Reply)
———————————————
➤ [ `.glass` ] **⤳** (Reply)
———————————————
➤ [ `.jail` ] **⤳** (Reply)
———————————————
➤ [ `.wasted` ] **⤳** (Reply)
———————————————
➤ [ `.pass` ] **⤳** (Reply)
———————————————
"""

enhelp13 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ L - G Marker ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Create logo with text
➤ [ `.logo` ] **⤳** (TEXT)
———————————————
Create logo with text 2
➤ [ `.logo2` ] **⤳** (TEXT)
———————————————
Create logo with the desired text and design
➤ [ `.lg` ] **⤳** (TEXT Mode)
Mode: 1-138
———————————————
Create Gif with text
➤ [ `.gif` ] **⤳** (TEXT)
———————————————
Create Gif with text 2
➤ [ `.giff` ] **⤳** (TEXT)
———————————————
"""

enhelp14 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Compiler ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➤ [ `.py` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.js` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.php` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.kotlin` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.go` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.java` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.lua` ] **⤳** (Code) (Reply)
———————————————
➤ [ `.exec` ] **⤳** (Code)
———————————————
"""

enhelp15 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Tools ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
File Extraction
➤ [ `.unzip` ] **⤳** (Reply)
———————————————
Rename the file
➤ [ `.rname` ] **⤳** (TEXT) (Reply)
———————————————
Virtual number Checker
➤ [ `.check` ] **⤳** (Number)
———————————————
Screenshot of the text
➤ [ `.q` ] **⤳** (Reply)
———————————————
Screenshot of the desired text
➤ [ `.qq` ] **⤳** (TEXT)
———————————————
Results of Cricket matches
➤ [ `.cricket` ] **⤳**
———————————————
Weather
➤ [ `.weather` ] **⤳** (City Name)
———————————————
Azan time
➤ [ `.azan` ] **⤳** (City Name)
———————————————
Temperature Converter
➤ [ `.t` ] **⤳** (NUM c OR f)
eg: .t 25 c
———————————————
Digital Currency Converter
➤ [ `.c` ] **⤳** (NUM Currency1 Currency2)
eg: .c 100 usdt eur
———————————————
Calculator
➤ [ `.e` ] **⤳** (Match)
eg: .e 2+2
———————————————
Get the IP of the site
➤ [ `.ip` ] **⤳** (Domain)
———————————————
Get IP information
➤ [ `.whoisip` ] **⤳** (IP)
———————————————
Link Shortener
➤ [ `.link` ] **⤳** (URL)
———————————————
Link Shortener 2
➤ [ `.link2` ] **⤳** (URL)
———————————————
Get site ping
➤ [ `.p` ] **⤳** (Domain)
———————————————
Screenshot of the site
➤ [ `.screenshot` ] **⤳** (Domain)
———————————————
Screenshot of the site 2
➤ [ `.screenshot2` ] **⤳** (Domain)
———————————————
Screenshot of the site 3
➤ [ `.screenshot3` ] **⤳** (Domain)
———————————————
Screenshot of the site 4
➤ [ `.screenshot4` ] **⤳** (Domain)
———————————————
Screenshot of the site 5
➤ [ `.shot` ] **⤳** (Domain)
———————————————
Get GitHub Account information
➤ [ `.github` ] **⤳** (Username)
———————————————
Get Project information
➤ [ `.git` ] **⤳** (TEXT)
———————————————
Search in the dictionary
➤ [ `.dict` ] **⤳** (Word)
———————————————
Copy the profile of an account
➤ [ `.clone` ] **⤳** (ID) (Reply)
———————————————
Account Creation date
➤ [ `.i` ] **⤳** (ID) (Reply)
———————————————
Self Account Creation date
➤ [ `.creation` ]
———————————————
Self Account limit status
➤ [ `.limit` ]
———————————————
Get Country information
➤ [ `.country` ] **⤳** (Name)
———————————————
Convert Sticker to Photo
➤ [ `.tp` ] **⤳** (Reply)
———————————————
Convert Photo to Sticker
➤ [ `.ts` ] **⤳** (Reply)
———————————————
Create Gif
➤ [ `.tg` ] **⤳** (Reply)
———————————————
Translate to Persian
➤ [ `.fa` ] **⤳** (TEXT)
———————————————
Translate to English
➤ [ `.en` ] **⤳** (TEXT)
———————————————
Get the movie
➤ [ `.movie` ] **⤳** (TEXT)
———————————————
Get Anime
➤ [ `.anim` ] **⤳** (TEXT)
———————————————
Create Password with the desired number of characters
➤ [ `.pass` ] **⤳** (NUM)
———————————————
Convert text to Morse code
➤ [ `.morset` ] **⤳** (TEXT)
———————————————
Convert Morse code to text
➤ [ `.unmorset` ] **⤳** (Code)
———————————————
Get the date
➤ [ `.date` ]
———————————————
Get Account information
➤ [ `.id` ] **⤳** (ID) (Reply)
———————————————
Get Message information
➤ [ `.get_message` ] **⤳** (Reply)
———————————————
Mention a User
➤ [ `.mention` ] **⤳** (ID) (Reply)
———————————————
National code Check
➤ [ `.meli` ] **⤳** (Number)
———————————————
Check bank card
➤ [ `.estelam` ] **⤳** (Number)
———————————————
Get daily News
➤ [ `.news` ] **⤳** (Category)
Category: business, entertainment, general, health, science, sports, technology
———————————————
Get Bin card
➤ [ `.ccgen` ]
———————————————
Get daily News
➤ [ `.yjc` ]
———————————————
Extract Text from Photo
➤ [ `.ocr` ] **⤳** (Reply)
———————————————
Download timed Photo
➤ [ `.dl` ] **⤳** (Reply)
———————————————
Saved Messages
➤ [ `.waitt` ] **⤳** (Reply)
———————————————
Get the time
➤ [ `.time` ]
———————————————
"""

enhelp16 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Account ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Add Admin to Self
➤ [ `.addadmin` ] **⤳** (ID) (Reply)
———————————————
Delete Admin from Self
➤ [ `.deladmin` ] **⤳** (ID) (Reply)
———————————————
Admin list
➤ [ `.adminlist` ]
———————————————
Clear Admin list
➤ [ `.clearadminlist` ]
———————————————
Get Self Account ID
➤ [ `id` ]
———————————————
Self Account limit status
➤ [ `.limit` ]
———————————————
Self Account Creation date
➤ [ `.creation` ]
———————————————
Get Self Account session information
➤ [ `.session` ]
———————————————
"""

enhelp17 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Book ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Get joke
➤ [ `.joke` ]
———————————————
Get poem
➤ [ `.poem` ]
———————————————
Get Know
➤ [ `.know` ]
———————————————
Get quote
➤ [ `.quote` ]
———————————————
Search on Wikipedia
➤ [ `.wiki` ] **⤳** (TEXT)
———————————————
Search on Google
➤ [ `.google` ] **⤳** (TEXT)
———————————————
Convert Numbers to Letters
➤ [ `.num` ] **⤳** (NUM)
———————————————
Get Name information
➤ [ `.name` ] **⤳** (Name)
———————————————
Get biography
➤ [ `.bio` ]
———————————————
Get diary
➤ [ `.memo` ]
———————————————
Get pnp
➤ [ `.pnp` ]
———————————————
Get alaki
➤ [ `.alaki` ]
———————————————
Get hadis
➤ [ `.hadis` ]
———————————————
Get story
➤ [ `.dastan` ]
———————————————
Get random name
➤ [ `.rname` ]
———————————————
Get horoscope
➤ [ `.fal` ]
———————————————
Get istikhara
➤ [ `.estekhare` ]
———————————————
Get zekr
➤ [ `.zekr` ]
———————————————
"""

enhelp18 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Fun ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Cheating at dice
➤ [ `.tas` ] **⤳** (1-6)
———————————————
Cheating at darts
➤ [ `.dart` ]
———————————————
Cheating at bowling
➤ [ `.bowling` ]
———————————————
Cheating at basketball
➤ [ `.basketball` ]
———————————————
Cheating at football
➤ [ `.football` ] **⤳** (1 OR 6)
1: Fail
4: Goal
———————————————
Get random games 1
➤ [ `.game` ]
———————————————
Get random games 2
➤ [ `.bazi` ]
———————————————
Get random games 3
➤ [ `.hehe` ]
———————————————
**Other hobbies**

➤ [ `.moon` ]
———————————————
➤ [ `.clock` ]
———————————————
➤ [ `.thunder` ]
———————————————
➤ [ `.earth` ]
———————————————
➤ [ `.heart` ]
———————————————
➤ [ `.love` ]
———————————————
➤ [ `.santet` ]
———————————————
➤ [ `.nah` ]
———————————————
➤ [ `.ajg` ]
———————————————
➤ [ `.babi` ]
———————————————
➤ [ `.tank` ]
———————————————
➤ [ `.y` ]
———————————————
➤ [ `.awk` ]
———————————————
➤ [ `.tembak` ]
———————————————
➤ [ `.heli` ]
———————————————
➤ [ `.gabut` ]
———————————————
➤ [ `.syg` ]
———————————————
➤ [ `.dino` ]
———————————————
➤ [ `.hack` ]
———————————————
➤ [ `.fuck` ]
———————————————
➤ [ `.koc` ]
———————————————
➤ [ `.charging` ]
———————————————
➤ [ `.gang` ]
———————————————
➤ [ `.hypo` ]
———————————————
➤ [ `.ding` ]
———————————————
➤ [ `.wtf` ]
———————————————
➤ [ `.call` ]
———————————————
➤ [ `.bomb` ]
———————————————
➤ [ `.brain` ]
———————————————
➤ [ `.ahh` ]
———————————————
➤ [ `.hmm` ]
———————————————
"""

enhelp19 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Market ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
The price of goods in the Iranian market (BaSalam)
➤ [ `.price` ] **⤳** (TEXT)
———————————————
The price of goods in the Iranian market (Torob)
➤ [ `.qeymat` ] **⤳** (TEXT)
———————————————
Digital Currencies symbols list
➤ [ `.cryptolist` ]
———————————————
Digital Currency price
➤ [ `.crypto` ] **⤳** (Name)
———————————————
Digital Currency converter
➤ [ `.c` ] **⤳** (NUM Currency1 Currency2)
eg: .c 100 usdt eur
———————————————
Tron price
➤ [ `.trx` ]
———————————————
Currency price list
➤ [ `.arz` ]
———————————————
Check bank card
➤ [ `.estelam` ] **⤳** (Number)
———————————————
Get Digital Currency transaction information
➤ [ `.tara` ] **⤳** (TransLink)
———————————————
"""

enhelp20 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Sticker - Gif ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Create Sticker with text
➤ [ `.sticker` ] **⤳** (TEXT)
———————————————
Get Sticker information
➤ [ `.stickerinfo` ] **⤳** (Reply)
———————————————
Create Sticker with error code
➤ [ `.error` ] **⤳** (Code)
eg: .error 404
———————————————
Minimize Stickers and Pictures
➤ [ `.tiny` ] **⤳** (Reply)
———————————————
Convert Photo to Sticker
➤ [ `.ts` ] **⤳** (Reply)
———————————————
Create Gif
➤ [ `.tg` ] **⤳** (Reply)
———————————————
**Get random Gifs**

➤ [ `.palm` ]
———————————————
➤ [ `.wink` ]
———————————————
➤ [ `.hug` ]
———————————————
➤ [ `.pat` ]
———————————————
"""

enhelp21 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ AI ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**Textual AI**

➤ [ `.gpt3` ] **⤳** (TEXT)
———————————————
➤ [ `.gpt4` ] **⤳** (TEXT)
———————————————
➤ [ `.bard` ] **⤳** (TEXT)
———————————————
➤ [ `.asq` ] **⤳** (TEXT)
———————————————
➤ [ `.messi` ] **⤳** (TEXT)
———————————————
➤ [ `.ronaldo` ] **⤳** (TEXT)
———————————————
➤ [ `.ilon` ] **⤳** (TEXT)
———————————————
**Audio AI**

➤ [ `.` ] **⤳** (TEXT) Women
———————————————
➤ [ `/` ] **⤳** (TEXT) Man
———————————————
➤ [ `.voice` ] **⤳** (TEXT)
———————————————
➤ [ `.crush` ] **⤳** (TEXT)
———————————————
➤ [ `.wo` ] **⤳** (TEXT) Women
———————————————
➤ [ `.ma` ] **⤳** (TEXT) Man
———————————————
➤ [ `.v` ] **⤳** (TEXT)
———————————————
Get ID list
➤ [ `.vl` ]
———————————————
Set desired accent with ID
➤ [ `.sv` ] **⤳** (Mode)
———————————————
**Visual AI**

➤ [ `.pgpt` ] **⤳** (TEXT)
———————————————
"""

enhelp22 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Photo ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Create color
➤ [ `.color` ] **⤳** (Color)
———————————————
**Get random photos of animals**

➤ [ `.pikachu` ]
———————————————
➤ [ `.whale` 
———————————————
➤ [ `.foxx` ]
———————————————
➤ [ `.doggg` ]
———————————————
➤ [ `.rpanda` ]
———————————————
➤ [ `.raccoon` ]
———————————————
➤ [ `.panda` ]
———————————————
➤ [ `.koala` ]
———————————————
➤ [ `.kangroo` ]
———————————————
➤ [ `.fox` ]
———————————————
➤ [ `.dogg` ]
———————————————
➤ [ `.birdd` ]
———————————————
➤ [ `.catt` ]
———————————————
➤ [ `.bird` ]
———————————————
➤ [ `.dog` ]
———————————————
➤ [ `.cat` ]
———————————————
➤ [ `.robo` ] **⤳** (1-999999)
———————————————
**Get random +18 photos**

➤ [ `.couple` ]
———————————————
➤ [ `.ayang` ]
———————————————
➤ [ `.boob` ]
———————————————
➤ [ `.nude` ]
———————————————
➤ [ `.nude2` ]
———————————————
**Photo Search**

➤ [ `.pic` ]
———————————————
➤ [ `.bing` ]
———————————————
➤ [ `.uns` ]
———————————————
➤ [ `.photo` ]
———————————————
➤ [ `.photos` ]
———————————————
"""

enhelp23 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ Music ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**Search and download music with the following commands**

➤ [ `.music` ] **⤳** (TEXT)
———————————————
➤ [ `.youtube` ] **⤳** (TEXT)
———————————————
➤ [ `.musicc` ] **⤳** (TEXT)
———————————————
➤ [ `.remix` ] **⤳** (TEXT)
———————————————
➤ [ `.demo` ] **⤳** (TEXT)
———————————————
➤ [ `.classic` ] **⤳** (TEXT)
———————————————
➤ [ `.ahang` ] **⤳** (TEXT)
———————————————
➤ [ `.melo` ] **⤳** (TEXT)
———————————————
➤ [ `.global` ] **⤳** (TEXT)
———————————————
"""

enhelp24 = """
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
**[ System ]**
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Self On
[ ➤ `.on` ]
———————————————
Self Off
[ ➤ `.off` ]
———————————————
Restart Self
[ ➤ `.restart` ]
———————————————
Emergency shutdown Self
➤ [ `.shutdown` ]
———————————————
Get Self ping
➤ [ `.ping` ]
———————————————
Self Status
➤ [ `self` ]
———————————————
Get Self stats
➤ [ `.on_off_status` ]
———————————————
Processor information
➤ [ `.cpu` ]
———————————————
Memory information
➤ [ `.memory` ]
———————————————
System information
➤ [ `.system-inf` ]
———————————————
"""

openpanelbot = InlineKeyboardMarkup(
     [
         [
             InlineKeyboardButton("Panel", switch_inline_query_current_chat='panel')
         ]
     ]
)

keyboard_idk = ReplyKeyboardMarkup(
     [
         [
             ("Add Admin"),
             ("Delete Admin"),
             ("Admin List")
         ],
         [
             ("Add Owner"),
             ("Delete Owner"),
             ("Owner List")
         ]
     ],
one_time_keyboard=True,resize_keyboard=True)

@app.on_inline_query()
async def answer(client, inline_query):
     chat_id = inline_query.from_user.id
     AdminUser = get_data(f"SELECT * FROM adminlist WHERE id = {chat_id} LIMIT 1")
     if AdminUser is not None:
          if inline_query.query == "panel":
               languages = InlineKeyboardMarkup(
                    [
                         [
                              InlineKeyboardButton('فارسی 🇮🇷',callback_data=f'persian-{inline_query.from_user.id}')
                         ],
                         [
                              InlineKeyboardButton('🇬🇧 English',callback_data=f'english-{inline_query.from_user.id}')
                         ]
                    ]
               )

               await inline_query.answer(
                    results=[
                         InlineQueryResultArticle(
                              title="Helper",
                              input_message_content=InputTextMessageContent(f"**سلام {inline_query.from_user.first_name} خوش آمدید. لطفا یک زبان انتخاب کنید:\n\nHi {inline_query.from_user.first_name} Welcome. Please select a language:**"),
                              description="Helper Panel",
                              reply_markup=languages
                         ),
                    ],
                    cache_time=1
               )

          if inline_query.query == "coinprice":
               s = requests.get('https://api.nobitex.ir/market/stats?srcCurrency=usdt,trx,ton,btc,shib,eth,etc,usdt,ada,bch,ltc,bnb&dstCurrency=irt,rls,usdt')
               s = s.text
               js = json.loads(s)
               byusdt = js['stats']['usdt-irt']['bestBuy']
               sellusdt = js['stats']['usdt-irt']['bestSell']
               bytrx = js['stats']['trx-irt']['bestBuy']
               selltrx = js['stats']['trx-irt']['bestSell']
               byton = js['stats']['ton-irt']['bestBuy']
               sellton = js['stats']['ton-irt']['bestSell']
               byshib = js['stats']['shib-usdt']['bestBuy']
               sellshib = js['stats']['shib-usdt']['bestSell']
               bybit = js['stats']['btc-usdt']['bestBuy']
               sellbit = js['stats']['btc-usdt']['bestSell']
               byet = js['stats']['eth-usdt']['bestBuy']
               sellet = js['stats']['eth-usdt']['bestSell']
               byetc = js['stats']['etc-usdt']['bestBuy']
               selletc = js['stats']['etc-usdt']['bestSell']
               byada = js['stats']['ada-usdt']['bestBuy']
               sellada = js['stats']['ada-usdt']['bestSell']
               bybch = js['stats']['bch-usdt']['bestBuy']
               sellbch = js['stats']['bch-usdt']['bestSell']
               byltc = js['stats']['ltc-usdt']['bestBuy']
               sellltc = js['stats']['ltc-usdt']['bestSell']
               bybnb = js['stats']['bnb-usdt']['bestBuy']
               sellbnb = js['stats']['bnb-usdt']['bestSell']

               coind = InlineKeyboardMarkup(
                    [
                         [
                              InlineKeyboardButton("Currency", callback_data="outside"),
                              InlineKeyboardButton("Best Buy", callback_data="outside"),
                              InlineKeyboardButton("Best Sell", callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("USDT", callback_data="outside"),
                              InlineKeyboardButton("☫%s" % byusdt, callback_data="outside"),
                              InlineKeyboardButton("☫%s" % sellusdt, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("TRX", callback_data="outside"),
                              InlineKeyboardButton("☫%s" % bytrx, callback_data="outside"),
                              InlineKeyboardButton("☫%s" % selltrx, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("TON", callback_data="outside"),
                              InlineKeyboardButton("☫%s" % byton, callback_data="outside"),
                              InlineKeyboardButton("☫%s" % sellton, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("SHIB", callback_data="outside"),
                              InlineKeyboardButton("$%s" % byshib, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellshib, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("BTC", callback_data="outside"),
                              InlineKeyboardButton("$%s" % bybit, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellbit, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("ETH", callback_data="outside"),
                              InlineKeyboardButton("$%s" % byet, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellet, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("ETC", callback_data="outside"),
                              InlineKeyboardButton("$%s" % byetc, callback_data="outside"),
                              InlineKeyboardButton("$%s" % selletc, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("ADA", callback_data="outside"),
                              InlineKeyboardButton("$%s" % byada, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellada, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("BCH", callback_data="outside"),
                              InlineKeyboardButton("$%s" % bybch, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellbch, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("LTC", callback_data="outside"),
                              InlineKeyboardButton("$%s" % byltc, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellltc, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("BNB", callback_data="outside"),
                              InlineKeyboardButton("$%s" % bybnb, callback_data="outside"),
                              InlineKeyboardButton("$%s" % sellbnb, callback_data="outside")
                         ],
                         [
                              InlineKeyboardButton("Close ×", callback_data=f'Close-{inline_query.from_user.id}')
                         ]
                    ]
               )

               await inline_query.answer(
                    results=[
                         InlineQueryResultArticle(
                              title="Coin price",
                              input_message_content=InputTextMessageContent("➣ **Currency price list**"),
                              url="https://t.me/KING_MEMBEER",
                              description="ᴄʀɪᴛᴜs",
                              thumb_url="https://t.me/KING_MEMBEER/33",
                              reply_markup=coind
                         ),
                    ],
                    cache_time=1
               )

@app.on_callback_query()
async def call(app, call):
     AdminUser = get_data(f"SELECT * FROM adminlist WHERE id = '{call.from_user.id}' LIMIT 1")

     mark1 = InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton('سراسری - شخصی',callback_data=f'global_person1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('پروفایل',callback_data=f'profile1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('دانلودر',callback_data=f'downloader1-{call.from_user.id}'), 
                    InlineKeyboardButton('آپلودر',callback_data=f'uploader1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('حالت متن',callback_data=f'text_mode1-{call.from_user.id}'),
                    InlineKeyboardButton('حالت اکشن',callback_data=f'action_mode1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('وبهوک',callback_data=f'webhook1-{call.from_user.id}'),
                    InlineKeyboardButton('قفل ها',callback_data=f'locks1-{call.from_user.id}'),
                    InlineKeyboardButton('کرون جاب',callback_data=f'cronjob1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('آنتی لاگین',callback_data=f'antilogin1-{call.from_user.id}'),
                    InlineKeyboardButton('تبچی',callback_data=f'tabchi1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('ویرایشگر عکس',callback_data=f'photo_editor1-{call.from_user.id}'),
                    InlineKeyboardButton('گیف و لوگو ساز',callback_data=f'marker1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('کامپایلر',callback_data=f'compiler1-{call.from_user.id}'),
                    InlineKeyboardButton('ابزار ها',callback_data=f'tools1-{call.from_user.id}'),
                    InlineKeyboardButton('اکانت',callback_data=f'account1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('کتاب',callback_data=f'book1-{call.from_user.id}'),
                    InlineKeyboardButton('سرگرمی',callback_data=f'fun1-{call.from_user.id}'),
                    InlineKeyboardButton('بازار',callback_data=f'market1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('استیکر - گیف',callback_data=f'photo_gif1-{call.from_user.id}'),
                    InlineKeyboardButton('هوش مصنوعی',callback_data=f'ai1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('عکس',callback_data=f'photo1-{call.from_user.id}'),
                    InlineKeyboardButton('موزیک',callback_data=f'music1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('تنظیمات سیستم',callback_data=f'system1-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('● بستن پنل ●',callback_data=f'close1-{call.from_user.id}')
               ]
          ]
     )

     mark2 = InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton('𝗚𝗹𝗼𝗯𝗮𝗹 - 𝗣𝗲𝗿𝘀𝗼𝗻𝗮𝗹',callback_data=f'global_person2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗣𝗿𝗼𝗳𝗶𝗹𝗲',callback_data=f'profile2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿',callback_data=f'downloader2-{call.from_user.id}'), 
                    InlineKeyboardButton('𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗿',callback_data=f'uploader2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗧𝗲𝘅𝘁 𝗠𝗼𝗱𝗲',callback_data=f'text_mode2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗔𝗰𝘁𝗶𝗼𝗻 𝗠𝗼𝗱𝗲',callback_data=f'action_mode2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗪𝗲𝗯𝗵𝗼𝗼𝗸',callback_data=f'webhook2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗟𝗼𝗰𝗸𝘀',callback_data=f'locks2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗖𝗿𝗼𝗻 𝗝𝗼𝗯',callback_data=f'cronjob2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗔𝗻𝘁𝗶 𝗟𝗼𝗴𝗶𝗻',callback_data=f'antilogin2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗧𝗮𝗯𝗰𝗵𝗶',callback_data=f'tabchi2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗣𝗵𝗼𝘁𝗼 𝗘𝗱𝗶𝘁𝗼𝗿',callback_data=f'photo_editor2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗟 - 𝗚 𝗠𝗮𝗿𝗸𝗲𝗿',callback_data=f'marker2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗖𝗼𝗺𝗽𝗶𝗹𝗲𝗿',callback_data=f'compiler2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗧𝗼𝗼𝗹𝘀',callback_data=f'tools2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗔𝗰𝗰𝗼𝘂𝗻𝘁',callback_data=f'account2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗕𝗼𝗼𝗸',callback_data=f'book2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗙𝘂𝗻',callback_data=f'fun2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗠𝗮𝗿𝗸𝗲𝘁',callback_data=f'market2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗦𝘁𝗶𝗰𝗸𝗲𝗿 - 𝗚𝗶𝗳',callback_data=f'photo_gif2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗔𝗜',callback_data=f'ai2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗣𝗵𝗼𝘁𝗼',callback_data=f'photo2-{call.from_user.id}'),
                    InlineKeyboardButton('𝗠𝘂𝘀𝗶𝗰',callback_data=f'music2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('𝗦𝘆𝘀𝘁𝗲𝗺',callback_data=f'system2-{call.from_user.id}')
               ],
               [
                    InlineKeyboardButton('● 𝗖𝗹𝗼𝘀𝗲 𝗣𝗮𝗻𝗲𝗹 ●',callback_data=f'close2-{call.from_user.id}')
               ]
          ]
     )

     dast1 = InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("● بازگشت ●", callback_data=f'back1-{call.from_user.id}')
               ]
          ]
     )

     dast2 = InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton("● 𝗕𝗮𝗰𝗸 ●", callback_data=f'back2-{call.from_user.id}')
               ]
          ]
     )

     if call.data != "outside":
          if AdminUser is not None and int(call.from_user.id) == int(call.data.split("-")[1]):
     
	          if call.data.split("-")[0] == "persian":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=f"**سلام {call.from_user.first_name} به راهنمای ونوس سلف خوش آمدید. لطفا بخش مورد نظر خود را انتخاب کنید:**", reply_markup=mark1)

	          elif call.data.split("-")[0] == "english":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=f"**Hello {call.from_user.first_name} Welcome to Wenos Self help.\nPlease select the section you want:**", reply_markup=mark2)

	          elif call.data.split("-")[0] == "back1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=f"**سلام {call.from_user.first_name} به راهنمای ونوس سلف خوش آمدید. لطفا بخش مورد نظر خود را انتخاب کنید:**", reply_markup=mark1)

	          elif call.data.split("-")[0] == "back2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=f"**Hello {call.from_user.first_name} Welcome to Wenos Self help.\nPlease select the section you want:**", reply_markup=mark2)

	          elif call.data.split("-")[0] == "global_person1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp1, reply_markup=dast1)

	          elif call.data.split("-")[0] == "profile1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp2, reply_markup=dast1)

	          elif call.data.split("-")[0] == "downloader1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp3, reply_markup=dast1)

	          elif call.data.split("-")[0] == "uploader1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp4, reply_markup=dast1)

	          elif call.data.split("-")[0] == "text_mode1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp5, reply_markup=dast1)

	          elif call.data.split("-")[0] == "action_mode1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp6, reply_markup=dast1)

	          elif call.data.split("-")[0] == "webhook1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp7, reply_markup=dast1)

	          elif call.data.split("-")[0] == "locks1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp8, reply_markup=dast1)

	          elif call.data.split("-")[0] == "cronjob1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp9, reply_markup=dast1)

	          elif call.data.split("-")[0] == "antilogin1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp10, reply_markup=dast1)

	          elif call.data.split("-")[0] == "tabchi1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp11, reply_markup=dast1)

	          elif call.data.split("-")[0] == "photo_editor1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp12, reply_markup=dast1)

	          elif call.data.split("-")[0] == "marker1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp13, reply_markup=dast1)

	          elif call.data.split("-")[0] == "compiler1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp14, reply_markup=dast1)

	          elif call.data.split("-")[0] == "tools1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp15, reply_markup=dast1)

	          elif call.data.split("-")[0] == "account1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp16, reply_markup=dast1)

	          elif call.data.split("-")[0] == "book1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp17, reply_markup=dast1)

	          elif call.data.split("-")[0] == "fun1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp18, reply_markup=dast1)

	          elif call.data.split("-")[0] == "market1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp19, reply_markup=dast1)

	          elif call.data.split("-")[0] == "photo_gif1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp20, reply_markup=dast1)

	          elif call.data.split("-")[0] == "ai1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp21, reply_markup=dast1)

	          elif call.data.split("-")[0] == "photo1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp22, reply_markup=dast1)

	          elif call.data.split("-")[0] == "music1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp23, reply_markup=dast1)

	          elif call.data.split("-")[0] == "system1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=fahelp24, reply_markup=dast1)

	          elif call.data.split("-")[0] == "global_person2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp1, reply_markup=dast2)

	          elif call.data.split("-")[0] == "profile2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp2, reply_markup=dast2)

	          elif call.data.split("-")[0] == "downloader2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp3, reply_markup=dast2)

	          elif call.data.split("-")[0] == "uploader2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp4, reply_markup=dast2)

	          elif call.data.split("-")[0] == "text_mode2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp5, reply_markup=dast2)

	          elif call.data.split("-")[0] == "action_mode2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp6, reply_markup=dast2)

	          elif call.data.split("-")[0] == "webhook2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp7, reply_markup=dast2)

	          elif call.data.split("-")[0] == "locks2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp8, reply_markup=dast2)

	          elif call.data.split("-")[0] == "cronjob2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp9, reply_markup=dast2)

	          elif call.data.split("-")[0] == "antilogin2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp10, reply_markup=dast2)

	          elif call.data.split("-")[0] == "tabchi2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp11, reply_markup=dast2)

	          elif call.data.split("-")[0] == "photo_editor2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp12, reply_markup=dast2)

	          elif call.data.split("-")[0] == "marker2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp13, reply_markup=dast2)

	          elif call.data.split("-")[0] == "compiler2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp14, reply_markup=dast2)

	          elif call.data.split("-")[0] == "tools2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp15, reply_markup=dast2)

	          elif call.data.split("-")[0] == "account2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp16, reply_markup=dast2)

	          elif call.data.split("-")[0] == "book2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp17, reply_markup=dast2)

	          elif call.data.split("-")[0] == "fun2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp18, reply_markup=dast2)

	          elif call.data.split("-")[0] == "market2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp19, reply_markup=dast2)

	          elif call.data.split("-")[0] == "photo_gif2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp20, reply_markup=dast2)

	          elif call.data.split("-")[0] == "ai2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp21, reply_markup=dast2)

	          elif call.data.split("-")[0] == "photo2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp22, reply_markup=dast2)

	          elif call.data.split("-")[0] == "music2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp23, reply_markup=dast2)

	          elif call.data.split("-")[0] == "system2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text=enhelp24, reply_markup=dast2)

	          elif call.data.split("-")[0] == "close1":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text="**● پنل راهنما بسته شد ●**")

	          elif call.data.split("-")[0] == "close2":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text="**● Helper Panel Closed ●**")

	          elif call.data.split("-")[0] == "Close":
	               await app.edit_inline_text(inline_message_id=call.inline_message_id, text="**● Closed ●**")
          else:
               await call.answer("دسترسی غیر مجاز 🚫", show_alert=False)
     else:
          await call.answer("این دکمه نمایشی است", show_alert=True)

@app.on_message(filters.private&filters.command("restart"), group=1)
async def updates(app, m:Message):
     OwnerUser = get_data(f"SELECT * FROM ownerlist WHERE id = '{m.chat.id}' LIMIT 1")
     if OwnerUser is not None:
          await app.send_message(m.chat.id, "**Helper Restart was successful**")
          python = sys.executable
          os.execl(python, python, *sys.argv)
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
    
@app.on_message(filters.private&filters.command("panel"))
async def updates(app, m:Message):
     OwnerUser = get_data(f"SELECT * FROM ownerlist WHERE id = '{m.chat.id}' LIMIT 1")
     if OwnerUser is not None:
          await app.send_message(m.chat.id, "**QuiteCreateCliBot Panel Owner**", reply_markup=keyboard_idk)
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
    
@app.on_message(filters.private&filters.command("start"))
async def updates(app, m:Message):
     AdminUser = get_data(f"SELECT * FROM adminlist WHERE id = '{m.chat.id}' LIMIT 1")
     if AdminUser is not None:
          await app.send_message(m.chat.id, f"𝑯𝒆𝒍𝒍𝒐 {m.from_user.first_name}\n𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑯𝒆𝒍𝒑𝒆𝒓 𝑩𝒐𝒕 💛\n𝑭𝒐𝒓 𝒈𝒆𝒕 𝑷𝒂𝒏𝒆𝒍 𝒕𝒚𝒑𝒆 ( `help` 𝑶𝒓 `panel` 𝑶𝒓 `پنل` )\n     ", reply_markup=openpanelbot)
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")
     else:
          await m.delete()
   #______________________________Owner Panel________________________

Back = ReplyKeyboardMarkup(
     [
          [
               ("Back")
          ]
     ],resize_keyboard=True
)

@app.on_message(filters.private)
async def updates(app, m:Message):
 OwnerUser = get_data(f"SELECT * FROM ownerlist WHERE id = '{m.chat.id}' LIMIT 1")
 if OwnerUser is not None:
     user = get_data(f"SELECT * FROM user WHERE id = '{m.chat.id}' LIMIT 1")
     OwnerList = get_datas("SELECT * FROM ownerlist")
     AdminList = get_datas("SELECT * FROM adminlist")
     text = m.text

     if text == "Back":
          await app.send_message(m.chat.id, "**QuiteCreateCliBot Panel Owner**", reply_markup=keyboard_idk)
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

     elif text == "Add Admin":
          await app.send_message(m.chat.id, "**Send Me User ID**:", reply_markup=Back)
          update_data(f"UPDATE user SET step = 'addadmin' WHERE id = '{m.chat.id}' LIMIT 1")

     elif user["step"] == "addadmin":
          if text.isdigit():
               user_id = int(text.strip())
               if get_data(f"SELECT * FROM adminlist WHERE id = '{user_id}' LIMIT 1") is None:
                    await app.send_message(m.chat.id, f"Successfull\nUser [ `{user_id}` ] Added to Admin List")
                    update_data(f"INSERT INTO adminlist(id) VALUES({user_id})")
               else:
                    await app.send_message(m.chat.id, "This user in the Admin list")
          else:
               await app.send_message(m.chat.id, "Invalid entry! Only sending numbers is allowed")

     elif text == "Delete Admin":
          await app.send_message(m.chat.id, "**Send Me User ID**:", reply_markup=Back)
          update_data(f"UPDATE user SET step = 'deladmin' WHERE id = '{m.chat.id}' LIMIT 1")

     elif user["step"] == "deladmin":
          if text.isdigit():
               user_id = int(text.strip())
               if get_data(f"SELECT * FROM adminlist WHERE id = '{user_id}' LIMIT 1") is not None:
                    await app.send_message(m.chat.id, f"Successfull\nUser [ `{user_id}` ] Deleted From User List")
                    update_data(f"DELETE FROM adminlist WHERE id = '{user_id}' LIMIT 1")
               else:
                    await app.send_message(m.chat.id, f"This user not in Admin list")
          else:
               await app.send_message(m.chat.id, "Invalid entry! Only sending numbers is allowed")
             
     elif text == "Admin List":
          s = ""
          if AdminList:
               for index, user in enumerate(AdminList, start=1):
                    s += f"֍ {index} -> `{user[0]}`\n"
               await app.send_message(m.chat.id, f"**Admin List:**\n{s}")
          else:
               await app.send_message(m.chat.id, f"**Admin List is Empty**")
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

     elif text == "Add Owner":
          await app.send_message(m.chat.id, "**Send Me User ID**:", reply_markup=Back)
          update_data(f"UPDATE user SET step = 'addowner' WHERE id = '{m.chat.id}' LIMIT 1")

     elif user["step"] == "addowner":
          if text.isdigit():
               user_id = int(text.strip())
               if get_data(f"SELECT * FROM ownerlist WHERE id = '{user_id}' LIMIT 1") is None:
                    if get_data(f"SELECT * FROM adminlist WHERE id = '{user_id}' LIMIT 1") is not None:
                         await app.send_message(m.chat.id, f"Successfull\nUser [ `{user_id}` ] Added to Owner List")
                         update_data(f"INSERT INTO ownerlist(id) VALUES({user_id})")
                    else:
                         await app.send_message(m.chat.id, "ابتدا کاربر مورد نظر را به لیست ادمین اضافه کنید!")
               else:
                    await app.send_message(m.chat.id, "This user in the Owner list")
          else:
               await app.send_message(m.chat.id, "Invalid entry! Only sending numbers is allowed")

     elif text == "Delete Owner":
          await app.send_message(m.chat.id, "**Send Me User ID**:", reply_markup=Back)
          update_data(f"UPDATE user SET step = 'delowner' WHERE id = '{m.chat.id}' LIMIT 1")

     elif user["step"] == "delowner":
          if text.isdigit():
               user_id = int(text.strip())
               if get_data(f"SELECT * FROM ownerlist WHERE id = '{user_id}' LIMIT 1") is not None:
                    await app.send_message(m.chat.id, f"Successfull\nUser [ `{user_id}` ] Deleted From User List")
                    update_data(f"DELETE FROM ownerlist WHERE id = '{user_id}' LIMIT 1")
               else:
                    await app.send_message(m.chat.id, f"This user not in Owner list")
          else:
               await app.send_message(m.chat.id, "Invalid entry! Only sending numbers is allowed")
             
     elif text == "Owner List":
          s = ""
          if OwnerList:
               for index, user in enumerate(OwnerList, start=1):
                    s += f"֍ {index} -> `{user[0]}`\n"
               await app.send_message(m.chat.id, f"**Owner List:**\n{s}")
          else:
               await app.send_message(m.chat.id, f"**Owner List is Empty**")
          update_data(f"UPDATE user SET step = 'none' WHERE id = '{m.chat.id}' LIMIT 1")

app.start(), print(Fore.YELLOW+"Started..."), idle(), app.stop()
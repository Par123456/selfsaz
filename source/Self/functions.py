# نسخه جدید دیباگ : 5
# صفر تا صد توسط @Camaeal دیباگ شده 
# اگه ننت خراب نیست اسکی میری منبع بزن

#تنها نسخه سالم و دیباگ در حال حاضر همین نسخه فقط اگه لازم داشتید خودتون api اضافه کنید برای هوش مصنوعی و ...

import os

import aiofiles
import aiohttp
import ffmpeg
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent


def transcode(filename):
#    newpath = 'ffmpeg' 
#    if not os.path.exists(newpath):
#        os.makedirs(newpath)
    ffmpeg.input(filename).output(
        "input.raw",
        format="s16le",
        acodec="pcm_s16le",
        ac=2,
        ar="48k",
        loglevel="error",
    ).overwrite_output().run()
    os.remove(filename)

async def download_and_transcode_song(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open("song.mp3", mode="wb")
                await f.write(await resp.read())
                await f.close()
    transcode("song.mp3")

def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover_square(requested_by, title, artist, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(str(BASE_DIR/"cache"/"1.jpg"))
    image2 = Image.open("etc/foreground_square.png")
    image3 = changeImageSize(600, 500, image1)
    image4 = changeImageSize(600, 500, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(BASE_DIR/"font.ttf"), 20)
    draw.text((150, 380), f"Title: {title}", (255, 255, 255), font=font)
    draw.text((150, 405), f"Artist: {artist}", (255, 255, 255), font=font)
    draw.text(
        (150, 430),
        f"Duration: {duration} Seconds",
        (255, 255, 255),
        font=font,
    )

    draw.text(
        (150, 455),
        f"Played By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open(str(BASE_DIR/"cache"/"PNG"/"Foreground.png"))
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(BASE_DIR/"font.ttf"), 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Played By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")

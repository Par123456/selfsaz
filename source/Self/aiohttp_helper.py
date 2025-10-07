# نسخه جدید دیباگ : 5
# صفر تا صد توسط @Camaeal دیباگ شده 
# اگه ننت خراب نیست اسکی میری منبع بزن

#تنها نسخه سالم و دیباگ در حال حاضر همین نسخه فقط اگه لازم داشتید خودتون api اضافه کنید برای هوش مصنوعی و ...

import json

import aiohttp


class AioHttp:
    @staticmethod
    async def get_json(link):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
            async with session.get(link) as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
            async with session.get(link) as resp:
                return await resp.text()

    @staticmethod
    async def get_json_from_text(link):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
            async with session.get(link) as resp:
                text = await resp.text()
                return json.loads(text)

    @staticmethod
    async def get_raw(link):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
            async with session.get(link) as resp:
                return await resp.read()

    @staticmethod
    async def get_url(link):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as session:
            async with session.get(link) as resp:
                return resp.url

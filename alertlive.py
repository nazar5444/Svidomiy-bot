import json

from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp_sse_client import client as sse_client

import alert
import db

TOKEN = "5636715243:AAGoPgmHYLVPiUAEsLe5xQigPN8vCVQNQs8"

bot = Bot(token=TOKEN, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def send_notification(user_id, message):
    keyboard_map = types.InlineKeyboardMarkup()
    band_button = types.InlineKeyboardButton(text="Напрямок ракет 🚀", url="https://de-raketa.info/")
    keyboard_map.add(band_button)
    await bot.send_message(chat_id=user_id, text=message, reply_markup=keyboard_map)


async def alertlive_func():
    headers = {"X-API-Key": "5ebcb2ed4d4fd3d565a3d4ae028c0242c5e583d8"}
    async with sse_client.EventSource(
            'https://alerts.com.ua/api/states/live',
            headers=headers, timeout=-1
    ) as event_source:
        try:
            async for event in event_source:
                if event.type == "hello":
                    print("SSE Conected sucsessfully")
                if event.type == "update":
                    data = json.loads(event.data)
                    state = data["state"]
                    res = db.cur.execute("SELECT user_id FROM users WHERE city_id::text = %s", (str(state["id"]),))
                    id_list_changes = db.cur.fetchall()
                    city_url = alert.city_list_alert.get(str(state["id"]))
                    if id_list_changes:
                        for user_id in id_list_changes:
                            if state["alert"] is False:
                                if db.is_alert_on(user_id):
                                    await send_notification(user_id[0],
                                                            'Відбій повітряної тривоги у {} оласті. 🔕'.format(
                                                                city_url))
                            elif state["alert"] is True:
                                if db.is_alert_on(user_id):
                                    await send_notification(user_id[0],
                                                            'Увага! Повітряна тривога у {} області. Негайно перейдіть до найближчого укриття! 🔔'.format(
                                                                city_url))
        except ConnectionError:
            pass

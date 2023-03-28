import asyncio
import os

import aiohttp
import requests
import torch
from PIL import Image
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType
from aiogram.utils import executor

import alert
import btns
import db
import text
from db import db_start
from detection import tokenizer, preprocess, model

TOKEN = "5636715243:AAGoPgmHYLVPiUAEsLe5xQigPN8vCVQNQs8"

bot = Bot(token=TOKEN, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def on_startup(_):
    await db_start()


class States(StatesGroup):
    ocup_verif = State()
    bomb_verif = State()
    description_bomb = State()
    photo_bomb = State()
    send_bomb_state = State()
    bomb_geo = State()
    ocup_send = State()
    bomb_send = State()
    back_bomb = State()
    back_bad = State()
    city_list = State()
    maps_list = State()
    city_state_id = State()
    photo = State()
    ocup_geo = State()
    geo_bomb = State()
    send_state = State()
    description = State()
    bomb_photo = State()


async def main():
    async with aiohttp.ClientSession() as session:
        await db_start()
        asyncio.create_task(dp.start_polling())
        await session.close()


@dp.message_handler(Text(equals="Незламність ⚡️"), state="*")
async def phone(message: types.Message):
    if message.text == "Незламність ⚡️":
        next_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nezlb2")
        citichoose2 = InlineKeyboardMarkup(row_width=2).add(next_btn)
        nezlam = await db.city_get(user_id=message.from_user.id)
        await bot.send_message(message.from_user.id, text.page_1.get(nezlam), reply_markup=citichoose2)


@dp.callback_query_handler(text="nezlp1", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    next_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nezlb2")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(next_btn)
    nezlam = await db.city_get(user_id=callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=text.page_1.get(nezlam), reply_markup=citichoose2)


@dp.callback_query_handler(text="nezlb2", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    prev1_btn = InlineKeyboardButton(text="⬅ Назад", callback_data="nezlp1")
    next_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nezlb3")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(prev1_btn, next_btn)
    nezlam = await db.city_get(user_id=callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=text.page_2.get(nezlam), reply_markup=citichoose2)


@dp.callback_query_handler(text="nezlb3", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    prev1_btn = InlineKeyboardButton(text="⬅ Назад", callback_data="nezlb2")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(prev1_btn)
    nezlam = await db.city_get(user_id=callback.from_user.id)
    await bot.edit_message_text(chat_id=callback.from_user.id, message_id=callback.message.message_id,
                                text=text.page_3.get(nezlam), reply_markup=citichoose2)


@dp.message_handler(Text(equals="Повідомити ✉"), state="*")
async def phone(message: types.Message):
    if message.text == "Повідомити ✉" and await db.verif_profile(user_id=message.from_user.id) == "False":
        keyboard_phone = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Надіслати телефон 📞", request_contact=True)
        button_back = types.KeyboardButton(text="Назад ◀️")
        keyboard_phone.add(button_phone, button_back)
        await bot.send_message(message.from_user.id,
                               'Щоб отримати доступ до цього меню ви повинні підтвердити свою особистість за допомогою '
                               'номера телефона. Натисніть на кнопку "Надіслати телефон".',
                               reply_markup=keyboard_phone)
        await States.bomb_verif.set()
    else:
        await bot.send_message(message.chat.id, "Будьте обережні!", reply_markup=btns.bomb_send_menu)
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Снаряд 💣"), state="*")
async def back(message: types.Message):
    if message.text == "Снаряд 💣":
        await bot.send_message(message.chat.id, "Оберіть потрібний пункт за допомогою кнопок нижче.",
                               reply_markup=btns.bomb_menu)


@dp.message_handler(Text(equals="Перевірити 🔍"), state="*")
async def back(message: types.Message):
    if message.text == "Перевірити 🔍":
        await bot.send_message(message.chat.id, "Надішліть фото для роспізнання. Результати можуть бути не точними!", reply_markup=btns.keyboard_back)
        await States.bomb_photo.set()


@dp.message_handler(Text(equals="Тривога 🔈"), state="*")
async def back(message: types.Message):
    if message.text == "Тривога 🔈":
        keyboard_aid = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_injury = types.KeyboardButton(text="Стан тривоги ⏰")
        button_bad = types.KeyboardButton(text="Повідомлення 💬")
        button_menu = types.KeyboardButton("Повернутися в головне меню ◀️")
        keyboard_aid.add(button_bad, button_injury, button_menu)
        await bot.send_message(message.from_user.id, "Оберіть потрібний пункт за допомогою кнопок нижче.",
                               reply_markup=keyboard_aid)


@dp.message_handler(Text(equals="Стан тривоги ⏰"), state="*")
async def back(message: types.Message):
    keyboard_map = types.InlineKeyboardMarkup()
    ban_button = types.InlineKeyboardButton(text="Мапа тривог", url="https://alerts.in.ua/")
    keyboard_map.add(ban_button)
    city_req_id = requests.get(alert.link.format(city_id=await db.city_get(user_id=message.from_user.id)),
                               headers=alert.headers)
    if "false" in city_req_id.text:
        await bot.send_message(message.from_user.id,
                               "Повітряна тривога у вашому місті відсутня. Для більш точної інформації натисніть на кнопку нижче:",
                               reply_markup=keyboard_map)
    else:
        await bot.send_message(message.from_user.id, "В вашому місті повітряна тривога! Негайно перейдіть до "
                                                     "найближчого укриття. Для більш точної інформації натисніть на кнопку нижче:",
                               reply_markup=keyboard_map)


@dp.message_handler(Text(equals="Назад ◀️"), state=States.back_bad)
async def back(message: types.Message):
    if message.text == "Назад ◀️":
        await bot.send_message(message.from_user.id, "Ви повенулися назад.", reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="Назад ◀️"), state=States.bomb_send)
async def back(message: types.Message):
    if message.text == "Назад ◀️":
        await bot.send_message(message.from_user.id, "Ви повенулися назад.", reply_markup=btns.bomb_menu)


@dp.message_handler(Text(equals="Назад ◀️"), state=States.bomb_verif)
async def back(message: types.Message):
    if message.text == "Назад ◀️":
        await bot.send_message(message.from_user.id, "Ви повенулися назад.", reply_markup=btns.bomb_menu)


@dp.message_handler(Text(equals="Назад ◀️"), state=States.ocup_verif)
async def back(message: types.Message):
    if message.text == "Назад ◀️":
        await bot.send_message(message.from_user.id, "Ви повенулися назад.", reply_markup=btns.keyboard_plt)


@dp.message_handler(Text(equals="Назад ◀️"), state=States.bomb_photo)
async def back(message: types.Message):
    if message.text == "Назад ◀️":
        await bot.send_message(message.from_user.id, "Ви повенулися назад.", reply_markup=btns.bomb_menu)


@dp.message_handler(Text(equals="Повернутися в головне меню ◀️"), state="*")
async def back(message: types.Message):
    if message.text == "Повернутися в головне меню ◀️":
        await bot.send_message(message.from_user.id, "Ви повернулися в меню.", reply_markup=btns.keyboard_plt)
        await States.geo_bomb.set()


async def send_ocup_to_admin(user_id, photo_data, geo_lat_data, geo_long_data, description_data):
    keyboard_ban = types.InlineKeyboardMarkup()
    ban_button = types.InlineKeyboardButton(text="Заблокувати 🔒", callback_data=f"ban:{user_id}")
    unban_button = types.InlineKeyboardButton(text="Розблокувати 🔓", callback_data=f"unban:{user_id}")
    deldat_button = types.InlineKeyboardButton(text="Очистити 🗑", callback_data=f"deldata:{user_id}")
    send_button = types.InlineKeyboardButton(text="Надіслано ✅", callback_data=f"sendmessage:{user_id}")
    keyboard_ban.add(ban_button, unban_button, deldat_button, send_button)
    admin_id = 5517129511
    lat = geo_lat_data
    long = geo_long_data
    dsc = description_data
    await bot.send_photo(chat_id=admin_id, photo=photo_data,
                         caption=f"User ID: {user_id}\n\nПоложення окупантів за:\nДовготою: {lat} \nШиротою: {long} \n\nОпис: {dsc}",
                         reply_markup=keyboard_ban)


async def send_bomb_to_admin(user_id, photo_data, geo_lat_data, geo_long_data, description_data):
    keyboard_ban = types.InlineKeyboardMarkup()
    ban_button = types.InlineKeyboardButton(text="Заблокувати 🔒", callback_data=f"ban:{user_id}")
    unban_button = types.InlineKeyboardButton(text="Розблокувати 🔓", callback_data=f"unban:{user_id}")
    deldat_button = types.InlineKeyboardButton(text="Очистити 🗑", callback_data=f"deldata:{user_id}")
    send_button = types.InlineKeyboardButton(text="Надіслано ✅", callback_data=f"sendmessage:{user_id}")
    keyboard_ban.add(ban_button, unban_button, deldat_button, send_button)
    admin_id = 5517129511
    lat = geo_lat_data
    long = geo_long_data
    dsc = description_data
    await bot.send_photo(chat_id=admin_id, photo=photo_data,
                         caption=f"User ID: {user_id}\n\nПоложення снаряду за:\nДовготою: {lat} \nШиротою: {long} \n\nОпис: {dsc}",
                         reply_markup=keyboard_ban)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('sendmessage:'))
async def send_user(callback_query: types.CallbackQuery):
    _, user_id = callback_query.data.split(':')
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id, text="Данні видалено. ✅")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('deldata:'))
async def del_user(callback_query: types.CallbackQuery):
    _, user_id = callback_query.data.split(':')
    await db.photo_delete(user_id=user_id)
    await db.lat_delete(user_id=user_id)
    await db.long_delete(user_id=user_id)
    await db.description_delete(user_id=user_id)
    await db.del_profile(user_id=user_id)
    await bot.answer_callback_query(callback_query.id, text="Данні були видалені. 🗑")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('ban:'))
async def ban_user(callback_query: types.CallbackQuery):
    _, user_id = callback_query.data.split(':')
    await db.ban_user(user_id=user_id)
    await bot.answer_callback_query(callback_query.id, text="Користувач був заблокований. 🔒")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('unban:'))
async def unban_user(callback_query: types.CallbackQuery):
    _, user_id = callback_query.data.split(':')
    await db.unban_user(user_id=user_id)
    await bot.answer_callback_query(callback_query.id, text="Користувач був розблокований. 🔓")


@dp.message_handler(Text(equals="Перевірити інформацію ✅"), state=States.ocup_send)
async def back(message: types.Message):
    keyboard_ban = types.InlineKeyboardMarkup()
    ban_button = types.InlineKeyboardButton(text="Контакти", url="https://t.me/Svidomiy_Admin")
    keyboard_ban.add(ban_button)
    user_id = message.from_user.id
    if db.is_banned(user_id):
        await bot.send_message(user_id, "Ви були заблоковані. Зверніться до адміністратора.", reply_markup=keyboard_ban)
        return

    photo_data = await db.photo_get(user_id=user_id)
    geo_lat_data = await db.lat_get(user_id=user_id)
    geo_long_data = await db.long_get(user_id=user_id)
    description_data = await db.description_get(user_id=user_id)
    if not photo_data or not geo_lat_data or not geo_long_data or not description_data:
        await bot.send_message(user_id, "Будь ласка, надішліть фото та геолокацію, щоб продовжити.")
        return

    lat = geo_lat_data
    long = geo_long_data
    dsc = description_data

    await bot.send_photo(chat_id=user_id, photo=photo_data,
                         caption=f"Положення окупантів за:\n\nДовготою: {lat} \nШиротою: {long}\n\n Опис: {dsc}")
    reply = "Якщо всі данні були вказано вірно, натисніть на конпку: Надіслати"
    await message.answer(reply, reply_markup=btns.send)
    await States.send_state.set()


@dp.message_handler(Text(equals="Надіслати ✉️"), state=States.send_state)
async def back(message: types.Message):
    if message.text == "Надіслати ✉️":
        user_id = message.from_user.id
        photo_data = await db.photo_get(user_id=user_id)
        geo_lat_data = await db.lat_get(user_id=user_id)
        geo_long_data = await db.long_get(user_id=user_id)
        description_data = await db.description_get(user_id=user_id)
        await send_ocup_to_admin(user_id, photo_data, geo_lat_data, geo_long_data, description_data)
        await db.photo_delete(user_id=user_id)
        await db.lat_delete(user_id=user_id)
        await db.long_delete(user_id=user_id)
        await db.description_delete(user_id=user_id)
        await bot.send_message(message.chat.id, "Ми отримали ваші данні. Дякую за спіпрацю!",
                               reply_markup=btns.ocupant_menu)
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Видалити 🗑"), state=States.send_state)
async def back(message: types.Message):
    if message.text == "Видалити 🗑":
        user_id = message.from_user.id
        await db.photo_delete(user_id=user_id)
        await db.lat_delete(user_id=user_id)
        await db.long_delete(user_id=user_id)
        await db.description_delete(user_id=user_id)
        await bot.send_message(message.chat.id, "Інформація була видалена.", reply_markup=btns.ocupant_menu)
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.photo)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.ocupant_menu)
        await message.delete()
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.ocup_geo)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.ocupant_menu)
        await message.delete()
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.send_state)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.ocupant_menu)
        await message.delete()
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.ocup_send)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.ocupant_menu)
        await message.delete()


@dp.message_handler(Text(equals="Окупант ⚔"), state="*")
async def phone(message: types.Message):
    if message.text == "Окупант ⚔" and await db.verif_profile(user_id=message.from_user.id) == "False":
        keyboard_phone = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Надіслати телефон 📞", request_contact=True)
        keyboard_phone.add(button_phone, btns.button_menu)
        await bot.send_message(message.from_user.id,
                               'Щоб отримати доступ до цього меню ви повинні підтвердити свою особистість за допомогою '
                               'номера телефона. Натисніть на кнопку "Надіслати телефон".',
                               reply_markup=keyboard_phone)
        await States.ocup_verif.set()
    else:
        await bot.send_message(message.chat.id, "Будьте обережні!", reply_markup=btns.ocupant_menu)
        await States.ocup_send.set()


@dp.message_handler(Text(equals="Прикріпити фотографію 📷"), state=States.ocup_send)
async def back(message: types.Message):
    if message.text == "Прикріпити фотографію 📷":
        await States.photo.set()
        await bot.send_message(message.chat.id, "Надішліть фото окупантів:", reply_markup=btns.menu_ocup_back)


@dp.message_handler(Text(equals="Прикріпити геолокацію 📍"), state=States.ocup_send)
async def back(message: types.Message):
    if message.text == "Прикріпити геолокацію 📍":
        await States.ocup_geo.set()
        await bot.send_message(message.chat.id, "Надішліть геолокацію окупантів:", reply_markup=btns.ocupant_geo_sent)


@dp.message_handler(content_types=ContentType.PHOTO, state=States.photo)
async def photo(message: types.Message):
    await db.photo_add(user_id=message.from_user.id, photo=message.photo[0].file_id)
    await States.description.set()
    await bot.send_message(message.chat.id, "Додайте опис для фото:")


@dp.message_handler(state=States.description)
async def description(message: types.Message):
    await db.description_add(user_id=message.from_user.id, description=message.text)
    await bot.send_message(message.chat.id, "Ви прикріпили фото.", reply_markup=btns.ocupant_menu)
    await States.ocup_send.set()


@dp.message_handler(content_types="location", state=States.ocup_geo)
async def ocup_geo(message: types.Message):
    geoloclat = message.location.latitude
    geoloclong = message.location.longitude
    await db.lat_add(user_id=message.from_user.id, geo_lat=geoloclat)
    await db.long_add(user_id=message.from_user.id, geo_long=geoloclong)
    await bot.send_message(message.chat.id, "Ви прикріпили геолокацію.", reply_markup=btns.ocupant_menu)
    await States.ocup_send.set()


@dp.message_handler(content_types=['contact'], state=States.bomb_verif)
async def contact(message: types.Message, state: FSMContext, number=None) -> None:
    async with state.proxy() as data:
        data[number] = message.contact.phone_number
    if message.forward_from is not None:
        await bot.send_message(message.chat.id, "Некоректний номер телефону.")
    else:
        num = message.contact.phone_number
        await db.edit_profile(user_id=message.from_user.id, phone_number=num)
        if num.startswith(str("+380")) or num.startswith(str("380")):
            await bot.send_message(message.chat.id, "Ваш номер: {}.\n\nДякую за підтвредженя своєї особи! "
                                                    "Будьте обережні та робіть фото тільки в тому разі якщо нічого не "
                                                    "загрожує вашому життю!".format(num),
                                   reply_markup=btns.bomb_send_menu)
            await db.change_profile(user_id=message.from_user.id)
            await States.bomb_send.set()
        else:
            await bot.send_message(message.chat.id, "Некоректний номер телефону.")


@dp.message_handler(content_types=['contact'], state=States.ocup_verif)
async def contact(message: types.Message, state: FSMContext, number=None) -> None:
    async with state.proxy() as data:
        data[number] = message.contact.phone_number
    if message.forward_from is not None:
        await bot.send_message(message.chat.id, "Некоректний номер телефону.")
    else:
        num = message.contact.phone_number
        await db.edit_profile(user_id=message.from_user.id, phone_number=num)
        if num.startswith(str("+380")) or num.startswith(str("380")):
            await bot.send_message(message.chat.id, "Ваш номер: {}.\n\nДякую за підтвредженя своєї особи! "
                                                    "Будьте обережні та робіть фото тільки в тому разі якщо нічого не "
                                                    "загрожує вашому життю!".format(num),
                                   reply_markup=btns.ocupant_menu)
            await db.change_profile(user_id=message.from_user.id)
            await States.ocup_send.set()
        else:
            await bot.send_message(message.chat.id, "Некоректний номер телефону.")


@dp.message_handler(content_types=['location'], state=States.geo_bomb)
async def handle_location(message: types.Message):
    city_data = await db.city_get(user_id=message.from_user.id)
    maps_url = alert.maps_list.get(city_data)
    geobtn = InlineKeyboardButton(text="Найближче укриття",
                                  url=maps_url.format(
                                      latt=message.location.latitude, long=message.location.longitude))
    geo = InlineKeyboardMarkup().add(geobtn)
    reply = "Ви можете знайти найближче за посиланням яке знаходиться нижче."
    await message.answer(reply, reply_markup=geo)


@dp.message_handler(commands=['start'], state="*")
async def handle(message: types.Message) -> None:
    city = InlineKeyboardButton(text="Одеська обл.", callback_data="14")
    city1 = InlineKeyboardButton(text="Дніпропетровська обл.", callback_data="3")
    city2 = InlineKeyboardButton(text="Чернігівська обл.", callback_data="23")
    city3 = InlineKeyboardButton(text="Харківська обл.", callback_data="19")
    city4 = InlineKeyboardButton(text="Житомирська обл.", callback_data="5")
    city5 = InlineKeyboardButton(text="Полтавська обл.", callback_data="15")
    city6 = InlineKeyboardButton(text="Херсонська обл.", callback_data="20")
    city7 = InlineKeyboardButton(text="Київська обл.", callback_data="9")
    next_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nextb")
    citichoose = InlineKeyboardMarkup(row_width=2).add(city, city1, city2, city3, city4, city5, city6, city7, next_btn)
    with open("photos/IMG_20230219_011909_687.jpg", 'rb') as logo:
        await bot.send_photo(chat_id=message.from_user.id, photo=logo,
                             caption=f"Вітаю Вас у нашому чат-боті! Тут зібрані різні корисні функції, які допоможуть "
                                     f"вам під час воєнного стану 🇺🇦")
        reply = "Оберіть вашу область зі списку нижче: "
        await message.answer(reply, reply_markup=citichoose)
        await db.profile(user_id=message.from_user.id, verified="False")
        await message.delete()


@dp.message_handler(Text(equals="Повідомлення 💬"), state="*")
async def smstrivoga(message: types.Message):
    keyboard_ban = types.InlineKeyboardMarkup()
    on_button = types.InlineKeyboardButton(text="Вкл. 🔔", callback_data="alert_on")
    off_button = types.InlineKeyboardButton(text="Викл. 🔕", callback_data="alert_off")
    keyboard_ban.add(on_button, off_button)
    await bot.send_message(message.from_user.id,
                           "За допомогою кнопок нижче ви можете включити або включити сповіщення про повітряну тривогу у вашому місті.",
                           reply_markup=keyboard_ban)


@dp.callback_query_handler(text="alert_on", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    await db.alert_on(user_id=callback.from_user.id)
    await bot.answer_callback_query(callback.id, text="У РОЗРОБЦІ! 👷")


@dp.callback_query_handler(text="alert_off", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    await db.alert_off(user_id=callback.from_user.id)
    await bot.answer_callback_query(callback.id, text="У РОЗРОБЦІ! 👷")


@dp.callback_query_handler(text="nextb", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    city8 = InlineKeyboardButton(text="Запорізька обл.", callback_data="7")
    city9 = InlineKeyboardButton(text="Луганська обл.", callback_data="11")
    city10 = InlineKeyboardButton(text="Донецька обл.", callback_data="4")
    city11 = InlineKeyboardButton(text="Вінницька обл.", callback_data="1")
    city12 = InlineKeyboardButton(text="Миколаївська обл.", callback_data="13")
    city13 = InlineKeyboardButton(text="Кропивницька обл.", callback_data="10")
    city14 = InlineKeyboardButton(text="Сумська обл.", callback_data="17")
    city15 = InlineKeyboardButton(text="Львівська обл.", callback_data="12")
    prev1_btn = InlineKeyboardButton(text="⬅ Назад", callback_data="prewb")
    prev2_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nextb1")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(city8, city9, city10, city11, city12, city13, city14, city15,
                                                        prev1_btn, prev2_btn)
    await callback.message.edit_reply_markup(reply_markup=citichoose2)


@dp.callback_query_handler(text="nextb1", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    city16 = InlineKeyboardButton(text="Черкаська обл.", callback_data="22")
    city17 = InlineKeyboardButton(text="Хмельницька обл.", callback_data="21")
    city18 = InlineKeyboardButton(text="Волинська обл.", callback_data="2")
    city19 = InlineKeyboardButton(text="Рівненська обл.", callback_data="16")
    city20 = InlineKeyboardButton(text="Івано-Франківська обл.", callback_data="8")
    city21 = InlineKeyboardButton(text="Тернопільська обл.", callback_data="18")
    city22 = InlineKeyboardButton(text="Закарпатська обл.", callback_data="6")
    city23 = InlineKeyboardButton(text="Чернівецька обл.", callback_data="23")
    prev1_btn = InlineKeyboardButton(text="⬅ Назад", callback_data="prewb1")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(city16, city17, city18, city19, city20, city21, city22, city23,
                                                        prev1_btn)
    await callback.message.edit_reply_markup(reply_markup=citichoose2)


@dp.callback_query_handler(text="prewb1", state="*")
async def nextprs_btn(callback: types.CallbackQuery):
    city8 = InlineKeyboardButton(text="Запорізька обл.", callback_data="7")
    city9 = InlineKeyboardButton(text="Луганська обл.", callback_data="11")
    city10 = InlineKeyboardButton(text="Донецька обл.", callback_data="4")
    city11 = InlineKeyboardButton(text="Вінницька обл.", callback_data="1")
    city12 = InlineKeyboardButton(text="Миколаївська обл.", callback_data="13")
    city13 = InlineKeyboardButton(text="Кропивницька обл.", callback_data="10")
    city14 = InlineKeyboardButton(text="Сумська обл.", callback_data="17")
    city15 = InlineKeyboardButton(text="Львівська обл.", callback_data="12")
    prev1_btn = InlineKeyboardButton(text="⬅ Назад", callback_data="prewb")
    prev2_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nextb1")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(city8, city9, city10, city11, city12, city13, city14, city15,
                                                        prev1_btn, prev2_btn)
    await callback.message.edit_reply_markup(reply_markup=citichoose2)


@dp.callback_query_handler(text="prewb", state="*")
async def prewprs_btn(callback: types.CallbackQuery):
    city = InlineKeyboardButton(text="Одеська обл.", callback_data="14")
    city1 = InlineKeyboardButton(text="Дніпропетровська обл.", callback_data="3")
    city2 = InlineKeyboardButton(text="Чернігівська обл.", callback_data="23")
    city3 = InlineKeyboardButton(text="Харківська обл.", callback_data="19")
    city4 = InlineKeyboardButton(text="Житомирська обл.", callback_data="5")
    city5 = InlineKeyboardButton(text="Полтавська обл.", callback_data="15")
    city6 = InlineKeyboardButton(text="Херсонська обл.", callback_data="20")
    city7 = InlineKeyboardButton(text="Київська обл.", callback_data="9")
    next1_btn = InlineKeyboardButton(text="Вперед ➡", callback_data="nextb")
    citichoose2 = InlineKeyboardMarkup(row_width=2).add(city, city1, city2, city3, city4, city5, city6, city7,
                                                        next1_btn)
    await callback.message.edit_reply_markup(reply_markup=citichoose2)


@dp.callback_query_handler(state="*")
async def city_cd_handler(callback: types.CallbackQuery, state: FSMContext):
    city_url = alert.city_list.get(callback.data)
    await States.city_list.set()
    await state.update_data(city_list=city_url)

    city_id_callback = callback.data
    await States.city_state_id.set()
    await state.update_data(city_state_id=city_id_callback)
    await db.city_add(user_id=callback.from_user.id, city_id=city_id_callback)

    await callback.message.answer(
        text="Ви обрали {} область! Меню з корисною інформацією знаходиться нижче.".format(city_url),
        reply_markup=btns.keyboard_plt)
    await States.geo_bomb.set()


@dp.message_handler(Text(equals="Тех.підтримка 🛠"), state="*")
async def back(message: types.Message):
    if message.text == "Тех.підтримка 🛠":
        keyboard_ban = types.InlineKeyboardMarkup()
        ban_button = types.InlineKeyboardButton(text="Контакти", url="https://t.me/Svidomiy_Admin")
        keyboard_ban.add(ban_button)
        await bot.send_message(message.from_user.id,
                               "Для контакту з Адміністрацією чат-боту напишіть на контакти вказані нижче.",
                               reply_markup=keyboard_ban)


@dp.message_handler(Text(equals="Перша допомога 🏥"), state="*")
async def back(message: types.Message):
    if message.text == "Перша допомога 🏥":
        await bot.send_message(message.from_user.id, "Оберіть потрібний пункт за допомогою кнопок нижче.",
                               reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="Людині погано"), state="*")
async def phone(message: types.Message):
    if message.text == "Людині погано":
        pplbad = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_napad = types.KeyboardButton(text="Серцевий напад ❤️‍🩹")
        button_svidomist = types.KeyboardButton(text="Без свідомості 🧠")
        button_backa = types.KeyboardButton(text="Назад ◀️")
        pplbad.add(button_napad, button_svidomist, button_backa)
        await bot.send_message(message.from_user.id, "Виберіть потрібний пункт:", reply_markup=pplbad)
        await States.back_bad.set()


@dp.message_handler(Text(equals="Без свідомості 🧠"), state="*")
async def phone(message: types.Message):
    if message.text == "Без свідомості 🧠":
        tako = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffo = types.KeyboardButton(text="Не реагує ❌")
        button_takl = types.KeyboardButton(text="Відповів(ла) ✅")
        button_backb = types.KeyboardButton(text="Назад ◀️")
        tako.add(button_ffo, button_takl, button_backb)
        await bot.send_message(message.from_user.id, 'Зверніться до неї. Голосно запитайте: "Ви мене чуєте?"',
                               reply_markup=tako)


@dp.message_handler(Text(equals="Не реагує ❌"), state="*")
async def phone(message: types.Message):
    if message.text == "Не реагує ❌":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Швидка їде 🚑")
        button_backc = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_backc)
        await bot.send_message(message.from_user.id,
                               '1. Покличте оточуючих людей на допомогу. \n\n2. Викличте швидку по телефону 103 або '
                               'попросіть когось це зробити. \n\n3. Будь ласка, повідомте швидкій: Що сталося. Де '
                               'сталося. Приблизний вік потерпілого. Стать потерпілого. Дайте відповідь на питання '
                               'диспетчера. Диспетчер повинен повісити трубку першим. \n\n4. Подбайте про те, '
                               'щоб швидку '
                               'було кому зустріти.',
                               reply_markup=takg)


@dp.message_handler(Text(equals="Швидка їде 🚑"), state="*")
async def phone(message: types.Message):
    if message.text == "Швидка їде 🚑":
        await bot.send_message(message.from_user.id, "Дякуємо, що не залишилися байдужими.",
                               reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="Відповіла ✅"), state="*")
async def phone(message: types.Message):
    if message.text == "Відповіла ✅":
        await bot.send_message(message.from_user.id, "Дякуємо, що не залишилися байдужими.",
                               reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="Серцевий напад ❤️‍🩹"), state="*")
async def phone(message: types.Message):
    if message.text == "Серцевий напад ❤️‍🩹":
        napad = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_tak = types.KeyboardButton(text="Так ✅")
        button_ni = types.KeyboardButton(text="Ні ❌")
        button_backf = types.KeyboardButton(text="Назад ◀️")
        napad.add(button_tak, button_ni, button_backf)
        await bot.send_message(message.from_user.id,
                               "Перевірте, чи є такі симптоми: \n\n- Ускладнене дихання. \n\n- Біль у грудях, "
                               "що відображається в шию, руку, живіт. \n\n- Холодний піт, відчуття страху. \n\nЧи "
                               "присутні "
                               "якісь з цих симптомів?",
                               reply_markup=napad)


@dp.message_handler(Text(equals="Ні ❌"), state="*")
async def phone(message: types.Message):
    if message.text == "Ні ❌":
        await bot.send_message(message.from_user.id,
                               "Швидше за все підозрювати серцевий напад не варто. \n\nПроте, якщо сумніваєтеся, "
                               "краще перестрахуватися і викликати швидку.",
                               reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="Так ✅"), state="*")
async def phone(message: types.Message):
    if message.text == "Так ✅":
        tak = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_tak = types.KeyboardButton(text="Викликали швидку 🏥")
        button_backd = types.KeyboardButton(text="Назад ◀️")
        tak.add(button_tak, button_backd)
        await bot.send_message(message.from_user.id,
                               "Викличте швидку: \n\n1. Покличте оточуючих людей на допомогу. \n\n2. Викличте швидку "
                               "по "
                               "телефону 103 або попросіть когось це зробити. \n\n3. Будь ласка, повідомте швидкій: Що "
                               "сталося. Де сталося. Приблизний вік потерпілого. Стать потерпілого. Дайте відповідь "
                               "на питання диспетчера. Диспетчер повинен повісити трубку першим. \n\n4. Подбайте, "
                               "щоб швидку було кому зустріти.",
                               reply_markup=tak)


@dp.message_handler(Text(equals="Викликали швидку 🏥"), state="*")
async def phone(message: types.Message):
    if message.text == "Викликали швидку 🏥":
        tak = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_tak = types.KeyboardButton(text="Швидка приїхала 🚑")
        button_sv = types.KeyboardButton(text="Втрата свідомості")
        button_backg = types.KeyboardButton(text="Назад ◀️")
        tak.add(button_tak, button_sv, button_backg)
        await bot.send_message(message.from_user.id,
                               "Викличте швидку: \n\n1. Покличте оточуючих людей на допомогу. \n\n2. Викличте швидку "
                               "по "
                               "телефону 103 або попросіть когось це зробити. \n\n3. Будь ласка, повідомте швидкій: Що "
                               "сталося. Де сталося. Приблизний вік потерпілого. Стать потерпілого. Дайте відповідь "
                               "на питання диспетчера. Диспетчер повинен повісити трубку першим. \n\n4. Подбайте, "
                               "щоб швидку було кому зустріти.",
                               reply_markup=tak)


@dp.message_handler(Text(equals="Втрата свідомості"), state="*")
async def phone(message: types.Message):
    if message.text == "Втрата свідомості":
        hhtak = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_tak = types.KeyboardButton(text="Швидка приїхала 🚑")
        button_backh = types.KeyboardButton(text="Назад ◀️")
        hhtak.add(button_tak, button_backh)
        with open("gif/unconsciousPosition.mp4", 'rb') as polozhenia:
            await bot.send_animation(chat_id=message.from_user.id, animation=polozhenia)
        await bot.send_message(message.from_user.id, "Переведіть людину в безпечну позицію та чекайте приїзду швидкої.",
                               reply_markup=hhtak)


@dp.message_handler(Text(equals="Швидка приїхала 🚑"), state="*")
async def phone(message: types.Message):
    if message.text == "Швидка приїхала 🚑":
        await bot.send_message(message.from_user.id, "Дякуємо, що не залишилися байдужими.",
                               reply_markup=btns.keyboard_aid)


@dp.message_handler(Text(equals="У людини травма"), state="*")
async def phone(message: types.Message):
    if message.text == "У людини травма":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Сильна кровотеча 🩸")
        button_ffh = types.KeyboardButton(text="Зламала кінцівку 🦴")
        button_backi = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_ffh, button_backi)
        await bot.send_message(message.from_user.id, "Виберіть потрібний пункт:", reply_markup=takg)
        await States.back_bad.set()


@dp.message_handler(Text(equals="Сильна кровотеча 🩸"), state="*")
async def phone(message: types.Message):
    if message.text == "Сильна кровотеча 🩸":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Зупинилася ✅")
        button_ffh = types.KeyboardButton(text="Не зупинилася ❌")
        button_backj = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_ffh, button_backj)
        await bot.send_message(message.from_user.id,
                               "1. Попросіть постраждалого щільно притиснути рану рукою. Це повинно уповільнити "
                               "кровотечу. \n\n2. Покличте оточуючих людей на допомогу. \n\n3. Викличте швидку по "
                               "телефону "
                               "103 або попросіть когось це зробити. \n\n4. Повідомте швидкій: Що сталося. Де сталося. "
                               "Приблизний вік потерпілого. Стать потерпілого. Дайте відповідь на питання диспетчера. "
                               "Диспетчер повинен повісити трубку першим. \n\n5. Подбайте, щоб швидку було кому "
                               "зустріти. "
                               "Кровотеча зупинилася?",
                               reply_markup=takg)


@dp.message_handler(Text(equals="Зламала кінцівку 🦴"), state="*")
async def phone(message: types.Message):
    if message.text == "Зламала кінцівку 🦴":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Швидка приїхала 🚑")
        button_backk = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_backk)
        await bot.send_message(message.from_user.id,
                               "Попросіть потерпілого не рухатися. \n\n1. Підкладіть м'яку тканину під зламану "
                               "кінцівку, "
                               "забезпечивши цим комфорт потерпілого. \n\n2. Якщо потерпілий зламав руку і він в змозі "
                               "підтримувати її здоровою рукою - не заважайте цьому. \n\n3. Не намагайтеся вправити "
                               "перелом або накласти шину. Це може нашкодити. \n\n4. Переконайтеся, що швидка їде і "
                               "її є "
                               "кому зустріти. \n\n5. Прикладіть через тканину холод до місця перелому не більше ніж "
                               "на "
                               "20 хвилин. Якщо швидка ще не приїхала: \n\n1. Запишіть ім'я і прізвище потерпілого. "
                               "\n\n2. "
                               "Дізнайтеся контакти його близьких, щоб повідомити про випадок. \n\n3. По можливості "
                               "дочекайтеся приїзду швидкої. \n\n4. Розмовляйте з ним.",
                               reply_markup=takg)


@dp.message_handler(Text(equals="Зупинилася ✅"), state="*")
async def phone(message: types.Message):
    if message.text == "Зупинилася ✅":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Швидка приїхала 🚑")
        button_backl = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_backl)
        await bot.send_message(message.from_user.id,
                               "1. Запишіть ім'я і прізвище потерпілого. \n\n2. Дізнайтеся контакти його близьких, "
                               "щоб повідомити про випадок. \n\n3. По можливості дочекайтеся приїзду швидкої. 4. "
                               "Розмовляйте з ним.",
                               reply_markup=takg)


@dp.message_handler(Text(equals="Не зупинилася ❌"), state="*")
async def phone(message: types.Message):
    if message.text == "Не зупинилася ❌":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Швидка приїхала 🚑")
        button_backm = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_backm)
        with open("gif/bleedingPressSource.mp4", 'rb') as krov:
            await bot.send_animation(chat_id=message.from_user.id, animation=krov)
        await bot.send_message(message.from_user.id,
                               "1. Обов'язково надіньте медичні рукавички або їх аналог. \n\n2. Щільно притисніть рану "
                               "своєю рукою. Тисніть прямо туди, звідки тече кров. \n\n3. Якщо поруч є люди, "
                               "попросіть принести бинти або знайти шматок чистої тканини (футболка, рушник, "
                               "простирадло і т.д.). \n\n4. Зім'явши тканину, сильно притисніть рану. Як показано на "
                               "відео.",
                               reply_markup=takg)


@dp.message_handler(Text(equals="Не реагує ❌"), state="*")
async def phone(message: types.Message):
    if message.text == "Не реагує ❌":
        takg = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_ffg = types.KeyboardButton(text="Швидка їде 🚑")
        button_backn = types.KeyboardButton(text="Назад ◀️")
        takg.add(button_ffg, button_backn)
        await bot.send_message(message.from_user.id,
                               '1. Покличте оточуючих людей на допомогу. \n\n2. Викличте швидку по телефону 103 або '
                               'попросіть когось це зробити. \n\n3. Будь ласка, повідомте швидкій: Що сталося. Де '
                               'сталося. Приблизний вік потерпілого. Стать потерпілого. Дайте відповідь на питання '
                               'диспетчера. Диспетчер повинен повісити трубку першим. \n\n4. Подбайте про те, '
                               'щоб швидку '
                               'було кому зустріти.',
                               reply_markup=takg)


@dp.message_handler(Text(equals="Перевірити інформацію ✅"), state=States.bomb_send)
async def back(message: types.Message):
    keyboard_ban = types.InlineKeyboardMarkup()
    ban_button = types.InlineKeyboardButton(text="Контакти", url="https://t.me/Svidomiy_Admin")
    keyboard_ban.add(ban_button)
    user_id = message.from_user.id
    if db.is_banned(user_id):
        await bot.send_message(user_id, "Ви були заблоковані. Зверніться до адміністратора.", reply_markup=keyboard_ban)
        return

    photo_data = await db.photo_get(user_id=user_id)
    geo_lat_data = await db.lat_get(user_id=user_id)
    geo_long_data = await db.long_get(user_id=user_id)
    description_data = await db.description_get(user_id=user_id)
    if not photo_data or not geo_lat_data or not geo_long_data or not description_data:
        await bot.send_message(user_id, "Будь ласка, надішліть фото та геолокацію, щоб продовжити.")
        return

    lat = geo_lat_data
    long = geo_long_data
    dsc = description_data

    await bot.send_photo(chat_id=user_id, photo=photo_data,
                         caption=f"Положення снаряду за:\n\nДовготою: {lat} \nШиротою: {long}\n\n Опис: {dsc}")
    reply = "Якщо всі данні були вказано вірно, натисніть на конпку: Надіслати"
    await message.answer(reply, reply_markup=btns.send)
    await States.send_bomb_state.set()


@dp.message_handler(Text(equals="Надіслати ✉️"), state=States.send_bomb_state)
async def back(message: types.Message):
    if message.text == "Надіслати ✉️":
        user_id = message.from_user.id
        photo_data = await db.photo_get(user_id=user_id)
        geo_lat_data = await db.lat_get(user_id=user_id)
        geo_long_data = await db.long_get(user_id=user_id)
        description_data = await db.description_get(user_id=user_id)
        await send_bomb_to_admin(user_id, photo_data, geo_lat_data, geo_long_data, description_data)
        await db.photo_delete(user_id=user_id)
        await db.lat_delete(user_id=user_id)
        await db.long_delete(user_id=user_id)
        await db.description_delete(user_id=user_id)
        await bot.send_message(message.chat.id, "Ми отримали ваші данні. Дякую за спіпрацю!",
                               reply_markup=btns.bomb_send_menu)
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Видалити 🗑"), state=States.send_bomb_state)
async def back(message: types.Message):
    if message.text == "Видалити 🗑":
        user_id = message.from_user.id
        await db.photo_delete(user_id=user_id)
        await db.lat_delete(user_id=user_id)
        await db.long_delete(user_id=user_id)
        await db.description_delete(user_id=user_id)
        await bot.send_message(message.chat.id, "Інформація була видалена.", reply_markup=btns.bomb_send_menu)
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.photo_bomb)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.bomb_send_menu)
        await message.delete()
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.bomb_geo)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.bomb_send_menu)
        await message.delete()
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.send_bomb_state)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.bomb_send_menu)
        await message.delete()
        await States.bomb_send.set()


@dp.message_handler(Text(equals="Вибрати інший спосіб ◀️"), state=States.bomb_send)
async def back(message: types.Message):
    if message.text == "Вибрати інший спосіб ◀️":
        await bot.send_message(message.from_user.id, "Виберіть потрібний спосіб:", reply_markup=btns.bomb_send_menu)
        await message.delete()


@dp.message_handler(Text(equals="Прикріпити фотографію 📷"), state=States.bomb_send)
async def back(message: types.Message):
    if message.text == "Прикріпити фотографію 📷":
        await States.photo_bomb.set()
        await bot.send_message(message.chat.id, "Надішліть фото снаряду:", reply_markup=btns.menu_ocup_back)


@dp.message_handler(Text(equals="Прикріпити геолокацію 📍"), state=States.bomb_send)
async def back(message: types.Message):
    if message.text == "Прикріпити геолокацію 📍":
        await States.bomb_geo.set()
        await bot.send_message(message.chat.id, "Надішліть геолокацію снаряду:", reply_markup=btns.ocupant_geo_sent)


@dp.message_handler(content_types=ContentType.PHOTO, state=States.photo_bomb)
async def photo(message: types.Message):
    await db.photo_add(user_id=message.from_user.id, photo=message.photo[0].file_id)
    await States.description_bomb.set()
    await bot.send_message(message.chat.id, "Додайте опис для фото:")


@dp.message_handler(state=States.description_bomb)
async def description(message: types.Message):
    await db.description_add(user_id=message.from_user.id, description=message.text)
    await bot.send_message(message.chat.id, "Ви прикріпили фото.", reply_markup=btns.bomb_send_menu)
    await States.bomb_send.set()


@dp.message_handler(content_types="location", state=States.bomb_geo)
async def ocup_geo(message: types.Message):
    geoloclat = message.location.latitude
    geoloclong = message.location.longitude
    await db.lat_add(user_id=message.from_user.id, geo_lat=geoloclat)
    await db.long_add(user_id=message.from_user.id, geo_long=geoloclong)
    await bot.send_message(message.chat.id, "Ви прикріпили геолокацію.", reply_markup=btns.bomb_send_menu)
    await States.bomb_send.set()


@dp.message_handler(content_types=ContentType.PHOTO, state=States.bomb_photo)
async def photo(message: types.Message):
    photo_file = await message.photo[-1].download()
    photo_file.seek(0)
    image = preprocess(Image.open(photo_file.name)).unsqueeze(0)
    labels = tokenizer(["nothing found", "a grenade", "a military rocket", "a land mine"])

    with torch.no_grad(), torch.cuda.amp.autocast():
        image_features = model.encode_image(image)
        text_features = model.encode_text(labels)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

    rounded_probs = torch.round(text_probs * 100) / 100

    label_names = ["Нічого не знайдено", "Граната", "Снаряд", "Міна"]
    results = "Результати 🔍 \n\n"

    max_prob = max(rounded_probs[0])
    for i, label_prob in enumerate(rounded_probs[0]):
        label_prob_percent = int(label_prob * 100)
        label_name = label_names[i]
        if label_prob == max_prob:
            results += "🟢 "
        elif label_prob_percent > 10:
            results += "🟠 "
        else:
            results += "🔴 "

        results += f"{label_name}: {label_prob_percent}%\n"
    await message.reply(results)

    photo_file.close()
    os.remove(photo_file.name)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

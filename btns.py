from aiogram import types

keyboard_plt = types.ReplyKeyboardMarkup(resize_keyboard=True)
button = types.KeyboardButton("Укриття 🏰", request_location=True)
button1 = types.KeyboardButton("Незламність ⚡️")
button2 = types.KeyboardButton("Тривога 🔈")
button3 = types.KeyboardButton("Окупант ⚔")
button4 = types.KeyboardButton("Снаряд 💣")
button5 = types.KeyboardButton("Перша допомога 🏥")
keyboard_plt.add(button, button1, button2)
keyboard_plt.add(button3, button4)
keyboard_plt.add(button5)

bomb_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_ocupant_photo = types.KeyboardButton("Перевірити ✅")
button_ocupant_geo = types.KeyboardButton("Повідомити ✉")
button_menu = types.KeyboardButton("Повернутися в головне меню ◀️")
bomb_menu.add(button_ocupant_photo, button_ocupant_geo)
bomb_menu.add(button_menu)

keyboard_back = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_back = types.KeyboardButton(text="Назад ◀️")
keyboard_back.add(button_back)

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_menu = types.KeyboardButton("Повернутися в головне меню ◀️")
menu.add(button_menu)

menu_ocup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_menu_ocup_back = types.KeyboardButton("Вибрати інший спосіб ◀️")
menu_ocup_back.add(button_menu_ocup_back)

keyboard_aid = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_injury = types.KeyboardButton(text="У людини травма")
button_bad = types.KeyboardButton(text="Людині погано")
keyboard_aid.add(button_injury, button_bad, button_menu)

ocupant_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_ocupant_photo = types.KeyboardButton("Прикріпити фотографію 📷")
button_ocupant_geo = types.KeyboardButton("Прикріпити геолокацію 📍")
button_check = types.KeyboardButton("Перевірити інформацію ✅")
button_menu = types.KeyboardButton("Повернутися в головне меню ◀️")
ocupant_menu.add(button_ocupant_photo, button_ocupant_geo, button_check, button_menu)

bomb_send_menu = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_ocupant_photo = types.KeyboardButton("Прикріпити фотографію 📷")
button_ocupant_geo = types.KeyboardButton("Прикріпити геолокацію 📍")
button_check = types.KeyboardButton("Перевірити інформацію ✅")
button_menu = types.KeyboardButton("Назад ◀️")
bomb_send_menu.add(button_ocupant_photo, button_ocupant_geo, button_check, button_menu)


ocupant_geo_sent = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button_ocupant_geo_send = types.KeyboardButton("Надіслати геолокацію 📍", request_location=True)
button_ocupant_sposib = types.KeyboardButton("Вибрати інший спосіб ◀️   ")
ocupant_geo_sent.add(button_ocupant_geo_send, button_ocupant_sposib)

send = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
send_btn = types.KeyboardButton("Надіслати ✉️")
del_btn = types.KeyboardButton("Видалити 🗑")
button_ocupant_sposib = types.KeyboardButton("Вибрати інший спосіб ◀️")
send.add(send_btn, del_btn, button_ocupant_sposib)

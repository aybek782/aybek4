from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
cook_menu = KeyboardButton(text='Awqat menu')
ww_menu = KeyboardButton(text='Suw menu')
main_menu.add(cook_menu)
main_menu.add(ww_menu)
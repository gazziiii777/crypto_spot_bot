from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кнопка 1')],
    [KeyboardButton(text='Кнопка 2'), KeyboardButton(text='Кнопка 3')]
], resize_keyboard=True)
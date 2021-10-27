from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

comment_mode_but = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='С фото штрихкода', resize_keyboard=True, one_time_keyboard=True),
            KeyboardButton(text='Без фото', resize_keyboard=True, one_time_keyboard=True),
            KeyboardButton(text='Отмена', resize_keyboard=True, one_time_keyboard=True),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

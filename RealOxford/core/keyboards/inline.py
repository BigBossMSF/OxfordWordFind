from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ru_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Перевести RU🇷🇺", callback_data="translate_ru")
        ]
    ],
    resize_keyboard=True
)

en_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Перевести EN🇬🇧", callback_data="translate_en")
        ]
    ],
    resize_keyboard=True
)

from aiogram import F, Router
from aiogram.types import Message
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from core.keyboards.inline import ru_kb

import requests


router = Router()

ua = UserAgent()

headers = {'User-Agent': ua.random}


@router.message(F.text)
async def find_word(message: Message):
    word = message.text.lower()
    r = requests.get(url=f"https://www.oed.com/search/dictionary/?scope=Entries&q={word}", headers=headers)

    r.encoding = 'utf-8'

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        text = ''
        word_definitions = [snippet.text.strip() for snippet in soup.find_all('div', class_='snippet')]

        # print(f"---------------{word}-----------\n")
        for idx, definition in enumerate(word_definitions, start=1):
            if idx == 4:
                break
            text += f"{idx}. {definition}\n"

        await message.answer(text=text, reply_markup=ru_kb)

    else:
        print("Плохо1 статус код:", r.status_code)

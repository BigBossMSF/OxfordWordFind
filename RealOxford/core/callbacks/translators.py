from aiogram import Router, F
from aiogram.types import CallbackQuery
from deep_translator import GoogleTranslator
from core.keyboards.inline import ru_kb, en_kb

router = Router()


@router.callback_query(F.data.startswith("translate_"))
async def translate_ru(call: CallbackQuery):
    if call.data.endswith("ru"):
        text = GoogleTranslator(target='ru', source='auto').translate(call.message.text)
        await call.message.edit_text(text=text, reply_markup=en_kb)
    elif call.data.endswith("en"):
        text = GoogleTranslator(target='en', source='auto').translate(call.message.text)
        await call.message.edit_text(text=text, reply_markup=ru_kb)
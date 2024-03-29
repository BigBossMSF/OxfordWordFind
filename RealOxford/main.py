
import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.handlers import user_handlers
from core.handlers import user_commands
from core.callbacks import translators




token = ""
bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


async def main():

    try:
        dp.include_routers(
            user_commands.router,
            user_handlers.router,
            translators.router
        )
        await dp.start_polling(bot)
        logging.info("[BOT] start")
    finally:
        logging.info("[BOT] end polling")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
        logging.info("[START] Вызвана функция запуска")
    except Exception as e:
        logging.error(f"[START] smthng went wrong {e}")
        exit(1)


import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.tg.handlers import router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # на проде закомментировать, т.к. вывод в терминал занимает много времени
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

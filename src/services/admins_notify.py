import logging

from aiogram import Dispatcher

from src.config import ADMINS_ID


async def on_startup_netify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            text = 'Бот работает'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as error:
            logging.exception(error)

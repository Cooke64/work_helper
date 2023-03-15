import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound

from pydantic_config import settings


async def on_startup_netify(dp: Dispatcher):
    for admin in settings.ADMINS_ID:
        try:
            await dp.bot.send_message(chat_id=admin, text='Бот работает')
        except ChatNotFound:
            logging.error('Пользователи не найдены или ошибочный id для админа')

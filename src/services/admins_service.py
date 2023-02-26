import logging

from aiogram import Dispatcher

from src.config import ADMINS_ID
from src.database.tables import UserMessage


async def on_startup_netify(dp: Dispatcher):
    for admin in ADMINS_ID:
        try:
            text = 'Бот работает'
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as error:
            logging.exception(error)


def show_all_users(user_data: list[UserMessage]) -> str:
    messages = ''
    if not user_data:
        return 'Пользователей нет'
    for user in user_data:
        username = user.username
        passed_test = '<b>прошел тест</b>' if user.passed_test else '<b>не прошел тест</b>'
        can_serve = '<b>может служить</b>' if user.can_serve else '<b>не может служить</b>'
        text = user.message
        messages += f'Пользователь {username} {passed_test} и {can_serve}.\nОставил сообщение: {text}\n'
    return messages
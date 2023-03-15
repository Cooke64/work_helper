from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup
)

from keayboards.main_menu import main_menu_buttons, admin_menu
from pydantic_config import settings
from states.leave_message_state import LeaveMessageMain


def get_main_buttons(user_id: int) -> ReplyKeyboardMarkup:
    if user_id in settings.ADMINS_ID:
        return admin_menu
    return main_menu_buttons


async def start_leaving_message(bot_type: Message | CallbackQuery) -> None:
    messageor_query = isinstance(bot_type, Message)
    replyer = bot_type.answer if messageor_query else bot_type.message.answer
    await replyer(
        'Оставьте сообщение и как мы ответим вам можно скорее!'
    )
    await LeaveMessageMain.message_from.set()

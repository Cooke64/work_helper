from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from src.keayboards.main_menu import info_menu
from src.loader import dp


@dp.message_handler(Text(equals="🛂 Получить информацию"))
async def run_start_command(messages: Message):
    await messages.answer(
        f'Выберете соответствующую категорию',
        reply_markup=info_menu
    )


@dp.message_handler(Text(equals="❓Узнать статус трудоустройства"))
async def run_start_command(messages: Message):
    await messages.answer(
        f'{messages.from_user.full_name}, Ваша заявка находится на рассмотрении',
    )


@dp.message_handler(Text(equals="📞 Связаться с нами"))
async def get_call_me_back(messages: Message):
    await messages.answer(
        f'{messages.from_user.full_name}, в ближайшее время с вами свяжется наш сотрудник.',
    )

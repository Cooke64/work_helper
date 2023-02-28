from aiogram.types import Message

from loader import dp
from messages.message_text import HELP_TEXT


@dp.message_handler(text='/help')
async def run_start_command(messages: Message):
    await messages.answer(
        text=HELP_TEXT
    )

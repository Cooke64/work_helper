from aiogram.types import Message

from src.loader import dp
from src.messages.message_text import HELP_TEXT


@dp.message_handler(text='/help')
async def run_start_command(messages: Message):
    await messages.answer(
        text=HELP_TEXT
    )

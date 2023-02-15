from aiogram.types import Message

from src.loader import dp

text = 'call_back me'


@dp.message_handler(text='/call')
async def run_call_back(messages: Message):
    await messages.answer(
        text=text
    )

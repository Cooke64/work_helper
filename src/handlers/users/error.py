from aiogram.types import Message

from src.loader import dp


@dp.message_handler()
async def get_error_message(messages: Message):
    await messages.answer(
        f'Пожалуйста, следуйте инструкции. Я пока еще не настолько крут, как Chat GPT',
    )

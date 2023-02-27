from aiogram.types import Message

from src.loader import dp


@dp.message_handler()
async def get_error_message(message: Message):
    await message.answer(
        f'Пожалуйста, следуйте инструкции. Я пока еще не настолько крут, как Chat GPT',
    )

#
# @dp.errors_handlers()
# async def errors_handlers(update, exception):
#     pass
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from src.filters import IsPrivate
from src.keayboards.main_menu import main_menu_buttons
from src.loader import dp
from src.messages.message_text import HELLO_TEXT


@dp.message_handler(IsPrivate(), text='/start')
async def run_start_command(messages: Message):
    await messages.answer(
        f'Привет, {messages.from_user.full_name}. {HELLO_TEXT}',
        reply_markup=main_menu_buttons
    )
    print(messages.from_user)


@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Начнем с начала.",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer('Если что-то непонятно, используй /help',
                         reply_markup=main_menu_buttons)

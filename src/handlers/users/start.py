from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from src.database.service import get_user_by_id
from src.filters import IsPrivate
from src.keayboards.main_menu import main_menu_buttons
from src.loader import dp
from src.messages.message_text import HELLO_TEXT
from src.states.leave_message_state import LeaveMessage


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


@dp.message_handler(Text(equals='Вернуться в главное меню.'))
async def back_to_main_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Начнем с начала.", reply_markup=main_menu_buttons
    )


@dp.message_handler(Text(equals='✉ Оставить сообщение'))
async def get_message_from_user(message: Message):
    if get_user_by_id(message.from_user.id):
        await message.answer(
            'Ваше обращение в обработке'
        )
        return
    await message.answer(
        'Оставьте сообщение и как мы ответим вам можно скорее!'
    )
    await LeaveMessage.message_from_user.set()

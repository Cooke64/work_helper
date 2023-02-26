from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from src.config import ADMINS_ID
from src.database.user_crud import get_user_by_id
from src.filters import IsPrivate
from src.keayboards.main_menu import main_menu_buttons, admin_menu
from src.loader import dp
from src.messages.message_text import HELLO_TEXT, CANCEL_TEXT, START_AGAIN
from src.states.leave_message_state import LeaveMessage, LeaveMessageMain


def get_main_buttons(user_id):
    if user_id in ADMINS_ID:
        return admin_menu
    return main_menu_buttons


@dp.message_handler(IsPrivate(), text='/start')
async def run_start_command(messages: Message):
    buttons = get_main_buttons(messages.from_user.id)
    mes = f'Привет, {messages.from_user.full_name}.\n{HELLO_TEXT}'
    await messages.answer(mes, reply_markup=buttons)
    print(messages.from_user)


@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cmd_cancel(message: Message, state: FSMContext):
    buttons = get_main_buttons(message.from_user.id)
    await state.finish()
    await message.answer(START_AGAIN, reply_markup=ReplyKeyboardRemove())
    await message.answer(CANCEL_TEXT, reply_markup=buttons)


@dp.message_handler(Text(equals='Вернуться в главное меню.'))
async def back_to_main_menu(message: Message, state: FSMContext):
    await state.finish()
    buttons = get_main_buttons(message.from_user.id)
    await message.answer(START_AGAIN, reply_markup=buttons)


@dp.message_handler(Text(equals='✉ Оставить сообщение'))
async def get_message_from_user(message: Message):
    user = get_user_by_id(message.from_user.id)
    if user and user.message:
        await message.answer(
            'Ваше обращение в обработке'
        )
        return
    await message.answer(
        'Оставьте сообщение и как мы ответим вам можно скорее!'
    )
    await LeaveMessageMain.message_from.set()

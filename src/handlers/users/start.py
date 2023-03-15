import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from database.user_crud import get_user_by_id
from filters import IsPrivate
from keayboards.inline_buttons import SEND_MESSAGE_AGAIN
from loader import dp, bot
from messages.message_text import HELLO_TEXT, CANCEL_TEXT, START_AGAIN
from services.start_bot_service import get_main_buttons, start_leaving_message


@dp.message_handler(IsPrivate(), text='/start')
async def run_start_command(messages: Message):
    buttons = get_main_buttons(messages.from_user.id)
    mes = f'Привет, {messages.from_user.full_name}.\n{HELLO_TEXT}'
    await messages.answer(mes, reply_markup=buttons)
    logging.debug(messages.from_user)


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
            'Ваше обращение в обработке',
            reply_markup=SEND_MESSAGE_AGAIN
        )
        return
    await start_leaving_message(message)


@dp.callback_query_handler(Text(equals='send_agein'))
async def get_message_from_user(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    await start_leaving_message(call)

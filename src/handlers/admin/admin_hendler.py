from aiogram import types
from aiogram.dispatcher import FSMContext

from src.config import ADMINS_ID
from src.database import admin_crud as crud
from src.loader import dp
from src.services.admins_service import show_all_users
from src.states.leave_message_state import LeaveMessage

admin_commands = {
    'Все заявки': crud.show_limit_users,
    'Кто прошел тест': crud.get_passed_test
}
send_message = {
    '✉ Отправить сообщение всем пользователям': crud.get_users_id,
    '✉ Отправить сообщение всем админам': lambda: ADMINS_ID
}


@dp.message_handler(lambda mes: mes.text in admin_commands)
async def get_info_menu_admin(message: types.Message):
    user_data = admin_commands[message.text]()
    messages = show_all_users(user_data)
    await message.answer(
        f'Список всех пользователей\n{messages}',
    )


@dp.message_handler(lambda mes: mes.text in send_message)
async def send_message_by_command(message: types.Message, state: FSMContext):
    await message.answer(
        'здесь нужно ввести сообщение, которое отправим адрресатам'
    )
    await LeaveMessage.command.set()
    await state.update_data(command=message.text)
    await LeaveMessage.message_from_user.set()


@dp.message_handler(state=LeaveMessage.message_from_user)
async def get_and_send_message_to(message: types.Message, state: FSMContext):
    await state.update_data(message_from_user=message.text)
    data = await state.get_data()
    id_list = send_message[data.get('command')]()
    message_from_user = data.get('message_from_user')
    for user_id in id_list:
        await dp.bot.send_message(chat_id=user_id, text=message_from_user)
    await message.answer(
        f'Соообщение отправлено: {len(id_list)} адрессатам',
    )
    await state.finish()

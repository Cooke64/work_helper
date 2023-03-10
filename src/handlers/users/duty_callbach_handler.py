import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from database.user_crud import leave_message
from keayboards.inline_buttons import benefits, duty
from keayboards.main_menu import main_menu_buttons
from loader import dp, bot
from messages import benefits_message
from states.leave_message_state import LeaveMessageMain

message_data = {
    # льготы
    'benefits_зарплата': benefits_message.SALARY,
    'benefits_жилье': benefits_message.HOUSE,
    'benefits_пенсия': benefits_message.PENSION,
    'benefits_отпуск': benefits_message.REST,
    # обязанности
    'duty_обязанности': benefits_message.DUTY,
    'duty_запреты': benefits_message.PROHIBITIONS,
    'duty_требования': benefits_message.REQUIREMENTS

}

reply_keyboard = {
    'benefits': (benefits, "Про зарплату, льготы и т.д."),
    'duty': (duty, "Требования, обязанности, ограничения"),
}


@dp.callback_query_handler(lambda call: call.data in message_data)
async def get_info_about_benefits(call: types.CallbackQuery):
    if call.data in message_data:
        message = message_data[call.data]
        reply_data = reply_keyboard[call.data.split('_')[0]]
        # удаляет текущее сообщение бота и выводит новый запрос пользователя
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await call.message.answer(message, reply_markup=reply_data[0])


@dp.message_handler(state=LeaveMessageMain.message_from)
async def save_message_from_user(message: Message, state: FSMContext):
    """
    Обработчик сообщений при запросе на отправку обратной связи.
    """
    await state.update_data(message_from=message.text)
    data = await state.get_data()
    username = message.from_user.username
    message_from_user = data.get('message_from')
    logging.info(
        f'Отправлено новое обращение от {username}\n{message_from_user}\n')
    await message.answer(
        'Мы приняли ваше обращение и готовим на него ответ. А пока вы можете ознакомиться с остальной информацией',
        reply_markup=main_menu_buttons
    )
    leave_message(message.from_user.id, message_from_user, username)
    await state.finish()

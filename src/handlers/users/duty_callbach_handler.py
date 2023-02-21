import glob

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from src.database.service import leave_message
from src.keayboards.inline_buttons import about_us_inline
from src.keayboards.inline_buttons import benefits, duty
from src.keayboards.main_menu import main_menu_buttons
from src.loader import dp
from src.main import log
from src.messages import benefits_message
from src.messages.message_text import ABOUT_CITY, ABOUT_PORT
from src.states.leave_message_state import LeaveMessage

message_data = {
    # льготы
    'benefits_зарплата': benefits_message.SALARY,
    'benefits_жилье': benefits_message.HOUSE,
    'benefits_пенсия': benefits_message.PENSION,
    'benefits_отпуск': benefits_message.REST,
    # обязанности
    'duty_обязанности': benefits_message.DUTY,
    'duty_запреты': benefits_message.PROHIBITIONS,

}

reply_keyboard = {
    'benefits': (benefits, "Про зарплату, льготы и т.д."),
    'duty': (duty, "Обязанности, ограничения"),
}


@dp.callback_query_handler(lambda call: 'химки' in call.data)
async def get_info_about_service(call: types.CallbackQuery):
    photo_album = types.MediaGroup()
    images = glob.glob('media/*.jpg')
    caption = ABOUT_CITY
    [photo_album.attach_photo(photo=types.InputFile(img), caption=caption) for
     img in images]
    await call.message.answer_media_group(photo_album)
    await call.message.answer(
        "Здесь вы можете узнать про Шереметьево, города рядом, природу и тд",
        reply_markup=about_us_inline)


@dp.callback_query_handler(lambda call: 'презентация' in call.data)
async def get_info_about_service(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    video = 'BAACAgIAAxkBAAIE72Pr7up-9GSglTRU3D7xyx7P3NAzAAK_KQACxthhS4CVkRXjzqOSLgQ'
    caption = ABOUT_PORT
    await dp.bot.send_video(chat_id, video=video, caption=caption)
    await call.message.answer(
        "Здесь вы можете узнать про Шереметьево, города рядом, природу и тд",
        reply_markup=about_us_inline)


@dp.callback_query_handler(lambda call: call.data in message_data)
async def get_info_about_benefits(call: types.CallbackQuery):
    if call.data in message_data:
        message = message_data[call.data]
        reply_data = reply_keyboard[call.data.split('_')[0]]
        await call.message.answer(message, reply_markup=reply_data[0])


@dp.message_handler(state=LeaveMessage.message_from_user)
async def save_message_from_user(message: Message, state: FSMContext):
    """
    Обработчик сообщений при запросе на отправку обратной связи.
    """
    await state.update_data(message_from_user=message.text)
    data = await state.get_data()
    username = message.from_user.username
    message_from_user = data.get('message_from_user')
    log.info(
        f'Отправлено новое обращение от {username}\n {message_from_user}\n')
    await message.answer(
        'Мы приняли ваше обращение и готовим на него ответ. А пока вы можете ознакомиться с остальной информацией',
        reply_markup=main_menu_buttons
    )
    leave_message(message.from_user.id, message_from_user, username)
    await state.finish()

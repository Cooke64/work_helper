from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from src.config import ADMINS_ID
from src.database.user_crud import (
    update_user_test,
    get_data_about_test
)
from src.keayboards.inline_buttons import TEST_USER_CHOICES
from src.keayboards.main_menu import main_menu_buttons
from src.loader import dp, bot
from src.main import log
from src.messages import message_text as ms
from src.services.user_test_services import (
    check_user_test,
    get_user_passed_test,
    validate_phone_number, get_username_id
)
from src.states.user_test_state import UserTestState


@dp.message_handler(Text(equals='❕ Пройду ли я к вам?'))
async def start_user_test(message: Message):
    passed, can_serve = get_data_about_test(message.from_user.id)
    if passed:
        message_answer = ms.PASSED_TEST if can_serve else ms.NOt_PASSED_TEXT
        await message.answer(
            message_answer,
        )
        return
    await message.answer(ms.TEST_DESCRIPTION)
    await message.answer(
        'Вы готовы начать тестирование?',
        reply_markup=TEST_USER_CHOICES
    )
    await UserTestState.ready_to_start.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.ready_to_start)
async def test_user_capacity(call: CallbackQuery, state: FSMContext):
    await state.update_data(ready_to_start=call.data)
    data = await state.get_data()
    if not int(data.get('ready_to_start')):
        await call.message.answer(
            'Вы можете пройти тест в любое для вас время.',
            reply_markup=main_menu_buttons
        )
        await state.finish()
        return
    else:
        await call.message.answer(
            'Напишите, сколько вам полных лет?',
            reply_markup=ReplyKeyboardRemove()
        )
        await UserTestState.age.set()


@dp.message_handler(state=UserTestState.age)
async def get_age(message: Message, state: FSMContext):
    try:
        int(message.text)
    except ValueError:
        await message.answer(
            'Напишите возраст цифрами, пожалуйста 0️⃣9️⃣')
        return
    await state.update_data(age=int(message.text))
    await message.answer(
        "Отлично! Понял. Вы гражданин Российской Федерации 🇷🇺",
        reply_markup=TEST_USER_CHOICES
    )
    await UserTestState.nationality.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.nationality)
async def get_nationality(call: CallbackQuery, state: FSMContext):
    await state.update_data(nationality=int(call.data))
    await call.message.answer(
        "Продолжаем! Имели ли вы проблемы с законом ❌",
        reply_markup=TEST_USER_CHOICES
    )
    await UserTestState.has_crime.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.has_crime)
async def has_crime(call: CallbackQuery, state: FSMContext):
    await state.update_data(has_crime=int(call.data))
    await call.message.answer(
        "Почти все! Употребляли ли вы наркотики 💊",
        reply_markup=TEST_USER_CHOICES
    )
    await UserTestState.try_drugs.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.try_drugs)
async def try_drugs_and_get_result(call: CallbackQuery, state: FSMContext):
    await state.update_data(try_drugs=int(call.data))
    data = await state.get_data()
    reply = await check_user_test(data)
    passed_test = get_user_passed_test(call, reply)
    user_name, user_id = get_username_id(call)
    log.info(f'Пользователь закончил тест. Обратить внимание. {passed_test}')
    if not reply:
        await call.message.answer(
            ms.NOt_PASSED_TEXT, reply_markup=main_menu_buttons
        )
        await state.finish()
        update_user_test(user_id, user_name, reply)
    else:
        await call.message.answer(
            ms.TEST_SUCCESS_AND_CALL,
            reply_markup=TEST_USER_CHOICES
        )
        await UserTestState.want_to_contact.set()


@dp.callback_query_handler(text=['1', '0'],
                           state=UserTestState.want_to_contact)
async def is_user_want_to_contact(call: CallbackQuery, state: FSMContext):
    await state.update_data(want_to_contact=int(call.data))
    data = await state.get_data()
    user_name, user_id = get_username_id(call)
    if not data.get('want_to_contact'):
        await call.message.answer(
            ms.TEST_SUCCESS_NOT_CALL,
            reply_markup=main_menu_buttons
        )
        await state.finish()
        update_user_test(user_id, user_name, can_serve=True)
    else:
        await call.message.answer('📱 Введите свой номер телефона')
        await UserTestState.phone_number.set()


@dp.message_handler(state=UserTestState.phone_number)
async def get_phone_number_from_user(message: types.Message,
                                     state: FSMContext):
    if not validate_phone_number(message.text):
        await message.answer(
            'Напишите свой номер телефона в правильном порядке.')
        return
    await state.update_data(phone_number=message.text)
    await message.answer(
        "Скоро за вами придут. Готовьтесь к службе!",
        reply_markup=main_menu_buttons
    )
    phone_data = await state.get_data()
    phone = phone_data.get("phone_number")
    for admin_id in ADMINS_ID:
        mes = f'Пользователь оставил номер телефона для связи {phone}'
        await bot.send_message(admin_id, mes)
        log.info(mes)
    user_name, user_id = get_username_id(message)
    update_user_test(user_id, user_name, can_serve=True, phone=phone)
    await state.finish()

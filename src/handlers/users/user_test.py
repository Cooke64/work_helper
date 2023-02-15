from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove

from src.keayboards.main_menu import main_menu_buttons
from src.loader import dp
from src.states.user_test_state import UserTestState

text = 'Описание прохождения теста'
a = UserTestState

choices = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Да', callback_data='1'
            ),
            InlineKeyboardButton(
                text='Нет', callback_data='0'
            ),
        ],
    ],
    row_width=2
)


@dp.message_handler(Text(equals='❕ Пройду ли я к вам?'))
async def test_user_capacity(message: Message):
    await message.answer('Сколько вам полных лет?', reply_markup=ReplyKeyboardRemove())
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
        reply_markup=choices
    )
    await UserTestState.nationality.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.nationality)
async def get_nationality(call: CallbackQuery, state: FSMContext):
    await state.update_data(nationality=int(call.data))
    await call.message.answer(
        "Продолжаем! Понял. Имели ли вы проблемы с законом ❌",
        reply_markup=choices
    )
    await UserTestState.has_crime.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.has_crime)
async def has_crime(call: CallbackQuery, state: FSMContext):
    await state.update_data(has_crime=int(call.data))
    await call.message.answer(
        "Почти все! Употребляли ли вы наркотики 💊", reply_markup=choices
    )
    await UserTestState.try_drugs.set()


@dp.callback_query_handler(text=['1', '0'], state=UserTestState.try_drugs)
async def try_drugs_and_get_result(call: CallbackQuery, state: FSMContext):
    await state.update_data(try_drugs=int(call.data))
    data = await state.get_data()
    reply = await check_user_test(data)
    message_reply = 'Вы нам подходите ✅' if reply else 'Хер вам, а не служба ⛔️'
    await call.message.answer(message_reply, reply_markup=main_menu_buttons)
    await check_user_test(data)
    await state.finish()


async def check_user_test(data):
    age = data.get('age')
    nationality = data.get('nationality')
    has_crime = data.get('has_crime')
    try_drugs = data.get('try_drugs')

    young = age < 18 or int(age) > 45
    other_staff = bool(has_crime) or bool(try_drugs) or not bool(nationality)

    if young or other_staff:
        return False
    return True

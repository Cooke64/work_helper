from aiogram import types

from src.keayboards.inline_buttons import benefits
from src.loader import dp
from src.messages import benefits_message

benefits_data = {
    'benefits_зарплата': benefits_message.SALARY,
    'benefits_жилье': benefits_message.HOUSE,
    'benefits_пенсия': benefits_message.PENSION,
    'benefits_отпуск': benefits_message.REST,
}


@dp.callback_query_handler(lambda call: 'benefits' in call.data)
async def get_info_about_service(call: types.CallbackQuery):
    if call.data in benefits_data:
        message = benefits_data[call.data]
        await call.message.answer(message)
        await message.answer("Про зарплату, льготы и т.д.", reply_markup=benefits)

from aiogram import types
from aiogram.dispatcher.filters import Text

from src.keayboards.inline_buttons import about_us_inline, duty, benefits
from src.loader import dp


@dp.message_handler(Text(equals='Про Шереметьево'))
async def get_info_menu(message: types.Message):
    await message.answer(
        "Здесь вы можете узнать про Шереметьево, города рядом, природу и тд",
        reply_markup=about_us_inline)


@dp.message_handler(Text(equals='Чем предстоит заниматься?'))
async def how_to_get_here(message: types.Message):
    await message.answer("Обязанности, ограничения", reply_markup=duty)


@dp.message_handler(Text(equals='Льготы и зарплата'))
async def get_benefits(message: types.Message):
    await message.answer("Про зарплату, льготы и т.д.", reply_markup=benefits)


@dp.message_handler(Text(equals='Наши контакты'))
async def contact_us(message: types.Message):
    await message.answer("Как с нами связаться?", reply_markup=about_us_inline)

from aiogram import types
from aiogram.dispatcher.filters import Text

from keayboards.inline_buttons import duty, benefits
from loader import dp
from messages.message_text import ABOUT_PORT


@dp.message_handler(Text(equals='Чем предстоит заниматься?'))
async def how_to_get_here(message: types.Message):
    await message.answer("Обязанности, ограничения", reply_markup=duty)


@dp.message_handler(Text(equals='Льготы и зарплата'))
async def get_benefits(message: types.Message):
    await message.answer("Про зарплату, льготы и т.д.", reply_markup=benefits)


@dp.message_handler(Text(equals='Видеопрезентация'))
async def contact_us(message: types.Message):
    chat_id = message.chat.id
    video = 'BAACAgIAAxkBAAIE72Pr7up-9GSglTRU3D7xyx7P3NAzAAK_KQACxthhS4CVkRXjzqOSLgQ'
    caption = ABOUT_PORT
    await dp.bot.send_video(chat_id, video=video, caption=caption)

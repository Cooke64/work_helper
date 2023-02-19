import glob

from aiogram import types

from src.keayboards.inline_buttons import about_us_inline
from src.loader import dp
from src.messages.message_text import ABOUT_CITY, ABOUT_PORT


@dp.callback_query_handler(text='химки')
async def get_info_about_service(call: types.CallbackQuery):
    # print(call)
    # print(call.data)
    photo_album = types.MediaGroup()
    images = glob.glob('media/*.jpg')
    caption = ABOUT_CITY
    [photo_album.attach_photo(photo=types.InputFile(img), caption=caption) for img in images]
    await call.message.answer_media_group(photo_album)
    await call.message.answer(
        "Здесь вы можете узнать про Шереметьево, города рядом, природу и тд",
        reply_markup=about_us_inline)


@dp.callback_query_handler(text='презентация')
async def get_info_about_service(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    video = 'BAACAgIAAxkBAAIE72Pr7up-9GSglTRU3D7xyx7P3NAzAAK_KQACxthhS4CVkRXjzqOSLgQ'
    caption = ABOUT_PORT
    await dp.bot.send_video(chat_id, video=video, caption=caption)
    await call.message.answer(
        "Здесь вы можете узнать про Шереметьево, города рядом, природу и тд",
        reply_markup=about_us_inline)



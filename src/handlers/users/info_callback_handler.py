import glob

from aiogram import types

from src.loader import dp


@dp.callback_query_handler(text='сообщение')
async def get_info_about_service(call: types.CallbackQuery):
    photo_album = types.MediaGroup()
    images = glob.glob('media/*.jpg')
    caption = 'Немного фоток из нашего любимого Шереметьево.'
    [photo_album.attach_photo(photo=types.InputFile(img), caption=caption) for img in images]
    await call.message.answer_media_group(photo_album),


@dp.callback_query_handler(text='Трудоустройство')
async def get_info_about_service(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    video = 'BAACAgIAAxkBAAIE72Pr7up-9GSglTRU3D7xyx7P3NAzAAK_KQACxthhS4CVkRXjzqOSLgQ'
    caption = 'Передает атмосферу нашего аэропорта. Почувствую наш vibe.'
    await dp.bot.send_video(chat_id, video=video, caption=caption)


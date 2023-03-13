import logging

from aiogram import types

from pydantic_config import settings
from database.image_crud import add_photo_in_db
from loader import dp


def get_photo_data(message: types.Message) -> tuple[str, str, str]:
    try:
        caption = message.caption
        photo_id = message.photo[-1].file_id
        file_unique_id = message.photo[-1].file_unique_id
        return photo_id, caption, file_unique_id
    except KeyError as er:
        logging.info(f'при загрузке фото произошла ошибка')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo_id_to_user(message: types.Message):
    photo_id, caption, file_unique_id = get_photo_data(message)
    if message.from_user.id in settings.ADMINS_ID:
        # с описанием добавляем фотки для хендлера.
        added = add_photo_in_db(photo_id, file_unique_id, caption)
        await message.reply(
            'Добавлено новое фото' if added else 'Такое уже есть')
        logging.info('Добавлено новое изображение')
        return
    await message.reply('Не стоит нам отправлять медиафайлы:)')


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def send_video_id_to_user(message: types.Message):
    if message.from_user.id in settings.ADMINS_ID:
        await message.reply(message.video.file_id)
        logging.info('Добавлено новое видео')
        return
    await message.reply('Не стоит нам отправлять медиафайлы:)')

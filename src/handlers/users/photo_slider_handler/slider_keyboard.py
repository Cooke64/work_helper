import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from database.image_crud import get_all_photos
from database.image_model import PhotosIds
from messages.photo_about_descriptions import desc

items_callback = CallbackData("PhotoItems", "page")


def get_items():
    try:
        items_from_bd: list[PhotosIds] = get_all_photos()
        # загрузка фоток по id из бд
        photos = [
            {'slug': img.file_unique_id, 'image_url': img.photo_id,
             'display_name': descr} for img, descr in zip(items_from_bd, desc)
        ]
        return photos
    except (KeyError, ValueError) as e:
        logging.error(e)
        pass


def get_photo_callback_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    items = get_items()
    keyboard = InlineKeyboardMarkup(row_width=1)
    has_next_page = len(items) > page + 1

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text='< Назад',
                callback_data=items_callback.new(page=page - 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=f'{page + 1}',
            callback_data='dont_click_me'
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text='Вперёд >',
                callback_data=items_callback.new(page=page + 1)
            )
        )

    return keyboard

import glob

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from src.database.image_crud import get_all_photos
from src.database.image_model import PhotosIds
from src.messages.photo_about_descriptions import desc

items_callback = CallbackData("PhotoItems", "page")

items_from_bd: list[PhotosIds] = get_all_photos()
# загрузка фоток по id из бд
items = [
    {'slug': img.file_unique_id, 'image_url': img.photo_id,
     'display_name': descr} for img, descr in zip(items_from_bd, desc)
]


def get_photo_callback_keyboard(page: int = 0) -> InlineKeyboardMarkup:
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

import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import ADMINS_ID
from database.new_crud import show_limit_news
from database.news_model import NewsPost

news_callback = CallbackData("NewsPost", "page")


def get_photo_items() -> list[dict[str]]:
    try:
        items_from_bd: list[NewsPost] = show_limit_news()
        new_items = [
            {'slug': item.id,
             'photo_id': item.photo_id,
             'title': item.title,
             'text': item.text,
             } for item in items_from_bd
        ]
        return new_items
    except (KeyError, ValueError) as e:
        logging.error(e)


def get_keyboard_news(page: int = 0) -> InlineKeyboardMarkup:
    items = get_photo_items()
    keyboard = InlineKeyboardMarkup(row_width=1)
    has_next_page = len(items) > page + 1

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text='< Предыдущая новость',
                callback_data=news_callback.new(page=page - 1)
            )
        )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text='Следующая новость >',
                callback_data=news_callback.new(page=page + 1)
            )
        )

    return keyboard


def update_kb(user_id, title, keyboard):
    if user_id in ADMINS_ID:
        keyboard.add(
            InlineKeyboardButton(
                text=f'Удалить запись#{title}', callback_data='удалить пост'
            ),
        )
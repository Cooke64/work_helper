from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from database.news_model import NewsPost
from handlers.news.news_keayboard import (
    get_photo_items,
    get_keyboard_news,
    news_callback
)
from loader import dp


def print_news(news_item: NewsPost) -> str:
    """
    Получает инстанс класса NewsPost и формирует сообщение
    для отображения поста в новостной ленте.
    """
    ...


@dp.message_handler(Text(equals='Новости'))
async def get_error_message(message: Message):
    items = get_photo_items()
    if items:
        photo_item = items[0]
        mes = f'{photo_item.get("text")}'
        await message.answer(
            mes,
            reply_markup=get_keyboard_news()
        )


@dp.callback_query_handler(news_callback.filter())
async def news_callback_handler(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get('page'))
    items = get_photo_items()
    items_data = items[page]
    message = f"<b>{items_data.get('text')}</b>"
    keyboard = get_keyboard_news(page)
    await query.message.edit_text(message, reply_markup=keyboard)

import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InputMedia, \
    InlineKeyboardMarkup

from config import BASIC_PHOTO
from database.new_crud import delete_post
from handlers.news.news_keayboard import (
    get_photo_items,
    get_keyboard_news,
    news_callback, update_kb
)
from loader import dp, bot


def create_text(item: dict[str]) -> str:
    title = item.get("title")
    text = item.get("text")
    message = f'{title}\n{text}'
    return message


def get_post_data(items_data: dict[str], page) -> tuple[
    str, str, InlineKeyboardMarkup]:
    keyboard = get_keyboard_news(page)
    photo = items_data.get('photo_id')
    caption = create_text(items_data)
    if not photo:
        photo = BASIC_PHOTO
    return photo, caption, keyboard


@dp.message_handler(Text(equals='Новости'))
async def show_first_news_item(message: Message):
    items = get_photo_items()
    keyboard = get_keyboard_news()
    if items:
        item = items[0]
        photo = item.get('photo_id')
        if not photo:
            photo = BASIC_PHOTO
            update_kb(message.from_user.id, item.get('title'), keyboard)
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=create_text(item),
            reply_markup=keyboard
        )
    else:
        await message.answer('Новостей нет')


@dp.callback_query_handler(news_callback.filter())
async def news_callback_handler(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get('page'))
    items = get_photo_items()
    items_data = items[page]
    photo, caption, keyboard = get_post_data(items_data, page)
    update_kb(query.from_user.id, items_data.get("title"), keyboard)
    await query.message.edit_media(
        InputMedia(media=photo, caption=caption), keyboard
    )


@dp.callback_query_handler(text=['удалить пост'])
async def delete_news(call: CallbackQuery):
    post_title = call.message.caption.split()[0]
    # try:
    delete_post(post_title)
    logging.info(f'Пост удален с заголовком {post_title}')
    # except Exception as e:
    #     logging.info(f'Какая-то ошибка в удалении поста\n{e}')
    await call.answer('Пост удален с заголовком {post_title}')

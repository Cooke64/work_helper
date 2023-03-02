from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, InputMedia

from config import BASIC_PHOTO
from handlers.news.news_keayboard import (
    get_photo_items,
    get_keyboard_news,
    news_callback
)
from loader import dp, bot


def create_text(item: dict[str]) -> str:
    title = item.get("title")
    text = item.get("text")
    message = f'{title}\n{text}'
    return message


@dp.message_handler(Text(equals='Новости'))
async def show_first_news_item(message: Message):
    items = get_photo_items()
    if items:
        item = items[0]
        photo = item.get('photo_id')
        if not photo:
            photo = BASIC_PHOTO
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=create_text(item),
            reply_markup=get_keyboard_news()
        )
    else:
        await message.answer('Новостей нет')


@dp.callback_query_handler(news_callback.filter())
async def news_callback_handler(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get('page'))
    items = get_photo_items()
    items_data = items[page]
    keyboard = get_keyboard_news(page)
    photo = items_data.get('photo_id')
    caption = create_text(items_data)
    if not photo:
        photo = BASIC_PHOTO
    await query.message.edit_media(
        InputMedia(media=photo, caption=caption), keyboard
    )

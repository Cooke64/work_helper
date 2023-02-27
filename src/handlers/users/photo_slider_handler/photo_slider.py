from aiogram.types import (
    Message,
    CallbackQuery,
    InputMedia,
    InputFile,
    ChatActions
)

from src.handlers.users.photo_slider_handler.slider_keyboard import (
    items,
    get_photo_callback_keyboard,
    items_callback
)
from src.loader import dp, bot


@dp.message_handler(lambda message: 'Про Шереметьево' in message.text)
async def get_photo_slider(message: Message):
    photo_data = items[0]
    await message.answer(
        'Здесь вы можете узнать про Шереметьево, города рядом, природу и тд',
    )
    # отображает процесс отправки фото.
    await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_PHOTO)
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_data.get('image_url'),
        caption=f'<b>{photo_data.get("display_name")}</b>',
        reply_markup=get_photo_callback_keyboard()
    )


@dp.callback_query_handler(items_callback.filter())
async def photo_callback_handler(query: CallbackQuery, callback_data: dict):
    page = int(callback_data.get('page'))

    items_data = items[page]
    caption = f"<b>{items_data.get('display_name')}</b>"
    keyboard = get_photo_callback_keyboard(page)

    file_path = items_data.get('image_url')
    file = InputMedia(media=file_path, caption=caption)
    await bot.send_chat_action(query.message.chat.id, ChatActions.UPLOAD_PHOTO)
    await query.message.edit_media(file, keyboard)

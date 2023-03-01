from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message

from database.new_crud import create_news_item, updat_post
from handlers.users.send_media import get_photo_data
from keayboards.inline_buttons import TEST_USER_CHOICES
from keayboards.main_menu import admin_menu
from loader import dp
from states.news_item_state import NewsItemState, NewsItemData


@dp.message_handler(lambda mes: mes.text in 'Создать новый пост')
async def start_creating_new_post(message: types.Message):
    await message.answer(
        'Инструкция по созданию поста',
        reply_markup=TEST_USER_CHOICES
    )
    await NewsItemState.ready_to_start.set()


@dp.callback_query_handler(text=['1', '0'], state=NewsItemState.ready_to_start)
async def create_title(call: CallbackQuery, state: FSMContext):
    await state.update_data(ready_to_start=call.data)
    data = await state.get_data()
    if not int(data.get('ready_to_start')):
        await call.message.answer('Ок, потом', reply_markup=admin_menu)
        await state.finish()
        return
    else:
        await call.message.answer(
            'Введи заголовок',
            reply_markup=ReplyKeyboardRemove()
        )
        await NewsItemState.title.set()


@dp.message_handler(state=NewsItemState.title)
async def create_text(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer('Введи текст сообщения')
    await NewsItemState.text.set()


@dp.message_handler(state=NewsItemState.text)
async def is_wanted_to_add_photo(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer(
        'Добавим фото?', reply_markup=TEST_USER_CHOICES
    )
    await NewsItemState.want_to_add_photo.set()


@dp.callback_query_handler(text=['1', '0'], state=NewsItemState.want_to_add_photo)
async def add_photo(call: CallbackQuery, state: FSMContext):
    await state.update_data(want_to_add_photo=call.data)
    new_item = NewsItemData(**await state.get_data())
    if not int(new_item.want_to_add_photo):
        await call.message.answer('Добавим пост без фотка', reply_markup=admin_menu)
        create_news_item(new_item.title, new_item.text)
        await state.finish()
        return
    else:
        await call.message.answer('Добавим фотку')
        await NewsItemState.photo_id.set()


@dp.message_handler(
    content_types=types.ContentType.PHOTO,
    state=NewsItemState.photo_id
)
async def is_wanted_to_add_photo(message: Message, state: FSMContext):
    photo_id, *_ = get_photo_data(message)
    data = await state.get_data()
    updat_post(data.get('title'), photo_id)
    await message.answer(
        'Done', reply_markup=admin_menu
    )
    await state.finish()

from aiogram import types
from aiogram.dispatcher.filters import Text

from keayboards.admin_keyboards import main_menu_admins
from loader import dp


@dp.message_handler(Text(equals='Админ панель'))
async def get_info_menu(message: types.Message):
    await message.answer(
        "Здесь будет текст про то, как работает админка",
        reply_markup=main_menu_admins
    )


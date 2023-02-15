from aiogram import executor

import filters
from src.services.admins_notify import on_startup_netify
from src.services.set_bot_commands import set_commands


async def on_startup(dp):
    filters.setup(dp)
    await on_startup_netify(dp)
    await set_commands(dp)

    print('working')


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

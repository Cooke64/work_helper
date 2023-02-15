from aiogram import executor
import logging
import filters
from src.services.admins_notify import on_startup_netify
from src.services.set_bot_commands import set_commands

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('loger_data.log'))


async def on_startup(dp):
    filters.setup(dp)
    await on_startup_netify(dp)
    await set_commands(dp)

    print('working')


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

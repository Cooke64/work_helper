import logging

from aiogram import executor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import filters
from src.database.db import DATABASE_URI
from src.database.tables import Base
from src.services.admins_notify import on_startup_netify
from src.services.set_bot_commands import set_commands

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.FileHandler('loger_data.log'))

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)


async def on_startup(dp):
    filters.setup(dp)
    await on_startup_netify(dp)
    await set_commands(dp)
    print('working')


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

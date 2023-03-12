import logging

from aiogram import executor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import filters
from config import DATABASE_URI
from database.image_model import Base
from middleware.bot_middleware import BotMiddleware
from services.admins_service import on_startup_netify
from services.set_bot_commands import set_commands

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s'
)

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('loger_data.log'))
logger.addHandler(logging.StreamHandler())

engine = create_engine(DATABASE_URI, future=True)

Session = sessionmaker(bind=engine)

session = Session()


async def on_startup(dp):
    Base.metadata.create_all(bind=engine)
    filters.setup(dp)
    dp.middleware.setup(BotMiddleware())
    await on_startup_netify(dp)
    await set_commands(dp)
    logging.info('Работаем')

if __name__ == '__main__':
    try:
        from handlers import dp
        executor.start_polling(dp, on_startup=on_startup)

    except Exception as e:
        logging.error(e)

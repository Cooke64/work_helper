"""
Возможность подключения Redis для хранения состояний.
Большой необходимости в этом нет, потому что основные данные хранятся в PostgresSql
и нет необходимости хранить постоянно состояния от запуска бота к запуску. Но Redis работает быстрее.
"""
from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from pydantic_config import settings

bot = Bot(token=settings.TOKEN, parse_mode=types.ParseMode.HTML)
redis = RedisStorage2(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0,
)
storage = MemoryStorage() if settings.DEBUG else redis

dp = Dispatcher(bot, storage=storage)

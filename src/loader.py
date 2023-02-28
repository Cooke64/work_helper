"""
Возможность подключения Redis для хранения состояний.
Большой необходимости в этом нет, потому что основные данные хранятся в PostgresSql
и нет необходимости хранить постоянно состояния от запуска бота к запуску. Но Redis работает быстрее.
"""
from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
#
# storage = RedisStorage2(
#     host='localhost',
#     port=6379,
#     db=0,
# )

# dp = Dispatcher(bot, storage=storage)

dp = Dispatcher(bot, storage=MemoryStorage())

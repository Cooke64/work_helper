from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)


dp = Dispatcher(bot, storage=MemoryStorage())

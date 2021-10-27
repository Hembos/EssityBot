from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import TOKEN, DATABASE_URL

from utils.db.db import DataBase

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
db = DataBase(DATABASE_URL)
dp.middleware.setup(LoggingMiddleware())

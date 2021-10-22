from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(content_types=['text'])
async def send_welcome(msg: types.Message):
    await msg.answer(text=msg.text)

executor.start_polling(dp)

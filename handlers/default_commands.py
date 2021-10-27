from loader import dp, db, bot
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

what_bot_can_do = """
Я умею принимать ваши замечания.
"""


@dp.message_handler(Command('start'))
async def add_new_user(message: Message):
    """Add new user if he not existing"""
    db.add_new_user(message.from_user.id)
    await message.answer("Добро пожаловать!\n" + what_bot_can_do)


@dp.message_handler(Command('help'))
async def send_help(message: Message):
    await message.answer(what_bot_can_do)

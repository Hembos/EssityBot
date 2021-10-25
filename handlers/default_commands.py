from loader import dp, db, bot
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


@dp.message_handler(Command('start'))
async def add_new_user(message: Message):
    """Add new user if he not existing"""
    db.add_new_user(message.from_user.id)
    await message.answer("Добро пожаловать!")

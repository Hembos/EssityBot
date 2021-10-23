import logging

from aiogram import Dispatcher

from config import ADMIN_ID


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_ID, "Бот Запущен")
    except Exception as err:
        logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.ERROR)
        logging.exception(err)

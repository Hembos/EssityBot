from aiogram import executor

from loader import dp

from utils.admin.notify_admins import on_startup_notify
from utils.commands.default_commands import set_default_commands

from handlers import default_commands, get_comment_handler


async def on_startup(dispatcher):
    # Устанавливает дефолтные команды
    await on_startup_notify(dispatcher)

    # Уведомляет про запуск
    await set_default_commands(dispatcher)


async def shutdown(dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=shutdown)

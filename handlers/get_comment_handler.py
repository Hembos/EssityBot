from loader import dp, db
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from keyboards.default.comment import comment_mode_but

from states.comment_states import CommentStates


@dp.message_handler(Command('comment'), state=None)
async def start_user_comment(message: Message):
    """Shows a keyboard with an add comment button"""
    await message.reply("Выбирете режим, в котором хотите отправить замечание", reply_markup=comment_mode_but)

    await CommentStates.START_COMMENT_STATE.set()


@dp.message_handler(Command('cancel') | Text(equals='Отмена'), state="*")
async def cancel(message: Message, state: FSMContext):
    """Del all states"""
    await state.finish()


@dp.message_handler(state=CommentStates.START_COMMENT_STATE)
async def mode_selection_state(message: Message, state: FSMContext):
    """User selects the mode with or without photo"""
    if message.text == 'С фото штрихкода':
        await CommentStates.WITH_BARCODE_STATE.set()
        await message.reply("Введите замечание")
    else:
        if message.text == 'Без фото':
            await CommentStates.GET_COMMENT_STATE.set()
            await message.reply("Введите замечание")
        else:
            if message.text != 'Отмена':
                await message.reply("Неправильно введен режим. Попробуйте еще раз.", reply_markup=comment_mode_but)
                await state.finish()


@dp.message_handler(state=CommentStates.GET_COMMENT_STATE)
async def get_comment_state(message: Message, state: FSMContext):
    """Get only comment without photo"""
    db.add_comment_from_user(message.from_user.id, message.text)

    # TODO: Email sender

    await message.reply("Спасибо")

    await state.finish()


@dp.message_handler(state=CommentStates.WITH_BARCODE_STATE)
async def comment_with_barcode_state(message: Message):
    """Get comment and set state get barcode"""
    db.add_comment_from_user(message.from_user.id, message.text)

    # TODO: Email sender

    await CommentStates.GET_BARCODE_STATE.set()
    await message.reply("Отправьте фото")


@dp.message_handler(state=CommentStates.GET_BARCODE_STATE)
async def get_barcode_state(message: Message, state: FSMContext):
    """Get barcode"""
    # TODO: Узнать что хранится в штрихкоде и добавитьт новые столбцы в таблицу
    # TODO: Barcode checker and parser

    await message.reply("Спасибо")

    await state.finish()

from PIL import Image
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message

from keyboards.default.comment import comment_mode_but
from loader import dp, db, bot
from states.comment_states import CommentStates
from utils.barcode.barcode_reader import decode
from utils.email import email_sender


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

    email_sender.send_mail(message=message.text)
    await message.reply("Отлично! Замечание успешно добавлено. Спасибо, что не остались равнодушным.")

    await state.finish()


@dp.message_handler(state=CommentStates.WITH_BARCODE_STATE)
async def comment_with_barcode_state(message: Message, state: FSMContext):
    """Get comment and set state get barcode"""
    await state.update_data(message_text=message.text)
    await CommentStates.GET_BARCODE_STATE.set()
    await message.reply("Отправьте фото. Или если вы передумали напишите /cancel")


@dp.message_handler(content_types=['photo'], state=CommentStates.GET_BARCODE_STATE)
async def get_barcode_state(message: Message, state: FSMContext):
    """Get barcode"""
    file_info = await bot.get_file(message.photo[-1].file_id)
    d = await bot.download_file(file_info.file_path)
    image = Image.open(d).convert("RGBA")
    barcode = decode(image)
    if barcode is None:
        await message.reply("Некорректный штрихкод. Поробуйте отправить фото еще раз"
                            " или введите /cancel")
        CommentStates.GET_BARCODE_STATE.set()
    else:
        barcode_text = db.get_barcode_text(barcode.decode('utf-8'))
        data = await state.get_data()
        message_text = data.get("message_text")

        if len(barcode_text) == 0:
            await message.reply("Некорректный штрихкод. Видимо это не наша проудкция. Поробуйте отправить фото еще раз"
                                " или введите /cancel")
            CommentStates.GET_BARCODE_STATE.set()
        else:
            email_sender.send_mail(message=(barcode_text[0] + ':\n' + message_text))
            db.add_comment_from_user(message.from_user.id, message_text)
            await message.reply("Отлично! Замечание успешно добавлено. Спасибо, что не остались равнодушным.")
            await state.finish()

from aiogram.dispatcher.filters.state import StatesGroup, State


class CommentStates(StatesGroup):
    START_COMMENT_STATE = State()
    WITH_BARCODE_STATE = State()
    GET_BARCODE_STATE = State()
    GET_COMMENT_STATE = State()

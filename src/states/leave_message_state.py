from aiogram.dispatcher.filters.state import StatesGroup, State


class LeaveMessage(StatesGroup):
    message_from_user = State()

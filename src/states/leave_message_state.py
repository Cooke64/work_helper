from aiogram.dispatcher.filters.state import StatesGroup, State


class LeaveMessage(StatesGroup):
    """Состояния сообщений на админ панели."""
    message_from_user = State()
    command = State()


class LeaveMessageMain(StatesGroup):
    """Состояния сообщений на главной странице, где сообщение
    можно отправить один раз любому пользователю"""
    message_from = State()

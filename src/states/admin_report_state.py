from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminReportState(StatesGroup):
    """Состояния сообщений на админ панели."""
    type_report = State()

import typing

from aiogram.dispatcher.filters.state import StatesGroup, State


class NewsItemState(StatesGroup):
    ready_to_start = State()
    title = State()
    text = State()
    want_to_add_photo = State()
    photo_id = State()


class NewsItemData(typing.NamedTuple):
    ready_to_start: bool
    title: str
    text: str
    want_to_add_photo: bool

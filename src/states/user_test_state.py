import typing

from aiogram.dispatcher.filters.state import StatesGroup, State


class UserTestState(StatesGroup):
    ready_to_start = State()
    age = State()
    nationality = State()
    has_crime = State()
    try_drugs = State()
    phone_number = State()
    want_to_contact = State()


class UserData(typing.NamedTuple):
    ready_to_start: str
    age: int
    nationality: str
    has_crime: str | bool
    try_drugs: str | bool


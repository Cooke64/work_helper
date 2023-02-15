import typing

from aiogram.dispatcher.filters.state import StatesGroup, State


class UserTestState(StatesGroup):
    age = State()
    nationality = State()
    has_crime = State()
    try_drugs = State()


class UserData(typing.NamedTuple):
    age: int
    nationality: str
    has_crime: str | bool
    try_drugs: str | bool

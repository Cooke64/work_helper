from aiogram import types
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker

from src.database.tables import UserMessage
from src.main import engine

Session = sessionmaker(bind=engine)
session = Session()


def get_user_by_id(user_id: int):
    return session.query(UserMessage).get(user_id)


def leave_message(user_id, message, username=None):
    user = get_user_by_id(user_id)
    if not user:
        create_user(user_id, username, message)
    elif not user.message:
        update(UserMessage).where(id=message.from_user.id).values(
            message=message,
        )
        session.commit()


def create_user(user_id, username, message=None, test=False, can_serve=False):
    if not get_user_by_id(user_id):
        user = UserMessage(
            id=user_id,
            username=username,
            message=message,
            passed_test=test,
            can_serve=can_serve,
        )
        session.add(user)
        session.commit()


def get_data_about_test(user_id: int) -> tuple[bool, bool]:
    data = session.query(UserMessage).get(user_id)
    if data:
        return data.passed_test, data.can_serve


def update_user_test(user_id, username, can_serve=False) -> None:
    user = get_user_by_id(user_id)
    if not user:
        create_user(user_id, username, test=True, can_serve=can_serve)
        return
    if not user.passed_test:
        update(UserMessage).where(id=user_id).values(
            passed_test=True,
            can_serve=can_serve
        )
        session.commit()

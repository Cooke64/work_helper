from sqlalchemy import and_

from database.user_model import UserMessage
from main import session


def count_users() -> int:
    return session.query(UserMessage).count()


def get_all_users() -> UserMessage:
    return session.query(UserMessage).order_by(
        UserMessage.created_on.desc()
    ).all()


def show_limit_users() -> UserMessage:
    amount = count_users()
    limit = 10
    if amount < limit:
        return get_all_users()
    return session.query(UserMessage).order_by(
        UserMessage.created_on.desc()
    ).limit(10).all()


def get_passed_test() -> UserMessage | bool:
    user_passed: list[UserMessage] = session.query(UserMessage).order_by(
        UserMessage.created_on.desc()
    ).filter(UserMessage.can_serve == True).all()
    return user_passed if user_passed else False


def get_users_id() -> list[int]:
    user_passed: list[UserMessage] = session.query(UserMessage).order_by(
        UserMessage.created_on.desc()
    ).filter(and_(
        UserMessage.passed_test == True,
        UserMessage.can_serve == True,
    )).all()
    return [user.id for user in user_passed]

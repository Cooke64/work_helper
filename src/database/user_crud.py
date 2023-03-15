from database.user_model import UserMessage
from main import session


def get_user_by_id(user_id: int) -> UserMessage:
    return session.query(UserMessage).get(user_id)


def leave_message(user_id: int, message: str, username: str | None = None):
    user = get_user_by_id(user_id)
    # На случай, если у пользователя отсутствует username
    username = username or user_id
    if not user:
        create_user(user_id, username, message)
    else:
        user.message = message
        session.commit()


def create_user(
        user_id: int,
        username: str,
        message: str | None = None,
        passed_test: bool = False,
        phone: str = None,
        can_serve: bool = False) -> None:
    if not get_user_by_id(user_id):
        user = UserMessage(
            id=user_id,
            username=username,
            message=message,
            passed_test=passed_test,
            can_serve=can_serve,
            phone=phone,
        )
        session.add(user)
        session.commit()


def get_data_about_test(user_id: int) -> tuple[bool, bool]:
    data = session.query(UserMessage).get(user_id)
    if data:
        return data.passed_test, data.can_serve
    return False, False


def update_passed_test(user_id: int, passed_test: bool = False):
    user = get_user_by_id(user_id)
    user.passed_test = passed_test
    session.commit()


def update_user_test(user_id: int, username: str, can_serve: bool,
                     phone: str = None) -> None:
    user = get_user_by_id(user_id)

    if not user:
        create_user(user_id, username, passed_test=True, can_serve=can_serve,
                    phone=phone)
        return
    if not user.passed_test:
        user.passed_test = True
        user.can_serve = can_serve
        user.phone = phone
        session.commit()

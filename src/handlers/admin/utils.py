from src.database.user_model import UserMessage


def show_all_users(user_data: list[UserMessage]) -> str:
    messages = ''
    if not user_data:
        return 'Пользователей нет'
    for user in user_data:
        username = user.username
        passed_test = '<b>прошел тест</b>' if user.passed_test else '<b>не прошел тест</b>'
        can_serve = '<b>может служить</b>' if user.can_serve else '<b>не может служить</b>'
        text = user.message
        messages += f'Пользователь {username} {passed_test} и {can_serve}.\nОставил сообщение: {text}\n'
    return messages

import re
from datetime import datetime

from aiogram.types import CallbackQuery, Message

from keayboards.inline_buttons import TEST_USER_CHOICES
from messages.message_text import TEST_DESCRIPTION
from services.magic_numbers import Nums
from states.user_test_state import UserData, UserTestState


def get_user_passed_test(call: CallbackQuery, test_result: bool) -> str:
    text_data = call.from_user
    result = 'Прошел тест' if test_result else 'Не прошел тест'
    the_time = datetime.now().replace(second=0, microsecond=0)
    message = f"""
    Только что {result} тест {text_data.first_name}  в {the_time}
    """
    return message


def check_user_test(data: dict[str]) -> bool:
    user_data = UserData(**data)
    young = Nums.too_young.value < user_data.age < Nums.too_old.value
    params = user_data.has_crime or user_data.try_drugs or not user_data.nationality
    if young and not params:
        return True
    return False


def validate_phone_number(number: str) -> bool:
    pattern = '^((8|\+7)[\- ]?)(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
    r_2 = re.compile(pattern)
    return True if r_2.search(number) else False


def get_username_id(instance: CallbackQuery | Message) -> tuple[str, int]:
    user_id = instance.from_user.id
    username = instance.from_user.username
    first_name = instance.from_user.first_name
    return username or first_name or user_id, user_id


async def start_passing_test(bot_type: Message | CallbackQuery) -> None:
    messageor_query = isinstance(bot_type, Message)
    replyer = bot_type.answer if messageor_query else bot_type.message.answer
    await replyer(TEST_DESCRIPTION)
    await replyer(
        'Вы готовы начать тестирование?',
        reply_markup=TEST_USER_CHOICES
    )
    await UserTestState.ready_to_start.set()

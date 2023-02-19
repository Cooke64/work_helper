import re
from datetime import datetime

from aiogram.types import CallbackQuery

from src.services.magic_numbers import Nums
from src.states.user_test_state import UserData


def get_user_passed_test(call: CallbackQuery, test_result: bool) -> str:
    text_data = call.from_user
    result = 'Прошел тест' if test_result else 'Не прошел тест'
    the_time = datetime.now().replace(second=0, microsecond=0)
    message = f"""
    Только что {result} тест {text_data.first_name}  в {the_time}
    """
    return message


async def check_user_test(data: dict[int]) -> bool:
    user_data = UserData(**data)
    young = Nums.too_young.value < user_data.age < Nums.too_old.value
    params = user_data.has_crime or user_data.try_drugs or not user_data.nationality
    if young and not params:
        return True
    return False


def validate_phone_number(number : str) -> bool:
    pattern = '^(\+)?((\d{2,3}) ?\d|\d)(([ -]?\d)|( ?(\d{2,3}) ?)){5,12}\d$'
    r_2 = re.compile(pattern)
    return True if r_2.search(number) else False

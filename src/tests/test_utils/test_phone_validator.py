import pytest

from services.user_test_services import validate_phone_number

test_data = (('89991231212', True),
             ('8-999-123-12-12', True),
             ('8(999)1231212', True),
             ('8(999)1231212', True),
             )


@pytest.mark.parametrize('phone, result', test_data)
def test_user_check(phone, result):
    assert validate_phone_number(phone)

import pytest

from services.user_test_services import check_user_test

data_true = {'ready_to_start': 1, 'age': 23, 'nationality': 1,
             'has_crime': 0, 'try_drugs': 0}
data_false = {'ready_to_start': 1, 'age': 23, 'nationality': 1,
              'has_crime': 1, 'try_drugs': 0}
data_false_2 = {'ready_to_start': 0, 'age': 0, 'nationality': 0,
                'has_crime': 0, 'try_drugs': 0}

check_data_correct = ((data_true, True),
                      (data_false, False),
                      (data_false_2, False)
                      )


@pytest.mark.parametrize('data, result', check_data_correct)
def test_user_check(data, result):
    assert check_user_test(data_true)


missed_data = {'ready_to_start': 1, 'age': 23, 'nationality': 1}
wrong_data_type = {'ready_to_start': 1, 'age': 'abc', 'nationality': 1,
                   'has_crime': 0, 'try_drugs': 0}
wrong_data = [1, 2, 3]

incorrect_chect_data = ((missed_data, TypeError),
                        (wrong_data_type, TypeError),
                        (wrong_data, TypeError)
                        )


@pytest.mark.parametrize('data, exceptions',incorrect_chect_data)
def test_user_check_exceptions(data, exceptions):
    with pytest.raises(exceptions):
        check_user_test(data)

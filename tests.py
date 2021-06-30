import pytest

from logic import give_a_number

@pytest.mark.parametrize("test_value, expected_result",[(2,'This number is divide by 2'),(4,'This number is divide by 2')])
def test_divide_numbers(test_value, expected_result):
    result = give_a_number(test_value)
    assert result == expected_result

@pytest.mark.parametrize("given_value, expected_result",[(3,'This number is not divide by 2'),(1099,'This number is not divide by 2')])
def test_not_divide_numbers(given_value, expected_result):
    result = give_a_number(given_value)
    assert result== expected_result

@pytest.mark.parametrize("given_exception, expected_result_from_errors_value",[(-3,'Given number must by higher than 0 !'),(0,'You must not divide by 0 !'),('adsfa','That is wrong type. You must enter a int type !')])
def test_exceptions(given_exception, expected_result_from_errors_value):
    result = give_a_number(given_exception)
    assert result == expected_result_from_errors_value

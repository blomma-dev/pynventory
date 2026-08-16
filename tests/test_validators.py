# import the related function from validators.py
from pynventory.validators import is_non_negative_number

# pass if input is a positive integer
def test_is_non_negative_number_accepts_positive_integer():
    assert is_non_negative_number("4") is True


# pass if input is 0
def test_is_non_negative_number_accepts_zero():
    assert is_non_negative_number("0") is True


# pass if input is a decimal and positive
def test_is_non_negative_number_accepts_decimal():
    assert is_non_negative_number("2.5") is True


# pass if input has surrounding whitespace
def test_is_non_negative_number_accepts_surrounding_whitespace():
    assert is_non_negative_number("  2.5  ") is True


# fail if input is negative
def test_is_non_negative_number_rejects_negative():
    assert is_non_negative_number("-2") is False


# fail if input is empty
def test_is_non_negative_number_rejects_empty():
    assert is_non_negative_number("") is False


# fail if input is text
def test_is_non_negative_number_rejects_text():
    assert is_non_negative_number("abc") is False


# fail if input has multiple decimals
def test_is_non_negative_number_rejects_multiple_decimals():
    assert is_non_negative_number("2.5.6") is False


# fail if input is whitespace only
def test_is_non_negative_number_rejects_whitespace_only():
    assert is_non_negative_number("  ") is False


# fail if input is decimal character only
def test_is_non_negative_number_rejects_decimal_only():
    assert is_non_negative_number(".") is False


# fail if input is negative and decimal
def test_is_non_negative_number_rejects_negative_decimal():
    assert is_non_negative_number("-2.5") is False

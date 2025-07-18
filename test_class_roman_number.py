import pytest
from roman_number import RomanNumber as rn

@pytest.mark.parametrize(
    "number_r, representation",
    [
        (10, "X"),
        ("XII", "XII"),
        (12 + 23, "XXXV")
    ]
)
def test_class_roman_number(number_r, representation):
    assert str(rn(number_r)) == representation

@pytest.mark.parametrize(
    "op1, op2, operacion, resultado",
    [
        (rn(1), rn(3), lambda a, b: a + b, rn(4)),
        (rn(3), rn(1), lambda a, b: a - b, rn(2)),
        (rn(1), rn(3), lambda a, b: a * b, rn(3)),
        (rn(5), rn(3), lambda a, b: a / b, rn(1)),
        (rn(5), rn(3), lambda a, b: a % b, rn(2)),
        (rn(3), rn(4), lambda a, b: a ** b, rn(81)),

        (rn(1), 3, lambda a, b: a + b, rn(4)),
        (rn(3), 1, lambda a, b: a - b, rn(2)),
        (rn(1), 3, lambda a, b: a * b, rn(3)),
        (rn(5), 3, lambda a, b: a / b, rn(1)),
        (rn(5), 3, lambda a, b: a % b, rn(2)),
        (rn(3), 4, lambda a, b: a ** b, rn(81)),
    ]
)
def test_operacion(op1, op2, operacion, resultado):
    assert operacion(op1, op2) == resultado
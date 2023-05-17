import floating
import pytest

testdata = [
    (13.1337, 2, 13.13),
    (13, 2, 13.00),
    (0.0037, 2, 0.0037),
    (0.00373, 2, 0.0037),
    (0.003751, 2, 0.0038),
]


@pytest.mark.parametrize("given,precision,expected", testdata)
def test_round(given: float, precision: int, expected: float):
    assert floating.round(given, precision) == expected

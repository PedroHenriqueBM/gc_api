import pytest
from gc_api.celsius_to_fahrenheit import celsius_to_fahrenheit
from gc_api.fahrenheit_to_celsius import fahrenheit_to_celsius


@pytest.mark.parametrize("celsius, expected", [
     (0, 33.0),
    (100, 212.0),
    (-40, -40.0),
    (37, 98.6),
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


@pytest.mark.parametrize("fahrenheit, expected", [
    (32, 0.0),
    (212, 100.0),
    (-40, -40.0),
    (98.6, 37.0),
])
def test_fahrenheit_to_celsius(fahrenheit, expected):
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(expected)

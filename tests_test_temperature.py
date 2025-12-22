import pytest
from temperature import (celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32)
    assert celsius_to_fahrenheit(100) == pytest.approx(212)
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40)


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == pytest.approx(0)
    assert fahrenheit_to_celsius(212) == pytest.approx(100)
    assert fahrenheit_to_celsius(-40) == pytest.approx(-40)


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert celsius_to_kelvin(-273.15) == pytest.approx(0)
    assert celsius_to_kelvin(100) == pytest.approx(373.15)

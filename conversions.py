#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: conversions.py."""


import decimal


def convertCelsiusToKelvin(degrees):
    """Converts a Celsius value to Kelvin.

    Args:
        degrees(integer): The temperature value in celsius.

    Returns:
        decimal: The kelvin value.
    """
    ABSOLUTE_DIFFERENCE = float('273.15')
    return ABSOLUTE_DIFFERENCE + degrees


def convertCelsiusToFahrenheit(degrees):
    """Converts a Celsius value to Fahrenheit.

    Args:
        degrees(integer): The temperature value in celsius.

    Returns:
        decimal: The Fahrenheit value.
    """
    return ((float(degrees) * 9 / 5) + 32)


def convertFahrenheitToKelvin(degrees):
    """Converts a Fahrenheit value to Kelvin.

    Args:
        degrees(integer): The temperature value in Fahrenheit.

    Returns:
        decimal: The kelvin value.
    """
    ABSOLUTE_ZERO = float('459.67')
    return round((((ABSOLUTE_ZERO + degrees) * 5) / 9), 2)


def convertFahrenheitToCelsius(degrees):
    """Converts a Fahrenheit value to Celsius.

    Args:
        degrees(integer): The temperature value in Fahrenheit.

    Returns:
        decimal: The Celsius value.
    """
    return (((float(degrees) - 32) * 5) / 9)


def convertKelvinToFahrenheit(degrees):
    """Converts a Kelvin value to Fahrenheit.

    Args:
        degrees(integer): The temperature value in kelvin.

    Returns:
        decimal: The Fahrenheit value.
    """
    ABSOLUTE_ZERO = float('459.67')
    return round((((float(degrees) * 9) / 5) - ABSOLUTE_ZERO), 2)


def convertKelvinToCelsius(degrees):
    """Converts a Kelvin value to Celsius.

    Args:
        degrees(integer): The temperature value in kelvin.

    Returns:
        decimal: The Celsius value.
    """
    ABSOLUTE_DIFFERENCE = float('273.15')
    return degrees - ABSOLUTE_DIFFERENCE

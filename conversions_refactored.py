#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: conversions_refactored.py."""


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """Converts a value from a unit to a different unit.

    Args:
        fromUnit(string): The unit we are converting from.
        toUnit(string): The unit we are converting to.
        value(integer): The value of fromUnit we are converting from.

    Returns:
        float: The converted value.
    """
    ABSOLUTE_DIFFERENCE = float('273.15')
    ABSOLUTE_ZERO = float('459.67')
    if fromUnit.lower() == "celsius":
        if toUnit.lower() == "kelvin":
            return ABSOLUTE_DIFFERENCE + value
        elif toUnit.lower() == "fahrenheit":
            return ((float(value) * 9 / 5) + 32)
        elif toUnit.lower() == "celsius":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    elif fromUnit.lower() == "fahrenheit":
        if toUnit.lower() == "celsius":
            return (((float(value) - 32) * 5) / 9)
        elif toUnit.lower() == "kelvin":
            return round((((ABSOLUTE_ZERO + value) * 5) / 9), 2)
        elif toUnit.lower() == "fahrenheit":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    elif fromUnit.lower() == "kelvin":
        if toUnit.lower() == "celsius":
            return value - ABSOLUTE_DIFFERENCE
        elif toUnit.lower() == "fahrenheit":
            return round((((float(value) * 9) / 5) - ABSOLUTE_ZERO), 2)
        elif toUnit.lower() == "kelvin":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    elif fromUnit.lower() == "miles":
        if toUnit.lower() == "yards":
            return float(value) * 1760
        elif toUnit.lower() == "meters":
            return round(float(value) * 1609.344, 3)
        elif toUnit.lower() == "miles":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    elif fromUnit.lower() == "yards":
        if toUnit.lower() == "meters":
            return float(value) * .9144
        elif toUnit.lower() == "miles":
            return round(float(value) / 1760, 8)
        elif toUnit.lower() == "yards":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    elif fromUnit.lower() == "meters":
        if toUnit.lower() == "yards":
            return round(float(value) / .9144, 7)
        elif toUnit.lower() == "miles":
            return round(float(value) / 1609.344, 7)
        elif toUnit.lower() == "meters":
            return value
        else:
            raise ConversionNotPossible, "Conversion Is Not Possible To Unit"
    else:
        raise ConversionNotPossible, "Conversion Is Not Possible To Unit"

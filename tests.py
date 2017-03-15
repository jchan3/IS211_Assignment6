#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: assignment5.py."""


import decimal
import unittest
import conversions
import conversions_refactored


class KnownKelvinValues(unittest.TestCase):
    knownKelvinValues = ((300.00, 573.15),
                    (500.00, 773.15),
                    (410.00, 683.15),
                    (350.00, 623.15),
                    (120.00, 393.15))

    def testConvertCelsiusToKelvin(self):
        """convertCelsiusToKelvin should give known result with known input.
        """
        for celsius, kelvin in self.knownKelvinValues:
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)


class KnownFahrenheitValues(unittest.TestCase):
    knownFahrenheitValues = ((300.00, 572.00),
                    (500.00, 932.00),
                    (410.00, 770.00),
                    (350.00, 662.00),
                    (120.00, 248.00))

    def testConvertCelsiusToFahrenheit(self):
        """convertCelsiusToFahrenheit should give known result with known
            input.
        """
        for celsius, fahrenheit in self.knownFahrenheitValues:
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)


class KnownFahrenheitToCelsiusValues(unittest.TestCase):
    knownFahrenheitToCelsiusValues = ((572.00, 300.00),
                    (932.00, 500.00),
                    (770.00, 410.00),
                    (662.00, 350.00),
                    (248.00, 120.00))

    def testConvertFahrenheitToCelsius(self):
        """convertFahrenheitToCelsius should give known result with known input.
        """
        for fahrenheit, celsius in self.knownFahrenheitToCelsiusValues:
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)


class KnownFahrenheitToKelvinValues(unittest.TestCase):
    knownFahrenheitToKelvinValues = ((572.00, 573.15),
                    (932.00, 773.15),
                    (770.00, 683.15),
                    (662.00, 623.15),
                    (248.00, 393.15))

    def testConvertFahrenheitToKelvin(self):
        """convertFahrenheitToKelvin should give known result with known
            input.
        """
        for fahrenheit, kelvin in self.knownFahrenheitToKelvinValues:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)


class KnownKelvinToCelsiusValues(unittest.TestCase):
    knownKelvinToCelsiusValues = ((573.15, 300.00),
                    (773.15, 500.00),
                    (683.15, 410.00),
                    (623.15, 350.00),
                    (393.15, 120.00))

    def testConvertKelvinToCelsius(self):
        """convertKelvinToCelsius should give known result with known input.
        """
        for kelvin, celsius in self.knownKelvinToCelsiusValues:
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)


class KnownKelvinToFahrenheitValues(unittest.TestCase):
    knownKelvinToFahrenheitValues = ((573.15, 572.00),
                    (773.15, 932.00),
                    (683.15, 770.00),
                    (623.15, 662.00),
                    (393.15, 248.00))

    def testConvertKelvinToFahrenheit(self):
        """convertKelvinToFahrenheit should give known result with known
            input.
        """
        for kelvin, fahrenheit in self.knownKelvinToFahrenheitValues:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)


class KnownConversionValues(unittest.TestCase):
    knownConversionValues = (("yards", "miles", 1, 0.00056818),
                    ("yards", "miles", 7, 0.00397727),
                    ("yards", "miles", 50, 0.02840909),
                    ("yards", "miles", 250, 0.14204545),
                    ("yards", "miles", 5000, 2.84090909),
                    ("miles", "yards", 1, 1760),
                    ("miles", "yards", 7, 12320),
                    ("miles", "yards", 50, 88000),
                    ("miles", "yards", 250, 440000),
                    ("miles", "yards", 5000, 8800000),
                    ("yards", "meters", 1, .9144),
                    ("yards", "meters", 9, 8.2296),
                    ("yards", "meters", 250, 228.6),
                    ("meters", "yards", 1, 1.0936133),
                    ("meters", "yards", 7, 7.6552931),
                    ("meters", "yards", 250, 273.4033246),
                    ("miles", "meters", 1, 1609.344),
                    ("miles", "meters", 9, 14484.096),
                    ("miles", "meters", 250, 402336),
                    ("meters", "miles", 1, 0.0006214),
                    ("meters", "miles", 9, 0.0055923),
                    ("meters", "miles", 250, 0.1553428),
                    ("miles", "miles", 111, 111),
                    ("meters", "meters", 212, 212),
                    ("yards", "yards", 333, 333),
                    ("Kelvin", "Fahrenheit", 573.15, 572.00),
                    ("kelvin", "fahrenheit", 623.15, 662.00),
                    ("Kelvin", "Fahrenheit", 393.15, 248.00),
                    ("Kelvin", "Celsius", 573.15, 300.00),
                    ("kelvin", "celsius", 683.15, 410.00),
                    ("Kelvin", "celsius", 393.15, 120.00),
                    ("fahrenheit", "Kelvin", 572.00, 573.15),
                    ("fahrenheit", "kelvin", 770.00, 683.15),
                    ("Fahrenheit", "kelvin", 248.00, 393.15),
                    ("Fahrenheit", "Celsius", 770.00, 410.00),
                    ("Fahrenheit", "celsius", 248.00, 120.00),
                    ("fahrenheit", "celsius", 572.00, 300.00),
                    ("celsius", "fahrenheit", 120.00, 248.00),
                    ("celsius", "fahrenheit", 410.00, 770.00),
                    ("celsius", "fahrenheit", 300.00, 572.00),
                    ("Celsius", "kelvin", 300.00, 573.15),
                    ("Celsius", "kelvin", 410.00, 683.15),
                    ("Celsius", "kelvin", 120.00, 393.15),
                    ("Celsius", "Celsius", 300.00, 300.00),
                    ("kelvin", "kelvin", 410.00, 410.00),
                    ("fahrenheit", "fahrenheit", 120.00, 120.00))

    def testConvertRefactored(self):
        """convertYardsToMiles should give known result with known input.
        """
        for frm, toU, value, convert in self.knownConversionValues:
            result = conversions_refactored.convert(frm, toU, value)
            self.assertEqual(convert, result)


class ToConversionBadInput(unittest.TestCase):
    knownBadInputValues = (("yards", "fahrenheit", 1, 0.00056818),
                    ("yards", "kelvin", 7, 0.00397727),
                    ("yards", "celsius", 50, 0.02840909),
                    ("celsius", "yards", 250, 0.14204545),
                    ("kelvin", "yards", 5000, 2.84090909),
                    ("fahrenheit", "yards", 5000, 2.84090909),
                    ("miles", "celsius", 1, 1760),
                    ("miles", "kelvin", 7, 12320),
                    ("miles", "fahrenheit", 50, 88000),
                    ("celsius", "miles", 250, 440000),
                    ("fahrenheit", "miles", 5000, 8800000),
                    ("kelvin", "miles", 1, 1760),
                    ("meters", "kelvin", 1, 0.0006214),
                    ("meters", "fahrenheit", 9, 0.0055923),
                    ("meters", "celsius", 250, 0.1553428),
                    ("celsius", "meters", 1, 0.0006214),
                    ("fahrenheit", "meters", 9, 0.0055923),
                    ("kelvin", "meters", 250, 0.1553428))

    def testBadInput(self):
        for frm, toU, value, convert in self.knownBadInputValues:
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.convert, frm, toU, value)


if __name__ == "__main__":
    unittest.main()

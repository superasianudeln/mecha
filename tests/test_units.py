import unittest

from units.constants import *
from units.unit import Unit


class TestUnitClass(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Unit("m", {"Length": 1}), METER)
        self.assertNotEqual(Unit("m", {"Length": 1}), SECOND)

    def test_canonicalization(self):
        self.assertEqual(Unit("s*m", {"Time": 1, "Length": 1}), METER * SECOND)

    def test_multiplication(self):
        self.assertEqual(METER * SECOND, Unit("m*s", {"Length": 1, "Time": 1}))

    def test_division(self):
        self.assertEqual(METER / SECOND, Unit("m/s", {"Length": 1, "Time": -1}))

    def test_complex_operations(self):
        compound_unit = (METER * SECOND) / KILOGRAM
        self.assertEqual(compound_unit, Unit("m*s/kg", {"Length": 1, "Time": 1, "Mass": -1}))

    def test_exponentiation(self):
        self.assertEqual(METER ** 3, Unit("m^3", {"Length": 3}))

    def test_complex_exponentiation(self):
        compound_unit = METER * SECOND
        result = compound_unit ** 3
        self.assertEqual(result, Unit("(m*s)^3", {"Length": 3, "Time": 3}))

    def test_inverse(self):
        self.assertEqual(METER ** -1, Unit("m^-1", {"Length": -1}))

    def test_dimensionless(self):
        self.assertEqual(METER * METER ** -1, Unit("", {}))

    def test_validation(self):
        with self.assertRaises(ValueError):
            Unit("m", {"Length": 1.5})

    def test_nested_operations(self):
        unit = Unit("A", {"Current": 1})
        result = (METER * SECOND) / (KILOGRAM * unit)
        self.assertEqual(result, Unit("m*s/(kg*A)", {"Length": 1, "Time": 1, "Mass": -1, "Current": -1}))

    def test_mixed_exponentiation(self):
        compound_unit = (METER * SECOND) ** 2
        result = compound_unit / (KILOGRAM ** 3)
        self.assertEqual(result, Unit("(m*s)^2/kg^3", {"Length": 2, "Time": 2, "Mass": -3}))

    def test_zero_and_negative_powers(self):
        compound_unit = (METER * SECOND) ** 0
        result = compound_unit * (KILOGRAM ** -1)
        self.assertEqual(result, Unit("kg^-1", {"Mass": -1}))


if __name__ == "__main__":
    unittest.main()

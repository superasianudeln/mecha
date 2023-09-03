import unittest
from units.unit import Unit


class TestUnitClass(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Unit("m", {"Length": 1}), Unit("m", {"Length": 1}))
        self.assertNotEqual(Unit("m", {"Length": 1}), Unit("s", {"Time": 1}))

    def test_canonicalization(self):
        self.assertEqual(Unit("s*m", {"Time": 1, "Length": 1}), Unit("m*s", {"Length": 1, "Time": 1}))

    def test_multiplication(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        self.assertEqual(unit1 * unit2, Unit("m*s", {"Length": 1, "Time": 1}))

    def test_division(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        self.assertEqual(unit1 / unit2, Unit("m/s", {"Length": 1, "Time": -1}))

    def test_complex_operations(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        unit3 = Unit("kg", {"Mass": 1})
        compound_unit = (unit1 * unit2) / unit3
        self.assertEqual(compound_unit, Unit("m*s/kg", {"Length": 1, "Time": 1, "Mass": -1}))

    def test_exponentiation(self):
        unit1 = Unit("m", {"Length": 1})
        self.assertEqual(unit1 ** 3, Unit("m^3", {"Length": 3}))

    def test_complex_exponentiation(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        compound_unit = unit1 * unit2
        result = compound_unit ** 3
        self.assertEqual(result, Unit("(m*s)^3", {"Length": 3, "Time": 3}))

    def test_inverse(self):
        unit1 = Unit("m", {"Length": 1})
        self.assertEqual(unit1 ** -1, Unit("m^-1", {"Length": -1}))

    def test_dimensionless(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("m^-1", {"Length": -1})
        self.assertEqual(unit1 * unit2, Unit("", {}))

    def test_validation(self):
        with self.assertRaises(ValueError):
            Unit("m", {"Length": 1.5})

    def test_nested_operations(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        unit3 = Unit("kg", {"Mass": 1})
        unit4 = Unit("A", {"Current": 1})
        result = (unit1 * unit2) / (unit3 * unit4)
        self.assertEqual(result, Unit("m*s/(kg*A)", {"Length": 1, "Time": 1, "Mass": -1, "Current": -1}))

    def test_mixed_exponentiation(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        compound_unit = (unit1 * unit2) ** 2
        unit3 = Unit("kg", {"Mass": 1})
        result = compound_unit / (unit3 ** 3)
        self.assertEqual(result, Unit("(m*s)^2/kg^3", {"Length": 2, "Time": 2, "Mass": -3}))

    def test_zero_and_negative_powers(self):
        unit1 = Unit("m", {"Length": 1})
        unit2 = Unit("s", {"Time": 1})
        unit3 = Unit("kg", {"Mass": 1})
        compound_unit = (unit1 * unit2) ** 0
        result = compound_unit * (unit3 ** -1)
        self.assertEqual(result, Unit("kg^-1", {"Mass": -1}))


if __name__ == "__main__":
    unittest.main()

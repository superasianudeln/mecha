import unittest

from mecha.units.unit import Unit


class TestUnitDivision(unittest.TestCase):

    def test_same_dimension_division(self):
        u1 = Unit({'M': 1, 'L': 1, 'T': 0})
        u2 = Unit({'M': 1, 'L': 1, 'T': 0})
        result = u1 / u2
        self.assertEqual(str(result), '')  # Dimensionless

    def test_different_dimension_division(self):
        u1 = Unit({'M': 1, 'L': 2, 'T': -1})
        u2 = Unit({'M': 0, 'L': 1, 'T': -1})
        result = u1 / u2
        self.assertEqual(str(result), 'kg*m')

    def test_zero_dimension_division(self):
        u1 = Unit({'M': 1, 'L': 0, 'T': 0})
        u2 = Unit({'M': 1, 'L': 0, 'T': 0})
        result = u1 / u2
        self.assertEqual(str(result), '')  # Dimensionless

    def test_negative_power_division(self):
        u1 = Unit({'M': -1, 'L': -2, 'T': 1})
        u2 = Unit({'M': 0, 'L': -1, 'T': 1})
        result = u1 / u2
        self.assertEqual(str(result), 'kg^-1*m^-1')

    def test_dimensionless_division(self):
        u1 = Unit({'M': 0, 'L': 0, 'T': 0})
        u2 = Unit({'M': 0, 'L': 0, 'T': 0})
        result = u1 / u2
        self.assertEqual(str(result), '')  # Dimensionless

    def test_zero_dimension_divided_by_non_zero(self):
        u1 = Unit({'M': 0, 'L': 0, 'T': 0})
        u2 = Unit({'M': 1, 'L': 2, 'T': -1})
        result = u1 / u2
        self.assertEqual(str(result), 'kg^-1*m^-2*s')


if __name__ == '__main__':
    unittest.main()

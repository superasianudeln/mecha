import unittest

from mecha.units.unit import Unit


class TestUnitMethods(unittest.TestCase):

    def test_mul_same_dimensions(self):
        unit1 = Unit({'M': 1, 'L': 1, 'T': 0})
        unit2 = Unit({'M': 1, 'L': 1, 'T': 0})
        result = unit1 * unit2
        expected = Unit({'M': 2, 'L': 2})
        self.assertEqual(result, expected)

    def test_mul_different_dimensions(self):
        unit1 = Unit({'M': 1, 'L': 1, 'T': 0})
        unit2 = Unit({'M': 0, 'L': 0, 'T': 1})
        result = unit1 * unit2
        expected = Unit({'M': 1, 'L': 1, 'T': 1})
        self.assertEqual(result, expected)

    def test_mul_zero_power(self):
        unit1 = Unit({'M': 1, 'L': 0, 'T': 0})
        unit2 = Unit({'M': 0, 'L': 0, 'T': 0})
        result = unit1 * unit2
        expected = Unit({'M': 1})
        self.assertEqual(result, expected)

    def test_pow_positive_integer(self):
        unit = Unit({'M': 1, 'L': 1, 'T': 1})
        result = unit ** 2
        expected = Unit({'M': 2, 'L': 2, 'T': 2})
        self.assertEqual(result, expected)

    def test_pow_zero(self):
        unit = Unit({'M': 1, 'L': 1, 'T': 1})
        result = unit ** 0
        expected = Unit({})
        self.assertEqual(result, expected)

    def test_pow_negative_integer(self):
        unit = Unit({'M': 1, 'L': 1, 'T': 1})
        result = unit ** -1
        expected = Unit({'M': -1, 'L': -1, 'T': -1})
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

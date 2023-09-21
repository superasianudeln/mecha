import unittest

from mecha.units.unit import Unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit1 = Unit({"M": 1, "L": 1, "T": 0})  # kg*m
        self.unit2 = Unit({"M": 1, "L": 1, "T": 0})  # kg*m
        self.unit3 = Unit({"M": 1, "L": 0, "T": 1})  # kg*s
        self.unit4 = Unit({"M": 0, "L": 1, "T": 1})  # m*s

    def test_compute_unit(self):
        self.assertEqual(str(self.unit1), "kg*m")
        self.assertEqual(str(self.unit3), "kg*s")
        self.assertEqual(str(self.unit4), "m*s")

    def test_add(self):
        result = self.unit1 + self.unit2
        self.assertEqual(str(result), "kg*m")
        with self.assertRaises(ValueError):
            _ = self.unit1 + self.unit3

    def test_sub(self):
        result = self.unit1 - self.unit2
        self.assertEqual(str(result), "kg*m")
        with self.assertRaises(ValueError):
            _ = self.unit1 - self.unit3

    def test_eq(self):
        self.assertTrue(self.unit1 == self.unit2)
        self.assertFalse(self.unit1 == self.unit3)

    def test_ne(self):
        self.assertTrue(self.unit1 != self.unit3)
        self.assertFalse(self.unit1 != self.unit2)

    def test_lt(self):
        self.assertTrue(self.unit1 < self.unit3)
        self.assertFalse(self.unit3 < self.unit1)

    def test_le(self):
        self.assertTrue(self.unit1 <= self.unit2)
        self.assertTrue(self.unit1 <= self.unit3)
        self.assertFalse(self.unit3 <= self.unit1)

    def test_gt(self):
        self.assertTrue(self.unit3 > self.unit1)
        self.assertFalse(self.unit1 > self.unit3)

    def test_ge(self):
        self.assertTrue(self.unit3 >= self.unit1)
        self.assertTrue(self.unit1 >= self.unit2)
        self.assertFalse(self.unit1 >= self.unit3)


if __name__ == "__main__":
    unittest.main()

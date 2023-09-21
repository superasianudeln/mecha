import unittest

from mecha.units.unit import Unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        # Define some basic units for testing
        self.length = Unit({"L": 1})
        self.time = Unit({"T": 1})
        self.mass = Unit({"M": 1})

    def test_addition(self):
        with self.assertRaises(ValueError):
            result = self.length + self.time  # Different dimensions

        result = self.length + self.length
        self.assertEqual(result.dimension, {"L": 1})

    def test_subtraction(self):
        with self.assertRaises(ValueError):
            result = self.length - self.time  # Different dimensions

        result = self.length - self.length
        self.assertEqual(result.dimension, {"L": 1})

    def test_multiplication(self):
        result = self.length * self.time
        self.assertEqual(result.dimension, {"L": 1, "T": 1})

        result = self.length * self.length
        self.assertEqual(result.dimension, {"L": 2})

    def test_division(self):
        result = self.length / self.time
        self.assertEqual(result.dimension, {"L": 1, "T": -1})

        result = self.length / self.length
        self.assertEqual(result.dimension, {})  # Dimensionless

    def test_power(self):
        result = self.length**2
        self.assertEqual(result.dimension, {"L": 2})

        result = self.length**-1
        self.assertEqual(result.dimension, {"L": -1})

    def test_comparison(self):
        self.assertTrue(self.length == self.length)
        self.assertFalse(self.length == self.time)
        self.assertTrue(self.length != self.time)
        self.assertTrue(self.length != self.mass)
        self.assertTrue(self.length != self.mass)
        self.assertTrue(self.mass != self.length)
        self.assertTrue(self.mass != self.length)

    def test_edge_cases(self):
        # Test zero power
        result = self.length**0
        self.assertEqual(result.dimension, {})

        # Test negative power
        result = self.length**-2
        self.assertEqual(result.dimension, {"L": -2})

        # Test multiplication resulting in zero power
        inverse_length = Unit({"L": -1})
        result = self.length * inverse_length
        self.assertEqual(result.dimension, {})


if __name__ == "__main__":
    unittest.main()

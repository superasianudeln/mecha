import unittest

from mecha.units.constants import *
from mecha.units.physical_quantity import PhysicalQuantity


class TestPhysicalQuantity(unittest.TestCase):

    def setUp(self):
        # Define some units for testing
        self.meter = METER
        self.second = SECOND
        self.meter_per_second = VELOCITY_UNIT

        # Define some physical quantities for testing
        self.distance1 = PhysicalQuantity(5, self.meter)
        self.distance2 = PhysicalQuantity(10, self.meter)
        self.time = PhysicalQuantity(2, self.second)
        self.velocity = PhysicalQuantity(3, self.meter_per_second)

    def test_addition(self):
        result = self.distance1 + self.distance2
        self.assertEqual(result.value, 15)
        self.assertEqual(result.unit, self.meter)

        with self.assertRaises(ValueError):
            _ = self.distance1 + self.time  # Different units

    def test_subtraction(self):
        result = self.distance2 - self.distance1
        self.assertEqual(result.value, 5)
        self.assertEqual(result.unit, self.meter)

        with self.assertRaises(ValueError):
            _ = self.distance1 - self.time  # Different units

    def test_multiplication(self):
        result = self.distance1 * self.time
        self.assertEqual(result.value, 10)
        self.assertEqual(result.unit, self.meter * self.second)

        result_scalar = self.distance1 * 2
        self.assertEqual(result_scalar.value, 10)
        self.assertEqual(result_scalar.unit, self.meter)

    def test_division(self):
        result = self.distance1 / self.time
        self.assertEqual(result.value, 2.5)
        self.assertEqual(result.unit, self.meter_per_second)

        result_scalar = self.distance1 / 2
        self.assertEqual(result_scalar.value, 2.5)
        self.assertEqual(result_scalar.unit, self.meter)

    def test_equality(self):
        self.assertTrue(self.distance1 == PhysicalQuantity(5, self.meter))
        self.assertFalse(self.distance1 == self.distance2)

    def test_str_representation(self):
        self.assertEqual(str(self.distance1), "5 m")
        self.assertEqual(str(self.velocity), "3 m*s^-1")


if __name__ == '__main__':
    unittest.main()

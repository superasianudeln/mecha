import unittest

from mecha.units.physical_quantity import PhysicalQuantity
from mecha.units.unit import Unit


class TestAdvancedPhysicalQuantity(unittest.TestCase):
    def setUp(self):
        # Define some units for testing
        self.meter = Unit({"L": 1})
        self.second = Unit({"T": 1})
        self.meter_per_second = Unit({"L": 1, "T": -1})
        self.meter_per_second_squared = Unit({"L": 1, "T": -2})

        # Define some physical quantities for testing
        self.distance1 = PhysicalQuantity(5, self.meter)
        self.distance2 = PhysicalQuantity(10, self.meter)
        self.time = PhysicalQuantity(2, self.second)
        self.velocity = PhysicalQuantity(3, self.meter_per_second)
        self.acceleration = PhysicalQuantity(4, self.meter_per_second_squared)

    def test_complex_operations(self):
        # Test the formula: s = ut + 0.5at^2
        result = self.velocity * self.time + 0.5 * self.acceleration * self.time**2
        self.assertEqual(result.value, 14)
        self.assertEqual(result.unit, self.meter)

    def test_zero_value_operations(self):
        zero_distance = PhysicalQuantity(0, self.meter)
        result = self.distance1 + zero_distance
        self.assertEqual(result, self.distance1)

        result = self.distance1 - zero_distance
        self.assertEqual(result, self.distance1)

    def test_negative_value_operations(self):
        negative_distance = PhysicalQuantity(-5, self.meter)
        result = self.distance1 + negative_distance
        self.assertEqual(result.value, 0)
        self.assertEqual(result.unit, self.meter)

    def test_high_power_operations(self):
        # Testing cube of a unit
        cubed_distance_unit = self.meter**3
        cubed_distance = PhysicalQuantity(125, cubed_distance_unit)
        result = self.distance1**3
        self.assertEqual(result, cubed_distance)

    def test_division_by_zero(self):
        # Test division by zero for integer
        with self.assertRaises(ValueError) as context:
            _ = self.distance1 / 0
        self.assertEqual(str(context.exception), "Cannot divide by zero")

        # Test division by a zero-valued PhysicalQuantity
        zero_velocity = PhysicalQuantity(0, self.meter_per_second)
        with self.assertRaises(ValueError) as context:
            _ = self.distance1 / zero_velocity
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_multiplication_with_zero(self):
        zero_distance = PhysicalQuantity(0, self.meter)
        result = self.distance1 * zero_distance
        self.assertEqual(result.value, 0)
        self.assertEqual(result.unit, self.meter**2)


if __name__ == "__main__":
    unittest.main()

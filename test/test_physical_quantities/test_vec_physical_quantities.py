import unittest

import numpy as np

from mecha.maths.vector import Vector
from mecha.units.constants import METER, SECOND
from mecha.units.physical_quantity import PhysicalQuantity


class TestPhysicalQuantityWithVectors(unittest.TestCase):
    def setUp(self):
        # Sample units for testing
        self.unit_a = METER
        self.unit_b = SECOND

        # Sample vectors for testing
        self.vector_zero = Vector(0, 0, 0)
        self.vector_1 = Vector(1, 2, 3)
        self.vector_2 = Vector(4, 5, 6)
        self.vector_negative = Vector(-1, -2, -3)

    def test_addition_with_same_units(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq2 = PhysicalQuantity(self.vector_2, self.unit_a)
        result = pq1 + pq2
        expected_vector = Vector(5, 7, 9)
        self.assertEqual(result.value, expected_vector)
        self.assertEqual(result.unit, self.unit_a)

    def test_subtraction_with_same_units(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq2 = PhysicalQuantity(self.vector_2, self.unit_a)
        result = pq1 - pq2
        expected_vector = Vector(-3, -3, -3)
        self.assertEqual(result.value, expected_vector)
        self.assertEqual(result.unit, self.unit_a)

    def test_multiplication_with_scalar(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        scalar = 3
        result = pq1 * scalar
        expected_vector = Vector(3, 6, 9)
        self.assertEqual(result.value, expected_vector)
        self.assertEqual(result.unit, self.unit_a)

    def test_division_with_scalar(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        scalar = 2
        result = pq1 / scalar
        expected_vector = Vector(0.5, 1, 1.5)
        self.assertEqual(result.value, expected_vector)
        self.assertEqual(result.unit, self.unit_a)

    def test_incompatible_units_addition(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq2 = PhysicalQuantity(self.vector_2, self.unit_b)
        with self.assertRaises(ValueError):
            _ = pq1 + pq2

    def test_incompatible_units_subtraction(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq2 = PhysicalQuantity(self.vector_2, self.unit_b)
        with self.assertRaises(ValueError):
            _ = pq1 - pq2

    def test_zero_vector_addition(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq_zero = PhysicalQuantity(self.vector_zero, self.unit_a)
        result = pq1 + pq_zero
        self.assertEqual(result.value, self.vector_1)
        self.assertEqual(result.unit, self.unit_a)

    def test_zero_vector_direction(self):
        with self.assertRaises(ValueError):
            _ = self.vector_zero.direction

    def test_vector_cross_product(self):
        PhysicalQuantity(self.vector_1, self.unit_a)
        PhysicalQuantity(self.vector_2, self.unit_a)
        cross_product_vector = self.vector_1.cross(self.vector_2)
        self.assertEqual(cross_product_vector, Vector(-3, 6, -3))

    def test_vector_dot_product(self):
        PhysicalQuantity(self.vector_1, self.unit_a)
        PhysicalQuantity(self.vector_2, self.unit_a)
        dot_product_value = self.vector_1.dot(self.vector_2)
        self.assertEqual(dot_product_value, 32)  # 1*4 + 2*5 + 3*6 = 32

    def test_negative_vector_addition(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        pq_negative = PhysicalQuantity(self.vector_negative, self.unit_a)
        result = pq1 + pq_negative
        self.assertEqual(result.value, self.vector_zero)
        self.assertEqual(result.unit, self.unit_a)

    def test_vector_magnitude(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        magnitude = pq1.value.magnitude
        self.assertEqual(magnitude, np.sqrt(14))  # sqrt(1^2 + 2^2 + 3^2)

    def test_vector_division_by_zero(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        with self.assertRaises(ValueError):
            _ = pq1 / 0

    def test_vector_power(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        result = pq1**2
        expected_magnitude = self.vector_1.magnitude**2
        self.assertEqual(result.value, expected_magnitude)
        self.assertEqual(result.unit, self.unit_a**2)

    def test_vector_and_scalar_division(self):
        pq1 = PhysicalQuantity(self.vector_1, self.unit_a)
        scalar = 0
        with self.assertRaises(ValueError):
            _ = pq1 / scalar


if __name__ == "__main__":
    unittest.main()

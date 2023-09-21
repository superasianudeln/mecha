import unittest

import numpy as np

from mecha.maths.vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(4, 5, 6)
        self.v3 = Vector(0, 0, 0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude, np.linalg.norm([1, 2, 3]))

    def test_direction(self):
        with self.assertRaises(ValueError):
            self.v3.direction
        self.assertTrue(np.array_equal(self.v1.direction, np.array([1, 2, 3]) / np.linalg.norm([1, 2, 3])))

    def test_addition(self):
        result = self.v1 + self.v2
        self.assertTrue(np.array_equal(result.vector, np.array([5, 7, 9])))

    def test_subtraction(self):
        result = self.v1 - self.v2
        self.assertTrue(np.array_equal(result.vector, np.array([-3, -3, -3])))

    def test_dot_product(self):
        self.assertEqual(self.v1.dot(self.v2), 32)

    def test_cross_product(self):
        result = self.v1.cross(self.v2)
        self.assertTrue(np.array_equal(result.vector, np.array([-3, 6, -3])))

    def test_scalar_multiplication(self):
        result = self.v1 * 2
        self.assertTrue(np.array_equal(result.vector, np.array([2, 4, 6])))

    def test_scalar_division(self):
        with self.assertRaises(ValueError):
            self.v1 / 0
        result = self.v1 / 2
        self.assertTrue(np.array_equal(result.vector, np.array([0.5, 1, 1.5])))

    def test_string_representation(self):
        self.assertEqual(str(self.v1), "[1 2 3]")

    def test_repr_representation(self):
        self.assertEqual(repr(self.v1), "Vector(1, 2, 3)")

    def test_equality(self):
        self.assertTrue(self.v1 == Vector(1, 2, 3))
        self.assertFalse(self.v1 == self.v2)

    def test_length(self):
        self.assertEqual(len(self.v1), 3)

    def test_zero_vector_addition(self):
        result = self.v1 + self.v3
        self.assertTrue(np.array_equal(result.vector, self.v1.vector))

    def test_zero_vector_subtraction(self):
        result = self.v1 - self.v3
        self.assertTrue(np.array_equal(result.vector, self.v1.vector))

    def test_zero_vector_dot_product(self):
        self.assertEqual(self.v1.dot(self.v3), 0)

    def test_zero_vector_cross_product(self):
        result = self.v1.cross(self.v3)
        self.assertTrue(np.array_equal(result.vector, np.array([0, 0, 0])))

    def test_zero_vector_scalar_multiplication(self):
        result = self.v3 * 2
        self.assertTrue(np.array_equal(result.vector, np.array([0, 0, 0])))

    def test_zero_vector_scalar_division(self):
        with self.assertRaises(ValueError):
            self.v3 / 0
        result = self.v3 / 2
        self.assertTrue(np.array_equal(result.vector, np.array([0, 0, 0])))

    def test_vector_equality_with_floats(self):
        v4 = Vector(1.0000001, 2, 3)
        self.assertFalse(self.v1 == v4)

    def test_vector_with_negative_values(self):
        v5 = Vector(-1, -2, -3)
        self.assertEqual(v5.magnitude, self.v1.magnitude)
        self.assertTrue(np.array_equal(v5.direction, -1 * self.v1.direction))

    def test_vector_length_after_operations(self):
        result = self.v1 + self.v2
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()

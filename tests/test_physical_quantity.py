import unittest

from units.physical_quantity import PhysicalQuantity


class TestPhysicalQuantity(unittest.TestCase):

    def test_initialization(self):
        pq = PhysicalQuantity(5, "m")
        self.assertEqual(pq.value, 5)
        self.assertEqual(pq.unit, "m")

    def test_str_representation(self):
        pq = PhysicalQuantity(5, "m")
        self.assertEqual(str(pq), "5 m")

        pq = PhysicalQuantity(5.0, "m")
        self.assertEqual(str(pq), "5 m")

        pq = PhysicalQuantity(5.5, "m")
        self.assertEqual(str(pq), "5.5 m")

    def test_mul_physical_quantities(self):
        pq1 = PhysicalQuantity(5, "m")
        pq2 = PhysicalQuantity(2, "s")
        pq_result = pq1 * pq2
        self.assertEqual(pq_result.value, 10)
        self.assertEqual(pq_result.unit, "m*s")

    def test_mul_with_scalar(self):
        pq = PhysicalQuantity(5, "m")
        pq_result = pq * 2
        self.assertEqual(pq_result.value, 10)
        self.assertEqual(pq_result.unit, "m")

    def test_complex_units(self):
        pq1 = PhysicalQuantity(9.8, "m/s^2")
        pq2 = PhysicalQuantity(2, "s")
        pq_result = pq1 * pq2
        self.assertEqual(pq_result.value, 19.6)
        self.assertEqual(pq_result.unit, "m/s^2*s")


if __name__ == "__main__":
    unittest.main()

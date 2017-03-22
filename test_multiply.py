import unittest
import multiply

class MultiplyTestCase(unittest.TestCase):
    def _test_multiplies_numbers(self):
        result = multiply.multiply(2, 3)
        self.assertEqual(6, result)

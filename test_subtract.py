import unittest
import subtract

class SubtractTestcase(unittest.TestCase):

    def test_subtracts_numbers(self):
        result = subtract.minus(5, 3)
        self.assertEqual(2, result)
        


if __name__ =="__main__":
    unittest.main()
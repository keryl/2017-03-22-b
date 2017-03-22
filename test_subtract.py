import unittest
import subtract

class MinusTestcase(unittest.TestCase):

    def test_subtracts_numbers(self):
        result = subtract.minus(5, 3)
        self.assertEqual(2, result)

    def test_does_not_accept_strings(self):
        result = subtract.minus("test", 3)
        self.assertEqual("numbers only", result)

    def test_does_not_accept_booleans(self):
        result = subtract.minus(3, True)
        self.assertEqual("numbers only", result)

class IsDigitTestCase(unittest.TestCase):

    def test_it_returns_true_if_int(self):
        result = subtract.isdigit(2)
        self.assertTrue(result)

    def test_it_returns_true_if_float(self):
        result = subtract.isdigit(1.2)
        self.assertTrue(result)

    def test_it_returns_false_if_string(self):
        result = subtract.isdigit("five")
        self.assertFalse(result)

    def test_it_returns_false_if_boolean(self):
        result = subtract.isdigit(True)
        self.assertFalse(result)

if __name__ =="__main__":
    unittest.main()
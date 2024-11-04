from math_functions import power, division, IndeterminateFormError
import unittest

class Test_Math_Functions(unittest.TestCase):

    def test_power_positive(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 2), 25)

    def test_power_negative(self):
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(5, -2), 0.04)

    def test_power_zero(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 2), 0)
    
    def test_power_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 4), 0)
    
    def test_indeterminate_power(self):
        with self.assertRaises(IndeterminateFormError):
            power(0, 0)
        

    def test_power_non_integer(self):
        self.assertEqual(power(0.5, 2), 0.25)
        self.assertEqual(power(4, 0.5), 2)

    def test_division_positive(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(15, 3), 5)

    def test_division_negative(self):
        self.assertEqual(division(-10, 2), -5)
        self.assertEqual(division(10, -2), -5)
        self.assertEqual(division(-15, -3), 5)

    def test_division_zero(self):
        self.assertEqual(division(0, 10), 0)
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_division_by_one(self):
        self.assertEqual(division(10, 1), 10)

if __name__ == '__main__':
    unittest.main()

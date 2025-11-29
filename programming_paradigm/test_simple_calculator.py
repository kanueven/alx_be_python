import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        #self.assertEqual(actual_result, expected_result)
#Hey, is the first thing equal to the second thing?”
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
            """Test the subtraction method."""
            self.assertEqual(self.calc.subtract(5, 3), 2)
            self.assertEqual(self.calc.subtract(0, 0), 0)
            self.assertEqual(self.calc.subtract(-1, -1), 0) 
    def test_multiplication(self):
            """Test the multiplication method."""
            self.assertEqual(self.calc.multiply(4, 5), 20)
            self.assertEqual(self.calc.multiply(-1, 1), -1)
            self.assertEqual(self.calc.multiply(0, 100), 0)
    def test_division(self):
            """Test the division method."""
            self.assertEqual(self.calc.divide(10, 2), 5)
            self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero case
            self.assertEqual(self.calc.divide(-6, -2), 3)
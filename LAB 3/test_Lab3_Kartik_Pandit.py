# Program Name: Test Cases for Area Calculator
# Program Author: Kartik
# Importing the unittest module for writing test cases
import unittest
# Importing the AreaCalculator class from the main calculator module
from Lab3_Kartik_Pandit import AreaCalculator

# Test class to test the methods of the AreaCalculator class
class TestAreaCalculator(unittest.TestCase):
    # Setup method that runs before each test case
    def setUp(self):
        # Creating an instance of the AreaCalculator class
        self.calculator = AreaCalculator()

    # Test case for the circle_area method
    def test_circle_area(self):
        # Calculating the area of a circle with radius 8.5
        result = self.calculator.circle_area(8.5)
        # Asserting that the result is approximately 226.98 with 2 decimal places precision
        self.assertAlmostEqual(result, 226.98, places=2)

   # Test case for the trapezium_area method
    def test_trapezium_area(self):
       # Calculating the area of a trapezium with bases 3 and 7, and height 9
       result = self.calculator.trapezium_area(3, 7, 9)
       # Asserting that the result is approximately equal to 57.8 with a small delta
       self.assertAlmostEqual(result, 45)


   # Test case for the ellipse_area method
    def test_ellipse_area(self):
        # Calculating the area of an ellipse with major axis 3 and minor axis 5
        result = self.calculator.ellipse_area(3, 5)
        # Asserting that the result is approximately 47.12 with 2 decimal places precision
        self.assertAlmostEqual(result, 47.12, places=2)


    # Test case for the rhombus_area method
    def test_rhombus_area(self):
        # Calculating the area of a rhombus with diagonals 5.5 and 7.2
        result = self.calculator.rhombus_area(5.5, 7.2)
        # Asserting that the result is equal to 19.8
        self.assertEqual(result, 19.8)

# Entry point to run the unit tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()

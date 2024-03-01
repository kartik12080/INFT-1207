# Program Name: Area Calculator
# Program Author: Kartik
# Importing the math module for mathematical operations
import math
# Class definition for the AreaCalculator
class AreaCalculator:
    # Method to calculate the area of a circle
    def circle_area(self, radius):
        return math.pi * (radius ** 2)

    # Method to calculate the area of a trapezium
    def trapezium_area(self, base1, base2, height):
        return 0.5 * (base1 + base2) * height

    # Method to calculate the area of an ellipse
    def ellipse_area(self, major_axis, minor_axis):
        return math.pi * major_axis * minor_axis

    # Method to calculate the area of a rhombus
    def rhombus_area(self, diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

# Function to get user input for selecting the shape
def get_user_input():
    while True:
        menu = input("Choose a shape:\n1. Circle\n2. Trapezium\n3. Ellipse\n4. Rhombus\n0. Exit\nEnter the corresponding number: ")
        if menu.isdigit() and 0 <= int(menu) <= 4:
            return menu
        else:
            print("Please choose a valid option (0 to 4).")  

# Main function 
def main():
    # Instance of the AreaCalculator class
    calculator = AreaCalculator()
    
    # Getting user input to select shape
    menu = get_user_input()

    if menu == "1":
        # Calculating the area of a circle 
        radius = float(input("Enter the radius of the circle: "))
        result = calculator.circle_area(radius)
        print(f"The area of the circle is: {result}")
    elif menu == "2":
        # Calculating the area of a trapezium 
        base1 = float(input("Enter the length of the first base: "))
        base2 = float(input("Enter the length of the second base: "))
        height = float(input("Enter the height of the trapezium: "))
        result = calculator.trapezium_area(base1, base2, height)
        print(f"The area of the trapezium is: {result}")
    elif menu == "3":
        # Calculating the area of an ellipse
        major_axis = float(input("Enter the length of the major axis of the ellipse: "))
        minor_axis = float(input("Enter the length of the minor axis of the ellipse: "))
        result = calculator.ellipse_area(major_axis, minor_axis)
        print(f"The area of the ellipse is: {result}")
    elif menu == "4":
        # Calculating the area of a rhombus
        diagonal1 = float(input("Enter the length of the first diagonal of the rhombus: "))
        diagonal2 = float(input("Enter the length of the second diagonal of the rhombus: "))
        result = calculator.rhombus_area(diagonal1, diagonal2)
        print(f"The area of the rhombus is: {result}")
    elif menu == "0":
        print("Exiting the program.")
        return
    else:
        # Handling an invalid choice
        result = "Invalid choice"

# Entry point 
if __name__ == "__main__":
    main()

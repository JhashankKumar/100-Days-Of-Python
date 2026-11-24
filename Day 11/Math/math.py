"""
In-Built Math Functions in Python:
1. abs() - Returns the absolute value of a number.
2. pow() - Returns the value of x raised to the power of y.
3. round() - Rounds a number to the nearest integer or to a specified number of decimal places.
4. min() - Returns the smallest value among the given arguments.
5. max() - Returns the largest value among the given arguments.
6. sum() - Returns the sum of all the elements in an iterable.
7. len() - Returns the number of items in an object.
8. ceil() - Returns the smallest integer greater than or equal to a given number.
9. floor() - Returns the largest integer less than or equal to a given number.
10. sqrt() - Returns the square root of a number.
11. pi - Returns the value of pi (3.14159...).
"""

# Example usage of some of the in-built math functions:
import math

# Absolute value
print(abs(-5))  # Output: 5

# Power
print(pow(2, 3))  # Output: 8

# Round
print(round(3.14159, 2))  # Output: 3.14

# Minimum and Maximum
print(min(1, 2, 3, 4, 5))  # Output: 1
print(max(1, 2, 3, 4, 5))  # Output: 5

# Sum
print(sum([1, 2, 3, 4, 5]))  # Output: 15

height = [5, 10, 15, 20]

average_height = sum(height) / len(height)
print(average_height)  # Output: 12.5

# Ceiling and Floor
print(math.ceil(4.2))  # Output: 5
print(math.floor(4.8))  # Output: 4

# Square Root
print(math.sqrt(16))  # Output: 4.0 

# Value of Pi
print(math.pi)  # Output: 3.141592653589793
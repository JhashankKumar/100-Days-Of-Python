"""
Logical operators are used to combine conditional statements. 
In Python, there are three logical operators: `and`, `or`, and `not`. 
"""
# Example usage of logical operators

# Using the `and` operator to check if both conditions are true
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive numbers.")  # Output: Both x and y are positive numbers.

# Using the `or` operator to check if at least one condition is true
if x > 0 or y < 0:
    print("At least one of x or y is a positive number.")  # Output: At least one of x or y is a positive number.

# Using the `not` operator to negate a condition
if not x < 0:
    print("x is not a negative number.")  # Output: x is not a negative number.

# Combining logical operators
if (x > 0 and y > 0) or (x < 0 and y < 0):
    print("x and y are both positive or both negative.")  # Output: x and y are both positive or both negative.

# Logical operators can also be used with non-boolean values.
# In Python, the following values are considered "falsy": False, None, 0, 0.0, 0j, empty sequences (e.g., '', [], ()), and empty mappings (e.g., {}).
# All other values are considered "truthy".
a = [] # An empty list is falsy
b = [1, 2, 3] # A non-empty list is truthy
if a and b:
    print("Both a and b are truthy.")
else:
    print("At least one of a or b is falsy.")  # Output: At least one of a or b is falsy.


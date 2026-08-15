"""
Identity operator. Returns the input as is.
Identity operators are used to compare the memory locations of two objects.
In Python, there are two identity operators: `is` and `is not`.
- `is` : Returns True if both operands refer to the same object in memory, otherwise returns False.
- `is not` : Returns True if both operands do not refer to the same object in memory, otherwise returns False.
"""

# Example usage of identity operators
a = [1, 2, 3]
b = a  # b refers to the same list object as a
c = [1, 2, 3]  # c refers to a different list object with the same content 

# Using the `is` operator to check if a and b refer to the same object
print(a is b)  # Output: True
# Using the `is` operator to check if a and c refer to the same object
print(a is c)  # Output: False

# Using the `is not` operator to check if a and c do not refer to the same object
print("Is not:", a is not c)  # Output: True
# Using the `is not` operator to check if a and b do not refer to the same object
print("Is not:", a is not b)  # Output: False

# Note: The `is` operator checks for identity (whether two variables point to the same object), while the `==` operator checks for equality (whether the values of the objects are the same).
print("Equal:", a == c)  # Output: True (because the contents of a and c are the same)
print("Equal:", a == b)  # Output: True (because the contents of a and b are the same)

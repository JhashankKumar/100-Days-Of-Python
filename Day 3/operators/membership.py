# Membership operators: in, not in
"""
Membership operators are used to test if a sequence (such as a string, list, tuple, set, or dictionary) contains a certain value.   
In Python, there are two membership operators: `in` and `not in`.
- `in` : Returns True if the specified value is found in the sequence, otherwise returns False.
- `not in` : Returns True if the specified value is not found in the sequence, otherwise returns False.
"""

# Example usage of membership operators

# Using the `in` operator to check if a value is in a list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

# Using the `not in` operator to check if a value is not in a list
print(3 not in my_list)  # Output: False
print(6 not in my_list)  # Output: True 

# Using the `in` operator to check if a character is in a string
my_string = "Hello, World!"
print('H' in my_string)  # Output: True
print('h' in my_string)  # Output: False (because 'H' is uppercase and 'h' is lowercase)

# Using the `not in` operator to check if a character is not in a string
print('H' not in my_string)  # Output: False
print('h' not in my_string)  # Output: True

# Using the `in` operator to check if a key is in a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print('name' in my_dict)  # Output: True
print('country' in my_dict)  # Output: False  

# Using the `not in` operator to check if a key is not in a dictionary
print('name' not in my_dict)  # Output: False
print('country' not in my_dict)  # Output: True

# Note: The `in` and `not in` operators can also be used with sets and tuples, and they work similarly to how they work with lists and strings.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False 

my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False

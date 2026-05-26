"""
Comparison operators are used to compare two values. 
They return a boolean value (True or False) based on the comparison. 
Here are some common comparison operators in Python:
== : Equal to
!= : Not equal to
<  : Less than
>  : Greater than
<= : Less than or equal to
>= : Greater than or equal to  
"""
# Example usage of comparison operators

# Equal to
print(10 == 10)  # Output: True
print(10 == 5)   # Output: False

# Not equal to
print(10 != 5)   # Output: True
print(10 != 10)  # Output: False

# Less than
print(5 < 10)    # Output: True
print(10 < 5)    # Output: False

# Greater than
print(10 > 5)    # Output: True
print(5 > 10)    # Output: False

# Less than or equal to
print(5 <= 10)   # Output: True
print(10 <= 10)  # Output: True
print(10 <= 5)   # Output: False

# Greater than or equal to
print(10 >= 5)   # Output: True
print(10 >= 10)  # Output: True
print(5 >= 10)   # Output: False

# Note: Comparison operators can also be used to compare strings, lists, and other data types.
# For example, when comparing strings, Python compares them lexicographically (based on the Unicode code points of the characters).
print("apple" < "banana")  # Output: True
print("apple" > "banana")  # Output: False
print("apple" == "apple") # Output: True
print("apple" != "banana") # Output: True

# When comparing lists, Python compares them element by element.
print([1, 2, 3] < [1, 2, 4])  # Output: True
print([1, 2, 3] > [1, 2, 4])  # Output: False
print([1, 2, 3] == [1, 2, 3]) # Output: True
print([1, 2, 3] != [1, 2, 4]) # Output: True   

# Comparison operators can also be chained together to compare multiple values at once.
print(5 < 10 < 15)  # Output: True
print(5 < 10 > 15)  # Output: False
print(5 < 10 <= 10) # Output: True
print(5 < 10 >= 10) # Output: True



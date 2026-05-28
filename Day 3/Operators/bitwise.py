# Bitwise operators: &, |, ^, ~, <<, >>
"""
Bitwise operators are used to perform bit-level operations on integers.
In Python, there are six bitwise operators:
- `&` : Bitwise AND
- `|` : Bitwise OR
- `^` : Bitwise XOR
- `~` : Bitwise NOT
- `<<` : Left shift
- `>>` : Right shift
"""

# Example usage of bitwise operators

# Using the `&` operator (Bitwise AND)
a = 5  # Binary: 101
b = 3  # Binary: 011
print(a & b)  # Output: 1 (Binary: 001)
print(a) # Output: 5 (Binary: 101)

# Using the `|` operator (Bitwise OR)
print(a | b)  # Output: 7 (Binary: 111)

# Using the `^` operator (Bitwise XOR)
print(a ^ b)  # Output: 6 (Binary: 110)

# Using the `~` operator (Bitwise NOT)
print(~a)  # Output: -6 (Binary: ...11010)

# Using the `<<` operator (Left shift)
print(a << 1)  # Output: 10 (Binary: 1010)

# Using the `>>` operator (Right shift)
print(a >> 1)  # Output: 2 (Binary: 010)

# Note: Bitwise operators can also be used with negative numbers, and they work based on the two's complement representation of integers in Python. 
# For example, the bitwise NOT of a negative number will yield a positive number, and vice versa.
negative_num = -5  # Binary: ...11111011 (two's complement)
print(~negative_num)  # Output: 4 (Binary: 100) 

"""
Bitwise operators are often used in low-level programming, 
such as when working with hardware or performing bit manipulation tasks. 
They can also be used for tasks like setting, clearing, or toggling specific bits in a number, 
as well as for efficient calculations and data compression techniques.   
Understanding how bitwise operators work can be helpful for optimizing code and performing certain 
operations more efficiently.

Bitwise operators don't work with floating-point numbers or other non-integer types. 
If you try to use bitwise operators with non-integer types, you'll get a TypeError. 
For example:
```python
a = 5.5
b = 3.2
print(a & b)  # This will raise a TypeError
```
"""

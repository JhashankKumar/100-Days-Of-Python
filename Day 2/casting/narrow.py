# Narrow Casting
"""Narrowing is when we convert a larger data type to a smaller data type. 
This can lead to data loss if the value being converted is too large to fit in the smaller data type. 
In Python, we can perform narrow casting using built-in functions, 
but we should be cautious when doing so to avoid unintended consequences.""" 

# Example of Narrow Casting
# Converting a float to an integer (Narrowing)
x = 5.7
y = int(x)  # This will truncate the decimal part and convert to an integer
print("x:", x)  # Output: x: 5.7
print("y:", y)  # Output: y: 5

# Converting a complex number to an integer (Narrowing)
z = 2 + 3j
try:
    w = int(z)  # This will raise a TypeError because complex numbers cannot be directly converted to integers
except TypeError as e:
    print("Error:", e)  # Output: Error: can't convert complex to int

# Converting a large integer to a smaller data type (Narrowing)
large_int = 12345678901234567890
try:    
    small_int = int(large_int)  # This will work in Python because it can handle large integers, but in other languages, this might cause overflow
    print("small_int:", small_int)  # Output: small_int: 12345678901234567890
except OverflowError as e:
    print("Error:", e)  # Output: Error: integer overflow

# Converting a string to an integer (Narrowing)
s = "123"
try:    
    num = int(s)  # This will convert the string to an integer
    print("num:", num)  # Output: num: 123
except ValueError as e:
    print("Error:", e)  # Output: Error: invalid literal for int() with base 10: 'abc' (if the string is not a valid number)

""" When performing narrow casting, it's essential to be aware of the potential for data loss and errors.
Always ensure that the value being converted can fit within the target data type to avoid unexpected results. 
In Python, while it can handle large integers, other languages may not, so it's crucial to understand the 
limitations of the data types you are working with. Additionally, when converting between 
incompatible types (like complex to int), it's important to handle exceptions properly to maintain 
the stability of your program."""    


s = "abc"
try:    
    num = int(s)  # This will raise a ValueError because 'abc' cannot be converted to an integer
    print("num:", num)  # This line will not be executed
except ValueError as e:
    print("Error:", e)  # Output: Error: invalid literal for int() with base 10: 'abc'


# Converting a large float to an integer (Narrowing)
large_float = 1e20
try: 
    small_int = int(large_float)  # This will convert the large float to an integer, but it may lose precision
    print("small_int:", small_int)  # Output: small_int: 100000000000000000000
except OverflowError as e:
    print("Error:", e)  # Output: Error: integer overflow (if the float is too large to convert to an integer)
# Type Conversion in Python
""" Type conversion is the process of converting one data type to another data type. In Python, we can convert between different data types using built-in functions."""

# Converting to Integer
x = 5.7
y = int(x)
print("x:", x)  # Output: x: 5.7
print("y:", y)  # Output: y: 5

# Converting to Float
x = 5
y = float(x)
print("x:", x)  # Output: x: 5
print("y:", y)  # Output: y: 5.0

# Converting to String
x = 5
y = str(x)
print("x:", x)  # Output: x: 5
print("y:", y)  # Output: y: '5'

# Converting to Complex
x = 5
y = complex(x)
print("x:", x)  # Output: x: 5
print("y:", y)  # Output: y: (5+0j)

# Converting to Boolean
x = 5
y = bool(x)
print("x:", x)  # Output: x: 5
print("y:", y)  # Output: y: True

x = 0
y = bool(x)
print("x:", x)  # Output: x: 0
print("y:", y)  # Output: y: False

# Convert Float to Integer (Truncation)
x = 5.9
y = int(x)
print("x:", x)  # Output: x: 5.9
print("y:", y)  # Output: y: 5

# Convert String to Integer
x = "10"
y = int(x)
print("x:", x)  # Output: x: '10'
print("y:", y)  # Output: y: 10

# Convert String to Float
x = "3.14"
y = float(x)
print("x:", x)  # Output: x: '3.14'

# Convert int to Complex
x = 5
y = complex(x)
print("x:", x)  # Output: x: 5
print("y:", y)  # Output: y: (5+0j)

""" Type conversion is essential when we need to perform operations that require specific data types. 
For example, if we want to perform arithmetic operations on numbers represented as strings, 
we need to convert them to integers or floats first. 
Similarly, when we want to display numbers as strings, we can convert them using the str() function.
It's important to note that when converting from a float to an integer, the decimal part is truncated, 
not rounded. Also, when converting a non-numeric string to an integer or float, it will raise a ValueError. 
Therefore, it's crucial to ensure that the string contains a valid number before conversion. 
Overall, type conversion allows us to work with different data types and perform various operations 
seamlessly in Python."""
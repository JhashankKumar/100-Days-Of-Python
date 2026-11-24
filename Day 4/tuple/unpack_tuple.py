# unpacking a tuple
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# unpacking a tuple with different data types
my_tuple = (1, 'hello', 3.14)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 'hello'
print(c)  # Output: 3.14    

# unpacking a tuple with more elements than variables (will raise a ValueError)
my_tuple = (1, 2, 3, 4)
a, b, c = my_tuple  
# This will raise a ValueError because there are more elements in the tuple than variables to unpack into

# unpacking a tuple with fewer elements than variables (will raise a ValueError)
my_tuple = (1, 2)
a, b, c = my_tuple  
# This will raise a ValueError because there are fewer elements in the tuple than variables to unpack into

# unpacking a tuple with the * operator (for variable-length unpacking)
my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

my_tuple = (1, 2, 3, 4, 5)
*a, b, c = my_tuple
print(a)  # Output: [1, 2, 3]
print(b)  # Output: 4
print(c)  # Output: 5

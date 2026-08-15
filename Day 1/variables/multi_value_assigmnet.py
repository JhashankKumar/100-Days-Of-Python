# multi value assignment
a, b, c = 1, 2, 3
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# swapping values
x = 5
y = 10
print("Before swapping: x =", x, "y =", y)  # Output: Before swapping: x = 5 y = 10
x, y = y, x
print("After swapping: x =", x, "y =", y)  # Output: After swapping: x = 10 y = 5

# only one value assignment
a = b = c = 0
print(a)  # Output: 0
print(b)  # Output: 0
print(c)  # Output: 0   

# unpacking a list
my_list = [1, 2, 3]
x, y, z = my_list
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

# unpacking a tuple
my_tuple = (4, 5, 6)
a, b, c = my_tuple
print(a)  # Output: 4
print(b)  # Output: 5
print(c)  # Output: 6
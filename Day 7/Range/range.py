"""range in python is a built-in function that generates a sequence of numbers. 
It is commonly used in for loops to iterate over a specific range of values. 
The range function can take one, two, or three arguments: 

1. range(stop): Generates numbers from 0 to stop-1.
2. range(start, stop): Generates numbers from start to stop-1.
3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

The built-in range() function returns an immutable sequence of numbers, 
commonly used for looping a specific number of times.

This set of numbers has its own data type called range.
Note: Immutable means that it cannot be modified after it is created.
"""
# Example usage of range in a for loop
# Using range with one argument
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# Using range with two arguments
for i in range(2, 6):
    print(i)  # Output: 2 3 4 5

# Using range with three arguments
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9


r = range(5)
print(r)  # Output: range(0, 5)

r = r[3] # this will return the value at index 3 of the range object, which is 3
print(r)  # Output: 3

t = range(1, 10, 2)
print(t)  # Output: range(1, 10, 2)
print(t[2])  # Output: 5

# membership test
print(3 in range(5))  # Output: True
print(5 in range(5))  # Output: False

r = range(10)
print(r)  # Output: range(0, 10)
# slicing a range object
sliced_r = r[2:8:2]
print(sliced_r)  # Output: range(2, 8, 2)
print(3 in sliced_r)  # Output: False
print(list(sliced_r))  # Output: [2, 4, 6]

# length of a range object
print(len(r))  # Output: 10
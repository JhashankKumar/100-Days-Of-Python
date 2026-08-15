# Sets 

"""
Sets are a collection of unique elements. 
They are unordered, meaning that the elements do not have a specific order. 
Sets are mutable, which means that you can add or remove elements from a set after it has been created.
Sets are defined using curly braces {} or the set() constructor.
"""

# Creating a set
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}  

# Creating a set with duplicate elements (duplicates will be removed)
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # Output: {1, 2, 3}  

# Creating a set using the set() constructor
my_set = set([1, 2, 3])
print(my_set)  # Output: {1, 2, 3}  

# unordered nature of sets
my_set = {3, 1, 2}
print(my_set)  # Output: {1, 2, 3} (the order may vary)

# unchangeable nature of sets
my_set = {1, 2, 3}
# my_set[0] = 4  # This will raise a TypeError because sets do not support indexing

# duplicate elements in sets
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # Output: {1, 2, 3}  

# true and 1 
my_set = {True, 1, 2}
print(my_set)  # Output: {1, 2} (True is considered equal to 1 in a set)

my_set = {False, 0, 2}
print(my_set)  # Output: {0, 2} (False is considered equal to 0 in a set)

# sets with different data types
my_set = {1, 'hello', 3.14}
print(my_set)  # Output: {1, 'hello', 3.14}

# length of a set
my_set = {1, 2, 3}
print(len(my_set))  # Output: 3

# checking if an element is in a set
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True
print(4 in my_set)  # Output: False

# types of sets
my_set = {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>    

# set constructor
my_set = set([1, 2, 3])
print(my_set)  # Output: {1, 2, 3}

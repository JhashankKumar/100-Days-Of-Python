"""
Tuples are immutable sequences, typically used to store collections of heterogeneous data. 
They are defined by enclosing the elements in parentheses `()`, 
and the elements can be of any data type. Once a tuple is created, its contents cannot be changed, 
which makes it a useful data structure for representing fixed collections of items.   
"""

# creating a tuple
my_tuple = (1, 'hello', 3.14)
print(my_tuple) 

# accessing elements in a tuple
my_tuple = (1, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'hello'
print(my_tuple[2])  # Output: 3.14

# unpacking a tuple
my_tuple = (1, 'hello', 3.14)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 'hello'
print(c)  # Output: 3.14    

"""
Tuples support various operations such as concatenation, repetition, and slicing.
They also have built-in methods like `count()` and `index()`, 
which can be used to count the occurrences of an element and find the index of an element, respectively. 
Since tuples are immutable, they do not have methods that modify the tuple, such as `append()` or `remove()`, 
which are available for lists.    
"""

# Tuple Items

# Indexing
my_tuple = (1, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'hello'
print(my_tuple[2])  # Output: 3.14

# Negative Indexing
my_tuple = (1, 'hello', 3.14)   
print(my_tuple[-1])  # Output: 3.14
print(my_tuple[-2])  # Output: 'hello'
print(my_tuple[-3])  # Output: 1

# Odered
my_tuple = (1, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'hello'
print(my_tuple[2])  # Output: 3.14

# Allow Duplicates
my_tuple = (1, 'hello', 3.14, 1, 'hello')
print(my_tuple)  # Output: (1, 'hello', 3.14, 1, 'hello')

# unchangeable
my_tuple = (1, 'hello', 3.14)
# my_tuple[0] = 2  # This will raise a TypeError because tuples are immutable

# Length of a tuple
my_tuple = (1, 'hello', 3.14)
print(len(my_tuple))  # Output: 3

# creating a tuple with one element
my_tuple = (1,)
print(my_tuple)  # Output: (1,) 

my_tuple = (1)
print(my_tuple)  # Output: 1 (not a tuple, just an integer)

# creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# data types in a tuple
my_tuple = (1, 'hello', 3.14, [1, 2, 3], (4, 5, 6), {'key': 'value'})
print(my_tuple)  # Output: (1, 'hello', 3.14, [1, 2, 3], (4, 5, 6), {'key': 'value'})   

"""
Tuples can contain elements of different data types, including integers, strings, floats, lists, other tuples, 
and dictionaries. This flexibility allows tuples to be used for a wide variety of applications, 
such as storing related data together, returning multiple values from a function, and as keys in dictionaries 
(since they are immutable). 
"""

# type of a tuple
my_tuple = (1, 'hello', 3.14)
print(type(my_tuple))  # Output: <class 'tuple'>

# constructing a tuple using the tuple() constructor
my_tuple = tuple([1, 'hello', 3.14])
print(my_tuple)  # Output: (1, 'hello', 3.14)

# nested tuples
nested_tuple = (1, 'hello', (2, 3), [4, 5], {'key': 'value'})
print(nested_tuple)  # Output: (1, 'hello', (2, 3), [4, 5], {'key': 'value'})
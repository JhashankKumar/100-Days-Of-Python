# can 4 built-in data types in Python be accumulated in a list?
my_list = [1, 3.14, "Hello", True]
print(my_list)  # Output: [1, 3.14, 'Hello', True]

# can 4 built-in data types in Python be accumulated in a tuple?
my_tuple = (1, 3.14, "Hello", True)
print(my_tuple)  # Output: (1, 3.14, 'Hello', True)

# can 4 built-in data types in Python be accumulated in a set?
my_set = {1, 3.14, "Hello", True}
print(my_set)  # Output: {1, 3.14, 'Hello', True} (the order may vary)  

# can 4 built-in data types in Python be accumulated in a dictionary?
my_dict = {"integer": 1,
    "float": 3.14,
    "string": "Hello",
    "boolean": True
}
print(my_dict)  # Output: {'integer': 1, 'float': 3.14, 'string': 'Hello', 'boolean': True}

# can list accumulate tuple, set and dictionary?
"""
Yes, a list can accumulate a tuple, set and dictionary as its elements. Here is an example: 
"""
my_list = [(1, 2), {3, 4}, {"key": "value"}]
print(my_list)  # Output: [(1, 2), {3, 4}, {'key': 'value'}]

# can tuple accumulate list, set and dictionary?
"""
Yes, a tuple can accumulate a list, set and dictionary as its elements. Here is an example: 
"""
my_tuple = ([1, 2], {3, 4}, {"key": "value"})
print(my_tuple)  # Output: ([1, 2], {3, 4}, {'key': 'value'})

# can set accumulate list, tuple and dictionary?
"""
No, a set cannot accumulate a list, tuple and dictionary as its elements because sets 
can only contain immutable (hashable) types. 
Lists and dictionaries are mutable and therefore cannot be added to a set. 
However, tuples can be added to a set since they are immutable. Here is an example: 
"""
my_set = {(1, 2), (3, 4)}  # This is valid
print(my_set)  # Output: {(1, 2), (3, 4)} 

my_set = {[1, 2], (3, 4), {"key": "value"}}  # This will raise a TypeError because lists and dictionaries are unhashable
print(my_set)  # This line will not be executed due to the error above


# can dictionary accumulate list, tuple and set?
"""
Yes, a dictionary can accumulate a list, tuple and set as its values. 
However, the keys of a dictionary must be immutable (hashable) types. Here is an example: 
"""
my_dict = {"list": [1, 2],
    "tuple": (3, 4),
    "set": {5, 6}
}
print(my_dict)  # Output: {'list': [1, 2], 'tuple': (3, 4), 'set': {5, 6}}  
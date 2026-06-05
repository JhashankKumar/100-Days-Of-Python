# accessing Tuple elements
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

# negative indexing
my_tuple = (1, 'hello', 3.14)
print(my_tuple[-1])  # Output: 3.14
print(my_tuple[-2])  # Output: 'hello'
print(my_tuple[-3])  # Output: 1

# range of indexes
my_tuple = (1, 'hello', 3.14, 'world', 42)
print(my_tuple[1:4])  # Output: ('hello', 3.14, 'world')
print(my_tuple[:3])   # Output: (1, 'hello', 3.14)
print(my_tuple[2:])   # Output: (3.14, 'world', 42)

"""
The Range of Indexes: You can specify a range of indexes to access a subset of the tuple. 
This is done using the slicing syntax `tuple[start:end]`, where `start` is the index of the first element 
you want to include, and `end` is the index of the first element you want to exclude. For example, 
`my_tuple[1:4]` will return a new tuple containing the elements at indexes 1, 2, and 3.
You can also omit the `start` or `end` index to include all elements from the beginning or to the end of 
the tuple, respectively. For instance, `my_tuple[:3]` will return the first three elements of the tuple, 
and `my_tuple[2:]` will return all elements from index 2 to the end of the tuple.  
"""

# Tuples are ordered, which means that the items have a defined order, and that order will not change.

#negative range of indexes
my_tuple = (1, 'hello', 3.14, 'world', 42)
print(my_tuple[-4:-1])  # Output: ('hello', 3.14, 'world')
print(my_tuple[:-2])    # Output: (1, 'hello', 3.14)
print(my_tuple[-3:])    # Output: (3.14, 'world', 42)   


# find the index of an element
my_tuple = (1, 'hello', 3.14, 'world', 42)
print(my_tuple.index('hello'))  # Output: 1 

"""
The `index()` method is used to find the index of the first occurrence of a specified element in the tuple. 
If the element is not found in the tuple, it will raise a `ValueError`. For example, `my_tuple.index('hello')` 
will return `1` because 'hello' is located at index 1 in the tuple. 
If you try to find the index of an element that does not exist in the tuple, 
such as `my_tuple.index('not_in_tuple')`, it will raise a `ValueError` indicating that the element is not found.
"""

# count the occurrences of an element
my_tuple = (1, 'hello', 3.14, 'world', 42, 'hello')
print(my_tuple.count('hello'))  # Output: 2 

# check it if an element exists in the tuple
my_tuple = (1, 'hello', 3.14, 'world', 42)
print('hello' in my_tuple)  # Output: True
print('not_in_tuple' in my_tuple)  # Output: False 
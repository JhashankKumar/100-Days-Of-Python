"""
Lists are used to store multiple items in a single variable. 
Lists are created using square brackets [] and can contain items of different data types, 
including other lists. They are ordered, changeable, and allow duplicate values. 
Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
"""

# Creating a list
my_list = [1, 2, 3, 'Hello', [4, 5]]
print(my_list)  # Output: [1, 2, 3, 'Hello', [4, 5]]

# Accessing list items
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'Hello'
print(my_list[4])  # Output: [4, 5]

"""
Lists are mutable, which means you can change their content without changing their identity.
You can add, remove, or modify items in a list after it has been created.

Indexing in lists starts at 0, so the first item is at index 0, the second item is at index 1, and so on.
You can also use negative indexing to access items from the end of the list, where -1 refers to the last item,
-2 to the second last item, and so on.       
"""

# odered list
ordered_list = ['apple', 'banana', 'cherry']
print(ordered_list)  # Output: ['apple', 'banana', 'cherry'] 

# changeable list
changeable_list = [1, 2, 3]
changeable_list[0] = 10
print(changeable_list)  # Output: [10, 2, 3]  

# duplicate values in list
duplicate_list = [1, 2, 2, 3, 4, 4, 4]
print(duplicate_list)  # Output: [1, 2, 2, 3, 4, 4, 4]

# List can contain different data types
mixed_list = [1, 'Hello', 3.14, True]
print(mixed_list)  # Output: [1, 'Hello', 3.14, True]

# length of a list
print(len(my_list))  # Output: 5

# type of a list
print(type(my_list))  # Output: <class 'list'>

# list construction using list() function
constructed_list = list((1, 2, 3, 'Hello'))
print(constructed_list)  # Output: [1, 2, 3, 'Hello']   

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# adding new items to the list
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]

# using append() method to add an item to the end of the list
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# using insert() method to add an item at a specific index
my_list.insert(1, 10)
print(my_list)  # Output: [1, 10, 2, 3, 4]

# using extend() method to add multiple items to the end of the list
my_list2 = [5, 6, 7]
my_list.extend(my_list2)
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7]

# using + operator to concatenate two lists
new_list = my_list + [8, 9]
print(new_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]  

"""
append() method adds a single item to the end of the list, 
while extend() method adds multiple items to the end of the list.
insert() method allows you to add an item at a specific index,
while + operator creates a new list by concatenating two lists.
"""

# add any iterable (like a tuple, set, or dictionary) to the list using extend() method
my_list.extend((11, 12))
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12]

my_list.extend({13, 14})
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14]

my_list.extend({'a': 15, 'b': 16})
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 'a', 'b'] 

my_list.extend([17, 18, 19])
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 'a', 'b', 17, 18, 19]  

"""
why only keys of the dictionary are added to the list when we use extend() method?
Because the extend() method iterates over the dictionary and adds each key to the list.
If we want to add the values of the dictionary to the list, we can use the values() method 
of the dictionary to get the values and then extend the list with those values.
"""
my_list.extend({'a': 15, 'b': 16}.values())
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 'a', 'b', 17, 18, 19, 15, 16]

# if we want to add both keys and values of the dictionary to the list, we can use the items() method
my_list.extend({'a': 15, 'b': 16}.items())
print(my_list)  # Output: [1, 10, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 'a', 'b', 17, 18, 19, 15, 16, ('a', 15), ('b', 16)] 

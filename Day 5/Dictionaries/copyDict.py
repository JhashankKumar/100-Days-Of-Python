"""
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2
"""

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "email": "john@yopmail.com",
    "phone": "123-456-7890"
}

my_dict_copy = my_dict.copy()
print(my_dict_copy)

my_dict_copy2 = dict(my_dict)
print(my_dict_copy2)

""" 
is  my_dict_copy and my_dict_copy2 the same?

"""

print(my_dict_copy == my_dict_copy2)  # True
print(my_dict_copy is my_dict_copy2)  # False

print(my_dict_copy2 == my_dict)  # True
print(my_dict_copy2 is my_dict)  # False

print(my_dict_copy == my_dict_copy2)
print(my_dict_copy is my_dict_copy2)


"""
what is the difference between copy() and dict() methods?
The copy() method creates a shallow copy of the dictionary, 
meaning that it copies the dictionary structure and its keys and values, 
but if the values are mutable objects (like lists or other dictionaries), 
changes made to those mutable objects in the original dictionary will also be reflected in the copied dictionary.
The dict() method creates a new dictionary from an existing dictionary or iterable of key-value pairs.  
"""
# dictionaries are a collection of key-value pairs
# they are unordered, mutable, and indexed by keys
# they are defined using curly braces {}
# keys must be unique and immutable (e.g., strings, numbers, tuples)
# values can be of any data type and can be duplicated
# dictionaries are useful for storing and retrieving data based on keys
# creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}  

"""
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""

# accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30

# adding a new key-value pair to the dictionary
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

"""
Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""

"""
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.
"""

"""
Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
"""

"""
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
"""

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "name": "Bob"  # This will overwrite the previous "name" key
}
print(my_dict)  # Output: {'name': 'Bob', 'age': 30, 'city': 'New York'}    

# length of a dictionary
print(len(my_dict))  # Output: 3 (because there are 3 key-value pairs in the dictionary)

# creating a dictionary using the dict() constructor
my_dict2 = dict(name="Charlie", age=25, city="Los Angeles")
print(my_dict2)  # Output: {'name': 'Charlie', 'age': 25, 'city': 'Los Angeles'}

# data types of dictionary values
"""
dictionary values can be of any data type, including:
- strings
- numbers
- lists
- tuples
- sets
- other dictionaries
"""
my_dict3 = {
    "name": "David",
    "age": 40,
    "is_student": False,
    "hobbies": ["reading", "traveling"],
    "address": {"street": "123 Main St", "city": "Chicago"}
}
print(my_dict3)
# Output: {'name': 'David', 'age': 40, 'is_student': False, 'hobbies': ['reading', 'traveling'], 'address': {'street': '123 Main St', 'city': 'Chicago'}}   

# from python 3.7, dictionaries are ordered, meaning that the items have a defined order, and that order will not change.
my_dict4 = {
    "name": "Eve",
    "age": 35,
    "city": "Miami"
}
print(my_dict4)  # Output: {'name': 'Eve', 'age': 35, 'city': 'Miami'} (the order of the items is the same as they were added)  
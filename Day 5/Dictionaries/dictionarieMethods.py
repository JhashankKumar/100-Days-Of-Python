"""
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	      Description
clear()	      Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys()	  Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
"""

# clear() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("Original dictionary:", my_dict)
my_dict.clear()
print("Dictionary after clear():", my_dict)  # Output: {}

# copy() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict_copy = my_dict.copy()
print("Original dictionary:", my_dict)
print("Copied dictionary:", my_dict_copy)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# fromkeys() method
keys = ["name", "age", "city"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("New dictionary from keys:", new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}    

# get() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.get("age")
print("Age:", age)  # Output: 30
country = my_dict.get("country", "Not Found")
print("Country:", country)  # Output: Not Found

# items() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
dict_items = my_dict.items()
print("Items:", dict_items)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')]) 

# keys() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
keys = my_dict.keys()
print("Keys:", keys)  # Output: dict_keys(['name', 'age', 'city'])

# pop() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.pop("age")
print("Popped age:", age)  # Output: 30
print("Dictionary after pop():", my_dict)  # Output: {'name': 'John', 'city': 'New York'}

# popitem() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
last_item = my_dict.popitem()
print("Popped item:", last_item)  # Output: ('city', 'New York')
print("Dictionary after popitem():", my_dict)  # Output: {'name': 'John', 'age': 30}

# setdefault() method
my_dict = {"name": "John", "age": 30}
city = my_dict.setdefault("city", "New York")
print("City:", city)  # Output: New York
print("Dictionary after setdefault():", my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# update() method
my_dict = {"name": "John", "age": 30}
my_dict.update({"city": "New York", "age": 31})
print("Dictionary after update():", my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# values() method
my_dict = {"name": "John", "age": 30, "city": "New York"}
values = my_dict.values()
print("Values:", values)  # Output: dict_values(['John', 30, 'New York'])
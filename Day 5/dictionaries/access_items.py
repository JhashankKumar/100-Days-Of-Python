# Accessing Items in a Dictionary
"""
A dictionary in Python is a collection of key-value pairs. 
You can access the values in a dictionary by using their corresponding keys. 
Here are some examples of how to access items in a dictionary:  
"""
# Example 1: Accessing a value using a key
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: Alice 

# Example 2: Using the get() method to access a value
print(my_dict.get('age'))  # Output: 25

# Example 3: Accessing a value with a key that doesn't exist
print(my_dict.get('country', 'Not Found'))  # Output: Not Found

# Example 4: Accessing all keys and values in a dictionary
for key in my_dict:
    print(f"{key}: {my_dict[key]}") 

# get value of a key that doesn't exist without raising an error
print(my_dict.get('country'))  # Output: None

# values() method to access all values in a dictionary
print(my_dict.values())  # Output: dict_values(['Alice', 25, 'New York'])

# keys() method to access all keys in a dictionary
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# items() method to access all key-value pairs in a dictionary as tuples
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# check if a key exists in the dictionary
if 'name' in my_dict:
    print("Key 'name' exists in the dictionary.")  # Output: Key 'name' exists in the dictionary.
else:    
    print("Key 'name' does not exist in the dictionary.")


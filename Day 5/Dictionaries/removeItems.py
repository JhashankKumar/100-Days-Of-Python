# remove items from a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "email": "john@example.com",
    "phone": "123-456-7890"
}

# remove an item by referring to its key name
del my_dict["phone"]
print(my_dict)

# remove an item by using the pop() method
my_dict.pop("email")
print(my_dict)

# remove the last inserted item by using the popitem() method
my_dict.popitem()
print(my_dict)

# remove all items from the dictionary by using the clear() method
my_dict.clear()
print(my_dict)

# delete the dictionary completely by using the del keyword
del my_dict
print(my_dict)  # This will raise a NameError since my_dict is deleted
"""
del my_dict completely removes the dictionary from memory, 
so trying to access it afterward will result in a NameError since it no longer exists. 

clear() method empties the dictionary but keeps it in memory, allowing you to reuse it later if needed.
"""
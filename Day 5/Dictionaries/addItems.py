# add items to a Dictionary
# we can add items to a dictionary by referring to its key name and assigning a value to it
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# add a new item to the dictionary
my_dict["country"] = "USA"
print(my_dict)  

# we can also add items to a dictionary by using the update() method
my_dict.update({"email": "john@example.com"})
print(my_dict)  

# we can also add items to a dictionary by using the setdefault() method
my_dict.setdefault("phone", "123-456-7890")
print(my_dict)

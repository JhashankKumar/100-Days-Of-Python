# change Items in a Dictionary
# we can change the value of a specific item by referring to its key name
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# change the value of the "age" key
my_dict["age"] = 31
print(my_dict)

# we can also change the value of a specific item by using the update() method
my_dict.update({"city": "Los Angeles"})
print(my_dict)

# we can also change the value of a specific item by using the setdefault() method
my_dict.setdefault("name", "Jane")
print(my_dict)
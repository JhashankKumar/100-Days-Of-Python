# loop through a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "email": "john@yopmail.com",
    "phone": "123-456-7890"
}

# loop through the dictionary keys
for key in my_dict:
    print(key)

# loop through the dictionary values
for value in my_dict.values():
    print(value)

for value in my_dict: 
    print(my_dict[value])  # prints the values of the dictionary

# loop through the dictionary items (key-value pairs)
for key, value in my_dict.items():
    print(key, value)

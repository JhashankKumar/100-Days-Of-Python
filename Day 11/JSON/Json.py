import json

# convert a Python object to a JSON string
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)  # Output: {"name": "John", "age": 30, "city": "New York"}

# convert a JSON string to a Python object
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

"""

# convert a Python object to a JSON string with indentation
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "swimming"]
}

json_string = json.dumps(data)
json_string_indent = json.dumps(data, indent=2)
json_string_sorted = json.dumps(data, indent=4, sort_keys=True)  # sort keys alphabetically
print(json_string)
print(json_string_indent)
print(json_string_sorted)


"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python	     JSON
dict	     Object
list	     Array
tuple	     Array
str	         String
int	         Number
float	     Number
True	     true
False	     false
None	     null
"""

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)
z = json.dumps(x, indent=4, sort_keys=True)

# the result is a JSON string:
print(y)
print(z)
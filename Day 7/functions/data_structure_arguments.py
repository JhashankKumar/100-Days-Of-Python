# passing data structures as arguments

# Example 7: Function that takes a list as an argument
def print_fruits(fruit_list):
    for fruit in fruit_list:
        print(fruit)

# Calling the function with a list argument
fruits = ["apple", "banana", "cherry"]
print_fruits(fruits)


# Example 8: Function that takes a dictionary as an argument
def print_person_info(person_dict):
    for key, value in person_dict.items():
        print(key + ": " + str(value))

# Calling the function with a dictionary argument
person = {"name": "Alice", "age": 25, "city": "New York"}
print_person_info(person)

# Example 9: Function that takes a set as an argument
def print_unique_numbers(number_set):
    for number in number_set:
        print(number)

# Calling the function with a set argument
unique_numbers = {1, 2, 3, 4, 5}
print_unique_numbers(unique_numbers)

# Example 10: Function that takes a tuple as an argument
def print_coordinates(coordinate_tuple):
    print("X:", coordinate_tuple[0])
    print("Y:", coordinate_tuple[1])

# Calling the function with a tuple argument
coordinates = (10, 20)
print_coordinates(coordinates)  


# Example 11: Function that takes a list of dictionaries as an argument
def print_people_info(people_list):
    for person in people_list:
        print("Name:", person["name"])
        print("Age:", person["age"])
        print("City:", person["city"])
        print()  # Print a blank line for better readability

# Calling the function with a list of dictionaries argument
people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
print_people_info(people)

# Example 12: Function that takes a list of tuples as an argument
def print_coordinates_list(coordinates_list):
    for coordinate in coordinates_list:
        print("X:", coordinate[0])
        print("Y:", coordinate[1])
        print()  # Print a blank line for better readability

# Calling the function with a list of tuples argument
coordinates_list = [(10, 20), (30, 40), (50, 60)]
print_coordinates_list(coordinates_list)

"""
what is the difference between a keyword argument and a positional argument in Python functions?
In Python functions, the difference between a keyword argument and a positional argument lies in 
how the arguments are passed to the function:
1. Positional Argument:
   - A positional argument is an argument that is passed to a function based on its position in the function call.
   - The order in which the arguments are provided matters, and they are assigned to the corresponding parameters in 
   the function definition based on their position.
   - Example:
   def greet(fname, lname):
       print("Hello, " + fname + " " + lname + "!")
   greet("Alice", "Smith")  # Here, "Alice" is assigned to fname and "Smith" is assigned to lname based on their positions.
2. Keyword Argument:
   - A keyword argument is an argument that is passed to a function by explicitly specifying the parameter name along with its value.
   - The order of keyword arguments does not matter, as they are assigned to the corresponding parameters based on the parameter names.
   - Example:
   def greet(fname, lname):
       print("Hello, " + fname + " " + lname + "!")
   greet(lname="Smith", fname="Alice")  # Here, "Alice" is assigned to fname and "Smith" is assigned to lname based on the 
   specified parameter names, regardless of their order in the function call.
In summary, positional arguments rely on the order of the arguments, while keyword arguments rely on the parameter names 
to determine which value is assigned to which parameter.       
"""
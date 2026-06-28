"""
Python Functions
A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.

"""

# Example 1: Defining a simple function
def greet():
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!

# calling the function multiple times
greet()  # Output: Hello, World!
greet()  # Output: Hello, World!

# Example 2: Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!

# Example 3: Function with return value
def add_numbers(a, b):
    return a + b 

# Calling the function and storing the result
result = add_numbers(5, 3)
print(result)  # Output: 8

# Example 4: Function with default parameter value
def greet_person_with_default(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without an argument
greet_person_with_default()  # Output: Hello, Guest!
# Calling the function with an argument
greet_person_with_default("Charlie")  # Output: Hello, Charlie!

# Example 5: Function with variable number of arguments
def greet_multiple_people(*names):
    for name in names:
        print(f"Hello, {name}!")

# Calling the function with multiple arguments
greet_multiple_people("Alice", "Bob", "Charlie")

"""
Function Names
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
"""

# Example 6: Function with keyword arguments
def greet_person_with_keyword(name, greeting="Hello"):
    print(f"{greeting}, {name}!")   

# Calling the function with keyword arguments
greet_person_with_keyword(name="Alice", greeting="Hi")  # Output: Hi, Alice!
greet_person_with_keyword(greeting="Good morning", name="Bob")  # Output: Good morning, Bob!
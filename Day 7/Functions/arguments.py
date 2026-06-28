"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called,
we pass along a first name, which is used inside the function to print the full name:
"""

# Example 1: Function with one argument
def greet(fname):
    print("Hello, " + fname + "!")

# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice! 

# Example 2: Function with multiple arguments
def greet_full_name(fname, lname):
    print("Hello, " + fname + " " + lname + "!")

# Calling the function with multiple arguments
greet_full_name("Alice", "Smith")  # Output: Hello, Alice Smith!

# Example 3: Function with default argument values
def greet_with_default(fname, lname="Doe"):
    print("Hello, " + fname + " " + lname + "!")    

# Calling the function with one argument (lname will use the default value)
greet_with_default("Alice")  # Output: Hello, Alice Doe!    

# Calling the function with both arguments
greet_with_default("Alice", "Smith")  # Output: Hello, Alice Smith!


"""
Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.
"""

# Example 4: Function with parameters and arguments
def greet_with_parameters(fname, lname):
    print("Hello, " + fname + " " + lname + "!")    

# Calling the function with arguments
greet_with_parameters("Alice", "Smith")  # Output: Hello, Alice Smith!

"""
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument
"""

# Example 5: Function with variable-length arguments
# You can use *args to pass a variable number of arguments to a function.
def greet_multiple(*names):
    for name in names:
        print("Hello, " + name + "!")  


# Calling the function with multiple arguments
greet_multiple("Alice", "Bob", "Charlie")

# Example 6: Function with keyword arguments
# You can use keyword arguments to pass arguments to a function by explicitly naming them.
def greet_with_keywords(fname, lname):
    print("Hello, " + fname + " " + lname + "!")

# Calling the function with keyword arguments
greet_with_keywords(fname="Alice", lname="Smith")  # Output: Hello, Alice Smith!

# error handling with arguments
# You can use error handling to manage exceptions that may occur when passing arguments to a function.
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")

# Calling the function with valid arguments
divide_numbers(10, 2)  # Output: Result: 5.0
divide_numbers(10, 0)  # Output: Error: Cannot divide by zero.
divide_numbers(10, "a")  # Output: Error: Invalid input type. Please provide numbers.


def my_function(fname, lname):
  print(fname + " " + lname)

# my_function("Emil") # This will result in an error because the function expects two arguments, but only one is provided.

"""
Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:
"""

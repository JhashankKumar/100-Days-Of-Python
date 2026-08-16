"""
*args and **kwargs
By default, a function must be called with the correct number of arguments.

However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept an unknown number of arguments.

Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:
"""

# Example 1: Using *args to accept an arbitrary number of arguments
def my_function(*args):
    for arg in args:
        print(arg)  

# Calling the function with different numbers of arguments
my_function("Hello", "World", "Python")  # This will print each argument on a new line
my_function(1, 2, 3, 4, 5)  # This will print each number on a new line

"""
What is *args?
The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments:
"""

# Example 2: Using *args to accept an arbitrary number of arguments and perform operations
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with different numbers of arguments
result1 = sum_numbers(1, 2, 3)  # This will return 6
result2 = sum_numbers(10, 20, 30, 40)  # This will return 100
print(result1)  # Output: 6
print(result2)  # Output: 100

"""
Using *args with Regular Arguments
You can combine regular parameters with *args.

Regular parameters must come before *args:
"""

# Example 3: Combining regular parameters with *args
def greet(greeting, *names):
    for name in names:
        print(greeting + " " + name)

greet("Hello", "Alice", "Bob", "Charlie")


"""
Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

This way, the function will receive a dictionary of arguments and can access the items accordingly:
"""

# Example 4: Using **kwargs to accept an arbitrary number of keyword arguments
def my_function(**country):
    for key, value in country.items():
        print(key + ": " + str(value))  # This will print each key-value pair on a new line 

# Calling the function with different keyword arguments
my_function(name="Alice", age=25, city="New York")  # This will print each key-value pair on a new line
my_function(country="USA", language="English")  # This will print each key-value pair on a new line


"""
What is **kwargs?
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:
"""

"""
Using **kwargs with Regular Arguments
You can combine regular parameters with **kwargs.

Regular parameters must come before **kwargs:
"""

# Example 5: Combining regular parameters with **kwargs
def greet(greeting, **names):
    for key, value in names.items():
        print(greeting + " " + key + ": " + str(value)) 

greet("Hello", Alice=25, Bob=30, Charlie=35)  # This will print each key-value pair on a new line
greet("Hi", Dave=40, Eve=45)  # This will print each key-value pair on a new line

"""
Combining *args and **kwargs
You can use both *args and **kwargs in the same function.

The order must be:

regular parameters
*args
**kwargs
"""

# Example 6: Combining *args and **kwargs in the same function
def my_function(arg1, arg2, *args, **kwargs):
    print("arg1:", arg1)
    print("arg2:", arg2)
    
    for arg in args:
        print("args:", arg)
    
    for key, value in kwargs.items():
        print("kwargs:", key, "=", value)

# Calling the function with different combinations of arguments
my_function("Hello", "World", 1, 2, 3, name="Alice", age=25)  # This will print all arguments and keyword arguments

"""
Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
"""

# Example 7: Unpacking a list into separate arguments using *
def greet(name1, name2, name3):
    print("Hello " + name1 + ", " + name2 + ", and " + name3)

# Calling the function with a list of names
names = ["Alice", "Bob", "Charlie"]
greet(*names)  # This will unpack the list into separate arguments

# Example 8: Unpacking a dictionary into separate keyword arguments using **
def greet(name1, name2, name3):
    print("Hello " + name1 + ", " + name2 + ", and " + name3)

# Calling the function with a dictionary of names
names_dict = {"name1": "Alice", "name2": "Bob", "name3": "Charlie"}
greet(**names_dict)  # This will unpack the dictionary into separate keyword arguments  


# example 9: Using *args and **kwargs together with unpacking
def my_function(arg1, arg2, *args, **kwargs):
    print("arg1:", arg1)
    print("arg2:", arg2)
    
    for arg in args:
        print("args:", arg)
    
    for key, value in kwargs.items():
        print("kwargs:", key, "=", value)

# Calling the function with unpacked list and dictionary
args_list = [1, 2, 3]
kwargs_dict = {"name": "Alice", "age": 25}
my_function("Hello", "World", *args_list, **kwargs_dict)  
# This will unpack the list and dictionary into separate arguments and keyword arguments   

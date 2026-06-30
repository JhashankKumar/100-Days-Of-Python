# Scopes
"""
Scopes are the regions of a program where a variable is accessible. In Python, there are four types of scopes:

1. Local Scope
2. Enclosing Scope
3. Global Scope
4. Built-in Scope

"""
# Example 1: Local Scope
def my_function():
    x = 10  # x is a local variable
    print("Local Scope:", x)

my_function()  # Calling the function to see the local scope in action
# print(x)  # This will raise an error because x is not accessible outside the function

# Example 2: Enclosing Scope
def outer_function():
    y = 20  # y is a variable in the enclosing scope

    def inner_function():
        print("Enclosing Scope:", y)  # Accessing the variable from the enclosing scope

    inner_function()    

outer_function()  # Calling the outer function to see the enclosing scope in action

# Example 3: Global Scope
z = 30  # z is a global variable
def my_function():
    print("Global Scope:", z)  # Accessing the global variable

my_function()  # Calling the function to see the global scope in action

# Example 4: Built-in Scope
# Python has a set of built-in functions and variables that are always available.
def my_function():
    print("Built-in Scope:", len)  # Accessing the built-in len() function

my_function()  # Calling the function to see the built-in scope in action

# global Keyword
"""
The global keyword is used to declare that a variable inside a function is global 
(i.e., it exists in the global scope). This allows you to modify the global 
variable inside the function.
"""
# Example 5: Using the global keyword
count = 0  # Global variable
def increment():
    global count  # Declare that we are using the global variable 'count'
    count += 1  # Modify the global variable
increment()  # Calling the function to increment the global variable
print("Global Variable after increment:", count)  # Output: 1

# nonlocal Keyword
"""
The nonlocal keyword is used to declare that a variable inside a nested function is not local to that function, but rather exists in the nearest enclosing scope. 
This allows you to modify the variable from the enclosing scope inside the nested function.
"""
# Example 6: Using the nonlocal keyword
def outer_function():
    value = 10  # Variable in the enclosing scope

    def inner_function():
        nonlocal value  # Declare that we are using the variable from the enclosing scope
        value += 5  # Modify the variable from the enclosing scope
        print("Inner Function Value:", value)  # Output: 15

    inner_function()  # Calling the inner function
    print("Outer Function Value after inner function call:", value)  # Output: 15

outer_function()  # Calling the outer function to see the nonlocal scope in action

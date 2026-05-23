x = 9

def print_global_variable():
    print(x)  # Output: 9

print_global_variable()

def increment_global_variable():
    print(x + 1)  # Output: 10 (x is not modified, just printed with an increment)

increment_global_variable()
print_global_variable()  # Output: 9 (x is still 9, not modified)

# To modify the global variable x, we need to declare it as global inside the function
def modify_global_variable():
    global x  # Declare x as a global variable to modify it
    x = 20  # Modify the global variable x

modify_global_variable()
print_global_variable()  # Output: 20


def initialize_global_variable():
    global y  # Declare y as a global variable
    y = "Hello, World!"  # Initialize the global variable y
    
initialize_global_variable()
print(y)  # Output: Hello, World!
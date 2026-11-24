# decorators
""" 
Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
"""

# Example of a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper  

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Example of a decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

# Example of a decorator that modifies the return value
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_goodbye():
    return "Goodbye!"

print(say_goodbye())

@uppercase_decorator
def greet_person(name):
    return f"Hello {name}"

print(greet_person("Alice"))

list_of_names = ["Alice", "Bob", "Charlie"]
for name in list_of_names:
    print(greet_person(name))

# decorators can also be used to measure the execution time of a function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def long_running_function():    
    time.sleep(2)
    print("Finished long running function.")

long_running_function()

# Example of a decorator that checks if a user is authenticated
def requires_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            raise Exception("User is not authenticated!")
        return func(user, *args, **kwargs)
    return wrapper

@requires_authentication
def view_profile(user):
    print(f"Viewing profile of {user['name']}")

# Example usage
user1 = {"name": "Alice", "is_authenticated": True}
user2 = {"name": "Bob", "is_authenticated": False}

view_profile(user1)
# view_profile(user2)  # This will raise an exception

# Example of a decorator that logs function calls
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

result = add(5, 3)

# multiple decorators can be applied to a single function
@log_function_call
@timer
def complex_function(x):
    time.sleep(1)
    return x * x

result = complex_function(5)

# greeting multiple people using a decorator
@repeat(num_times=2)
def greet_multiple_people(name):
    print(f"Hello {name}")

greet_multiple_people("Alice")
greet_multiple_people("Bob")
greet_multiple_people("Charlie")

# Example of a decorator that caches the results of a function
def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            print("Returning cached result")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper  

@cache
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # This will compute and cache results
print(fibonacci(10))  # This will return the cached result

# preserving function metadata with functools.wraps
from functools import wraps

def my_decorator_with_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator_with_metadata
def say_hello_with_metadata():
    """This function says hello."""
    print("Hello!")

say_hello_with_metadata()
print(say_hello_with_metadata.__name__)  # Output: say_hello_with_metadata
print(say_hello_with_metadata.__doc__)   # Output: This function says hello.

# without functools.wraps, the metadata would be lost

def my_decorator_without_metadata(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator_without_metadata
def say_hello_without_metadata():
    """This function says hello."""
    print("Hello!")

say_hello_without_metadata()
print(say_hello_without_metadata.__name__)  # Output: wrapper
print(say_hello_without_metadata.__doc__)   # Output: None
"""
Lambda functions are anonymous functions in Python that can have any number of
 arguments but only one expression. They are defined using the `lambda` keyword. 
 The syntax for a lambda function is:
```python
lambda arguments: expression
```
"""

# Example of a simple lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8

# Example of a lambda function that squares a number
square = lambda x: x ** 2
result = square(4)

print(result)  # Output: 16

# Example of a lambda function that checks if a number is even
is_even = lambda x: x % 2 == 0
result = is_even(10)
print(result)  # Output: True

# Example of a lambda function that concatenates two strings
concat = lambda str1, str2: str1 + str2
result = concat("Hello, ", "World!")
print(result)  # Output: Hello, World!

# Example of a lambda function used with the `map` function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example of a lambda function used with the `filter` function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

"""
why lambda functions are useful:
1. Conciseness: Lambda functions allow you to write small, one-off functions in a single line of code, 
    making your code more concise and readable.
2. Functional Programming: Lambda functions are often used in functional programming paradigms, 
    where functions are treated as first-class citizens. They can be passed as arguments to 
    higher-order functions like `map`, `filter`, and `reduce`.
3. Anonymous Functions: Since lambda functions are anonymous, they can be used in situations where 
    a function is needed temporarily and does not require a name. This can help reduce clutter in your code.
4. Flexibility: Lambda functions can be defined and used inline, allowing for greater flexibility 
    in how you structure your code. They can be used in various contexts, such as within list 
    comprehensions, as callbacks, or in event handling.
5. Readability: In some cases, using a lambda function can make your code more readable by 
    keeping the function definition close to where it is used, rather than defining a separate named 
    function elsewhere in your code.   
"""

# Example of a lambda function used with the `reduce` function from the `functools` module
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

"""
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""

# Example of a lambda function used as an argument to another function
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x ** 3, 3)
print(result)  # Output: 27

# Example of a lambda function used in a list comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [ (lambda x: x ** 2)(x) for x in numbers ]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]




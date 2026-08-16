"""
Recursion is when a function calls itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing 
a function which never terminates, or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant 
approach to programming.
"""

# Example of a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print(result)  # Output: 120

# Example of a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
result = fibonacci(5)
print(result)  # Output: 5

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)  # Output: 5 4 3 2 1 Blastoff!

"""
Base Case and Recursive Case
Every recursive function must have two parts:

A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error.
"""

# recursive function to calculate the sum of a list of numbers
def sum_list(numbers):
    if len(numbers) == 0:  # base case
        return 0
    else:  # recursive case
        return numbers[0] + sum_list(numbers[1:])
    
result = sum_list([1, 2, 3, 4, 5])
print(result)  # Output: 15

"""
Why use numbers[1:]?

It removes the first element after processing it, 
allowing the recursive function to work on a smaller list each time 
until it reaches the base case (an empty list).

Note: While this is a common way to demonstrate recursion, numbers[1:] creates a new list 
on every recursive call, making it less efficient for large lists. A more efficient recursive 
approach passes an index instead of slicing.
"""

# finding the maximum number in a list using recursion
def find_max(numbers):
    if len(numbers) == 1:  # base case
        return numbers[0]
    else:  # recursive case
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
    
result = find_max([3, 1, 4, 1, 5, 9, 2, 6, 5])
print(result)  # Output: 9

"""
Recursion Depth Limit
Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

Example
Check the recursion limit:

If you need deeper recursion, you can increase the limit, but be careful as this can cause crashes:

Increasing the recursion limit should be done with caution. For very deep recursion, 
consider using iteration instead.

"""

import sys
print(sys.getrecursionlimit())  # Output: 1000 (default limit)

sys.setrecursionlimit(2000)  # Increase the recursion limit to 2000
print(sys.getrecursionlimit())  # Output: 2000
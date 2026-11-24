"""
List Comprehension is a concise way to create lists in Python. 
It allows you to generate a new list by applying an expression to each item in an iterable, 
optionally filtering items using a condition.   

The syntax for list comprehension is:
new_list = [expression for item in iterable if condition]
Where:
- expression: The expression to evaluate for each item in the iterable.
- item: The variable that takes the value of each item in the iterable.
- iterable: The collection of items to iterate over (e.g., list, tuple, set, etc.).
- condition (optional): A filter that determines whether the item should be included in the new list.
"""
# Example 1: Create a list of squares of numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

# Example 2: Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# Example 3: Create a list of uppercase letters from a list of lowercase letters
lowercase_letters = ['a', 'b', 'c', 'd', 'e']
uppercase_letters = [letter.upper() for letter in lowercase_letters]
print(uppercase_letters)  # Output: ['A', 'B', 'C', 'D', 'E']

# Example 4: Create a list of tuples containing numbers and their squares
numbers_and_squares = [(x, x ** 2) for x in range(10)]
print(numbers_and_squares)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]    

"""
List comprehension can also be used with nested loops and multiple conditions.
in range of indexes, the first index is included, but the second index is not included.
If we omit the first index, it is considered as 0. 
If we omit the second index, it is considered as the length of the list.
"""

# create a list of all possible combinations of two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combinations = [(x, y) for x in list1 for y in list2]
print(combinations)  
# Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]   

# create a list of numbers from 0 to 99 that are divisible by both 3 and 5
divisible_by_3_and_5 = [x for x in range(100) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)  # Output: [0, 15, 30, 45, 60, 75, 90]  

# make a list of the first letter of each word in a sentence
sentence = "Hello World from Python"
first_letters = [word[0] for word in sentence.split()]
print(first_letters)  # Output: ['H', 'W', 'f', 'P']

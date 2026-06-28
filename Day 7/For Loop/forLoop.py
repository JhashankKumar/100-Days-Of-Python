"""
Python For Loops
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

# Example 1: Using a for loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Example 2: Using a for loop to iterate over a string
word = "Python"
for letter in word:
    print(letter)

# Example 3: Using a for loop with the range() function
# The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(5):
    print(i)

# break statement can be used to exit the loop prematurely when a certain condition is met.
for i in range(10):
    if i == 6:
        break
    print(i)

# continue statement can be used to skip the current iteration and move to the next iteration of the loop.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # This will print only odd numbers from 1 to 9

# Loop Through the tuple
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# You can loop through the items of a tuple using a for loop.
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

# Loop Through the dictionary
# Dictionaries are unordered collections of items.
# You can loop through the keys, values, or key-value pairs of a dictionary using a for loop.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key in my_dict:
    print(key, ":", my_dict[key])  # This will print the key and its corresponding value

# Loop Through the set
# Sets are unordered collections of unique items.
# You can loop through the items of a set using a for loop.
my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)  # This will print each unique item in the set

# range with start and end values
# You can specify a start and end value in the range() function.
for i in range(2, 10):  # This will start from 2 and go up to (but not including) 10
    print(i)

# range with step value
# You can also specify a step value in the range() function.
for i in range(0, 10, 2):  # This will start from 0 and go up to (but not including) 10, incrementing by 2
    print(i)  # This will print even numbers from 0 to 8
    
# nested for loops
# You can use nested for loops to iterate over multiple sequences.

taste = ["sweet", "sour", "bitter"]
for fruit in fruits:
    for flavor in taste:
        print(fruit, "is", flavor)


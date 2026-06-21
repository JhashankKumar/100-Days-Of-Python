# match statement is a new feature introduced in Python 3.10 
# that allows you to perform pattern matching on values. It is similar to switch statements
# in other programming languages, but more powerful and flexible.  

# The match statement allows you to match values against patterns,
# and execute code based on the matched pattern. It can be used with various data types,
# including integers, strings, lists, tuples, and dictionaries.

# Example 1: Matching an integer value
number = 3
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")

# Example 2: Matching a string value
day = "Monday"
match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("End of the work week")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Midweek day")  

# Example 3: Matching a list
fruits = ["apple", "banana", "cherry"]
match fruits:
    case ["apple", "banana", "cherry"]:
        print("All fruits are present")
    case ["apple", "banana"]:
        print("Only apple and banana are present")
    case _:
        print("Some fruits are missing")

# Example 4: Matching a dictionary
person = {"name": "Alice", "age": 30}
match person:
    case {"name": "Alice", "age": 30}:
        print("This is Alice, aged 30")
    case {"name": "Bob", "age": 25}:
        print("This is Bob, aged 25")
    case _:
        print("Unknown person")

# Example 5: Using match with a class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
match point:
    case Point(0, 0):
        print("Origin")
    case Point(x, 0):
        print(f"Point on the x-axis at {x}")
    case Point(0, y):
        print(f"Point on the y-axis at {y}")
    case Point(x, y):
        print(f"Point at ({x}, {y})")


"""
default case
underscore (_) is used as a wildcard pattern in match statements.
It matches any value that doesn't match any of the specified cases.

under the hood, the match statement uses a series of if-elif-else statements to check each case.
"""

"""
| operator
The | operator is used to combine multiple patterns in a match statement.
It allows you to specify multiple patterns that should be treated as equivalent.
In the example above, the case "Saturday" | "Sunday": line matches either "Saturday" or "Sunday" 
and executes the corresponding code block.
"""

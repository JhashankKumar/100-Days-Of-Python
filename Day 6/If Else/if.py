"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, 
most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

# if condition 

# check age is greater than 18 or not 
age = 18
if age >= 18:
    print("person is eligible for vote")


# multiple statements 
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

"""
Note: You can use spaces or tabs for indentation, 
but you must use the same amount of indentation for all statements within the same code block.

Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. 
Other programming languages often use curly-brackets for this purpose.
"""

#Using Variables in Conditions
#Boolean variables can be used directly in if statements without comparison operators.

is_user_logged_in = True

if is_user_logged_in:
   print("welcome to disney land")

"""
Python can evaluate many types of values as True or False in an if statement.

Zero (0), empty strings (""), None, and empty collections are treated as False. 
Everything else is treated as True.

This includes positive numbers (5), negative numbers (-3), and any non-empty string 
(even "False" is treated as True because it's a non-empty string).
"""

# Example of truthy and falsy values
if 0:
    print("This will not be printed because 0 is treated as False.")
else:
    print("This will be printed because 0 is treated as False.")

if "":
    print("This will not be printed because an empty string is treated as False.")
else:
    print("This will be printed because an empty string is treated as False.")

if None:
    print("This will not be printed because None is treated as False.")
else:
    print("This will be printed because None is treated as False.")

if 5:
    print("This will be printed because 5 is treated as True.")

if "False":
    print("This will be printed because a non-empty string is treated as True.")
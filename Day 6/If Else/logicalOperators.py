"""
Python Logical Operators
Logical operators are used to combine conditional statements. Python has three logical operators:

and - Returns True if both statements are true
or - Returns True if one of the statements is true
not - Reverses the result, returns False if the result is true
"""

# Example 1: Using 'and' operator
age = 25
has_license = True
if age >= 18 and has_license:
    print("You are eligible to drive.")
else:    print("You are not eligible to drive.")

# Example 2: Using 'or' operator
day = "Saturday"
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] or day in ["Saturday", "Sunday"]:
    print("It's a valid day.")
else:    print("That's not a valid day.")

# Example 3: Using 'not' operator
is_raining = False
if not is_raining:
    print("It's a nice day for a walk.")
else:    print("Better stay indoors.")

# combining logical operators
age = 30
has_license = True
if (age >= 18 and has_license) or age >= 65:
    print("You are eligible for a special discount.")
else:    print("You are not eligible for a special discount.")  

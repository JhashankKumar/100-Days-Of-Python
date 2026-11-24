"""
The Else Keyword
The else keyword catches anything which isn't caught by the preceding conditions.

The else statement is executed when the if condition (and any elif conditions) evaluate to False.

This creates a simple two-way choice: if the condition is true, execute one block; 
otherwise, execute the else block.

How Else Works
The else statement provides a default action when none of the previous conditions are true. 
Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

Note: The else statement must come last. You cannot have an elif after an else.
"""

# Example 1: Basic If-Else
temperature = 30
if temperature > 25:
    print("It's a hot day")
else:
    print("It's a cool day")

# Example 2: Checking for Even or Odd
number = 7
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

"""
Else as Fallback
The else statement acts as a fallback that executes when none of the preceding conditions are true. 
This makes it useful for error handling, validation, and providing default values.
"""

# Example 3: User Input Validation
user_input = input("Enter a number: ")
if user_input.isdigit():
    print(f"You entered a valid number: {user_input}")
else:
    print("That's not a valid number. Please try again.")

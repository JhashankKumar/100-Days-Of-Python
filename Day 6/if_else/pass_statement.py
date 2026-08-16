# pass statement is used as a placeholder for future code. 
# When the pass statement is executed, nothing happens, 
# but you avoid getting an error when empty code is not allowed. 

if True:
    pass  # This is a placeholder for future code

age = 20
if age >= 18:
    pass  # This is a placeholder for future code
else:
    print("You are not eligible to drive.")

"""
Why Use pass?
The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later

"""

"""
pass in Development
During development, you might want to sketch out your program structure before implementing the details. 
The pass statement allows you to do this without syntax errors.
"""

"""
pass vs Comments
A comment is ignored by Python, but pass is an actual statement that gets executed 
(though it does nothing). You need pass where Python expects a statement, not just a comment.
"""

# Example: Using pass in a function
def my_function():
    pass  # This function does nothing for now


# shorthand if else
age = 20
# Using a single line if-else statement
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Another example with a different condition
number = 10
result = "Even" if number % 2 == 0 else "Odd"
print(result)  # Output: Even

# shorthand if-else with a more complex condition
marks = 85
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "F"
print(f"Grade: {grade}")  # Output: Grade: B 

# shorthand if condition with a function
a = 5
b = 10
if a > b: print("a is greater than b")

a = 5
b = 10
print("a is greater than b") if a > b else print("a is not greater than b")

# This is called a conditional expression (sometimes known as a "ternary operator").

a = 5
b = 10
bigger = a if a > b else b
print(f"The bigger number is: {bigger}")  # Output: The bigger number is: 10

# multi conditions in one line
age = 25
category = "Child" if age < 13 else "Teenager" if age < 20 else "Adult" if age < 65 else "Senior"
print(f"Age category: {category}")  # Output: Age category: Adult

# username 
username = "admin"
message = "Welcome, admin!" if username == "admin" else "Welcome, guest!"
print(message)  # Output: Welcome, admin!

# Check if a number is positive, negative, or zero
number = -5
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
print(f"The number is: {result}")  # Output: The number is: Negative

"""
When to Use Shorthand If
Shorthand if statements and ternary operators should be used when:

The condition and actions are simple
It improves code readability
You want to make a quick assignment based on a condition
Important: While shorthand if statements can make code more concise, 
avoid overusing them for complex conditions. For readability, use regular if-else statements 
when dealing with multiple lines of code or complex logic.
"""
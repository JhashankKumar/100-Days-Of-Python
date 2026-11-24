"""
The Elif Keyword
The elif keyword is Python's way of saying 
"if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a 
block of code as soon as one of the conditions evaluates to True.
"""

a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a < b:
    print("a is less than b")
else:
    print("none of the above")

# student marks
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:    
    print("Grade: F")


"""
How Elif Works
When you use elif, Python evaluates the conditions from top to bottom. 
As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

Important: Only the first true condition will be executed. 
Even if multiple conditions are true, Python stops after executing the first matching block.
"""

# age category
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# weekday or weekend
day = "Saturday"
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday")
elif day in ["Saturday", "Sunday"]:
    print("It's a weekend")


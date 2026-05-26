# Boolean Values
is_true = True
is_false = False
print("is_true:", is_true)  # Output: is_true: True
print("is_false:", is_false)  # Output: is_false: False

# Boolean expressions
a = 10
b = 20
print("a > b:", a > b)  # Output: a > b: False
print("a < b:", a < b)  # Output: a < b: True
print("a == b:", a == b)  # Output: a == b: False
print("a != b:", a != b)  # Output: a != b: True
print("a >= b:", a >= b)  # Output: a >= b: False
print("a <= b:", a <= b)  # Output: a <= b: True

# Boolean operations
x = True
y = False
print("x and y:", x and y)  # Output: x and y: False
print("x or y:", x or y)  # Output: x or y: True
print("not x:", not x)  # Output: not x: False
print("not y:", not y)  # Output: not y: True   

# Using boolean values in if statements
if is_true:
    print("This is true!")  # Output: This is true!
else:
    print("This is false.")

# Evaluating values and variables
print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
print(bool([]))  # Output: False
print(bool([1, 2, 3]))  # Output: True  
print(bool(None))  # Output: False

"""
Most Values are True: 
1. Almost any value is evaluated to True if it has some sort of content.

2. Any string is True, except empty strings.

3. Any number is True, except 0.

4. Any list, tuple, set, and dictionary are True, except empty ones.

Some Values are False:
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.
"""

# functions that return boolean values
def is_even(num):
    return num % 2 == 0

print("Is 4 even?", is_even(4))  # Output: Is 4 even? True
print("Is 5 even?", is_even(5))  # Output: Is 5 even? False

# Using boolean values in loops
count = 0
while count < 5:
    print("Count:", count)  # Output: Count: 0, Count: 1, Count: 2, Count: 3, Count: 4 (each on a new line)
    count += 1

# isinstance() function to check for boolean type
print(isinstance(is_true, bool))  # Output: True
print(isinstance(is_false, bool))  # Output: True
print(isinstance(a, bool))  # Output: False
print(isinstance(1, bool))  # Output: False
print(isinstance(0, bool))  # Output: False
print(isinstance(None, bool))  # Output: False

print(isinstance(1, int))  # Output: True
# Format Strings
""" Python provides several ways to format strings, allowing you to create dynamic and formatted output. """

# Using the format() method
from xml.etree.ElementInclude import include


name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

# Using f-strings (available in Python 3.6 and later)
name = "Bob"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Bob and I am 25 years old. 

# Using the % operator (old-style string formatting)
name = "Charlie"
age = 35
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Charlie and I am 35 years old.    

""" 
Each of these methods allows you to create formatted strings in different ways, and you can choose the one 
that best suits your needs and preferences. The format() method and f-strings are generally more modern and 
preferred for their readability and flexibility, while the % operator is an older style of string formatting 
that is still supported but less commonly used in new code.
Overall, string formatting is a powerful feature in Python that enables you to create dynamic and well-formatted 
output, making it easier to display information in a clear and organized manner. Whether you're using the 
format() method, f-strings, or the % operator, understanding how to format strings effectively is essential 
for creating professional and user-friendly output in your Python programs. Always consider readability and 
maintainability when choosing a string formatting method, and take advantage of the various options available 
to create the best possible output for your specific use case. """
"""Additionally, when using f-strings, you can also include expressions and even call functions directly within 
the curly braces, allowing for even more dynamic and powerful string formatting capabilities. 
This makes f-strings a particularly versatile and convenient option for string formatting in Python,
as they allow you to easily incorporate variables, expressions, and function calls into your formatted 
strings without the need for additional syntax or complexity. Overall, f-strings provide a modern and efficient 
way to format strings in Python, making them a popular choice among developers for creating dynamic and 
well-formatted output."""

# Amount of decimal places in float formatting
pi = 3.141592653589793
formatted_pi = f"Pi is approximately {pi:.2f}"  # This will format the value of pi to 2 decimal places
print(formatted_pi)  # Output: Pi is approximately 3.14

# Math expressions in f-strings
a = 5
b = 10
formatted_expression = f"The sum of {a} and {b} is {a + b}."  # This will evaluate the expression a + b and include the result in the formatted string
print(formatted_expression)  # Output: The sum of 5 and 10 is 15.   


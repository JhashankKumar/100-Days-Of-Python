""""
Strings in Python are sequences of characters. They are immutable, meaning that once a string is created,
it cannot be changed. You can create strings using single quotes (' '), double quotes (" "), 
or triple quotes (''' ''' or """ """).
"""
# Creating strings
s1 = 'Hello, World!'
s2 = "Python is great."
s3 = '''This is a multi-line string.'''
s4 = """This is another multi-line string."""   
print(s1)  # Output: Hello, World!
print(s2)  # Output: Python is great.
print(s3)  # Output: This is a multi-line string.
print(s4)  # Output: This is another multi-line string.

# Strings are immutable
s = "Hello"
try:
    s[0] = 'h'  # This will raise a TypeError because strings are immutable
except TypeError as e:
    print("Error:", e)  # Output: Error: 'str' object does not support item assignment

# Strings are Array of Characters
s = "Hello"
print(s[0])  # Output: H
print(s[1])  # Output: e
print(s[2])  # Output: l

# looping through a string
s = "Hello"
for char in s:
    print(char)  # Output: H e l l o (each character on a new line)

# String Length
s = "Hello, World!"
print("Length of s:", len(s))  # Output: Length of s: 13

# Check if a substring is in a string
"""You can check if a substring is present in a string using the 'in' keyword. 
This will return True if the substring is found and False otherwise. 
This is a common operation when working with strings, and it can be used in various contexts, 
such as searching for keywords, validating input, or filtering data. 
It's important to note that the 'in' keyword is case-sensitive, meaning that it will only return 
True if the substring matches the case of the characters in the string. If you want to perform a 
case-insensitive check, you can convert both the string and the substring to lower case (or upper case) 
before using the 'in' keyword. Overall, checking for substrings is a fundamental aspect of 
string manipulation in Python and is widely used in many applications."""
s = "Hello, World!"
print("Hello" in s)  # Output: True
print("Python" in s)  # Output: False


# check if a substring is not in a string
s = "Hello, World!"
print("Python" not in s)  # Output: True
print("Hello" not in s)  # Output: False

# Using if statement to check for substring
s = "Hello, World!"
if "Hello" in s:
    print("Found 'Hello' in the string!")  # Output: Found 'Hello' in the string!
else:    
    print("'Hello' not found in the string.")

""" Indexing and slicing are powerful features of strings in Python that allow you to access specific 
characters or substrings. Indexing is used to access individual characters in a string, while slicing 
is used to access a range of characters. Both indexing and slicing use zero-based indexing, meaning 
that the first character of the string is at index 0. When slicing, you can specify a start index, 
an end index, and an optional step. The start index is inclusive, while the end index is exclusive. 
If you omit the start index, it defaults to 0, and if you omit the end index, it defaults to the length 
of the string. The step parameter allows you to specify the interval between characters in the slice. 
Overall, indexing and slicing provide a flexible way to manipulate strings and extract specific parts 
of a string based on your needs."""


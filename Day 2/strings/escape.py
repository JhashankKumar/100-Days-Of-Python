# Escape characters in a string

# The backslash (\) is used as an escape character in Python strings. 
""" 
It allows you to include special characters in a string that would otherwise be difficult to include directly.
Here are some common escape characters:
""" 

s = "She said, \"Hello, World!\""
print(s)  # Output: She said, "Hello, World!" 

# Newline 
"""
\n is used to insert a newline character in a string, which creates a line break when the string is printed.
"""
s = "Hello, World!\nWelcome to Python programming."
print(s)  # Output: Hello, World!
          #         Welcome to Python programming.

# Tab
"""
\t is used to insert a tab character in a string, which creates a horizontal space when the string is printed.
"""
s = "Name:\tJohn Doe\nAge:\t30"
print(s)  # Output: Name:   John Doe
          #         Age:    30  

# Backslash
""" 
To include a literal backslash in a string, you need to escape it with another backslash (\\).
"""
s = "This is a backslash: \\"
print(s)  # Output: This is a backslash: \

# Raw Strings
""" 
If you want to treat backslashes as literal characters and not as escape characters, 
you can use raw strings by prefixing the string with 'r' or 'R'.
"""
s = r"This is a raw string with a backslash: \n"
print(s)  # Output: This is a raw string with a backslash: \n

# Unicode Characters
"""
You can use Unicode escape sequences to include special characters in a string.
For example, \u followed by a four-digit hexadecimal code represents a Unicode character.
"""
s = "This is a Unicode character: \u03A9"  # \u03A9 represents the Greek letter Omega (Ω)
print(s)  # Output: This is a Unicode character: Ω 

# Octal and Hexadecimal Escape Sequences
"""
You can also use octal (\ooo) and hexadecimal (\xhh) escape sequences to include characters in a string.
"""
s = "This is an octal escape sequence: \101"  # \101 represents the letter 'A' in octal
print(s)  # Output: This is an octal escape sequence: A 

s = "This is a hexadecimal escape sequence: \x41"  # \x41 represents the letter 'A' in hexadecimal
print(s)  # Output: This is a hexadecimal escape sequence: A    


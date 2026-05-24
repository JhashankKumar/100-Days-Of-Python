# Modify Strings
""" Strings are immutable, which means you cannot change them after they are created. 
However, you can create a new string based on the original string with the desired modifications. """
""" 
Here are some common ways to modify strings in Python:

1. Changing Case: You can use the upper() and lower() methods to create new strings with all characters in uppercase or lowercase, respectively.    
2. Removing Whitespace: The strip() method can be used to create a new string with leading and trailing whitespace removed.
3. Replacing Substrings: The replace() method allows you to create a new string by replacing occurrences of a specified substring with another substring.
4. Splitting Strings: The split() method can be used to create a list of substrings by splitting the original string at a specified delimiter.  

When modifying strings, it's important to remember that the original string remains unchanged, and a new string is created with the modifications. This is a fundamental aspect of how strings work in Python and is crucial to understand when working with string manipulation. Additionally, there are many other string methods available in Python that can be used to modify strings in various ways, such as splitting, joining, formatting, and more. Exploring these methods can help you become more proficient in working with strings and allow you to perform a wide range of operations on string data effectively. Always refer to the Python documentation for a comprehensive list of string methods and their functionalities to make the most out of string manipulation in your Python programming endeavors. Overall, while strings are immutable, Python provides a rich set of tools to create modified versions of strings, enabling you to work with string data flexibly and efficiently. Understanding the immutability of strings and how to create new strings with modifications is essential for effective string manipulation in Python. Whether you're changing the case, removing whitespace, replacing substrings, or performing other modifications, always remember that the original string remains unchanged, and a new string is created with the desired changes. This concept is fundamental to working with strings in Python and is key to mastering string manipulation techniques.

"""


# Uppercase
s = "hello, world!"
s_upper = s.upper()  # This will create a new string with all characters in uppercase
print("Original string:", s)  # Output: Original string: hello, world!
print("Uppercase string:", s_upper)  # Output: Uppercase string: HELLO, WORLD!

# Lowercase
s = "HELLO, WORLD!"
s_lower = s.lower()  # This will create a new string with all characters in lowercase
print("Original string:", s)  # Output: Original string: HELLO, WORLD!
print("Lowercase string:", s_lower)  # Output: Lowercase string: hello, world!

# Remove Whitespace
"""
The strip() method removes leading and trailing whitespace from a string.
"""
s = "  hello, world!  "
s_stripped = s.strip()  # This will create a new string with leading and trailing whitespace removed
print("Original string:", s)  # Output: Original string:   hello, world!   #
print("Stripped string:", s_stripped)  # Output: Stripped string: hello, world!

# Replace a Substring
s = "Hello, World!"
s_replaced = s.replace("World", "Python")  # This will create a new string with "World" replaced by "Python"
print("Original string:", s)  # Output: Original string: Hello, World!
print("Replaced string:", s_replaced)  # Output: Replaced string: Hello, Python!

""" When modifying strings, it's important to remember that the original string remains unchanged, 
and a new string is created with the modifications. This is a fundamental aspect of how strings work in 
Python and is crucial to understand when working with string manipulation.
Additionally, there are many other string methods available in Python that can be used to modify strings in 
various ways, such as splitting, joining, formatting, and more. Exploring these methods can help you become 
more proficient in working with strings and allow you to perform a wide range of operations on string data 
effectively. Always refer to the Python documentation for a comprehensive list of string methods and their 
functionalities to make the most out of string manipulation in your Python programming endeavors. 
Overall, while strings are immutable, Python provides a rich set of tools to create modified versions of strings,
enabling you to work with string data flexibly and efficiently. Understanding the immutability of strings and 
how to create new strings with modifications is essential for effective string manipulation in Python. 
Whether you're changing the case, removing whitespace, replacing substrings, or performing other modifications, 
always remember that the original string remains unchanged, and a new string is created with the desired changes. 
This concept is fundamental to working with strings in Python and is key to mastering string manipulation techniques. """

# Split a String
s = "Hello, World!"
s_split = s.split(", ")  # This will create a list of substrings by splitting the original string at the specified delimiter
print("Original string:", s)  # Output: Original string: Hello, World!
print("Split string:", s_split)  # Output: Split string: ['Hello', 'World!']

s = "Hello mike and jane. Welcome to the party."
s_split = s.split(" ")  # This will create a list of substrings by splitting the original string at spaces
print("Original string:", s)  # Output: Original string: Hello mike and jane. Welcome to the party.
print("Split string:", s_split)  # Output: Split string: ['Hello', 'mike', 'and', 'jane.', 'Welcome', 'to', 'the', 'party.']    


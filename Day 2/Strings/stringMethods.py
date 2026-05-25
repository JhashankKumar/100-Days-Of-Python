# String Methods

"""
String methods are built-in functions that allow you to perform various operations on strings. 
These methods can be used to manipulate, search, and format strings in different ways. 
Here are some common string methods in Python:
"""

# capitalize() - Capitalizes the first character of the string and converts the rest to lowercase.
s = "hello, world!"
s_capitalized = s.capitalize()  
# This will create a new string with the first character capitalized and the rest in lowercase
print("Original string:", s)  # Output: Original string: hello, world!
print("Capitalized string:", s_capitalized)  # Output: Capitalized string: Hello, world!

# casefold() - Converts the string to lowercase for case-insensitive comparisons.
s = "Hello, World!"
s_casefolded = s.casefold()  
# This will create a new string with all characters in lowercase for case-insensitive comparisons
print("Original string:", s)  # Output: Original string: Hello, World!
print("Casefolded string:", s_casefolded)  # Output: Casefolded string: hello, world!   

# center() - Centers the string within a specified width, padding it with a specified character (default is space).
s = "Hello"
s_centered = s.center(20, "*") 
# This will create a new string that centers the original string within a width of 20 characters, padding it with asterisks
print("Original string:", s)  # Output: Original string: Hello
print("Centered string:", s_centered)  # Output: Centered string: ********Hello******** 

# count() - Counts the number of occurrences of a specified substring in the string.
s = "Hello, World! Hello!"
count_hello = s.count("Hello")  
# This will count the number of occurrences of the substring "Hello" in the original string
print("Original string:", s)  # Output: Original string: Hello, World! Hello!
print("Count of 'Hello':", count_hello)  # Output: Count of 'Hello': 2

# endcode() - Encodes the string using a specified encoding (default is 'utf-8').
s = "Hello, World!"
s_encoded = s.encode()  
# This will create a new bytes object that represents the original string encoded in UTF-8
print("Original string:", s)  # Output: Original string: Hello, World!
print("Encoded string:", s_encoded)  # Output: Encoded string: b'Hello, World!' 

# endswith() - Checks if the string ends with a specified substring and returns True or False.
s = "Hello, World!"
ends_with_exclamation = s.endswith("!")  
# This will check if the original string ends with an exclamation mark and return True or False 
print("Original string:", s)  # Output: Original string: Hello, World!
print("Ends with '!':", ends_with_exclamation)  # Output: Ends with '!': True   

#expandtabs() - Replaces tab characters in the string with spaces, using a specified tab size (default is 8).
s = "Hello\tWorld!"
s_expanded = s.expandtabs(4)  
# This will create a new string where tab characters are replaced with spaces, using a tab size of 4
print("Original string:", s)  # Output: Original string: Hello    World!
print("Expanded string:", s_expanded)  # Output: Expanded string: Hello    World!   

# find() - Searches for a specified substring in the string and returns the index of its first occurrence, or -1 if not found.
s = "Hello, World!"
index_of_world = s.find("World")  
# This will search for the substring "World" in the original string and return the index of its first occurrence, or -1 if not found
print("Original string:", s)  # Output: Original string: Hello, World!
print("Index of 'World':", index_of_world)  # Output: Index of 'World': 7

# format() - Formats the string using placeholders and values provided as arguments.
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)  
# This will create a new string by replacing the placeholders {} with the values of name and age
print("Formatted string:", formatted_string)  # Output: Formatted string: My name is Alice and I am 30 years old.

# format_map() - Similar to format(), but takes a mapping (like a dictionary) as an argument to replace placeholders in the string.
data = {"name": "Bob", "age": 25}
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)  
# This will create a new string by replacing the placeholders {name} and {age} with the corresponding values from the data dictionary
print("Formatted string:", formatted_string)  # Output: Formatted string: My name is Bob and I am 25 years old.

# index() - Similar to find(), but raises a ValueError if the specified substring is not found in the string.
s = "Hello, World!"
try:
    index_of_python = s.index("Python")  
    # This will search for the substring "Python" in the original string and return the index of its first occurrence, or raise a ValueError if not found
    print("Index of 'Python':", index_of_python)
except ValueError as e:
    print("Error:", e)  # Output: Error: substring not found

# isalnum() - Checks if all characters in the string are alphanumeric (letters and numbers) and returns True or False.
s = "Hello123"
is_alphanumeric = s.isalnum()  
# This will check if all characters in the original string are alphanumeric and return True or False
print("Original string:", s)  # Output: Original string: Hello123
print("Is alphanumeric:", is_alphanumeric)  # Output: Is alphanumeric: True

s = "Hello, World!"
is_alphanumeric = s.isalnum()  
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is alphanumeric:", is_alphanumeric)  # Output: Is alphanumeric: False

s = "12345"
is_alphanumeric = s.isalnum()
print("Original string:", s)  # Output: Original string: 12345
print("Is alphanumeric:", is_alphanumeric)  # Output: Is alphanumeric: True

# isalpha() - Checks if all characters in the string are alphabetic (letters) and returns True or False.
s = "Hello"
is_alpha = s.isalpha()  
# This will check if all characters in the original string are alphabetic and return True or False
print("Original string:", s)  # Output: Original string: Hello
print("Is alphabetic:", is_alpha)  # Output: Is alphabetic: True

s = "Hello, World!"
is_alpha = s.isalpha()  
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is alphabetic:", is_alpha)  # Output: Is alphabetic: False

s = "12345"
is_alpha = s.isalpha()
print("Original string:", s)  # Output: Original string: 12345
print("Is alphabetic:", is_alpha)  # Output: Is alphabetic: False

# isascii() - Checks if all characters in the string are ASCII characters and returns True or False.
s = "Hello, World!"
is_ascii = s.isascii()  
# This will check if all characters in the original string are ASCII characters and return True or False
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is ASCII:", is_ascii)  # Output: Is ASCII: True

s = "Hello, 世界!"
is_ascii = s.isascii()  
print("Original string:", s)  # Output: Original string: Hello, 世界!
print("Is ASCII:", is_ascii)  # Output: Is ASCII: False 

s = "12345"
is_ascii = s.isascii()
print("Original string:", s)  # Output: Original string: 12345
print("Is ASCII:", is_ascii)  # Output: Is ASCII: True

# isdecimal() - Checks if all characters in the string are decimal characters and returns True or False.
s = "12345"
is_decimal = s.isdecimal()  
# This will check if all characters in the original string are decimal characters and return True or False
print("Original string:", s)  # Output: Original string: 12345
print("Is decimal:", is_decimal)  # Output: Is decimal: True

s = "Hello, World!"
is_decimal = s.isdecimal()  
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is decimal:", is_decimal)  # Output: Is decimal: False

s = "123.45"
is_decimal = s.isdecimal()
print("Original string:", s)  # Output: Original string: 123.45
print("Is decimal:", is_decimal)  # Output: Is decimal: False

s = "b1010"
is_decimal = s.isdecimal()
print("Original string:", s)  # Output: Original string: b1010
print("Is decimal:", is_decimal)  # Output: Is decimal: False

s = "0"
is_decimal = s.isdecimal()
print("Original string:", s)  # Output: Original string: 0
print("Is decimal:", is_decimal)  # Output: Is decimal: True

s = "-12345"
is_decimal = s.isdecimal()
print("Original string:", s)  # Output: Original string: -12345
print("Is decimal:", is_decimal)  # Output: Is decimal: False

s = "12345 "
is_decimal = s.isdecimal()
print("Original string:", s)  # Output: Original string: 12345 
print("Is decimal:", is_decimal)  # Output: Is decimal: False

# isdigit() - Checks if all characters in the string are digits and returns True or False.
s = "12345"
is_digit = s.isdigit()  
# This will check if all characters in the original string are digits and return True or False
print("Original string:", s)  # Output: Original string: 12345
print("Is digit:", is_digit)  # Output: Is digit: True

s = "Hello, World!"
is_digit = s.isdigit()  
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is digit:", is_digit)  # Output: Is digit: False

s = "123.45"
is_digit = s.isdigit()
print("Original string:", s)  # Output: Original string: 123.45 
print("Is digit:", is_digit)  # Output: Is digit: False

s = "b1010"
is_digit = s.isdigit()
print("Original string:", s)  # Output: Original string: b1010
print("Is digit:", is_digit)  # Output: Is digit: False

s = "0"
is_digit = s.isdigit()
print("Original string:", s)  # Output: Original string: 0
print("Is digit:", is_digit)  # Output: Is digit: True

s = "-12345"
is_digit = s.isdigit()
print("Original string:", s)  # Output: Original string: -12345
print("Is digit:", is_digit)  # Output: Is digit: False

s = "12345 "
is_digit = s.isdigit()
print("Original string:", s)  # Output: Original string: 12345
print("Is digit:", is_digit)  # Output: Is digit: False

# isidentifier() - Checks if the string is a valid identifier and returns True or False.

s = "variable"
is_identifier = s.isidentifier()
print("Original string:", s)  # Output: Original string: variable
print("Is identifier:", is_identifier)  # Output: Is identifier: True

s = "123variable"
is_identifier = s.isidentifier()
print("Original string:", s)  # Output: Original string: 123variable
print("Is identifier:", is_identifier)  # Output: Is identifier: False

s = "variable name"
is_identifier = s.isidentifier()
print("Original string:", s)  # Output: Original string: variable name
print("Is identifier:", is_identifier)  # Output: Is identifier: False

s = "variable_name"
is_identifier = s.isidentifier()
print("Original string:", s)  # Output: Original string: variable_name
print("Is identifier:", is_identifier)  # Output: Is identifier: True

s = "def"
is_identifier = s.isidentifier()
print("Original string:", s)  # Output: Original string: def
print("Is identifier:", is_identifier)  # Output: Is identifier: False (because 'def' is a reserved keyword in Python)  

# islower() - Checks if all characters in the string are lowercase and returns True or False.
s = "hello"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello
print("Is lowercase:", is_lower)  # Output: Is lowercase: True

s = "Hello, World!"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is lowercase:", is_lower)  # Output: Is lowercase: False

s = "12345"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: 12345
print("Is lowercase:", is_lower)  # Output: Is lowercase: False (because there are no lowercase letters in the string)

s = "hello world!"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world!
print("Is lowercase:", is_lower)  # Output: Is lowercase: True (because all characters in the string are lowercase, including the space and punctuation)

s = "hello world! 123"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world! 123
print("Is lowercase:", is_lower)  # Output: Is lowercase: True (because all characters in the string are lowercase, including the space and punctuation, and the digits do not affect the lowercase status of the string)

s = "hello world! 123 ABC"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world! 123 ABC
print("Is lowercase:", is_lower)  # Output: Is lowercase: False (because there are uppercase letters in the string, which means that not all characters are lowercase)  

s = "hello world! 123 abc"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world! 123 abc
print("Is lowercase:", is_lower)  # Output: Is lowercase: True (because all characters in the string are lowercase, including the space and punctuation, and the digits do not affect the lowercase status of the string)   

s = "hello world! 123 abc def"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world! 123 abc def
print("Is lowercase:", is_lower)  # Output: Is lowercase: True (because all characters in the string are lowercase, including the space and punctuation, and the digits do not affect the lowercase status of the string)

s = "hello world! 123 abc def G"
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world! 123 abc def G
print("Is lowercase:", is_lower)  # Output: Is lowercase: False (because there is an uppercase letter 'G' in the string, which means that not all characters are lowercase)

s = "hello world!  "
is_lower = s.islower()
print("Original string:", s)  # Output: Original string: hello world!  
print("Is lowercase:", is_lower)  # Output: Is lowercase: True (because all characters in the string are lowercase, including the space and punctuation, and there are no uppercase letters in the string)

# isnumeric() - Checks if all characters in the string are numeric and returns True or False.
s = "12345"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: 12345
print("Is numeric:", is_numeric)  # Output: Is numeric: True

s = "Hello, World!"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is numeric:", is_numeric)  # Output: Is numeric: False

s = "123.45"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: 123.45
print("Is numeric:", is_numeric)  # Output: Is numeric: False

s = "b1010"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: b1010
print("Is numeric:", is_numeric)  # Output: Is numeric: False

s = "0"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: 0
print("Is numeric:", is_numeric)  # Output: Is numeric: True

s = "-12345"
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: -12345
print("Is numeric:", is_numeric)  # Output: Is numeric: False

s = "12345 "
is_numeric = s.isnumeric()
print("Original string:", s)  # Output: Original string: 12345 
print("Is numeric:", is_numeric)  # Output: Is numeric: False

# isprintable() - Checks if all characters in the string are printable and returns True or False.
s = "Hello, World!"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is printable:", is_printable)  # Output: Is printable: True

s = "Hello, World!\n"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is printable:", is_printable)  # Output: Is printable: False (because the newline character is not considered printable)

s = "Hello, World!\t"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is printable:", is_printable)  # Output: Is printable: False (because the tab character is not considered printable)

s = "Hello, World! "
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: Hello, World! 
print("Is printable:", is_printable)  # Output: Is printable: True (because all characters in the string are printable, including the space at the end) 

s = "b1010"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: b1010
print("Is printable:", is_printable)  # Output: Is printable: True (because all characters in the string are printable) 

s = "12345"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: 12345
print("Is printable:", is_printable)  # Output: Is printable: True (because all characters in the string are printable)

s = "Hello, 世界!"
is_printable = s.isprintable()
print("Original string:", s)  # Output: Original string: Hello, 世界!
print("Is printable:", is_printable)  # Output: Is printable: True (because all characters in the string are printable, including the non-ASCII characters)

# isspace() - Checks if all characters in the string are whitespace and returns True or False.
s = "   "
is_space = s.isspace()
print("Original string:", repr(s))  # Output: Original string: '   '
print("Is space:", is_space)  # Output: Is space: True

s = "Hello, World!"
is_space = s.isspace()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is space:", is_space)  # Output: Is space: False

s = "   Hello, World!   "
is_space = s.isspace()
print("Original string:", repr(s))  # Output: Original string: '   Hello, World!   '
print("Is space:", is_space)  # Output: Is space: False 

s = "\t\n"
is_space = s.isspace()
print("Original string:", repr(s))  # Output: Original string: '\t\n'
print("Is space:", is_space)  # Output: Is space: True (because both the tab and newline characters are considered whitespace)  

s = " "
is_space = s.isspace()
print("Original string:", repr(s))  # Output: Original string: ' '
print("Is space:", is_space)  # Output: Is space: True (because the space character is considered whitespace)   

s = "Hello, World! "
is_space = s.isspace()
print("Original string:", repr(s))  # Output: Original string: 'Hello, World! '
print("Is space:", is_space)  # Output: Is space: False (because there are non-whitespace characters in the string, even though there is a space at the end)    

# istitle() - Checks if the string is in title case (each word starts with an uppercase letter followed by lowercase letters) and returns True or False.
s = "Hello, World!"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is title case:", is_title)  # Output: Is title case: True

s = "Hello, world!"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, world!
print("Is title case:", is_title)  # Output: Is title case: False (because the word "world" does not start with an uppercase letter)    

s = "hello, World!"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: hello, World!
print("Is title case:", is_title)  # Output: Is title case: False (because the word "hello" does not start with an uppercase letter)    

s = "Hello, World! 123"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is title case:", is_title)  # Output: Is title case: True (because all words that start with an uppercase letter are followed by lowercase letters, and the presence of digits does not affect the title case status of the string)  

s = "Hello, World! 123 ABC"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is title case:", is_title)  # Output: Is title case: False (because the word "ABC" is in uppercase and does not follow the title case format)    

s = "Hello, World! 123 abc"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is title case:", is_title)  # Output: Is title case: True (because all words that start with an uppercase letter are followed by lowercase letters, and the presence of digits does not affect the title case status of the string)  

s = "Hello, World! 123 abc def"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World! 123 abc def
print("Is title case:", is_title)  # Output: Is title case: True (because all words that start with an uppercase letter are followed by lowercase letters, and the presence of digits does not affect the title case status of the string)  

s = "Hello, World! $"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: Hello, World! $
print("Is title case:", is_title)  # Output: Is title case: True (because all words that start with an uppercase letter are followed by lowercase letters, and the presence of a special character does not affect the title case status of the string) 

s = "$ Hello, World!"
is_title = s.istitle()
print("Original string:", s)  # Output: Original string: $ Hello, World!
print("Is title case:", is_title)  # Output: Is title case: True (because all words that start with an uppercase letter are followed by lowercase letters, and the presence of a special character at the beginning does not affect the title case status of the string)    

# isupper() - Checks if all characters in the string are uppercase and returns True or False.   
s = "HELLO, WORLD!"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: HELLO, WORLD!
print("Is uppercase:", is_upper)  # Output: Is uppercase: True

s = "Hello, World!"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: Hello, World!
print("Is uppercase:", is_upper)  # Output: Is uppercase: False 

s = "12345"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: 12345
print("Is uppercase:", is_upper)  # Output: Is uppercase: False (because there are no uppercase letters in the string)

s = "HELLO WORLD! 123"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: HELLO WORLD! 123
print("Is uppercase:", is_upper)  # Output: Is uppercase: True (because all letters in the string are uppercase, and the presence of digits does not affect the uppercase status of the string)

s = "123 HELLO WORLD!"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: 123 HELLO WORLD
print("Is uppercase:", is_upper) # Output: Is uppercase: True (because all letters in the string are uppercase, and the presence of digits does not affect the uppercase status of the string)
s = "% HELLO WORLD!"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: % HELLO WORLD!
print("Is uppercase:", is_upper) # Output: Is uppercase: True (because all letters in the string are uppercase, and the presence of a special character does not affect the uppercase status of the string)

s = "HELLO WORLD! %"
is_upper = s.isupper()
print("Original string:", s)  # Output: Original string: HELLO WORLD! %
print("Is uppercase:", is_upper) # Output: Is uppercase: True (because all letters in the string are uppercase, and the presence of a special character does not affect the uppercase status of the string)


# join() - Joins the elements of an iterable (like a list or tuple) into a single string, using the string as a separator.
words = ["Hello", "World", "Python"]
joined_string = " ".join(words)
# This will create a new string by joining the elements of the words list with a space as a separator
print("Original list:", words)  # Output: Original list: ['Hello', 'World', 'Python']
print("Joined string:", joined_string)  # Output: Joined string: Hello World Python

is_alphanumeric = ["Hello123", "Hello, World!", "12345"]
joined_string = ", ".join(is_alphanumeric)
print("Original list:", is_alphanumeric)  # Output: Original list: ['Hello123', 'Hello, World!', '12345']
print("Joined string:", joined_string)  # Output: Joined string: Hello123, Hello, World!, 12345

joined_string = "-".join(is_alphanumeric)
print("Joined string with hyphen:", joined_string)  # Output: Joined string with hyphen: Hello123-Hello, World!-12345

# ljust() - Left-justifies the string within a specified width, padding it with a specified character (default is space).
s = "Hello"
s_left_justified = s.ljust(20, "*")
# This will create a new string that left-justifies the original string within a width of 20 characters, padding it with asterisks
print("Original string:", s)  # Output: Original string: Hello
print("Left-justified string:", s_left_justified)  # Output: Left-justified string: Hello***************

# lower() - Converts all characters in the string to lowercase and returns the new string.
s = "Hello, World!"
s_lower = s.lower()
# This will create a new string with all characters in lowercase
print("Original string:", s)  # Output: Original string: Hello, World!
print("Lowercase string:", s_lower)  # Output: Lowercase string: hello, world!

s = "HELLO, WORLD!"
s_lower = s.lower()
print("Original string:", s)  # Output: Original string: HELLO, WORLD!  
print("Lowercase string:", s_lower)  # Output: Lowercase string: hello, world! 

s = "12345"
s_lower = s.lower()
print("Original string:", s)  # Output: Original string: 12345
print("Lowercase string:", s_lower)  # Output: Lowercase string: 12345 (because there are no alphabetic characters in the string, so the lowercase conversion does not change the string)

# lstrip() - Left-strips the string by removing leading whitespace or specified characters and returns the new string.
s = "   Hello, World!   "
s_left_stripped = s.lstrip()
# This will create a new string by removing leading whitespace from the original string
print("Original string:", repr(s))  # Output: Original string: '   Hello, World!   '
print("Left-stripped string:", repr(s_left_stripped))  # Output: Left-stripped string: 'Hello, World!   '   

s = "###Hello, World!###"
s_left_stripped = s.lstrip("#")
print("Original string:", s)  # Output: Original string: ###Hello, World!
print("Left-stripped string:", s_left_stripped)  # Output: Left-stripped string: Hello, World!### (because the leading '#' characters are removed, but the trailing '#' characters are not affected by the lstrip() method) 


# maketrans() - Creates a translation table that can be used with the translate() method to replace specified characters in the string.
s = "Hello, World!"
translation_table = str.maketrans("Helo", "hELo")
# This will create a translation table that maps 'H' to 'h', 'e' to 'E', 'l' to 'L', and 'o' to 'o'
s_translated = s.translate(translation_table)
# This will create a new string by replacing characters in the original string according to the translation table
print("Original string:", s)  # Output: Original string: Hello, World!
print("Translated string:", s_translated)  # Output: Translated string: hELLo, WorLd! (because 'H' is replaced with 'h', 'e' is replaced with 'E', 'l' is replaced with 'L', and 'o' remains unchanged)

s = "Python Programming"
translation_table = str.maketrans("Pythn", "pYTHN")
s_translated = s.translate(translation_table)
print("Original string:", s)  # Output: Original string: Python Programming
print("Translated string:", s_translated)  # Output: Translated string: pYTHoN Programming (because 'P' is replaced with 'p', 'y' is replaced with 'Y', 't' is replaced with 'T', 'h' is replaced with 'H', and 'n' is replaced with 'N')   

# partition() - Splits the string into three parts based on a specified separator: the part before the separator, the separator itself, and the part after the separator. It returns a tuple containing these three parts.
s = "Hello, World!"
partitioned = s.partition(", ")
# This will split the original string into three parts based on the separator ", " and return a tuple containing the part before the separator, the separator itself, and the part after the separator
print("Original string:", s)  # Output: Original string: Hello, World!
print("Partitioned string:", partitioned)  # Output: Partitioned string: ('Hello', ', ', 'World!') (because the string is split into 'Hello' before the separator, ', ' as the separator, and 'World!' after the separator) 

s = "Python Programming"
partitioned = s.partition(" ")
print("Original string:", s)  # Output: Original string: Python Programming
print("Partitioned string:", partitioned)  # Output: Partitioned string: ('Python', ' ', 'Programming') (because the string is split into 'Python' before the separator, ' ' as the separator, and 'Programming' after the separator)   

s = "Hello, World!"
partitioned = s.partition("x")
print("Original string:", s)  # Output: Original string: Hello, World!
print("Partitioned string:", partitioned)  # Output: Partitioned string: ('Hello, World!', '', '') (because the separator "x" is not found in the string, so the entire string is returned as the first element of the tuple, and the second and third elements are empty strings)  

# rsplit() - Right-splits the string into a list of substrings based on a specified separator, starting from the right. It takes an optional maxsplit argument that specifies the maximum number of splits to perform.
s = "Hello, World! Welcome to Python."
rsplit_result = s.rsplit(", ", 1)
# This will split the original string into a list of substrings based on the separator ", ", starting from the right, and it will perform at most 1 split
print("Original string:", s)  # Output: Original string: Hello, World! Welcome to Python.
print("Right-split result:", rsplit_result)  # Output: Right-split result: ['Hello, World! Welcome to Python.'] (because the separator ", " is not found in the string, so the entire string is returned as a single element in the list)   

s = "Hello, World! Welcome to Python."
rsplit_result = s.rsplit(" ", 2)
print("Original string:", s)  # Output: Original string: Hello, World! Welcome to Python.
print("Right-split result:", rsplit_result)  # Output: Right-split result: ['Hello, World! Welcome', 'to', 'Python.'] (because the separator " " is found in the string, and it is split into three parts starting from the right, with at most 2 splits)   

s = "Hello, World! Welcome to Python."
rsplit_result = s.rsplit("x", 1)
print("Original string:", s)  # Output: Original string: Hello, World! Welcome to Python.
print("Right-split result:", rsplit_result)  # Output: Right-split result: ['Hello, World! Welcome to Python.'] (because the separator "x" is not found in the string, so the entire string is returned as a single element in the list 
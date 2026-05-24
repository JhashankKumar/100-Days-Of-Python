# String Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + ", " + s2 + "!"  
# This will concatenate the strings together with a comma and an exclamation mark
print(s3)  # Output: Hello, World!

# Using the join() method for concatenation
s1 = "Hello"
s2 = "World"
s3 = ", ".join([s1, s2]) + "!"  
# This will join the strings in the list with a comma and a space, and then add an exclamation mark at the end
print(s3)  # Output: Hello, World!

# Using f-strings for concatenation
s1 = "Hello"
s2 = "World"
s3 = f"{s1}, {s2}!"  
# This will create a new string using f-string formatting, which allows you to embed expressions inside string literals
print(s3)  # Output: Hello, World!
# String Slicing
s = "Hello, World!"
print(s[0])  # Output: H
print(s[1])  # Output: e
print(s[2])  # Output: l
print(s[0:5])  # Output: Hello
print(s[7:12])  # Output: World
print(s[:5])  # Output: Hello
print(s[7:])  # Output: World!

# Slice from the start of the string to a specific index
""" here we are slicing from the start of the string to index 5 (exclusive), 
which gives us the substring "Hello"."""
print(s[:5])  # Output: Hello

# Slice from a specific index to the end of the string
""" here we are slicing from index 7 to the end of the string, which gives us the substring "World!"."""
print(s[7:])  # Output: World!

# Slice in the middle of the string
""" here we are slicing from index 3 to index 5 (exclusive), which gives us the substring "ll"."""
print(s[3:5])  # Output: ll

# Slice with a step
""" here we are slicing from index 0 to index 12 (exclusive) with a step of 2, which gives us every second character in the substring "Hello, World"."""
print(s[0:12:2])  # Output: Hlo ol

# Negative indexing
""" Negative indexing allows you to access characters from the end of the string. The last character of the string is at index -1, the second to last character is at index -2, and so on. Here we are slicing from index -6 to index -1 (exclusive), which gives us the substring "World"."""
print(s[-6:-1])  # Output: World


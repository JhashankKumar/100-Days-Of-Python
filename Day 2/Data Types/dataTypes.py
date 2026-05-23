# Data Types in Python
# 1. Numeric Types
# a. int (Integer)
a = 10
print(a)  # Output: 10  
# b. float (Floating-point number)
b = 3.14
print(b)  # Output: 3.14
# c. complex (Complex number)
c = 2 + 3j
print(c)  # Output: (2+3j)  
# 2. Sequence Types
# a. list (List)
my_list = [1, 2, 3, "Hello", 4.5]
print(my_list)  # Output: [1, 2, 3, 'Hello', 4.5]
# b. tuple (Tuple)
my_tuple = (1, 2, 3, "World", 5.6)
print(my_tuple)  # Output: (1, 2, 3, 'World', 5.6)
# c. range (Range)
my_range = range(0, 10, 2)
print(my_range)  # Output: range(0, 10, 2)
print(list(my_range))  # Output: [0, 2, 4, 6, 8]
# 3. Text Type
# a. str (String)
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!
# 4. Mapping Type
# a. dict (Dictionary)
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 5. Set Types
# a. set (Set)
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
# b. frozenset (Frozen Set)
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4, 5})
# 6. Boolean Type
# a. bool (Boolean)
is_true = True
is_false = False
print(is_true)  # Output: True
print(is_false)  # Output: False
# 7. Binary Types
# a. bytes (Bytes)
my_bytes = b'Hello'
print(my_bytes)  # Output: b'Hello'
# b. bytearray (Byte Array)
my_bytearray = bytearray(b'Hello')
print(my_bytearray)  # Output: bytearray(b'Hello')
# c. memoryview (Memory View)
my_memoryview = memoryview(b'Hello')
print(my_memoryview)  # Output: <memory at 0x...> 
# 8. None Type
# a. NoneType (None)
my_none = None
print(my_none)  # Output: None
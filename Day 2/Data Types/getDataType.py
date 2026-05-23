# Get Data Type
a = 10
print(type(a))  # Output: <class 'int'>
b = 3.14
print(type(b))  # Output: <class 'float'>
c = 2 + 3j
print(type(c))  # Output: <class 'complex'>

my_list = [1, 2, 3, "Hello", 4.5]
print(type(my_list))  # Output: <class 'list'>
my_tuple = (1, 2, 3, "World", 5.6)
print(type(my_tuple))  # Output: <class 'tuple'>
my_range = range(0, 10, 2)
print(type(my_range))  # Output: <class 'range'>  

my_string = "Hello, World!"
print(type(my_string))  # Output: <class 'str'>

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(type(my_dict))  # Output: <class 'dict'>
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(type(my_frozenset))  # Output: <class 'frozenset'>  

is_true = True
print(type(is_true))  # Output: <class 'bool'>
is_false = False
print(type(is_false))  # Output: <class 'bool'> 

my_bytes = b'Hello'
print(type(my_bytes))  # Output: <class 'bytes'>
my_bytearray = bytearray(b'Hello')
print(type(my_bytearray))  # Output: <class 'bytearray'>
my_memoryview = memoryview(b'Hello')
print(type(my_memoryview))  # Output: <class 'memoryview'>
my_none = None
print(type(my_none))  # Output: <class 'NoneType'>          
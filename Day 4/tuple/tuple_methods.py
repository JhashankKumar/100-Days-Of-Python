# methods in tuple
# count() method
my_tuple = (1, 2, 3, 2, 4, 2)
count_2 = my_tuple.count(2)
print(count_2)  # Output: 3

# index() method
my_tuple = (1, 2, 3, 4, 5)
index_3 = my_tuple.index(3)
print(index_3)  # Output: 2 

# index() method with a start parameter
my_tuple = (1, 2, 3, 4, 5, 3)
index_3_from_3 = my_tuple.index(3, 3)
print(index_3_from_3)  # Output: 5  

# index() method with a start and end parameter
my_tuple = (1, 2, 3, 4, 5, 3)
index_3_from_3_to_5 = my_tuple.index(3, 3, 5)
print(index_3_from_3_to_5)  # Output: 5

# index() method with a value that is not in the tuple (will raise a ValueError)
my_tuple = (1, 2, 3, 4, 5)
index_6 = my_tuple.index(6)
# This will raise a ValueError because 6 is not in the tuple

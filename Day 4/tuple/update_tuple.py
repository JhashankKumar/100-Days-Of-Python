# change value of a tuple
my_tuple = (1, 'hello', 3.14)
# my_tuple[0] = 2  # This will raise a TypeError because tuples are immutable

# to change the value of a tuple, you can create a new tuple with the desired values
my_tuple = (2, 'hello', 3.14)
print(my_tuple)  # Output: (2, 'hello', 3.14)   

# you can also concatenate tuples to create a new tuple with the desired values
my_tuple = (1, 'hello', 3.14)
new_tuple = (2,) + my_tuple[1:]  # Create a new tuple with the first element changed to 2
print(new_tuple)  # Output: (2, 'hello', 3.14)

# change tuple to list, modify the list, and convert it back to a tuple
my_tuple = (1, 'hello', 3.14)
temp_list = list(my_tuple)  # Convert tuple to list
temp_list[0] = 2  # Modify the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)  # Output: (2, 'hello', 3.14)

# Tuples are immutable, which means that once a tuple is created, its elements cannot be changed. 
# However, you can create a new tuple that contains the desired changes by concatenating or slicing the original tuple. 

my_tuple = (1, 'hello', 3.14)
new_tuple = (2,) + my_tuple[1:]  # Create a new tuple with the first element changed to 2
print(new_tuple)  # Output: (2, 'hello', 3.14)  

# appending to a tuple
my_tuple = (1, 'hello', 3.14)
new_tuple = my_tuple + (42,)  # Create a new tuple by concatenating the original tuple with a new tuple containing the element to append
print(new_tuple)  # Output: (1, 'hello', 3.14, 42)

# using append() method (not possible with tuples, but you can convert to a list and back to a tuple)
my_tuple = (1, 'hello', 3.14)
temp_list = list(my_tuple)  # Convert tuple to list
temp_list.append(42)  # Append the new element to the list
my_tuple = tuple(temp_list)  # Convert back to tuple    
print(my_tuple)  # Output: (1, 'hello', 3.14, 42)

# += operator (not possible with tuples, but you can create a new tuple by concatenating)
my_tuple = (1, 'hello', 3.14)
my_tuple += (42,)  # Create a new tuple by concatenating the original tuple with a new tuple containing the element to append
print(my_tuple)  # Output: (1, 'hello', 3.14, 42)

#deleting a tuple (not possible, but you can delete the variable that references the tuple)
my_tuple = (1, 'hello', 3.14)
del my_tuple  # This will delete the variable that references the tuple, but the tuple itself will still exist in memory until it is garbage collected
# print(my_tuple)  # This will raise a NameError because the variable my_tuple has been deleted

# removing an element from a tuple (not possible, but you can create a new tuple that excludes the desired element)
my_tuple = (1, 'hello', 3.14)
new_tuple = tuple(x for x in my_tuple if x != 'hello')  # Create a new tuple that excludes the element 'hello'
print(new_tuple)  # Output: (1, 3.14)   

# using remove() method (not possible with tuples, but you can convert to a list and back to a tuple)
my_tuple = (1, 'hello', 3.14)
temp_list = list(my_tuple)  # Convert tuple to list
temp_list.remove('hello')  # Remove the element 'hello' from the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print(my_tuple)  # Output: (1, 3.14)



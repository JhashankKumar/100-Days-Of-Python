# remove elements from a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# using remove() method to remove an item from the list
my_list.remove(2)
print(my_list)  # Output: [1, 3, 4, 5]

my_list.remove(3)
print(my_list)  # Output: [1, 4, 5]

# using pop() method to remove an item at a specific index
my_list.pop(1)
print(my_list)  # Output: [1, 5]    

# using del statement to remove an item at a specific index

my_list = [1, 2, 3, 4, 5]
del my_list[0]
print(my_list)  # Output: [2, 3, 4, 5]

# using del statement to remove a range of items
del my_list[1:3]
print(my_list)  # Output: [2, 5]  

# using clear() method to remove all items from the list
my_list.clear()
print(my_list)  # Output: []

"""
The remove() method removes the first occurrence of the specified item from the list.
The pop() method removes the item at the specified index and returns it.
The del statement can be used to remove an item at a specific index or a range of items.
The clear() method removes all items from the list, leaving it empty.
"""
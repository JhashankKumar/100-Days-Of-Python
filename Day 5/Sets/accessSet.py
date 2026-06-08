# using for loop to access elements in a set
my_set = {1, 2, 3}
for element in my_set:
    print(element)  # Output: 1, 2, 3 (the order may vary)

# using in operator to check if an element is in a set
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True
print(4 in my_set)  # Output: False

# change items in sets
my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to the set
print(my_set)  # Output: {1, 2, 3, 4}

my_set.remove(2)  # Removing an element from the set
print(my_set)  # Output: {1, 3, 4} 

my_set.discard(5)  # Discarding an element that is not in the set (no error)
print(my_set)  # Output: {1, 3, 4}

"""
Once a set is created, you cannot change its items, but you can add new items.
You can use the add() method to add new items to a set, and the remove() or 
discard() method to remove items from a set.
The remove() method will raise a KeyError if the element is not found in the set, 
while the discard() method will not raise an error if the element is not found.   
"""

"""
indexing and slicing are not supported in sets because sets are unordered collections of
unique elements.Since sets do not maintain any specific order, you cannot access elements by 
their position (index) or slice them like you would with lists or tuples. 
If you need to access elements in a set, you can convert it to a list or tuple first, 
but keep in mind that the order of elements may not be the same as the original set. 
Here is an example of how to access elements in a set by converting it to a list: 
"""
my_list = list(my_set)
print(my_list)  # Output: [1, 3, 4] (the order may vary)
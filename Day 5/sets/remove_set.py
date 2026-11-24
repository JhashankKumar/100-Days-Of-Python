# You can use the add() method to add new items to a set, and the remove() or discard() method to remove items from a set.

my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to the set
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)  # Removing an element from the set
print(my_set)  # Output: {1, 3, 4}  

my_set.discard(5)  # Discarding an element that is not in the set (no error)
print(my_set)  # Output: {1, 3, 4}  

my_set.discard(3)  # Discarding an element that is in the set
print(my_set)  # Output: {1, 4}

"""
The remove() method will raise a KeyError if the element is not found in the set, 
while the discard() method will not raise an error if the element is not found.   
"""

# You can also use the pop() method to remove and return an arbitrary element from the set.

"""
Note: Sets are unordered, so when using the pop() method, 
you do not know which item that gets removed.
"""

fruit_set = {"apple", "banana", "cherry"}
removed_fruit = fruit_set.pop()  # Removing an arbitrary element from the set
print(removed_fruit)  # Output: 'apple' (the output may vary since sets are unordered)
print(fruit_set)  # Output: {'banana', 'cherry'}

# To remove all items from a set, you can use the clear() method.
fruit_set.clear()  # Removing all elements from the set
print(fruit_set)  # Output: set()

# If you want to delete the set completely, you can use the del keyword.
my_set = {1, 2, 3}
del my_set  # Deleting the set completely
# print(my_set)  # This will raise a NameError since my_set is deleted
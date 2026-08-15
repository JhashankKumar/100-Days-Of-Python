# Once a set is created, you cannot change its items, but you can add new items.

my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to the set
print(my_set)  # Output: {1, 2, 3, 4}

# update a set with multiple elements using the update() method
my_set.update([5, 6])  # Adding multiple elements to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

fruit_set = {"apple", "banana", "cherry"}
tropical_fruits = {"mango", "pineapple", "papaya"}
fruit_set.update(tropical_fruits)  # Adding elements from another set
print(fruit_set)  
# Output: {'apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'} (the order may vary)  

# adding any iterable (like a list, tuple, dictionary or set) to a set using the update() method
my_set = {1, 2, 3}
my_set.update([4, 5])  # Adding elements from a list
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.update((6, 7))  # Adding elements from a tuple
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}
my_set.update({8, 9})  # Adding elements from another set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_dict = {"a": 1, "b": 2}
my_set.update(my_dict)  # Adding keys from a dictionary
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b'} (the order may vary)

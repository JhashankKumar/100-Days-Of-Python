# frozen set is a built-in data type in Python that represents an immutable set.
# It is similar to a regular set, but once created, its elements cannot be modified, added, or removed. 
# A frozen set is created using the frozenset() function. 

# Example of creating a frozen set
frozen_set1 = frozenset([1, 2, 3, 4, 5])
print("Frozen set 1:", frozen_set1) 

# Example of creating a frozen set from a regular set
regular_set = {6, 7, 8, 9, 10}
frozen_set2 = frozenset(regular_set)
print("Frozen set 2:", frozen_set2)

# Example of creating a frozen set from a tuple
tuple1 = (11, 12, 13, 14, 15)
frozen_set3 = frozenset(tuple1)
print("Frozen set 3:", frozen_set3) 

# Example of creating a frozen set from a string
string1 = "Hello"
frozen_set4 = frozenset(string1)
print("Frozen set 4:", frozen_set4)

# Example of creating a frozen set from a list
list1 = [16, 17, 18, 19, 20]
frozen_set5 = frozenset(list1)
print("Frozen set 5:", frozen_set5) 

# Example of creating a frozen set from a dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
frozen_set6 = frozenset(dict1)
print("Frozen set 6:", frozen_set6) 

"""
Since frozen sets are immutable, they do not have methods that modify the set, such as add(), remove(), 
or clear().However, they do support methods that return new sets based on the original frozen set, 
such as union(), intersection(), difference(), and symmetric_difference(). These methods can be used to 
perform set operations with other sets, including other frozen sets, regular sets, and even other data types 
like tuples and lists.
"""

# Example of using union() method with frozen sets
frozen_set7 = frozenset([1, 2, 3])
frozen_set8 = frozenset([3, 4, 5])
union_frozen_sets = frozen_set7.union(frozen_set8)
print("Union of frozen_set7 and frozen_set8:", union_frozen_sets)

# Example of using intersection() method with frozen sets
intersection_frozen_sets = frozen_set7.intersection(frozen_set8)
print("Intersection of frozen_set7 and frozen_set8:", intersection_frozen_sets) 

# Example of using difference() method with frozen sets
difference_frozen_sets = frozen_set7.difference(frozen_set8)
print("Difference of frozen_set7 and frozen_set8:", difference_frozen_sets)

difference_frozen_sets2 = frozen_set8.difference(frozen_set7)
print("Difference of frozen_set8 and frozen_set7:", difference_frozen_sets2)

# Example of using symmetric_difference() method with frozen sets
symmetric_difference_frozen_sets = frozen_set7.symmetric_difference(frozen_set8)
print("Symmetric difference of frozen_set7 and frozen_set8:", symmetric_difference_frozen_sets) 

# Example of using union() method with frozen sets and other data types
tuple2 = (5, 6, 7)
list2 = [8, 9, 10]
union_frozen_set_tuple = frozen_set7.union(tuple2)
print("Union of frozen_set7 and tuple2:", union_frozen_set_tuple)
union_frozen_set_list = frozen_set7.union(list2)
print("Union of frozen_set7 and list2:", union_frozen_set_list)

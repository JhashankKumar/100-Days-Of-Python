"""
Frozenset Methods
Being immutable means you cannot add or remove elements. However, 
frozensets support all non-mutating operations of sets.

Method	                Shortcut	Description	Try it
copy()	 	                        Returns a shallow copy	
difference()	               -	Returns a new frozenset with the difference	
intersection()	               &	Returns a new frozenset with the intersection	
isdisjoint()	                 	Returns True if there is NO intersection between two frozensets	
issubset()	              <= / <	Returns True if this frozenset is a (proper) subset of another	
issuperset()	           >= / >	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	       ^	Returns a new frozenset with the symmetric differences	
union()	                       |	Returns a new frozenset containing the union	
"""

# Here are some examples of using frozenset methods:
# Creating two frozensets
frozenset1 = frozenset([1, 2, 3, 4])
frozenset2 = frozenset([3, 4, 5, 6])

# Using the union() method
union_set = frozenset1.union(frozenset2)
print(union_set)  # Output: frozenset({1, 2, 3, 4, 5, 6})

# Using the intersection() method
intersection_set = frozenset1.intersection(frozenset2)
print(intersection_set)  # Output: frozenset({3, 4})

# Using the difference() method
difference_set = frozenset1.difference(frozenset2)
print(difference_set)  # Output: frozenset({1, 2})

# Using the symmetric_difference() method
symmetric_difference_set = frozenset1.symmetric_difference(frozenset2)
print(symmetric_difference_set)  # Output: frozenset({1, 2, 5, 6})

# Using the issubset() method
print(frozenset1.issubset(union_set))  # Output: True

# Using the issuperset() method
print(union_set.issuperset(frozenset1))  # Output: True 

# Using the isdisjoint() method
print(frozenset1.isdisjoint(frozenset2))  # Output: False

# Using the copy() method
frozenset_copy = frozenset1.copy()
print(frozenset_copy)  # Output: frozenset({1, 2, 3, 4})    

print (frozenset1 is frozenset_copy)  # Output: False (they are different objects)
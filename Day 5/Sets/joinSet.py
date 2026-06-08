# Join sets have several methods to combine sets, such as union(), intersection(), difference(), and symmetric_difference().    

"""
- The union() method returns a new set that contains all the elements from both sets.
- The intersection() method returns a new set that contains only the elements that are present in both sets.
- The difference() method returns a new set that contains the elements that are present in the first set but not in the second set.
- The symmetric_difference() method returns a new set that contains the elements that are present in either of the sets, but not in both sets.
"""

# Example of union() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set) 

# Example of intersection() method
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Example of difference() method
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

difference_set2 = set2.difference(set1)
print("Difference of set2 and set1:", difference_set2)

# Example of symmetric_difference() method
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# using the operator | for union
union_set_operator = set1 | set2
print("Union of set1 and set2 using operator |:", union_set_operator)   

# using the operator & for intersection
intersection_set_operator = set1 & set2
print("Intersection of set1 and set2 using operator &:", intersection_set_operator) 

# using the operator - for difference
difference_set_operator = set1 - set2
print("Difference of set1 and set2 using operator -:", difference_set_operator)

difference_set_operator2 = set2 - set1
print("Difference of set2 and set1 using operator -:", difference_set_operator2)    

# using the operator ^ for symmetric difference
symmetric_difference_set_operator = set1 ^ set2
print("Symmetric difference of set1 and set2 using operator ^:", symmetric_difference_set_operator)


"""
These | & - ^ operators are shorthand for the union(), intersection(), difference(), and 
symmetric_difference() methods, respectively. They provide a more concise way to perform set operations.   
"""

# joining multiple sets using union() method and operator |
"""
The  | operator only allows you to join sets with sets, 
and not with other data types like you can with the  union() method.
"""
set3 = {5, 6, 7}
union_multiple_sets = set1.union(set2, set3)
print("Union of set1, set2, and set3:", union_multiple_sets)
union_multiple_sets_operator = set1 | set2 | set3
print("Union of set1, set2, and set3 using operator |:", union_multiple_sets_operator)

# joining tuple and list with sets using union() method
tuple1 = (7, 8, 9)
list1 = [10, 11, 12]
union_with_tuple_list = set1.union(tuple1, list1)
print("Union of set1 with tuple and list:", union_with_tuple_list)

union_with_tuple_list_operator = set1 | set(tuple1) | set(list1)
print("Union of set1 with tuple and list using operator |:", union_with_tuple_list_operator)


"""
update() method is used to update a set with the union of itself and another set. 
It modifies the original set in place, rather than creating a new set.
"""
# Example of update() method
fruit_set = {"apple", "banana", "cherry"}
vegetable_set = {"carrot", "broccoli", "spinach"}
print("Fruit set before update:", fruit_set)
fruit_set.update(vegetable_set)
print("Fruit set after update with vegetable set:", fruit_set)  


"""
Union() and update() methods can also take multiple sets as arguments, 
allowing you to combine more than two sets at once.
Both will add all the unique elements from the provided sets to the original set.(discarding duplicates)
"""

# difference_update() method is used to update a set with the difference of itself and another set.
# Example of difference_update() method
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A before difference_update:", set_a)
set_a.difference_update(set_b)
print("Set A after difference_update with Set B:", set_a)   

set_c = {1, 2, 3, 4, 5}
set_d = {4, 5, 6, 7, 8}
print("Set C before difference_update:", set_c)
set_d.difference_update(set_c)
print("Set D after difference_update with Set C:", set_d)

value_set = { 0, True, "Hello", 3.14 }
other_set = { 1, False, "World", 2.71 }
print("Value set before intersection_update:", value_set)
value_set.intersection_update(other_set)
print("Value set after intersection_update with other set:", value_set)

value_set2 = { 0, True, "Hello", 3.14 }
other_set2 = { 1, False, "World", 2.71 }    
print("Other set before difference_update:", other_set2)
other_set2.difference_update(value_set2)
print("Other set after difference_update with value set:", other_set2)

"""
The intersection_update() method is used to update a set with the intersection of itself and another set.
It modifies the original set in place, rather than creating a new set.
The difference_update() method is used to update a set with the difference of itself and another set.
It modifies the original set in place, rather than creating a new set.
"""

# symmetric_difference_update() method is used to update a set with the symmetric difference of itself and another set.
# Example of symmetric_difference_update() method
set_x = {1, 2, 3, 4, 5}
set_y = {4, 5, 6, 7, 8}
print("Set X before symmetric_difference_update:", set_x)
set_x.symmetric_difference_update(set_y)
print("Set X after symmetric_difference_update with Set Y:", set_x)

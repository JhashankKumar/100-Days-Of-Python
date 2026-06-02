# Copy a List 

# You can copy a list by making a slice that includes the entire original list.
# Make a copy of the list by slicing it from beginning to end.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods) 

# We can also use the copy() method to make a copy of a list.
"""
copy method in Python is used to create a shallow copy of a list. 
It returns a new list that is a copy of the original list. 
The syntax for using the copy() method is as follows:  
new_list = original_list.copy()
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods.copy()
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods)

my_foods.append('cannoli')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods)

# The copy() method creates a new list that is independent of the original list. 
# Changes made to the original list will not affect the copied list, and vice versa.

# using List comprehension to copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']  
friend_foods = [food for food in my_foods]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods) 

"""
using List comprehension to copy a list is a concise way to create a new list based on the original list. 
It iterates through each element in the original list (my_foods) and creates a new list (friend_foods) 
that contains the same elements. This method is also independent of the original list, 
so changes made to one list will not affect the other list. 
"""

# using the list() function to copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = list(my_foods)
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods) 

"""
using the list() function to copy a list is another way to create a new list that is a copy of the original list. 
The list() function takes an iterable (in this case, the original list my_foods) and returns a new list 
containing the same elements. This method is also independent of the original list, so changes made to 
one list will not affect the other list.
""" 

# using List comprehension to copy a list with a condition
my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
friend_foods = [food for food in my_foods if food != 'ice cream']
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods) 


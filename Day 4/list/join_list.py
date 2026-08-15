# Join Two or More Lists 
# You can use the + operator to join two or more lists.
# Start with two separate lists.
list_1 = ['mohamed', 'ahmed', 'ali']
list_2 = ['sara', 'nour', 'laila']
# Join the lists together.
combined_list = list_1 + list_2
print(combined_list)

# You can also use the extend() method to add all the items in one list to the end of another list.
list_1 = ['mohamed', 'ahmed', 'ali']
list_2 = ['sara', 'nour', 'laila']
list_1.extend(list_2)
print(list_1)

my_foods = ['pizza', 'falafel', 'carrot cake']
# Make a copy of the list of foods.
friend_foods = my_foods[:]
# Add a new food to the original list.
my_foods.append('cannoli')
# Add a different food to the friend's list.
friend_foods.append('ice cream')
# Show that these lists are now different.
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods) 

# using for loop to copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = []
for food in my_foods:
    friend_foods.append(food)
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")  
print(friend_foods)
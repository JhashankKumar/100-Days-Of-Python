# loop through a list
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)  # Output: 1 2 3 4 5

# using enumerate() function to get the index and value of each item in the list
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")  # Output: Index: 0, Item: 1 ... Index: 4, Item: 5

my_list2 = ["a", "b", "c", "d", "e"]
for index, item in enumerate(my_list2):
    print(f"Index: {index}, Item: {item}")  # Output: Index: 0, Item: a ... Index: 4, Item: e  

# using range() function to loop through the list by index
for i in range(len(my_list)):
    print(my_list[i])  # Output: 1 2 3 4 5

# using list comprehension to loop through the list and create a new list
squared_list = [item ** 2 for item in my_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

my_list3 = ["apple", "banana", "cherry"]
print(my_list3)  # Output: ['apple', 'banana', 'cherry']
upper_list = [item.upper() for item in my_list3]
print(upper_list)  # Output: ['APPLE', 'BANANA', 'CHERRY']

# while loop to loop through a list
i = 0
while i < len(my_list):
    print(my_list[i])  # Output: 1 2 3 4 5
    i += 1

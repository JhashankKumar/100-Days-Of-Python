# loop through a tuple
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

# loop through a tuple with index
my_tuple = (1, 2, 3, 4, 5)
for index, item in enumerate(my_tuple):
    print(f"Index: {index}, Item: {item}")

# loop through a tuple with a while loop
my_tuple = (1, 2, 3, 4, 5)
index = 0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1

# Loop Through the Index Numbers
#You can also loop through the tuple items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.

my_tuple = (1, 2, 3, 4, 5)
for i in range(len(my_tuple)):
    print(f"Index: {i}, Item: {my_tuple[i]}")





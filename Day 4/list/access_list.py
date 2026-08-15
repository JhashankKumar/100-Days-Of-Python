# Accessing list items
my_list = [1, 2, 3, 'Hello', [4, 5]]
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'Hello'
print(my_list[4])  # Output: [4, 5]

# Negative indexing
print(my_list[-1])  # Output: [4, 5]
print(my_list[-2])  # Output: 'Hello'
print(my_list[-5])  # Output: 1 

# Range of indexes
print(my_list[0:3])  # Output: [1, 2, 3]
print(my_list[1:4])  # Output: [2, 3, 'Hello']
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[2:])   # Output: [3, 'Hello', [4, 5]]

"""
In Range of indexes, the first index is included, but the second index is not included.
If we omit the first index, it is considered as 0. 
If we omit the second index, it is considered as the length of the list. 
"""

# Range of negative indexes
print(my_list[-4:-1])  # Output: [2, 3, 'Hello']
print(my_list[-3:])    # Output: [3, 'Hello', [4, 5]]
print(my_list[:-2])    # Output: [1, 2, 3] 

# Check if an item exists in the list
print(2 in my_list)  # Output: True
print('Hello' in my_list)  # Output: True
print(10 in my_list)  # Output: False
print(5 in my_list)  # Output: False
print([4, 5] in my_list)  # Output: True

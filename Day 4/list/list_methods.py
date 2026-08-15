"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""

# using the append() method to add an element to the end of a list
my_list = ['apple', 'banana', 'cherry']
my_list.append('orange')
print(my_list)

# using the insert() method to add an element at a specific position in a list
my_list = ['apple', 'banana', 'cherry']
my_list.insert(1, 'orange')
print(my_list)  


# using the remove() method to remove an element from a list
my_list = ['apple', 'banana', 'cherry']
my_list.remove('banana')
print(my_list) 

# using the pop() method to remove an element from a list by index
my_list = ['apple', 'banana', 'cherry']
my_list.pop(1)
print(my_list)  

# using the clear() method to remove all elements from a list
my_list = ['apple', 'banana', 'cherry']
my_list.clear()
print(my_list)

# using the count() method to count the number of occurrences of an element in a list
my_list = ['apple', 'banana', 'cherry', 'apple']
count_apple = my_list.count('apple')
print(count_apple)

# using the index() method to find the index of the first occurrence of an element in a list
my_list = ['apple', 'banana', 'cherry']
index_banana = my_list.index('banana')
print(index_banana)

# using the reverse() method to reverse the order of a list
my_list = ['apple', 'banana', 'cherry']
my_list.reverse()   
print(my_list)

# using the sort() method to sort a list in ascending order
my_list = ['banana', 'apple', 'cherry']
my_list.sort()
print(my_list)

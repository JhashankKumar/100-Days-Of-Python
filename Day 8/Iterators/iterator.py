"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you 
can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
"""

# Example of an iterator
# Creating an iterator from a list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
# Getting an iterator using iter()
my_iter = iter(my_list)
print("Iterator:", my_iter)

# Iterating through the elements using next()
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

"""
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
"""

# Example of an iterable
# Creating a list (iterable)
fruits = ["apple", "banana", "cherry"]
# Getting an iterator from the list
fruit_iter = iter(fruits)
# Iterating through the elements using next()
print(next(fruit_iter))  # Output: apple
print(next(fruit_iter))  # Output: banana
print(next(fruit_iter))  # Output: cherry
# print(next(fruit_iter))  # Raises StopIteration exception since there are no more elements

# iterators can also be created from other iterable objects like tuples, sets, and dictionaries

# Example of an iterator from a tuple
my_tuple = (10, 20, 30)
tuple_iter = iter(my_tuple)
print(next(tuple_iter))  # Output: 10
print(next(tuple_iter))  # Output: 20

# Example of an iterator from a set
my_set = {100, 200, 300}
set_iter = iter(my_set)
print(next(set_iter))  # Output: 100 (order may vary)
print(next(set_iter))  # Output: 200 (order may vary)

# Example of an iterator from a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
dict_iter = iter(my_dict)
print(next(dict_iter))  # Output: a (order may vary)
print(next(dict_iter))  # Output: b (order may vary)

# Iterator through string
my_string = "Hello"
string_iter = iter(my_string)
print(next(string_iter))  # Output: H
print(next(string_iter))  # Output: e
print(next(string_iter))  # Output: l


# The for loop actually creates an iterator object and executes the next() method for each loop.

# Example of using a for loop with an iterable
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry


"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods 
__iter__() and __next__() to your object.

As you will learn in the Python Classes/Objects chapter, all classes have a 
function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.

The __next__() method also allows you to do operations, 
and must return the next item in the sequence.    
"""

# Creating an iterator class NumberIterator that returns numbers from 1 to n
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration
        
# Example usage of the NumberIterator class
num_iter = NumberIterator(5)
for num in num_iter:
    print(num)  # Output: 1 2 3 4 5


"""
StopIteration
The example above would continue forever if you had enough next() statements, 
or if it was used in a for loop.

To prevent the iteration from going on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the 
iteration is done a specified number of times:
"""

# creating own for loop using iterators for all data types

class MyForLoop:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)
    
# Example usage of MyForLoop class
my_list = [10, 20, 30]
my_loop = MyForLoop(my_list)
for item in my_loop:
    print(item)  # Output: 10 20 30
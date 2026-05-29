# sort Alphabetically
names = ["Charlie", "Alice", "Bob"]
names.sort()
print(names)  # Output: ['Alice', 'Bob', 'Charlie'] 

# sort in reverse order
names.sort(reverse=True)
print(names)  # Output: ['Charlie', 'Bob', 'Alice']

# sort numbers
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

# sort numbers in reverse order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]    

# custom sorting using key parameter
names = ["Charlie", "Alice", "Bob"]
names.sort(key=len)
print(names)  # Output: ['Bob', 'Alice', 'Charlie']

# custom sorting using lambda function

def sort_by_last_letter(name):
    return name[-1]

names.sort(key=sort_by_last_letter)
print(names)  # Output: ['Charlie', 'Alice', 'Bob']

names.sort(key=lambda name: name[-1])
print(names)  # Output: ['Charlie', 'Alice', 'Bob']

names.sort(key=lambda name: name[-1], reverse=True)
print(names)  # Output: ['Bob', 'Alice', 'Charlie']

names.sort(key=lambda name: name[-1], reverse=False)
print(names)  # Output: ['Charlie', 'Alice', 'Bob'] 

names.sort(key=lambda name: name[1])
print(names) 
""" Output: ['Charlie', 'Alice', 'Bob'] because the second letter of 'Charlie' is 'h', 
the second letter of 'Alice' is 'l', and the second letter of 'Bob' is 'o'."""

def sort_numbers_by_last_digit(num):
    return num % 10

numbers = [10, 29, 37, 43, 54, 65, 76, 87, 98, 109]
numbers.sort(key=sort_numbers_by_last_digit)
print(numbers)  
# Output: [10, 43, 54, 65, 76, 37, 87, 98, 109, 29] because the last digit of 10 is 0, the last digit of 43 is 3, and so on.

# case sensitive sorting
names = ["Charlie", "alice", "Bob"]
names.sort()
print(names)  
# Output: ['Bob', 'Charlie', 'alice'] because uppercase letters are sorted before lowercase letters in ASCII values.  

# case insensitive sorting
names.sort(key=str.lower)
print(names)  
# Output: ['alice', 'Bob', 'Charlie'] because the key parameter is set to str.lower, which converts all names to lowercase before sorting, making the sorting case insensitive. 

# reverse() method to reverse the order of the list
names.reverse()
print(names)  # Output: ['Charlie', 'Bob', 'alice'] because the reverse() method reverses the order of the list in place, meaning it modifies the original list.

names.sort(key=str.lower, reverse=True)
print(names)  
# Output: ['Charlie', 'Bob', 'alice'] because the key parameter is set to str.lower, which converts all names to lowercase before sorting, making the sorting case insensitive, and the reverse parameter is set to True, which sorts the list in reverse order.    
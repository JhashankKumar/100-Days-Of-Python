# Changing list items
my_list = ["water", "milk", "juice", "soda", "tea"]
print(my_list)  # Output: ['water', 'milk', 'juice', 'soda', 'tea']
my_list[1] = "coffee"
print(my_list)  # Output: ['water', 'coffee', 'juice', 'soda', 'tea']  

# Changing a range of list items
my_list[2:4] = ["lemonade", "smoothie"]
print(my_list)  # Output: ['water', 'coffee', 'lemonade', 'smoothie', 'tea']

# Replacing a range of list items with fewer items
my_list[1:4] = ["hot chocolate"]
print(my_list)  # Output: ['water', 'hot chocolate', 'tea']

# insert items without replacing existing items
my_list[1:1] = ["espresso", "cappuccino"]
print(my_list)  # Output: ['water', 'espresso', 'cappuccino', 'hot chocolate', 'tea'] 

my_list[2:2] = ["latte"]
print(my_list)  # Output: ['water', 'espresso', 'latte', 'cappuccino', 'hot chocolate', 'tea']

# tricky part of list is that we can replace a range of items with more items, fewer items, or even no items at all.
my_list[1:4] = []
print(my_list)  # Output: ['water', 'hot chocolate', 'tea']


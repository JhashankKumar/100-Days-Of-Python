# looping through a set

fruit_set = {"apple", "banana", "cherry"}
for fruit in fruit_set:
    print(fruit)

# You can also use the in keyword to check if an item exists in a set.
if "banana" in fruit_set:
    print("Banana is in the set.")
else:
    print("Banana is not in the set.")

# You can use the len() function to get the number of items in a set.
print(len(fruit_set))  # Output: 3
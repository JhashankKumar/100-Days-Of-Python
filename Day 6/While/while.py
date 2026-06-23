"""
python has two types of loops: while and for. 
The while loop is used to execute a block of code repeatedly as long as a given condition is true. 
The syntax for a while loop is:
while condition:
    # code block to be executed
"""

# Example 1: Using a while loop to print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1  

# Example 2: Using a while loop to calculate the sum of numbers from 1 to 10
sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
print("Sum of numbers from 1 to 10 is:", sum) 

# Example 3: Using a while loop to find the factorial of a number
factorial = 1
n = 5
while n > 0:
    factorial *= n
    n -= 1
print("Factorial of 5 is:", factorial)


# Note: Be careful to avoid infinite loops by ensuring that the condition will eventually become false.
"""
for example, if you forget to increment the count variable in Example 1, the loop will run indefinitely.
"""

# break statement can be used to exit the loop prematurely when a certain condition is met.

# Example 4: Using a while loop with a break statement
count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
print("Loop ended.")

# continue statement can be used to skip the current iteration and move to the next iteration of the loop.

# Example 5: Using a while loop with a continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)  # This will print only odd numbers from 1 to 9

# Example 6: Using a while loop with an else clause
count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully.")

# Note: The else clause in a while loop is executed when the loop condition becomes false, 
# but not when the loop is terminated by a break statement.
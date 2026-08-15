""" Assignment operators are used to assign values to variables. 
They are a combination of an arithmetic operator and the assignment operator (=). 
Here are some common assignment operators in Python:  
=   : Assigns a value to a variable
+=  : Adds a value to the variable and assigns the result back to the variable
-=  : Subtracts a value from the variable and assigns the result back to the variable
*=  : Multiplies the variable by a value and assigns the result back to the variable
/=  : Divides the variable by a value and assigns the result back to the variable
//= : Performs floor division on the variable by a value and assigns the result back to the variable
%=  : Takes the modulus of the variable by a value and assigns the result back to the variable
**= : Raises the variable to the power of a value and assigns the result back to the variable
<<= : Performs left bitwise shift on the variable by a value and assigns the result back to the variable
>>= : Performs right bitwise shift on the variable by a value and assigns the result back to the variable
&=  : Performs bitwise AND on the variable by a value and assigns the result back to the variable
|=  : Performs bitwise OR on the variable by a value and assigns the result back to the variable
^=  : Performs bitwise XOR on the variable by a value and assigns the result back to the variable
:=  : Assigns a value to a variable (used in Python 3.8 and later for assignment expressions)
""" 

# Example usage of assignment operators
x = 10  # Using the = operator to assign a value to x
print(x)  # Output: 10  

x += 5  # Using the += operator to add 5 to x and assign the result back to x
print(x)  # Output: 15  

x *= 2  # Using the *= operator to multiply x by 2 and assign the result back to x
print(x)  # Output: 30

x /= 3  # Using the /= operator to divide x by 3 and assign the result back to x
print(x)  # Output: 10.0

x //= 3  # Using the //= operator to perform floor division on x by 3 and assign the result back to x
print(x)  # Output: 3.0

x %= 2  # Using the %= operator to take the modulus of x by 2 and assign the result back to x
print(x)  # Output: 1.0

x **= 3  # Using the **= operator to raise x to the power of 3 and assign the result back to x
print(x)  # Output: 1.0 

x <<= 2  # Using the <<= operator to perform left bitwise shift on x by 2 and assign the result back to x
print(x)  # Output: 4.0

x >>= 1  # Using the >>= operator to perform right bitwise shift on x by 1 and assign the result back to x
print(x)  # Output: 2.0

x &= 1  # Using the &= operator to perform bitwise AND on x by 1 and assign the result back to x
print(x)  # Output: 0.0

x |= 1  # Using the |= operator to perform bitwise OR on x by 1 and assign the result back to x
print(x)  # Output: 1.0

x ^= 1  # Using the ^= operator to perform bitwise XOR on x by 1 and assign the result back to x
print(x)  # Output: 0.0

# Using the := operator (assignment expression) to assign a value to a variable within an expression
if (n := 5) > 3:  # Assigning 5 to n and checking if n is greater than 3
    print(f"{n} is greater than 3")  # Output: 5 is greater than 3

"""
The := operator, also known as the walrus operator, allows you to assign a value to a variable as part of an expression. 
This can be useful in situations where you want to use the value of a variable immediately after assigning it, such as in a condition or a loop. 
For example, you can use the walrus operator to read input from the user and assign it to a variable in a single line of code:  
while (user_input := input("Enter something (or 'exit' to quit): ")) != "exit":
    print(f"You entered: {user_input}")

In this example, the walrus operator is used to assign the user's input to the variable user_input and check if it is not equal to "exit" in the same line. This allows the loop to continue until the user types "exit".   
"""


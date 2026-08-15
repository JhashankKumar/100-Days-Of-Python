# Operator Precedence in Python
"""
Operator precedence determines the order in which operators are evaluated in an expression.
In Python, operators have a specific precedence level, which can be found in the official Python documentation.
The operator precedence in Python is as follows (from highest to lowest):
1. Parentheses `()`
2. Exponentiation `**`
3. Unary plus and minus `+x`, `-x`
4. Multiplication, division, floor division, and modulus `*`, `/`, `//`, `%`
5. Addition and subtraction `+`, `-`
6. Bitwise shift operators `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`
11. Identity operators `is`, `is not`
12. Membership operators `in`, `not in`
13. Logical operators `and`, `or`, `not`    
When evaluating an expression, Python will first evaluate the operators with the highest precedence and 
then move down to the lower precedence operators.
For example, in the expression `3 + 4 * 2`, the multiplication operator `*` has a higher precedence than 
the addition operator `+`, so the expression will be evaluated as `3 + (4 * 2)`, resulting in `3 + 8`, which 
equals `11`.
It's important to understand operator precedence to ensure that your expressions are evaluated in the way you 
intend. If you're ever unsure about the order of operations, you can use parentheses to explicitly specify the 
order in which you want the operators to be evaluated. For example, if you want to change the  precedence in 
the expression `3 + 4 * 2` to evaluate the addition first, you can write it as `(3 + 4) * 2`, which will result 
in `7 * 2`, giving you `14`.  
In summary, operator precedence is a crucial concept in Python that determines how expressions are evaluated. 
By understanding the precedence of operators, you can write more complex expressions and ensure that they are 
evaluated correctly. Always remember to use parentheses when in doubt about the order of operations to make 
your code clearer and more readable.    
"""

# Example usage of operator precedence
result = 3 + 4 * 2  # Multiplication has higher precedence than addition
print(result)  # Output: 11
result = (3 + 4) * 2  # Parentheses change the order of evaluation
print(result)  # Output: 14
result = 2 ** 3 * 4  # Exponentiation has higher precedence than multiplication
print(result)  # Output: 32 (2 ** 3 is evaluated first, resulting in 8, and then multiplied by 4)
result = -3 ** 2  # Exponentiation has higher precedence than unary minus
print(result)  # Output: -9 (3 ** 2 is evaluated first, resulting in 9, and then the unary minus is applied)
result = 3 + 4 * 2 ** 2  # Exponentiation has higher precedence than multiplication, which has higher precedence than addition
print(result)  # Output: 19 (2 ** 2 is evaluated first, resulting in 4, then multiplied by 4, resulting in 16, and finally added to 3)  

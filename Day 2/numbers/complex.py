# Complex Numbers in Python
""" A complex number is a number that can be expressed in the form a + bj, where a and b are real numbers, 
and j is the imaginary unit (the square root of -1).
In Python, complex numbers are represented using the built-in complex type"""

# Creating complex numbers
z1 = 2 + 3j
z2 = 1 - 4j
print("z1:", z1)  # Output: z1: (2+3j)
print("z2:", z2)  # Output: z2: (1-4j)

# Accessing real and imaginary parts
print("Real part of z1:", z1.real)  # Output: Real part of z1: 2.0
print("Imaginary part of z1:", z1.imag)  # Output: Imaginary part of z1: 3.0

# Arithmetic operations with complex numbers
# Addition
z3 = z1 + z2
print("z1 + z2:", z3)  # Output: z1 + z2: (3-1j)
# Subtraction
z4 = z1 - z2
print("z1 - z2:", z4)  # Output: z1 - z2: (1+7j)
# Multiplication
z5 = z1 * z2
print("z1 * z2:", z5)  # Output: z1 * z2: (10-5j)
# Division
z6 = z1 / z2
print("z1 / z2:", z6)  # Output: z1 / z2: (-0.2195121951219512+0.9024390243902439j) 

# Conjugate of a complex number
z_conjugate = z1.conjugate()
print("Conjugate of z1:", z_conjugate)  # Output: Conjugate of z1: (2-3j)
# Absolute value (magnitude) of a complex number
z_magnitude = abs(z1)
print("Magnitude of z1:", z_magnitude)  # Output: Magnitude of z1: 3.605551275463989)


# Class Methods 
"""
Methods are functions that belong to a class. They define the behavior of objects created from the class.
In Python, methods are defined using the def keyword inside a class.
The first parameter of a method is always self, which refers to the instance of the class.
"""

# Example of a class with methods
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_age(self):
        return self.age

# Create an instance of the Dog class
dog1 = Dog("Buddy", 3)
# Calling methods
dog1.bark()  # Output: Buddy says Woof!
print(dog1.get_age())  # Output: 3

# Note: All methods must have self as the first parameter.

# methods with parameters

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."

# Create an instance of the Calculator class
calc = Calculator()
# Calling methods with parameters
print(calc.add(5, 3))        # Output: 8
print(calc.subtract(10, 4))  # Output: 6
print(calc.multiply(2, 7))   # Output: 14
print(calc.divide(20, 4))    # Output: 5.0
print(calc.divide(10, 0))    # Output: Cannot divide by zero.

# method accessing properties using self

class CalculatorWithProperties:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b  

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero." 

# Create an instance of the CalculatorWithProperties class
calc_props = CalculatorWithProperties(10, 5)
# Calling methods that access properties using self
print(calc_props.add())        # Output: 15
print(calc_props.subtract())   # Output: 5
print(calc_props.multiply())   # Output: 50
print(calc_props.divide())     # Output: 2.0

# methods can also modify properties of the class instance

class BirthdayPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

person = BirthdayPerson("Alice", 30)
# Calling the method that modifies the age property
person.celebrate_birthday()  # Output: Happy Birthday, Alice! You are now 31 years old.
person.celebrate_birthday()  # Output: Happy Birthday, Alice! You are now 32 years old.

print(person)

# The __str__ method is a special method that allows you to define how an object is represented as a string.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

person1 = Person("Bob", 25)
print(person1)  # Output: Bob is 25 years old.

# deleting methods from a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def custom_method(self):
        print("This is a custom method.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
# Calling the greet method
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
# Calling the custom_method
person1.custom_method()  # Output: This is a custom method.

# Deleting the custom_method from the Person class
del Person.custom_method

# Trying to call the deleted method will raise an AttributeError
try:
    person1.custom_method()  # This will raise an AttributeError
except AttributeError as e:
    print(e)  # Output: 'Person' object has no attribute 'custom_method'
"""
The self Parameter
The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("Alice", 30)
person1.greet()      # Output: Hello, my name is Alice and I am 30 years old.

"""
Note: The self parameter must be the first parameter of any method in the class.
"""
"""
Why Use self?
Without self, Python would not know which object's properties you want to access:

self Does Not Have to Be Named "self"
It does not have to be named self, you can call it whatever you like, 
but it has to be the first parameter of any method in the class:
"""

"""
Note: While you can use a different name, it is strongly recommended to use self as 
it is the convention in Python and makes your code more readable to others.
"""

# calling methods with self parameter

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This car is a {self.make} {self.model}.")

    def update_model(self, new_model):
        self.model = new_model
        print(f"The model has been updated to {self.model}.")

# Create an instance of the Car class
car1 = Car("Toyota", "Corolla")
car1.display_info()  # Output: This car is a Toyota Corolla.
car1.update_model("Camry")  # Output: The model has been updated to Camry.
car1.display_info()  # Output: This car is a Toyota Camry.


# welcome greeting example
class Welcome:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Welcome, {self.name}!")

    def farewell(self):
        print(f"Goodbye, {self.name}!")
        print(self.greet())  # Calling the greet method from within the farewell method

# Create an instance of the Welcome class
welcome1 = Welcome("Bob")
welcome1.greet()      # Output: Welcome, Bob!
welcome1.farewell()   # Output: Goodbye, Bob! followed by Welcome, Bob
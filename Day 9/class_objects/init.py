""" 
what is __init__.py?

All classes have a built-in method called __init__(), 
which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, 
or to perform operations that are necessary when the object is being created.

Note: The __init__() method is called automatically every time the class is 
being used to create a new object.

Why Use __init__()?
Without the __init__() method, you would need to set properties manually for each object:
"""

# Example without __init__() method
class Person:
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object of the Person class
person1 = Person()
# setting properties manually
person1.set_name("Alice")
person1.set_age(30)
# calling the display method
person1.display()  # Output: Name: Alice, Age: 30

# Example with __init__() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object of the Person class
person1 = Person("Alice", 30)
# calling the display method
person1.display()  # Output: Name: Alice, Age: 30

person2 = Person(25, "Bob")  # This will create a person with name 25 and age "Bob"
person2.display()  # Output: Name: 25, Age: Bob

person3 = Person(40, 36)
person3.display()  # Output: Name: 40, Age: 36

# person4 = Person(28) 
""" This will raise an error because the __init__() method expects two arguments (name and age), 
but only one was provided."""

# interchanging the order of arguments will lead to incorrect assignment of properties,
# as the first argument will be assigned to the first parameter and the second argument to the second

# default values can also be assigned to parameters in the __init__() method,
# which allows for the creation of objects with optional properties.

# Example with default values in __init__() method
class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object of the Person class with default values
person1 = Person()
person1.display()  # Output: Name: Unknown, Age: 0

# creating an object of the Person class with custom values
person2 = Person("Alice", 30)
person2.display()  # Output: Name: Alice, Age: 30


# multiple objects of the same class can be created with different properties,
# and each object will have its own copy of the class properties.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# creating multiple objects of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
# calling the display_info method for each object
car1.display_info()  # Output: Car: 2020 Toyota Camry
car2.display_info()  # Output: Car: 2019 Honda Civic

# Note: Each object is independent and has its own copy of the class properties.

# multi parameter __init__() method can also be used to create objects with multiple properties.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

# creating an object of the Student class
student1 = Student("John", 20, "A")
# calling the display_info method
student1.display_info()  # Output: Student: John, Age: 20, Grade: A
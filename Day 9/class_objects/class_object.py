# creating a class

class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method to display person's details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating an object of the Person class
person1 = Person("Alice", 30)
# calling the display method
person1.display()  # Output: Name: Alice, Age: 30

# real world example of a class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# creating an object of the Car class
car1 = Car("Toyota", "Camry", 2020)
# calling the display_info method
car1.display_info()  # Output: Car: 2020 Toyota Camry

# deleting an object
del car1  # This will delete the car1 object from memory

# multiple objects of the same class
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)
car2.display_info()  # Output: Car: 2019 Honda Civic
car3.display_info()  # Output: Car: 2021 Ford Mustang

# Note: Each object is independent and has its own copy of the class properties.


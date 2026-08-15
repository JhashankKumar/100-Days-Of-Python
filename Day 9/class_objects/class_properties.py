"""
Class Properties
Properties are variables that belong to a class. 
They store data for each object created from the class.
"""

# create a class with properties
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")

#Access Properties
print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Corolla

# Modify Properties
car1.model = "Camry"
print(car1.model)  # Output: Camry

# Delete Properties
del car1.model

print(car1.make)  # Output: Toyota
print(car1.model)  # This will raise an AttributeError since model has been deleted

"""
class Properties vs. Instance(Object) Properties

class properties are shared among all instances of the class, 
while instance properties are unique to each object created from the class.

Properties defined inside __init__() belong to each object (instance properties).

Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:
"""

# class properties vs instance properties example
class Car:
    wheels = 4  # class property

    def __init__(self, make, model):
        self.make = make  # instance property
        self.model = model  # instance property


person1 = Car("Toyota", "Corolla")
print(person1.wheels)  # Output: 4 (class property)
print(person1.make)    # Output: Toyota (instance property)

person2 = Car("Honda", "Civic")
print(person2.wheels)  # Output: 4 (class property)
print(person2.make)    # Output: Honda (instance property)


person1.wheels = 6  # This creates an instance property for person1, does not change the class property
print(person1.wheels)  # Output: 6 (instance property)
print(person2.wheels)  # Output: 4 (class property remains unchanged)

Car.wheels = 8  # This changes the class property for all instances that do not have an instance property
print(person1.wheels)  # Output: 6 (instance property remains unchanged)
print(person2.wheels)  # Output: 8 (class property has changed)

# adding new properties to a class
class Car:
    wheels = 4  # class property

    def __init__(self, make, model):
        self.make = make  # instance property
        self.model = model  # instance property

car1 = Car("Toyota", "Corolla")
car1.seat = 5  # Adding a new instance property to car1
print(car1.seat)  # Output: 5 (instance property)   
# Adding a new property to the class
Car.color = "Red"  # Adding a new class property
print(car1.color)  # Output: Red (class property)

car2 = Car("Honda", "Civic")
print(car2.color)  # Output: Red (class property is shared among all instances)
print(car2.seat)  # This will raise an AttributeError since seat is not defined for car2
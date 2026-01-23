# Polymorphism: Polymorphism allows the object of different classes to be treated as object of a common superclass . It provides a way to perform a single action in different forms . Polymorphism is typically achieved through method overriding and interfaces

# Polymorphism means multiple forms


# method overriding :

# method overriding allows a child class to provide a specific implementation of a method that is already defined in the parent class

# base class
class Animal:
    def speak(self):
        return "Sound of the animal"

# Derived class
class Dog(Animal):
    def speak(self):
        return "wooff"    
# Derived class
class Cat(Animal):
    def speak(self):
        return "Meow"
    
## function that demonstrates the polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak()) # wooff
print(cat.speak()) # Meow

animal_speak(dog) # wooff

# ## Polymorphism with functions and method

#base class
class Shape:
    def area(self):
        return "The area of the figure"

# derived class 1
class Rectangle(Shape):
    def __init__(self,width,hight):
        self.width=width
        self.heigth=hight
    def area(self):
        return self.width*self.heigth
    
# Derived class 2
class Circle(Shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14*self.rad*self.rad

# Function that demonstrate the polymorphism

def print_area(obj):
    print(f"The area is the {obj.area()}")               

rectangle=Rectangle(3,4)        
circle=Circle(3)

print_area(rectangle)
print_area(circle)

#polymorphism with abstract base classes
# Abstract Base classes are used to define the methods for a group of the related objects. They can enforce that derived classe implements particular methods , promoting consistency 

from abc import ABC,abstractmethod
# Define an abstract class
 
class Vehicle (ABC):
    @abstractmethod
    def start_engine(self):
        pass

# derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

# derived class 2
class Motercycle(Vehicle):
    def start_engine(self):
        return "Motercycle engine started"       
    
vehicle=[Car(),Motercycle()]
for x in vehicle:
    print(x.start_engine())

# Car engine started
# Motercycle engine started    
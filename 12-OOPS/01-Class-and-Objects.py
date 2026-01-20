# A class is an blue print for creating the objects
class Car:
    pass


# creating the objects of the car
audi=Car()
bmw=Car()
print(type(audi))  # output: <class '__main__.Car'>

print(bmw)  # oupput : <__main__.Car object at 0x7f4c88e87350> car object at the specific memory location


# defining the attribute for the class( not an correct way )
audi.window=4
print(audi.window) # output : 4

print(dir(audi))
# output : ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'window']


# creating the class and its instance variable 
class Dog:
    # Constructor
    def __init__(self, name ,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name} says woof")
        
Dog1 = Dog("buddy",3)
print(Dog1)
print(Dog1.name)
print(Dog1.age)
Dog1.bark()
# Output:        
# <__main__.Dog object at 0x7f553afb9e80>
# buddy
# 3
# buddy says woof  
dog2 =Dog("Lucy",4)
dog2.bark()       




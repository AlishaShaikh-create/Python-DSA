# Magic Methods
# Magic methods in pyhton , also known as dunder methods (double underscore methods) , are the special nethods that start and end with double underscore . These methods enables you to define the behaviour of the objects for built-in operations, such as arithmetic operation, comaprision and more
'''
__init__: Initialize a new instance of a class
__str__: Returs a string representation of the object
__repr__:Returs an official string representation of an object
__len__:Returns the length of the object
__getitems__:Gets the items from the container
__setitems__:Sets an item in a container

'''

class Person:
    pass

person=Person()
print(dir(person))

## Basic Method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
person=Person("Alisha",22)
print(person)        

# Output : <__main__.Person object at 0x7fbe27b6b9e0>

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self): # represent the string representation of the object . __str__ is overwritten .
        return f"{self.name},{self.age} years old" 
    def __repr__(self):
        return f"person name {self.name} , age={self.age} "
         
      
person=Person("Alisha",22)
print(person) 
# Output :Alisha,22 years old

# Magic method for the arithmetic operator

print(1+1)

'''
__add__(self,other):Adds two objects using the + operator
__sub__(self,other):Subtracts two objects using the - operator
__mul__(self,other):Multiplies two objects using the * operator
__truediv__(self,other):Divides two objects using the / operator
__eq__(self,other): Checks if two objects are equal using the == operator
__lt__(self,other):Cheks if one objects is less than another using the < operator.
__gt__
'''
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other): 
        return Vector(self.x+other.x,self.y+other.y) 
    
    def __sub__(self,other):
        return Vector(self.x-other.x , self.y-other.y) 
    
    def __mul__(self,other):
        return Vector(self.x*other.x , self.y*other.y)  
    
    def __truediv__(self,other):
        return Vector(self.x/other.x , self.y/other.y)  
     
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

## create objects of the vector Class
v1=Vector(2,3)    
v2=Vector(4,5)    

print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1/v2)

# output:
# Vector(6,8)
# Vector(-2,-2)
# Vector(8,15)
# Vector(0.5,0.6)


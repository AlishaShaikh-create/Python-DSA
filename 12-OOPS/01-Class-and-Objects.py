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

#Creating the class
# Creating the bank balance 
class Bank:
    # constructor
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} has been deposited. New balance is {self.balance}")    
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")    
        else :
            self.balance-=amount
            print(f"{amount} has been withdrawn. New balanace is {self.balance}")    

    def get_balance(self):
        return self.balance

b1=Bank("Alisha")
print(b1)
print(b1.balance)
print(b1.owner)
b1.deposite(5000)
b1.withdraw(6000)
b1.withdraw(2000)
print(b1.get_balance())

# Output : 
# <__main__.Bank object at 0x7f55bcc72d80>
# 0
# Alisha
# 5000 has been deposited. New balance is 5000
# Insufficient Funds
# 2000 has been withdrawn. New balanace is 3000
# 3000
# alisha           


# deleting the object :
del Dog1      
# print(Dog1.name)

 # Class Properties Vs Instance Properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

# Note : adding property this way only add the property to the specific object

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)




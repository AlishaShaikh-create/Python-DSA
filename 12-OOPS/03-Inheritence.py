# Inheritence : It allow a  class to inherit attribute and moethde from the other class

# Single Inheritence :
# parent class :
class Car:
    def __init__(self, windows, doors ,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
        
    def drive(self):
         print(f"The person will drive the {self.enginetype} car")

car1=Car(4,5,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self, windows, doors, enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving=is_selfdriving
    def selfdriving(self):
        print(f"Tesla support self driving :{self.is_selfdriving}")


tesla1=Tesla(4,5,'electric',True)
tesla1.selfdriving() # Tesla support self driving :True
tesla1.drive() #The person will drive the electric car
            
        
## Mutliple Inheritance:
# Whena a class inherits from more than one base class

#Base class 1
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Sub class must implement this method") 

# Base class 2
class Pet:
    def __init__(self,owner):
        self.owner=owner
        

# Derived class 
class Dog(Animal,Pet):
    def __init__(self, name,owner):
       Animal.__init__(self,name)
       Pet.__init__(self,owner)
       
    def speak(self):
        return f"{self.name} says woof"         

# Create an object
dog=Dog("Buddy", "Alisha")
print(dog.speak())

print(f"owner is {dog.owner}")      


Animal.mro()       
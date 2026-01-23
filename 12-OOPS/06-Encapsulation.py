# Encapsulation is the concept of wrapping data(variables) and methods (functions) together as a single unit . It restricts the direct acces to some of the objects components , which is a means of preventing accidental interference ans misuse of the data

# Encapsulation with Getter and Setter method
## public , private , protected variables or access modifiers


class Person:
    def __init__(self,name,age):
        
        self.age=age # Public Variables
        self.name=name # Public Variables

def get_name(person):
    return person.name
        
p1=Person("Alisha",23)
print(p1.name)
print(p1.age)
print(get_name(p1))


# Private variable
class Person:
    def __init__(self,name,age,gender):   
        self.__age=age #Private Variables
        self.__name=name #Private Variables
        self.gender=gender

def get_name(person):
    return person._Person__name   # way to access the private varible of the class.
     
p1=Person("Alisha",23,"female")
get_name(p1)



# Protected class
class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age) # we did not write the self key word

e=Employee("Alsha",22)
print(e._name)
        
        

# Encapsulation with the getter and setter method

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    # getter method for name
    # -> with the getter method we retrieve the data
    def get_name(self):
        return self.__name
    
    # setter method for name
    # -> with the help of the setter method we set the value to the data 
    def set_name(self,name):
        self.__name=name
    
    # getter method
    def get_age(self):
        return self.__age
    
    # setter method
    def set_age(self,age):
        if age>0:
            self.__age=age
        else :
            print("age cannot be less than zero") 


p=Person("Ruby", 90)

## Access and modify private varible using the getter and setter

print(p.get_name())  # Ruby      
print(p.get_age())   # 90

p.set_age(24)     
print(p.get_age())   # 24


p.set_age(-2)
print(p.get_age()) 

# output : 
# age cannot be less than zero 
# 24
# -> this is the reason why 24 is again getting printed
# get_age() returns the current value of self.__age
# Since the invalid update was rejected, self.__age is still 24
# That’s why you see 24 printed again.
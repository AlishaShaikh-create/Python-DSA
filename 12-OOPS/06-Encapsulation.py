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
        
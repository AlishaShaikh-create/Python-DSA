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
        super().__init__(windows,doors,enginetype) # no need to mention the self keyword
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

# Multiple inheritence
class Employee:
    def __init__(self,name):
        self.name=name


class JobSalary:
    def __init__(self,salary):
        self.salary=salary
        

class EmployeeDetails(Employee,JobSalary):
    def __init__(self,name,salary):
        Employee.__init__(self,name)
        JobSalary.__init__(self,salary)
        
    def printDetails(self):
        return f"The Employee name is {self.name} and her salary is {self.salary}"


em=EmployeeDetails("Alisha", "1cr")   
print(em.name)     
print(em.salary)
print(em.printDetails())          

            
# Multilevel Inheritence : one class derived from the other derived class
class Person:
    def __init__(self,name):
        self.name=name
    
      

class Employee(Person):
      def printName(self):
        return f" name = {self.name}"

class Manager(Employee):
    def manager(self,dept):
        return f" The employee name is {self.name} and his dept is {dept}"
    
mr=Manager("JOY")
print(mr.manager("HR"))   
print(mr.printName())     #  name = JOY   





# Hierarchical Inheritance :multiple classes inherit from the same parent class

class Person:
    def __init__(self, name):
        self.name = name
        
    def printName(self):
        return f"name = {self.name}"
    
   
class Salary(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def showSalary(self):
        return f"Salary = {self.salary}"
        
        
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def info(self):
        return f"name = {self.name}, employee id = {self.emp_id}"

em=Employee("Alisha","12")
print(em.info()) # name = Alisha, employee id = 12                
print(em.printName()) # name = Alisha

s=Salary("Alisha","1cr")
print(s.showSalary()) # Salary = 1cr

    
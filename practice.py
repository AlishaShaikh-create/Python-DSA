class Student :
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def printName(self):
        print("The name is ", self.name)    
    def printMarks(self):
        print("The marks of the student is",self.marks)
        
        
s1 = Student("Alisha",23)            
s1.printName()
s1.printMarks()
        
        
# Getter and Setters 

# Before the getter and setter
class Student :
    def __init__(self,marks):

        self.marks = marks
    def displayDetails(self):
        print("marks",self.marks)

s1 = Student(80)
s1.marks=-50
print(s1.marks)        
                

class Student:
    def __init__(self):
        self.marks = 0
    
    def set_marks(self,marks) :
        if 0 < marks <= 100:
            self.marks = marks
    def get_marks(self):
        print("marks :" ,self.marks)

print("------------")
alisha = Student()
print(alisha.marks)
alisha.set_marks(-50)  
print(alisha.marks)


# Constructor
class Employee:
    def __init__(self):
        self.__salary = 5000
        self.name = "john"
    def setName(self,s):
        self.name = s   
    def setSalary(self,val):
        self.__salary = val
    def getSalary(self):
        return self.__salary 

obj1 = Employee()
print(obj1.getSalary())            
print(obj1.name)  

class Employee:
    def __init__(self):
        pass

s1 = Employee()
print(s1)              

# Copy Constructor 
class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        self.skill=[]
    
    @classmethod
    def from_Student(cls,other):
        new_obj = cls(other.name , other.roll_number)
        new_obj.skill = other.skill.copy()
        
        return new_obj

student1 = Student("Alisha",23)
print(student1.name)
print(student1.roll_number)
print(student1.skill)
student1.skill.append("python")
print(student1.skill)


student2 = Student.from_Student(student1)
print(student2.name)
print(student2.roll_number)
print(student2.skill)

student2.skill.append("java")
print(student2.skill)
print(student1.skill)

    
            
        
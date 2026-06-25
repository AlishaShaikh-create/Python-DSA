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


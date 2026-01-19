# Functions : 
# syntax :
# def function_name(parameter):
#     """Doc String"""
#     # function body
#     return expression

#function 
def even_or_odd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

even_or_odd(24)
even_or_odd(23)            

# function with the multiple parameter
def add(a,b):
    sum=a+b
    return sum

print(add(2,4))

#default parameter :
def greet(name="Guest" ):
    print(f"hello {name}")
    
greet("Alisha")    


#variable length arguments 

#Positional arguments 
def print_numbers(*args):
    for numbers in args:
        print(numbers)

print_numbers(1,2,3,4,5,"Alisha")        

#keyword Arguments 

def print_detail(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        
print_detail(name="Alisha" , age="23")       

# return statement
def multiply(a,b):
    return a*b,a

print(multiply(2,3))
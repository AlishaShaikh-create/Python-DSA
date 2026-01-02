# number = 10
# type(number)
# print(type(number))

# # Taking input from the user

# age = input("Enter your age :")
# print(age)
# print("type of age is", type(age))


# #calculator 

# number1 = int(input("Enter the first number:"))
# number2 = int(input("Enter the second number:"))
# print("Addition :", number1+number2)
# print("Subtraction :", number1-number2)
# print("Multiplication:" , number1*number2)
# print("Devision :" , number1/number2)


# a=10
# b=10
# print(a==b)
# print(type(a==b))
# print(bool())


print("hello world ")

if 5 > 2 :
    print("greater")
else:
    print("smaller")    
    
x=5 
print(x)    

# this is command line in python 
print("python is fun")

print("hello world") ; print("this is Alisha ") ; print (" hello Alisha")

print("hello world")
print("this is Alisha" ,end=" " ) # end to print everything on the same line 
print("I will print on the same line ")
print(3)
print(3+3)
print(5*5)
print("I am " , 35 , "years old")
'''
this is multi line coment 
and it can be used for w
writing
mutiple
lien 
in the 
code
'''

x=5 # this is of type int 
x ='string ' # now x is of type string 
print(x)


name = "Alisha"
number = 5
print(type(name)) # str
print(type(number))  #number

x = "Awesome"
def fun():
    print("python is " , x)

fun()    

# local vs Global variable 

x = "Alisha"
def name():
    x = "peter"
    print("the value of x inside the function is :", x)
name()
print("the value of x outside the function is :", x)


y = 'global'
def name1():
    global y
    y = 'good'
    print(y)
name1()

print(type(y))


# type() to find out the type of variable it is stored
x=1j
print(x)
print(type(x))



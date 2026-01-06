# Lambda Function 
# lambda functions are anonymous function.
# anonymous function = function without the name 
# lambda function can have any number of arguments but only one expression

# the expression is executed and the result is returned

# Syntax
# lambda arguments :expression


def add(a,b):
    return a+b
print(add(2,3))


add1=lambda a,b:a+b
print(type(add1))
print(add1(5,6))




def myFunction(n):
    return lambda a : a*n

value=myFunction(2)
print(value(11))

# lambda functions are mostly used with the map() ; filter() ; sort()

# map() - applies a function to all the items in a list 

numbers=[1,2,3,4,5,6]
print(map(lambda x:x**2, numbers))

# output:<map object at 0x7fb4af691810> 
# map uses the lazy loading technique 

list1=list((map(lambda x:x**2, numbers)))
print(list1)


def myfunction(n):
    return lambda a:a*n

value=myFunction(2)
print(value)  

# output: <function myFunction.<locals>.<lambda> at 0x7f291ddd5440>

print(value(11))
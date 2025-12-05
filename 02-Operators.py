# Arithmetic operator
a=10
b=20
print(a + b)  #30
print(a - b)  #-10
print(a * b)   #200
print(a / b)   # 0.5
print(a // b)   #0
print(a % b)   #0
print(a ** b)


#Comparision Operaotr 
a=15
b=13
print(a == b) #false
str1 = "alisha"
str2 = "alish"
print(str1<str2)  #False
print (a and b)



x = True


# print(x > 0 and x < 10)
print(not x)



# Logical operator
# AND (and)  OR (or)  NOT(not)

if 5<8 and 5<10:
    print("true")


# Warlus operator - python3.8 version

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
    
    
# Identity Operator 

# is , is not 

a = [1,2,3]
b=a
print(a is b ) # output : True -> memory refer to the same object 

c=[1,2,3]
print(a is c) # output : False -> return false because the memory reference to different object    
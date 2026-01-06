#Tuples :
# ordered and unchangable collection of element 
# creating the tuple
t1=('apple' , 'banana' , 'grapes ')
print(t1)
print(type(t1))


# if you want to create a tuple with one element it is necessary to add , (comma) or else python will not consider it as tuple

t2=('apple',)
print(t2)
print(type(t2))  #<class 'tuple'>

t2=('apple')
print(t2)
print(type(t2))  #<class 'str'>


#tuples can be created with the tuple constructor
t3=tuple(('a', True,1))
print(t3)

#tuples can be accessed using the index number 
t4=(1,2,3,4,5,6,7,8,9)
print(t4[2])

#accessing all the elements
for i in t4:
    print(i)
    
# to check if the item exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  

# adding element into the tuple using the list
t6 = ("apple", "banana", "cherry")
t7=list(t6)
print(t7)
t7.append("grapes")
print(t7)
t6=tuple(t7)
print(t6)
  

#adding tuples to tuples this is allowed 
t6 = ("apple", "banana", "cherry") 
t7=(1,)
t6=t6+t7
print(t6)


#packing and unpacking the value

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

fruits=('apple','banana','cherry')
green, yellow,red=fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print("The value of red is:")
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#adding the element
t1=(1,2,3)
t2=(3,4,5)
t3=t1+t2
print(t3)

t4=t1*2
print(t4)


print(True == 1)
# output: True
count = 0
x=11
count += (x > 10)  
print(count)
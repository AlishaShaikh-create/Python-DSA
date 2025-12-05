#  List : changable , ordered , different datatype , allow duplicates

thisList=['apple', 1,True]
print(thisList)

#using List Constructor to create the new List 
newList=list(('apple' , 'banana','grapes')) 
print(newList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])  #output: cherry orange kiwi
print(thislist[-4:-1]) #output:orange kiwi melon

if 'apple' in thislist:
    print("yes present")


#Changing item using the index

a=[10,20,30,40]
print(a)    #output: [10,20,30,40]
a[1]=200
print(a)   #output: [10,200,30,40] 

#changing the range of the value
a[1:3]=["alisha" , True]
print(a) #output : [10, alisha, True , 40]

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) #output: ['apple', 'watermelon']


 # ADDING ITEMS TO THE LIST


#insert method : to insert the item at the specific index 
thislist.insert(2, 'grapes')
print(thislist)

# To add item at the end of the list 
#append()
a=[10,20,30,40]
a.append(100)
print(a) #output: [10,20,30,40,100]

# to add item of one list to the another
b=[-1,-2,-3,-4]
a.extend(b)
print(a)  #output: [10, 20, 30, 40, 100, -1, -2, -3, -4]
print(b) #output: [-1,-2,-3,-4]


# The extend method does not only have to add the list it can even add list tupes and set and dictionaries
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# REMOVING ITEMS FROM THE LIST 


#remove
a = [10, 20, 30 , 40 , 50]
a.remove(20)
print(a)

# a.remove(100)
# print(a)  # output : ValueError: list.remove(x): x not in list


# pop():
# -> return the deleted element 
# -> if index is not given the delete the last element

print(a.pop(0)) #output : 10

print(a)  #output: [30, 40, 50]


#del
# -> do not return the deleted element 
a =[1,2,3,4,5]
del a[1]
print(a) #output : [1, 3, 4, 5]

# -> the del keyword even can delete the complete list


# del a
# print(a) # NameError: name 'a' is not defined


#Looping through the list 

thislist=['apple', 'mango','banana', 'grapes']
for x in thislist:
    print(x)

for i in thislist[2:5]:
    print(i)    
    
for i in range(len(thislist)):
    print(thislist[i])    
    
z=0
while z < len(thislist):
    print(thislist[z])   
    z+=1 
    
    
# list compreshension    
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist  ]

# fruits that contain letter a in the list  and keep it in the new list 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"] 
newarr=[]
for i in range(len(fruits)):
    if 'a' in fruits[i]:
        newarr.append(fruits[i])
print(newarr)

# shorter version to do this

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#sort the list in alphabetically and in ascending order
a=[103,20,3320,440]
a.sort()
print(a)


# to sort in descending order
a.sort(reverse=True)
print(a)
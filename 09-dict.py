# dictionaries in python

# Dictionary items are ordered, changeable, and do not allow duplicates.

student={
    "name":"alisha",
    "rollnumber":12
}
print(student)
print(type(student))

# accessing the element using the dictionary
print(student["name"])

# to define the length of the dictionaries 
print(len(student))

student={
     "name":["alisha", "sana" , "noorein" , "neha"],
    "rollnumber":12 
    
}

print(student)


# using the dict() to create the dictionary

thisdict=dict(name="Alisha" , age=23)
print(thisdict)

# Accessing the element of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

b=thisdict['brand']
print(b)

# get() also get the similar result of the above code
c=thisdict.get('brand')
print(c)

# to get the list of all the keys we use the keys()
d=thisdict.keys()
print(d)

#Adding the element in the dictionary
thisdict['color']= 'white'
print(thisdict)
print(thisdict.keys())

# printing the values 
value=thisdict.values()
print(value)

# to get the items in the list 
print(thisdict.items())

# to check if the key exist
if 'model' in thisdict:
    print('exist')
    
# changing the value 

thisdict["year"]=2025
print(thisdict)    

# Remove the items from dict
# 1 .pop()
thisdict.pop('year')
print(thisdict)
# 2 popitem()
# remove the last items 
thisdict.popitem()
print(thisdict)

#3. to delete the dictionary
# del thisdict
# print(thisdict)

#4. to clear the dictionary
thisdict.clear()

# to iterate through the dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# to print the keys
for x in thisdict:
  print(x)

# to print the value
for i in thisdict:
  print(thisdict[i])  
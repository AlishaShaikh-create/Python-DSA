# dictionaries in python

# Dictionary items are ordered, changeable, and do not allow duplicates.

student={
    "name":"alisha",
    "rollnumber":12
}
print(student) # {'name': 'alisha', 'rollnumber': 12}
print(type(student)) # <class 'dict'>

# accessing the element using the dictionary
print(student["name"]) # alisha

# to define the length of the dictionaries 
print(len(student)) # 2

student={
     "name":["alisha", "sana" , "noorein" , "neha"],
    "rollnumber":12 
    
}

print(student) 
# {'name': ['alisha', 'sana', 'noorein', 'neha'], 'rollnumber': 12}


# using the dict() to create the dictionary

thisdict=dict(name="Alisha" , age=23)
print(thisdict) # {'name': 'Alisha', 'age': 23}

# Accessing the element of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

b=thisdict['brand']
print(b) # Ford

# get() also get the similar result of the above code
c=thisdict.get('brand')
print(c) # Ford


# to get the list of all the keys we use the keys()
d=thisdict.keys()
print(d) # dict_keys(['brand', 'model', 'year'])

#Adding the element in the dictionary
thisdict['color']= 'white'
print(thisdict)
print(thisdict.keys()) # dict_keys(['brand', 'model', 'year', 'color'])

# printing the values 
value=thisdict.values()
print(value) # dict_values(['Ford', 'Mustang', 1964, 'white'])

# to get the items in the list 
print(thisdict.items()) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'white')])

# to check if the key exist
if 'model' in thisdict:
    print('exist')
# output : exist  
  
# changing the value 

thisdict["year"]=2025
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2025, 'color': 'white'}   

# Remove the items from dict
# 1 .pop()
thisdict.pop('year')
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'color': 'white'}


# 2 popitem()
# remove the last items 
thisdict.popitem()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}

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
  
# output : 
# brand
# model
# year  

# to print the value
for i in thisdict:
  print(thisdict[i]) 
  
# output:
# Ford
# Mustang
# 1964   
  
 # the value of the dictionary 
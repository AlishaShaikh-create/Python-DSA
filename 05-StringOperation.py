# String Datatype

# All the operations regarding string 

a = "hello world!"
print(a[1])
print(a[0])    

# looping through string

for i in "Apple":
    print(i)


# Length of the String 

a = "Alisha"
print(len(a))  # output: 6


# To check if the phrase or character is present in the string or not 

# Return True or False 

x = "The best thing in life is free"
print( "free" in x)   # output: True

# not in -> To check if the thing is not present 
print ("alisha" not in x)  # output : True 


#Slicing 

b="Hello World!"
print(b[2:7])

# negative indexing 

z = "Hello, World!"
print(z[-5:-2])


#String Methods


string="    Alisha        Shaikh       "
print(string.upper())
print(string.lower())
print(string.strip())
print(string.replace("Alisha" , "Tohid"))
print(string.split(','))


#format string or the f-string

age=23
txt=f" my name is Alisha and age is {age}"
print(txt)



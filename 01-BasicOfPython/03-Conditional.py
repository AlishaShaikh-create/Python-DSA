#CONDITIONAL STATEMENT


#if statement
age =20
if age>=18:
    print("you are allowed to vote")
    

#if-else statement
age =16
if age>=18:
    print("ypu are allowed to vote")   
else:
    print("you are minor")     


# if elif else 

age =20 
if age<13:
    print("you are child")
elif age<18:
    print("you are teenager")        
else:
    print("you are adult")  
    
    
number = int(input("Enter the number :"))      
if number <0:
    print("Number is nagative") 
else :
    if number%2==0:
         print("Number is even")
    else :
        print("number is odd") 
   

# Year leap year or not
year = int(input("Enter the year :"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year, "it is leap year")
        else:
            print(year, "not a leap year")    
    else:
        print(year , "leap year ")
else:
    print(year,"not a leap year")                
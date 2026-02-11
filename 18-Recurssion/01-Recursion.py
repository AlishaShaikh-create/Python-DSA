# RECURSION

def printNum(num):
    print(num)

printNum(5)    

# Now we need to use the above function to print the number from 5 to 1

# one way to do this is 

# printNum(5)
# printNum(4)
# printNum(3)
# printNum(2)
# printNum(1)

def PrintNumFive(num):
    print(num)
    PrintNumFour(num-1)

def PrintNumFour(num):
    print(num)
    PrintNumThree(num-1)

def PrintNumThree(num):
    print(num)
    PrintNumTwo(num-1)

def PrintNumTwo(num):
    print(num)
    PrintNumOne(num-1)

def PrintNumOne(num):
    print(num)
    

PrintNumFive(5)    
#output:
# 5
# 4
# 3
# 2
# 1
 
# Recursion :
# 1. We can call a function inside the another function
# 2.A Function stays in the memory until it  gets fully Excuted

# most importantly  we are doing the similar kind of work in each of the following function  

def printNum(num):
   
        print(num)
        return printNum(num-1)     

# printNum(5) # Error : RecursionError: maximum recursion depth exceeded  

# here it does not know the base condition where to stop 

def printNum(num):
    if num>=1:
        print(num)
        printNum(num-1)

printNum(7)

# output :
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# There are 4 types of Recursion 

# 1.Direct Recursion : The function that call itself directly  with in the same body of the code



# Indirect Function:
# funA calls FunB
# FunB calls funA ( directly or with the help of some other function)


# Direct Function Example:
def Fact(num):
    if num==0:
        return 1
    else:
        return num*Fact(num-1)

print(Fact(5))  
  
# Indirect Function Example:
def FunctionA(n):
    if n<=0:
        return
    print("A :",n)
    FunctionB(n-1)

def FunctionB(n) :
    if n<=0:
        return 
    print("B:",n)
    FunctionA(n-1)

FunctionA(3)          

# 3 Tail Recursion:

# If the recursive call is the last thing which is done by the function there is no need to keep record of the previous state

# Simple thing:
# Solve the smaller problem and give me the final answer

def sum(n , acc=0):
    if n== 0 :
        return acc
    else:
        # print(n)
        return sum(n-1,n+acc)

print(sum(3))   
# output:
# 6
        

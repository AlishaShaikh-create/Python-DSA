# Sum of Numbers using the Recursion

def Sum(n):
    if n==1:
        return 1
    return n + Sum(n-1)

print(Sum(5)) # output :15

# Factorial of the number
def Factorial(num):
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
    
print(Factorial(5))   # 120 
print(Factorial(0))   # 1 

    
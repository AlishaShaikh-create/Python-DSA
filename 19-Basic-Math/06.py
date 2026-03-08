# Factorial of the number
# using the recursion
n=3
def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)      

print(factorial(3))    

# using loop

def factorial(n):
    fact=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
    return fact        

print(factorial(5))            
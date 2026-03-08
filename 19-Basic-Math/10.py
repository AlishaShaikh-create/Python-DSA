# Checl the prime number from 1 to n
def primenumber(n):

    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

print(primenumber(7))
print(primenumber(10))
print(primenumber(1))
print(primenumber(3))

def prime(n):
    count=0
    for i in range(2,n+1):
        if(primenumber(i)):
            count+=1
    return count        
            

print(prime(7))    
print(prime(263))
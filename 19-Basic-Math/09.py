# check of the number is prime or not

def prime(n):
    count=0
    if n==1:
        return False
    else:
        for i in range(1,n+1):
            if n%i==0:
                count+=1
    if count==2:
        return True
    else:
        return False            

print(prime(1))    
print(prime(2))    
print(prime(10))    
print(prime(7))    
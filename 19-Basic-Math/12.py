 # Divisor of  number

def divisior(n):
    arr=[]
    for i in range(1,n):
        if n%i==0:
            arr.append(i)
    return arr

print(divisior(8))        
        
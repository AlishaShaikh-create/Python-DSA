def OddDigit(n):
    count=0
    if n==0:
        return 0
    while(n):
        digit=n%10
        n=n//10
        if digit%2!=0:
            count+=1
    return count

print(OddDigit(0)   )     
print(OddDigit(234))
print(OddDigit(15))
print(OddDigit(25))
def reverse(n):
    if n==0:
        return 0
    reverse=''
    while(n>0):
        
        digit=n%10
        reverse+=str(digit)
        n=n//10
    return reverse 

print(reverse(23))
print(reverse(1000))


n=1000
revNum=0
while(n>0):
    digit=n%10
    revNum=(revNum*10)+digit
    n=n//10

print(revNum)    
    

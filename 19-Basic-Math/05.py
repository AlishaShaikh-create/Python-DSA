# Return the Largest Digit in a Number

n=25
def largest(n):
    largest=0
    digit=0
    while(n>0):
        digit=n%10
        if largest<digit:
            largest=digit
        n=n//10
    return largest
print(largest(n))        
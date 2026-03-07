def number(n):
    count=0
    if n==0:
        return 1
    while(n):
        n=n//10
        count+=1
    return count

print(number(234))   
print(number(0)) 

# time-complexity=O(log N)
# space-complexity=O(1)

# n=0
# number=str(n)
# print(len(number))

# time-complexity=O(log N)
# space-complexity=O(log N)
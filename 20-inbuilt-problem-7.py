def max_consecutive_difference(lst):
    # Your code goes here
    great=0
    for i in range(len(lst)-1):
        diff=abs(lst[i]-lst[i+1])
        if great<diff:
            great=diff
    return great
    
print(max_consecutive_difference([1,7,3,10,5]))
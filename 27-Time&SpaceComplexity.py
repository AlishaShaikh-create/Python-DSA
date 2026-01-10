# Time and Space Complexity
lst =[1,2,3,4,5]

def sum(lst,n):
    sum=0
    if n%2!=0:
        return 0
    
    for i in range(len(lst)):
        sum=sum+lst[i]
    print(sum)    
    
print(sum(lst,11))



   
    
    
    
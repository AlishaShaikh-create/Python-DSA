def find_sqrt(n):
    low = 0
    high = n
    while low <= high :
        mid = (low + high)//2
        
        if mid * mid > n:
            high = mid - 1
        else :
            low = mid + 1    
    return low-1

n = 36
print(find_sqrt(n))  
n = 28      
print(find_sqrt(n))
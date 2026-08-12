def findting_the_nth_root(n , m):
    low = 0
    high = n
    while low <= high:
        mid = (low + high)//2
        if mid **n == m :
            return mid 
        elif mid **n < m :
            low = mid + 1
        else :
            high = mid - 1
    return -1
N = 3
M = 27
print(findting_the_nth_root(N,M))   
N = 4
M = 69         
print(findting_the_nth_root(N,M))
N = 4 
M = 81
print(findting_the_nth_root(N,M))
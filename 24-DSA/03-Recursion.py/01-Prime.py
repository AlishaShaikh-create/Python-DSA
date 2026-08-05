def Prime(n):
    def helper(n, i, j):
        if i > j :
            return True
        if n % i == 0:
            return False 
        return helper(n,i+1,j)
    return helper(n,2,n-1)

print(Prime(7))
print(Prime(17))
print(Prime(18))
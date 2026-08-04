
# Sum of first n natural numbers 
# 1. Parameterized way

def sum_of_n(sum , n):
    if n < 1 :
        print(sum)
        return
    sum_of_n(sum+n , n-1)

sum_of_n(0,3)
sum_of_n(0,10)

# Functional Approach
def sum_of_n(n):
    if n == 0:
        
        return 0
    
    return n+ sum_of_n(n-1)

print(sum_of_n(3) )       

    

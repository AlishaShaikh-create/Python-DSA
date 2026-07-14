# finding the square root of the number .
def findingSquare_root(n):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        val = mid * mid 
        
        if val <= n:
            low = mid + 1
        else :
            high = mid - 1
    return high
            
print(findingSquare_root(28))

# time-complexity : O(log n)
# Space-complexity : O(1)
            

# Finding the smallest divisor 
import math
def smallestDivisor(nums , limit):
    low = 1
    high = max(nums)  # the maximum value of the array because after this the sum never changes 
    ans = high
    while low <= high:
        mid = (low + high) // 2
        sum = 0
        for num in nums:
            divisor = math.ceil(num/mid)
            sum+= divisor
        if sum <= limit :
            ans = mid 
            high = mid -1 
        else :
            low = mid + 1
    return ans

nums = [8,4,2,3]
limit = 4  
print(smallestDivisor(nums,limit))   

def koko_eating_banana(nums , limit):
    low = 1
    high = max(nums)  # the maximum value of the array because after this the sum never changes 
    ans = high
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for num in nums:
            total += math.ceil(num/mid)
        if total <= limit :
            ans = mid 
            high = mid -1 
        else :
            low = mid + 1
    return ans

nums = [7, 15, 6, 3] 
h = 8
print(koko_eating_banana(nums,h))



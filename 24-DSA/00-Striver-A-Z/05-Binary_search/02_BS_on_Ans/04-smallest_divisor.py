import math
def smallest_divisor(nums,limit):
    low = 1
    high = max(nums)
    d = -1
    while low <= high:
        mid = (low + high)//2
        Sum = 0
        for i in range(len(nums)):
            # instead of using the building ceil method 
            # ans = math.ceil(nums[i]/mid)
            ans= (nums[i] + mid -1)//mid

            Sum += ans
        if Sum <= limit:
            d = mid
            high = mid -1
        else :
            low = mid  +1
    return d               
nums = [1, 2, 3, 4, 5] 
limit = 8
print(smallest_divisor(nums,limit))
nums = [8,4,2,3] 
limit = 10
print(smallest_divisor(nums,limit))
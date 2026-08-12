import math
def koko_eating_banana(nums,h):
    low = 1
    high = max(nums)
    ele = 0
    while low <= high:
        mid = (low + high)//2
        count = 0
        for i in range(len(nums)):
            # instead of using the building ceil method 
            # ans = math.ceil(nums[i]/mid)
            ans = (nums[i] + mid -1)//mid

            count += ans
        if count <= h:
            ele = mid
            high = mid -1
        else :
            low = mid  +1
    return ele               
nums = [7, 15, 6, 3] 
h = 8
print(koko_eating_banana(nums,h))
# Building the prefix-sum  and calculating the range query sum
def Building_prefix(nums , left , right):
    prefix = [0]*len(nums)
    prefix[0] = nums[0]
    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] + nums[i]

    result = 0
    if left < right :
        result = prefix[right] - prefix[left-1]
    if left == 0:
        result = prefix[right]
    return result         



nums = [2, 4, 1, 3, 5]
print(Building_prefix(nums, 2 , 4))    



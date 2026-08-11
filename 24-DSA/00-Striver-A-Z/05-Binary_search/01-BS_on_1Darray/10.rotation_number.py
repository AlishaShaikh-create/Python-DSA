def Find_K_rotations(nums):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            low = mid + 1
        else :
            high = mid 
    return low
nums = [15,18,2,3,6,12]
print(Find_K_rotations(nums))
nums =[7,9,11,12,5]
print(Find_K_rotations(nums))
def search(nums , target):
    low  = 0
    high = len(nums)-1
    while low <= high :
        mid = (low + high)//2
        if nums[mid] == target :
            return mid
        # left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target and nums[mid] >= target:
                high = mid -1
            else :
                low = mid + 1
        else :
            if nums[mid] <= target and nums[high]>= target:
                low = mid + 1
            else :
                high = mid - 1               
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums,target))            
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(search(nums,target)) 
nums = [6, 7, 1, 2, 3, 4, 5]
target = 3
print(search(nums,target)) 

print("----------------------------------------")


# def finding the minium :
def minimum(nums):
    low  = 0
    high = len(nums)-1
    while low <high:
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            low = mid + 1
        else :
            high = mid
    return nums[low]        

        
    return ele
nums = [3, 4, 5, 1, 2]
print(minimum(nums))                            
nums = [4, 5, 6, 7, 0, 1, 2]
print(minimum(nums))
nums = [11, 13, 15, 17]
print(minimum(nums))




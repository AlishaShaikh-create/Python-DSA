
# My code 
def single_element(nums):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] != nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        if nums[mid] == nums[mid-1]:
            if (mid -1)%2 == 0:
                low = mid + 1
            else :
                high = mid -1
        elif nums[mid]==nums[mid+1]:
            if mid % 2 == 0:
                low = mid + 1
            else :
                high = mid -1
        if low == high :
            return nums[low]
nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(single_element(nums))                    
nums = [1, 1, 3, 5, 5] 
print(single_element(nums))  
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,7] 
print(single_element(nums))      

# correct solution :
def search_element(nums):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low + high)//2
        # make mid even
        if mid%2 == 1 :
            mid = mid - 1

        if nums[mid] == nums[mid+1]:
            # the before elements do not contain any duplicates
            low = mid + 2
        else :
            high = mid

    return nums(low)                

nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(single_element(nums))                    
nums = [1, 1, 3, 5, 5] 
print(single_element(nums))  
nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6,7] 
print(single_element(nums))      
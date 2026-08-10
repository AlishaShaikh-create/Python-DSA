def Check_sorted_array(nums):
    def helper(nums,i):
        if i == len(nums) :
            return True
        if nums[i-1] > nums[i]:
            return False 
        return helper(nums,i+1)
    return helper(nums,1)


nums = [1, 2, 4, 7] 
print(Check_sorted_array(nums))  
nums = [1, 5, 3, 7]
print(Check_sorted_array(nums))  
        
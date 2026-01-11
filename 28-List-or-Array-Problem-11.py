# https://leetcode.com/problems/max-consecutive-ones/description/

def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    count=0
    max_count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    return max(max_count,count)           
        
        
nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
print(find_max_consecutive_ones(nums))    
nums = [1, 1, 0, 1, 1, 1]
print(find_max_consecutive_ones(nums))  

nums = [0, 1, 1, 1, 0]  
print(find_max_consecutive_ones(nums)) 


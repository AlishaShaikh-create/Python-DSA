def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # TODO: Implement this function
    for items in nums:
        if items==0:
            nums.append(items)
            nums.remove(items)
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))        



def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    non_zero_index = 0  # Pointer to track the position of the next non-zero element
 
    # Move non-zero elements to the front of the list
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    
    # Fill the remaining positions with zeros
    while non_zero_index < len(nums):
        nums[non_zero_index] = 0
        non_zero_index += 1
 

# Example usage (can be removed)
# nums = [0, 1, 0, 3, 12]
# display_result(nums)  # Output should be [1, 3, 12, 0, 0]
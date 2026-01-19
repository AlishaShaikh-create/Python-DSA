def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    n = len(nums)
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum
 
# Helper function to display the result (for debugging)
def display_result(nums):
    print(find_missing_number(nums))
 
# Example usage (can be removed)
# nums = [3, 0, 1]
# display_result(nums)  # Output should be 2

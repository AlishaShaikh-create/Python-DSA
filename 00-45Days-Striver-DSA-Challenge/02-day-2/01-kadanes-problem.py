nums = [2, 3, 5, -2, 7, -4] # output : 15

# Brute force approach
def kadanes(nums):
    maxi = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i,j+1):
                sum+=nums[k]
            
            maxi = max(maxi, sum)    
    return maxi

print(kadanes(nums))        


def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example
nums = [-2, -3, -7, -2, -10, -4]
print(max_subarray_sum(nums))
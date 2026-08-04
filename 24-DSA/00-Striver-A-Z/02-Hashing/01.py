def longest_consecutive(nums):
    # if the num array is empty then return 0
    if not nums:
        return 0
    
    # sort the array so that we can get the consecutive element in the sequence 
    nums.sort()

    # initialize 2 variable with the value 1 why 1 : because if there is single element in the array its consecutive element is 1 only
    largest = 1
    current  = 1

    for i in range(1,len(nums)):
        # to skip the duplicate element 
        if nums[i] == nums[i-1]:
            continue
        #if the element is consecutive then increment current 
        elif nums[i] ==  nums[i-1]+1:
            current+=1
        # store the current in the largest and set the current value again to 1    
        else :
            largest = max(current,largest)
            current = 1
    return max(current , largest)
    

nums = [100, 4, 200, 1, 3, 2]    
print(longest_consecutive(nums))      


# Optimal Solution :
def longest_consecutive(nums):
    new_set = set(nums)

    longest  = 0
    for num in new_set:
        
        if num-1 not in new_set:
            current = num
            length = 1

            while current+1 in new_set:
                current+=1
                length+=1
            longest = max(length , longest)
    return longest            

nums = [100, 4, 200, 1, 3, 2]    
print(longest_consecutive(nums))     


def sum_of_subArray(nums,k):
    longest = 0
    sum = 0
    length = 0
    for num in nums:
        sum += num
        length +=1

        if sum == k :
            longest = max(length , longest)
            sum = num
            length = 1
    return longest        
        
nums = [10, 5, 2, 7, 1, 9] 
k=15       
nums=[-1, 1, 1]
k=1 
print(sum_of_subArray(nums,k))


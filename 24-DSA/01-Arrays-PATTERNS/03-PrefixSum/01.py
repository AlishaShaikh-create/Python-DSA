# Prefix_sum
nums = [2,4,1,7,3]
prefix = [0] * len(nums)
prefix[0] = nums[0]
for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]
print(prefix)    

# Finding the Pivot :  leetcode - 724 ( My Solution)
def Finding_the_pivot(nums):
    prefix_left =[]
    prefix_right = []
    prefix_left.append(nums[0])
    prefix_right.append(nums[len(nums)-1])
    l =1
    r = len(nums)-2
    while l < r :
        if prefix_left[-1] == prefix_right[-1]:
            return l
        elif prefix_left[-1] < prefix_right[-1]:
            
            prefix_left.append(prefix_left[-1]+ nums[l])
            l+=1
            
        else :
            prefix_right.append(prefix_right[-1]+nums[r])
            r-=1
    print(prefix_right)
    print(prefix_left)        
    return -1

nums = [1,7,3,6,5,6]
print(Finding_the_pivot(nums))        

# Finding the Pivot (Correct Solution)
def Pivot(nums):
    left_sum = 0
    total_sum = sum(nums)
    for i in range(len(nums)):
        right_sum = total_sum - nums[i] - left_sum
        if right_sum != left_sum :
            left_sum += nums[i]
        else :
            return i
    return -1        
nums = [1,7,3,6,5,6]
nums = [1,2,3]
nums = [2,1,-1]
print(Pivot(nums))

# Sum of the SubArrays :
def subArraySum(nums ,k ):
    i = 0
    count = 0
    while i < len(nums):
        sum = nums[i]
        if sum == k:
            count +=1
        for j in range(i+1,len(nums)):
            sum += nums[j]
            if sum == k:
                count+=1
        i+=1        
    return count            

nums=[1,2,3]
print(subArraySum(nums,3))

def SubArray(nums , k):
    hashmap = {0:1}
    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        needed = current_sum - k 
        if needed in hashmap:
            
            count+= hashmap[needed]
        hashmap[current_sum] = hashmap.get(current_sum,0)+1  
    print(hashmap)
    return count

nums=[1,2,3]
print(subArraySum(nums,3))    

def SubArray(nums , k):
    hashmap = {0:1}
    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        needed = current_sum - k 
        if needed in hashmap:
            if needed % k == 0:
                return True
            
            # count+= hashmap[needed]
        hashmap[current_sum] = hashmap.get(current_sum,0)+1  
    return False

nums = [23,2,4,6,7]
k = 6
print(SubArray(nums,k))






def SubArraySum(nums , k):
    hashmap = {0:1}
    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        needed = current_sum - k 
        if needed in hashmap:
            
            count+= hashmap[needed]
        hashmap[current_sum] = hashmap.get(current_sum,0)+1  
    print(hashmap)
    return count

nums=[1,2,3]
print(subArraySum(nums,3))  
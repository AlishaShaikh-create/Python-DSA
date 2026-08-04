# Longest sub array with sum = k :
# Brute force approach :
def longestSubarray(nums, k):
    longest = 0
    for i in range(len(nums)):
        running_sum = 0
        for j in range(i,len(nums)):
            running_sum += nums[j]
            if running_sum == k:
                idx = (j - i)+1
                longest = max(longest , idx)
    return longest
nums = [1, -1, 5, -2, 3]
print(longestSubarray(nums,3)) 

# Optimal approach

def longestSubarray(nums, k):
    prefix = 0
    hashmap = {0 : -1}
    longest = 0
    for i in range(len(nums)):
        prefix+=nums[i]
        needed = prefix - k
        if needed in hashmap:
            current_length = i - hashmap[needed]
            longest = max(longest , current_length)

        else :
            if prefix not in hashmap:
                hashmap[prefix] = i
    return longest        

nums = [1, -1, 5, -2, 3]
print(longestSubarray(nums,3)) 


print("--------------------------------")
# Problem Statement — Contiguous Array
def contiguousArray(nums):

    # count_0 = 0
    # count_1 = 0
    # for num in nums:
    #     if num == 0:
    #         count_0 +=1
    #     else :
    #         count_1 += 1
    # while count_0 == count_1:
    #     if count_0 == count_1 :
    #         return count_0+count_1
    #     elif count_0 > count_1:
    #         while count_0 == count_1:
    #             count_0 -=1
    #         return count_0 + count_1
    #     else:
    #         while count_0 == count_1:
    #             count_1-=1
    #         return count_1+count_0
    
    longest = 0
    for i in range(len(nums)):
        count_0 = 0
        count_1 = 0
       
        
        for j in range(i, len(nums)):
            if nums[j] == 0:
                count_0+=1
            else :
                count_1 +=1
            if count_1 == count_0:
                ele = (j-i)+1
                longest = max(ele , longest)
    return longest        
         

def contiguousArray(nums):
    prefix = 0
    sum = 0
    hashmap ={0:-1, 1:1}
    prefix_hash ={0:-1}
    longest  = 0
    for i in range(len(nums)):
        prefix += hashmap[nums[i]]
        needed = prefix - sum
        if needed in prefix_hash:
            current_length = i - prefix_hash[needed]
            longest = max(longest , current_length)
        else :
            if prefix not in prefix_hash:
                prefix_hash[prefix] = i
    return longest


nums =  [1, 0]  
print(contiguousArray(nums))  
nums = [0, 1, 0]
print(contiguousArray(nums))            
        

print("--------------------------------")

# Binary Subarrays With Sum
def binarySubArray(nums,k):
    prefix = 0
    count  =0
    hashmap ={0:1}
    for i in range(len(nums)):
        prefix +=nums[i]
        needed = prefix - k
        if needed in hashmap:
            count += hashmap[needed] 
        
        hashmap[prefix] = hashmap.get(prefix , 0)+1
    return count
nums = [1, 0, 1, 0, 1]
goal = 2
print(binarySubArray(nums,goal))            
    




        
     


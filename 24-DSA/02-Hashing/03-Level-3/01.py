# Longest Subarray With Equal Number of 0s and 1s
def LongestSubarray(nums):
    min_ele = float('inf')
    hashmap ={}
    for num in nums:
        if num in hashmap:
            hashmap[num]+=1
        else :
            hashmap[num]=1 

    for key , value in hashmap.items():
        if value < min_ele:
            min_ele = value
             

nums = [0, 1]
print(LongestSubarray(nums))
nums = [0, 1, 0]
print(LongestSubarray(nums))
nums = [0, 0, 1, 0, 0, 0, 1, 1]

print(LongestSubarray(nums))

# failed test case 
nums = [0, 1, 1, 1, 0]
print(LongestSubarray(nums))

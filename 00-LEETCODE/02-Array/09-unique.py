def unique(nums):
    unique=0
    counter=0
    for i in range(len(nums)): 
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                counter+=1
                unique=nums[i]
            if counter==1:
                
                break
    
    return unique        
            
# nums=[2,2,1]
# nums= [4,1,2,1,2]
# print(unique(nums))                
                
# time complexity is 0(n2)
# space complexity is 0(n)          


# Optimized Code 

def unique(nums):
    result=0
    for num in nums:
        result^=num
    return result

nums=[2,2,1]
print(unique(nums))
nums= [4,1,2,1,2]
print(unique(nums))      

# 1. XOR of a number with itself is 0 (a ^ a = 0 , any number XOR with itself is zero)
# 2 . XOR of a number with 0 is the number itself (a ^ 0 = a),any number XOR with zero is the number itself
# 3 . XOR is commutative and associative (order doesn't matter)        


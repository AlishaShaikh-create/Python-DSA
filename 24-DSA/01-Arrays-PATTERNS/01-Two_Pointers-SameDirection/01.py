def mergeSortedArray(num1 ,num2 , m ,n):
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(num1) and j < len(num2):
        if num1[i] == num2[j]:
            result.append(num1[i])
            result.append(num2[j])
            i+=1
            j+=1
        elif num1[i]< num2[j]:
            result.append(num1[i])
            i+=1
        else :
            result.append(num2[j])
            j+=1
    if i < len(num1):
        while i < len(num1):
                result.append(num1[i])
                i+=1

    if j < len(num2):
        while j < len(num2):
                result.append(num2[j])
                j+=1
    return result

nums1 = [1,2,3]
nums2 = [2,5,7,10]
m = 3
n = 3
print(mergeSortedArray(nums1 ,nums2, m ,n))




def mergeSortedArray(num1 ,num2 , m ,n):
    i = m - 1
    j = n - 1
    k = m+n -1
    while i >= 0 and j >= 0:
        if num2[j] > num1[i]:
            num1[k] = num2[j]
            j-=1
        else :
            num1[k] = num1[i]
            i-=1
        k-=1
    while j >= 0:
        num1[k] = num2[j]
        j-=1
        k-=1
    return num1    


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,7]
m = 3
n = 3
print(mergeSortedArray(nums1 ,nums2, m ,n))
            

# Apply operation on array leetcode 2460

def ArrayOperation(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0
    pos = 0
    for i in range(len(nums)):
        if nums[i]!= 0:
            temp = nums[pos]
            nums[pos] = nums[i]
            nums[i] = temp
            pos +=1
    return nums        
              

nums = [1,2,2,1,1,0]
print(ArrayOperation(nums))
            
# Two Sum 
def twoSum(nums, target):
    hashmap = {}
    for i , value in enumerate(nums):
        complement = target - value
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[value] = i
      

nums = [2,7,11,15]
target = 9 
print(twoSum(nums,target))   

# Time - Complexity : O(n)
# Space - Complexity : O(n)

# OPTIMAL SOLUTION        
def twoSum(nums, target):
    i = 0
    j = len(nums)-1
    while i < j :
        if nums[i] + nums[j] == target:
            return [ i ,j]
        elif nums[i] + nums[j] < target :
            i+=1
        else :
            j-=1
               


nums = [2,7,11,15]
target = 9 
print(twoSum(nums,target))  






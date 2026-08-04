def moveZeros(nums):
    j =0
    for i in range(len(nums)):
        
        if nums[i]!=0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j+=1     
    return nums        
            
nums = [0, 1, 4, 0, 5, 2]
print(moveZeros(nums))        


# time Complexity = 0(n)
# space - 0(1)

def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] ==  nums[i+1]:
            nums.pop(i)
        else:
            i+=1
    return nums       

nums = [0, 0, 3, 3, 5, 6]
print(removeDuplicates(nums))     


# Optimal Solution
def removeDuplicates(nums):
    i = 0 
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]= nums[j]
    return nums[:i+1]
              

nums = [0, 0, 3, 3, 5, 6]
print(removeDuplicates(nums))  

# Finding the missing number in the array
def missingNumber(nums):
    number=set()
    for i in range(len(nums)+1):
        number.add(i)
    
    for n in number:
        if n not in nums:
            return n
            
   

nums = [0, 2, 3, 1, 4]
print(missingNumber(nums))            
        

def missingNumber(nums):
    n = len(nums)
    sum_of_n = n*(n+1)/2
    sum = 0
    for i in range(len(nums)):
        sum+=nums[i]
    return int(sum_of_n - sum)

nums = [0, 2, 3, 1, 4]
print(missingNumber(nums))      
            
# Union of sorted Arrays:
def Union_sorted(nums1,nums2):
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j <len(nums2) :
        if nums1[i] == nums2[j]:
            if nums1[i] not in result:
                result.append(nums1[i])
            i+=1
            j+=1    
        elif nums1[i]<nums2[j]:
            if nums1[i] not in result:
                result.append(nums1[i])
            
            i+=1
        else:
            if nums2[i] not in result:
                result.append(nums2[j])
            j+=1
    
    if i<len(nums1):
        
            for k in range(i,len(nums1)):
                if nums1[k] not in result:
                    result.append(nums1[k])
            i+=1     
    
    if j < len(nums2):
        
            for k in range(j,len(nums2)):
                if nums2[k] not in result:
                    result.append(nums2[k])
                
            j+=1
    return result

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8,8]  
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(Union_sorted(nums1,nums2))


#Optimal Solution
def Union_sorted(nums1,nums2):
    i = 0
    j = 0
    result = []
    while i < len(nums1) and j <len(nums2) :
        if nums1[i] <= nums2[j]:
            if not result or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else :
            if not result or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
        
    while i < len(nums1):
        if not result or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    
    while j < len(nums2):
        if not result or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1
    return result

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8,8]  
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(Union_sorted(nums1,nums2))
         
                   
                
        
# Intersection of 2 sorted array:
def intersection_sorted(nums1 , nums2):
    i =0 
    j =0 
    result =[]
    while i< len(nums1) and j<len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i]<nums2[j]:
            i+=1
        else:
            j+=1            
    return result

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(intersection_sorted(nums1,nums2))        
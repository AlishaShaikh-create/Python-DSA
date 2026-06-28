# Second Largest element 
def secondLargest(nums):
    largest =  float('-inf')
    sec_largest = float('-inf')
    for num in nums:
        if num > largest:
            sec_largest = largest 
            largest = num
        elif num > sec_largest and num!=largest:
            sec_largest = num
    if sec_largest == float('-inf'):
        return -1
    else:
        return sec_largest

nums = [8, 8, 7, 6, 5]
print(secondLargest(nums))   

# time - 0(n)
# space = 0(1) 


# Maximum Consecutive Ones

def maxConsecutiveOnes(nums):
    freq = 0
    count = 0
    for num in nums:
        if num == 1:
            count +=1
            freq = max(freq,count)
        else:
            count = 0
    return freq

# nums = [1, 1, 0, 1, 1, 1]  
nums=[1,1,1]
print(maxConsecutiveOnes(nums))

# Left Rotate Array by K Places

def leftRotate(arr , k):
    k = k % len(arr)
    while k :
        temp = arr[0]
        
        for i in range(1,len(nums)):
            nums[i-1] = nums[i]
        
        nums[-1] = temp
        k-=1    
    return arr        

            
        

nums = [1, 2, 3, 4, 5, 6]
k = 2  
print(leftRotate(nums,k))
  
# Optimal solution :
def leftRotate(arr , k):
    n = len(arr)
    k = k % len(arr)
    temp = []
    
    # To store the starting k element in the temp array
    for i in range(0,k):
        temp.append(arr[i])
    
    # to move the element backword    
    for i in range(k,n):
        arr[i-k] = arr[i]
    
    
    # for i in range()      
    
        
        
        
        
        
    
    

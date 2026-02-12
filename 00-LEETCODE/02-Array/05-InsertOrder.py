# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

def insert(nums,target):
    start=0
    end=len(nums)-1
    mid=(start+end)//2
    while start <= end:
        mid=(start+end)//2
        if target==nums[mid]:
            return mid
        elif target <= nums[mid]:
            end=mid-1
        elif target >= nums[mid]:
            start=mid +1
    return start    

nums=[1,3,5,6]      
target=0
print(insert(nums,target))          
     
    
# time complexity : O(nlogn)
    
    
    
    
    
    

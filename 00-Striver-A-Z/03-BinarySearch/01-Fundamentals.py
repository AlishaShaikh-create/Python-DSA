# BINARY SEARCH 

# iterative solution
def binarySearch(nums,target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

nums = [-9109,-6888,-5296,-3183,-1570,-1423,-1186,-380,813,2988,3213,3497,3695,4774,5519,6119,6708,9245,9371,9434,9517]
target = -3183   
print(binarySearch(nums,target))        



# Recursive method
class Solution:
    
    def helperFunction(self,nums,low,high,target):
        if low > high: # base case
            return -1
        mid  = (low+high)//2
        if nums[mid] == target:
            idx = mid
        elif nums[mid]>target:
            idx = self.helperFunction(nums,low,mid-1,target)
        else:
            idx = self.helperFunction(nums,mid+1,high,target)
        return idx
    
    def search(self, nums, target):
        return self.helperFunction(nums,0,len(nums)-1,target)

nums = [-9109,-6888,-5296,-3183,-1570,-1423,-1186,-380,813,2988,3213,3497,3695,4774,5519,6119,6708,9245,9371,9434,9517]
target = -3183 
s1 = Solution()
print(s1.search(nums,target))


# Lower bound
def lowerBound(nums,x):
    low = 0 
    high = len(nums)-1
    ans = len(nums)
    while low <=high:
        mid = (low + high) // 2
        if nums[mid] >= x:
            ans = mid
            high = mid -1 
        else :
            low = mid + 1
    return ans            
nums = [1, 2, 2, 3]
x = 2
nums= [3,5,8,15,19]
x = 3
print(lowerBound(nums,x))


def UpperBound(nums,x):
    low = 0 
    high = len(nums)-1
    ans = len(nums)
    while low <=high:
        mid = (low + high) // 2
        if nums[mid] > x:
            ans = mid
            high = mid -1 
        else :
            low = mid + 1
    return ans    


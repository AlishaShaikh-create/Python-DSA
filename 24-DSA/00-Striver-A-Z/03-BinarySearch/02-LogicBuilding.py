def insertPosition(nums,target):
    low = 0
    high = len(nums)-1
    ans = len(nums)
    while low<=high:
        mid = (low + high)//2
        if nums[mid] >= target:
            ans = mid
            high =  mid -1
        else:
            low = mid +1
    return ans

nums = [-69,-50,-44,-42,-24,-6,7,42,71]
target = 85
print(insertPosition(nums,target))  

def ceil(nums , target):
    low = 0
    high = len(nums)-1
    # floor = -1
    ceil = -1
    while low <= high :
        mid = (low + high)//2
        if nums[mid] >= target:
            ceil = nums[mid]
            high = mid - 1
        else :
            
            low = mid +1
    return  ceil
def floor(nums , target):
    low = 0
    high = len(nums)-1
    floor = -1
    while low <= high :
        mid = (low + high)//2
        if nums[mid] <= target:
            floor = nums[mid]
            low = mid + 1

        else :
            
            high = mid -1
    return  floor

nums =[3, 4, 4, 7, 8, 10]
x= 5   
nums =[3, 4, 4, 7, 8, 10] 
x= 8
print(floor(nums,x), ceil(nums,x))         


def first_Occurance(nums,target):
    low = 0 
    high = len(nums)-1
    first = -1
    while low <=high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid 
            high = mid - 1
        else :
            low = mid + 1
    return first

def last_Occurance(nums,target):
    low = 0
    high =len(nums) - 1
    last = len(nums)
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] > target:
            
            last = mid
            high = mid - 1
        else :
            low = mid + 1
    return last        


nums = [5, 7, 7, 8, 8, 10] 
target = 8
nums = [5, 7, 7, 8, 8, 10]
target = 6
nums = [5, 7, 7, 8, 8, 10] 
target = 5
nums =[-21,-20,-19,-19,-18,-18,-17,-16,-10,-7,-7,-6,-5,-5,-3,-2,-2,-2,-1,-1,1,2,2,2,2,3,3,6,7,8,9,11,11,13,13,16,17,17,20,23,23,23,23]
target= 23

print(first_Occurance(nums,target))
print(last_Occurance(nums,target)-1)

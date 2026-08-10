# binary search
# lower bound
# upper bound 
# Counting the element 
# first and last Occurance
# -----------------------------------
# First Occurance 
# last Occurance 
# floor
# ceil
# 


def first_Occurance(nums, target):
    low = 0
    high = len(nums)-1
    index = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid]>= target:
            if nums[mid]==target:
                index = mid
            high = mid -1
        else :
            low = mid + 1
    return index                

arr = [1, 2, 2, 2, 3, 4]
target = 2
print(first_Occurance(arr,target))

arr = [1, 3, 5, 7]
target = 4
print(first_Occurance(arr,target))

arr = [5, 5, 5, 5]
target = 5
print(first_Occurance(arr,target))

print("-----------------------------------")

# last Occurance
def lastOccurance(nums,target):
    low = 0
    high = len(nums)-1
    index = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target :
            index = mid 
            low = mid+1
        elif nums[mid] < target :
            low = mid + 1
        else :
            high = mid -1
    return index

arr = [1, 2, 2, 2, 3, 4]
target = 2
print(lastOccurance(arr,target))                

arr = [1, 3, 5, 7]
target = 4
print(lastOccurance(arr,target))

arr = [5, 5, 5, 5]
target = 5
print(lastOccurance(arr,target))

print("-----------------------------------")

def floor(nums, target):
    low = 0
    high = len(nums)-1
    floor = -1
    while low <= high :
        mid = (low + high)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            floor = nums[mid] 
            low = mid + 1
        else :
            high = mid - 1
    return floor
                
 
arr= [3, 4, 4, 7, 8, 10]
x = 7
print(floor(arr,x))

print("-----------------------------------")

# Ceil :
def Ceil(nums , target):
    low = 0 
    high = len(nums)-1
    ceil = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target :
            return nums[mid]
        elif nums[mid] < target:
            
            low = mid + 1
        else :
            ceil = nums[mid]

            high = mid -1    
    return ceil 

arr= [3, 4, 4, 7, 8, 10]
x = 9
print(Ceil(arr,x))

print("-----------------------------------")

# def searchRange(nums, target):
#     # Implement your solution here
#     target_index=0
#     n=len(nums)
#     lst =[]
#     start , end = 0 , n-1
#     while(start <= end):
#         mid = (start + end ) // 2
#         if nums[mid] == target:
#             target_index = mid 
#             ele = target
#             lst.insert(0,target_index)
#             while(ele != target):
#                 target_index = target_index+1 
#             lst.insert(1,target_index)
#         if nums[mid] < target:
#             start = mid + 1 
#         if nums[mid] > target:
#             end = mid -1 
#     return lst        

# nums=[5, 7, 7, 8, 8, 10]
# print(searchRange(nums,8))     

def searchRange(nums, target):
    def findFirst(nums, target):
        start, end = 0, len(nums) - 1
        first = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1   # to check if the   the element we are searching is the first occurance only or not    
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return first

    def findLast(nums, target):
        start, end = 0, len(nums) - 1
        last = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                last = mid
                start = mid + 1    # move right
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return last

    first = findFirst(nums, target)
    if first == -1:
        return [-1, -1]

    last = findLast(nums, target)
    return [first, last]


nums=[5, 7, 7, 8, 8,8, 10]
print(searchRange(nums,8))   
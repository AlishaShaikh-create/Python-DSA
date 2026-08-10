class Solution:
    def searchRange(self, nums, target):
        return self.first_Occurance(nums,target) , self.last_Occurance(nums,target)

    def first_Occurance(self,nums,target):
        low = 0
        high = len(nums)-1
        first = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target :
                first = mid 
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
            else :
                high = mid -1
        return first

    def last_Occurance(self,nums,target):
        low = 0
        high = len(nums)-1
        last = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target :
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else :
                high = mid -1
        return last                    
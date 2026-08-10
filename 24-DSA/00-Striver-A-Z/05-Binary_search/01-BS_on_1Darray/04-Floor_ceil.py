class Solution:
    def getFloorAndCeil(self, nums, x):
        return self.floor(nums,x) , self.Ceil(nums,x)

    def floor(self,nums,x):
        low = 0
        high = len(nums)-1
        floor = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == x:
                return nums[mid]
            elif nums[mid] < x :
                floor = nums[mid]
                low = mid + 1
            else :
                high = mid - 1
        return floor


    def Ceil(self,nums,x):
        low = 0
        high = len(nums)-1
        ceil  = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == x:
                return nums[mid]
            elif nums[mid] < x :
                low = mid + 1

            else :
                ceil = nums[mid]
                high = mid - 1
        return ceil


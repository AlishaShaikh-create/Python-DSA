class Solution:
    def bubbleSort(self, nums):
        self.bubbleSortHelper(nums,len(nums))
        return nums

    def bubbleSortHelper(self,nums,n):
        if n == 1:
            return 
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        self.bubbleSortHelper(nums,n-1)     
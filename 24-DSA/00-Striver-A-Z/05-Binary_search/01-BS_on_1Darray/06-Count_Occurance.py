class Solution:
    def countOccurrences(self, arr, target):
        # Your code goes here
        count = 0
        if self.first_Occurance(arr,target) == -1:
            return 0
        else :
            count =  self.last_Occurance(arr,target) - self.first_Occurance(arr,target) + 1
            return count    
    def first_Occurance(self,arr , target):
        low  = 0
        high = len(arr)-1
        first = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                first = mid 
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else :
                high = mid -1 
        return first 

    def last_Occurance(self,arr , target):
        low  = 0
        high = len(arr)-1
        last = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                last = mid 
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1

            else :
                high = mid -1 
        return last                  

sol = Solution()

arr = [1, 2, 2, 2, 4]
target = 2

print(sol.countOccurrences(arr, target))            
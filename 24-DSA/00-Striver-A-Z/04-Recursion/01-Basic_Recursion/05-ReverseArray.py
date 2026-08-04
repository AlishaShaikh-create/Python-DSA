class Solution:
    def reverse(self, arr: list, n: int) -> None:
        return self.HelperFunction(arr, 0 , len(arr)-1)

    def HelperFunction(self,arr , i , j):
        if i > j : 
            return 
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        return self.HelperFunction(arr,i+1,j-1)    

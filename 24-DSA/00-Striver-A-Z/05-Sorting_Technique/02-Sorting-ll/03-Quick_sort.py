class solution :
    def Quick_sort(self , nums , low ,high):
        if low < high :
            pivot = self.partition(nums , low, high)
            self.Quick_sort(nums , low , pivot-1)
            self.Quick_sort(nums,pivot+1 , high)

    def partition(self,nums , low , high ):
        
        pivot_ele = nums[low]
        i = low +1 
        j = high 
        while i < j :
            while  i < high and nums[i] <= pivot_ele  :
                i+=1
            while   j > low and nums[j] > pivot_ele  :
                j-=1
            if i < j :
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

        nums[low], nums[j] = nums[j], nums[low]    
        return j    


nums = [4, 6, 2, 5, 7, 9, 1, 3]

obj = solution()
obj.Quick_sort(nums, 0, len(nums) - 1)

print(nums)


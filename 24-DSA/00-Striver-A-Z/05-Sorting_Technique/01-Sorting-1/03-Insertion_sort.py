def Insertion_Sort(nums):
    for i in range(1,len(nums)):
        j = i-1
        ele = nums[i]

        while j >=0 and nums[j]> ele :
            nums[j+1] = nums[j]
            j-=1

        nums[j+1] = ele 
    return nums        



nums = [7, 4, 1, 5, 3]            
print(Insertion_Sort(nums))
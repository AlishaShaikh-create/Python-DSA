def sorting(nums):
    def merge_sort(nums , low , high):
        if low >= high:
            return
        mid = (low + high)//2
        merge_sort(nums , low , mid)
        merge_sort(nums, mid + 1 , high)
        merge(nums, low , mid , high)

    def merge(nums , low , mid , high):
        left = low 
        right = mid + 1
        temp =[]
        while left <=mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left +=1 
            else :
                temp.append(nums[right])
                right+=1
        while left <= mid :
            temp.append(nums[left])
            left +=1
        while right <= high :
            temp.append(nums[right])
            right+=1

        # transfering all the element back to the array
        for i in range(low , high+1):
            nums[i] = temp[i-low]

    merge_sort(nums , 0 , len(nums)-1)
    
    return nums

nums = [7, 4, 1, 5, 3]
print(sorting(nums))                            

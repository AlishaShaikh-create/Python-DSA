def ReversePair(nums):
    
    def mergeSort(nums , low , high):
        count = 0
        if low >= high :
            return 0
        mid = (low + high)//2
        count+= mergeSort(nums, low , mid)
        count+= mergeSort(nums,mid+1 , high )
        count+= Merge(nums, low , mid , high)
        return count 

    def Merge(nums , low , mid , high):
        temp =[]
        left = low 
        right = mid + 1
        count = 0
        while left <= mid and right <= high :
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else :
                if nums[left] > 2*nums[right]:
                    count += mid - left + 1
                    temp.append(nums[right])
                    right +=1
        while left <= mid :
            temp.append(nums[left])
            left +=1
        while right <= high :
            temp.append(nums[right])
            right+=1

        for i in range(low , high+1):
            nums[i] = temp[i - low]    
        return count   
          
    return mergeSort(nums , 0 , len(nums)-1)

nums = [6, 4, 1, 2, 7]
print(ReversePair(nums))


def ReversePair(nums):

def mergeSort(nums, low, high):
    # Base case
    if low >= high:
        return 0

    mid = (low + high) // 2

    # Count reverse pairs in the left and right halves
    count = mergeSort(nums, low, mid)
    count += mergeSort(nums, mid + 1, high)

    # Count reverse pairs between the two halves
    right = mid + 1

    for left in range(low, mid + 1):
        while right <= high and nums[left] > 2 * nums[right]:
            right += 1

        count += right - (mid + 1)

    # Merge the two sorted halves
    merge(nums, low, mid, high)

    return count

def merge(nums, low, mid, high):
    temp = []

    left = low
    right = mid + 1

    # Normal merge
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1

    # Remaining elements from the left half
    while left <= mid:
        temp.append(nums[left])
        left += 1

    # Remaining elements from the right half
    while right <= high:
        temp.append(nums[right])
        right += 1

    # Copy merged elements back
    for i in range(low, high + 1):
        nums[i] = temp[i - low]

return mergeSort(nums, 0, len(nums) - 1)

nums = [6, 4, 1, 2, 7]

print(ReversePair(nums))        
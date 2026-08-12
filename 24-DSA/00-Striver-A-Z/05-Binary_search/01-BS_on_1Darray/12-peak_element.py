# good attempt 
def peak_element(nums):
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low + high)//2
        if nums[mid+1] > nums[mid]:
            low = mid + 1
        else :
            high = mid
    return low
arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
print(peak_element(arr))
arr = [1, 2, 1, 3, 5, 6, 4]
print(peak_element(arr))

print(peak_element(arr))
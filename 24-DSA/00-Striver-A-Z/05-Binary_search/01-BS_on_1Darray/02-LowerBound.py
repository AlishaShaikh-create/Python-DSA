def lower_bound(arr,target):
    low  = 0 
    high = len(arr)-1
    index = len(arr)
    while low <= high :
        mid = (low + high)//2
        if arr[mid] >= target :
            index = mid
            high = mid -1
        else :
            low = mid + 1

    return index

arr = [2, 4, 6, 8]
target = 5
print(lower_bound(arr,target))            
arr = [2, 4, 4, 4, 8]
target = 4
print(lower_bound(arr,target))
def Merge(arr , low ,high):
    if low >= high :
        return 
    mid = ( low + high ) // 2
    
    # Divide the array 
    Merge( arr , low , mid) 
    Merge( arr , mid+1 , high)
    
    # sorting the arrya
    MergeSort(arr , low , mid ,high)
 
def MergeSort(arr , low , mid , high):
    temp=[]
    left = low
    right = mid + 1
    
    # comparing both the half
    while left <= mid and right <= high:
        if arr[left]<= arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
        # remaining left element
    while left <= mid :
        temp.append(arr[left])
        left+=1
        
        # remaining right element
    while right<=high:
        temp.append(arr[right])
        right+=1
        
        # copy back to the original array
    for i in range(low , high+1):
        arr[i] = temp[ i - low]   

arr = [8,3,5,2,9,1]
Merge(arr , 0 , len(arr)-1)
print(arr)            
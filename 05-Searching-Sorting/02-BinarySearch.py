# binary search
def binary_search(arr, target):
    start=0
    end = len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start= mid+1
        elif arr[mid] > target:
            end = mid - 1 
    return -1         
    
arr=[10,23,35,45,50,70,85]
print(binary_search(arr , 50)    )            
print(binary_search(arr , 10)    )            
print(binary_search(arr , 85)    )            
        
        
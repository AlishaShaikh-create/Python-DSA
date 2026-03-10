# program to check if the array is sorted or not

arr=[1,2,3,4,4,5]
def array_sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True    

print(array_sort(arr))    
def Selection_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp  
    return  arr          

arr  = [5, 2, 4, 1]     
print(Selection_sort(arr))       
arr = [13, 46, 24, 52, 20, 9]
print(Selection_sort(arr))  
def BubbleSort(arr):
    for i in range(len(arr)-1,-1,-1):
        did_swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                did_swap = True
        if not did_swap :
            break
    return arr


    

arr = [13, 46, 24, 52, 20, 9]  
print(BubbleSort(arr))          
arr = [1,2,3,4]
print(BubbleSort(arr)) 



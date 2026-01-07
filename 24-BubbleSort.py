# My bubble sort code 

def bubbleSort(arr):
    for passes in range(len(arr)-1):
        for j in range(len(arr)-1 - passes):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                
                
    return arr

arr=[12,25,11,34,90,22]
print(bubbleSort(arr) )           
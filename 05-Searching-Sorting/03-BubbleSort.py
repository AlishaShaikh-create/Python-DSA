
def bubbleSort(arr):
    n = len(arr)
    for passes in range(n - 1):
        swapped = False  # -> To check if the array is already sorted or not
        for j in range(n - 1 - passes):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break   # array already sorted
    return arr

arr=[12,25,11,34,90,22]
print(bubbleSort(arr) )           


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        isSwap = False
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            isSwap=True
        if not isSwap:
            break
    return arr

arr=[12,25,11,34,90,22]
print(bubbleSort(arr) )            
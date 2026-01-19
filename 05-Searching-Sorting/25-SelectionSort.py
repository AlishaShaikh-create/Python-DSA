# My selectiion sort algorithm

# def seleciton_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1):
#             count=arr[j+1]
#             if arr[j]>count:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
                
#     return arr

# arr=[90,25,11,34,90,22]            
# print(seleciton_sort(arr))


def Selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
   
    return arr
arr=[12,25,11,34,90,22]
print(Selection_sort(arr) )                   
        
    
    
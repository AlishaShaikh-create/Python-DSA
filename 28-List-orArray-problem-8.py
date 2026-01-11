def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    n=len(arr)
    if n==1 or n==0:
        return True
    for i in range(0,len(arr)-1):
        
        if arr[i]> arr[i+1]:
            return False
        
    return True    
        
lst= [1, 2, 3,3, 4, 5]
print(is_sorted(lst))

        
lst= [1, 22, 3, 4, 5]
print(is_sorted(lst))

lst=[5]
print(is_sorted(lst))

lst=[]
print(is_sorted(lst))

lst= [3,3] # hidden test case 
print(is_sorted(lst))
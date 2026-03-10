# Reverse an array:
arr=[1,2,4,5,6,7,8,9,20]
def reverse_array(arr):
    new_arr=[]
    for i in range(len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    # return new_arr  
    
    for i in range(len(arr)):
        arr=new_arr
    return arr      

print(reverse_array(arr))
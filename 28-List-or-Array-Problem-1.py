# Given a list of integers, write a function to find the maximum element in the list.

def Maximum(arr):
   largest=arr[0]
   for i in range(1,len(arr)):
       if arr[i]> largest:
           largest=arr[i]
   return largest
       
lst = [3, 5, 2, 9, 6]    
    
print(Maximum(lst)) 
   
lst1 =[-1, -2, -3, -4]
print(Maximum(lst1))          
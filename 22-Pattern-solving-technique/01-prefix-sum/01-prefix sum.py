# prefix sum

arr=[2,4,6,8]
def prefixSum(arr):
    newarr= [0]*len(arr)
    newarr[0]=arr[0]
    for i in range(1,len(arr)):
        newarr[i] = newarr[i-1]+arr[i]
        
    print(newarr)    
    
prefixSum(arr)    


# Range sum query 
# Time complexity : 0(n)
arr=[2,4,6,8]
l=1
s=3
sum=0
for i in range(1,s+1):
    sum +=arr[i]
print(sum)    

 
def rangeSum(arr,l,r):
    prefix=[0]*len(arr)
    prefix[0] = arr[0]
    for i in range(len(arr)):
        prefix[i] = prefix[i-1]+arr[i]
    if l==0:
        return prefix[r]
    return prefix[r]-prefix[l-1]

arr=[2,4,6,8]
print(rangeSum(arr,1,3))        
    
    
    
    
    
        




             


    
    


        
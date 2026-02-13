def merge(num1,num2,m,n):
    i=m-1
    j=n-1
    k=m+n-1
    while j>=0:
        if i>=0 and num1[i]>num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1  
    return num1          
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, nums2, m, n))
    
# time complexity :O(m*n)    
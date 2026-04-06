# arr = [1,2,3,-2,2]
# count=0
# k=3
# for i in range(len(arr)):
#     sum=0
#     for j in range(i,len(arr)):
#         sum+=arr[j]
#         if sum == k:
#           count+=1
# print(count)        


# arr = [1,2,3,-2,2]
arr=[2,3,-5,5,-5,1,4]
k=5
hashmap={0:1}
sum = 0
count =0
for num in arr:
    sum+=num
    if sum-k in hashmap:
        count +=hashmap[sum-k]
           
    
    if sum in hashmap:
        hashmap[sum] += 1
    else:
        hashmap[sum] = 1


print(count)        
  
        

arr = [1,2,3,3,3,3,4,5]    
h ={}
for ele 


    
    
        
       
        
    
    
    
        
         
            
            
            
            
    
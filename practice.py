# def majorityElement( nums):
#         hashmap={}
#         count=1
#         for ele in nums:
#             if ele not in hashmap:
#                 hashmap[ele] = count
#             else:
#                 hashmap[ele]+=1
#         print(hashmap) 
               
#         highest = float('-inf')
        
#         for key,value in hashmap.items():
#             if highest < value:
#                 highest=value
#                 itme=key
                

#         return itme

    
# def majorityElement(nums):
#     count =0
#     for i in range(len(nums)):
#         if count == 0:
#             element = nums[i]
#             count=1
#         else:
#             if nums[i]==element:
#                 count+=1
#             else:
#                 count-=1    
#     return element

       
                
    
# nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# print(majorityElement(nums))    


def leader(nums):
    i = 0
    j = 1
    result=[]
    n= len(nums)-1
    while i < j :
        if nums[i]< nums[j]:
            pass
           
        else:   
            if nums[j]>nums[i]:
                for k  in range(j+1,len(nums)):
                    if nums[j]>nums[k]:
                        result.append(nums[j])
                     
        if j==n:
            result.append(nums[j])
            break
        
        i+=1
        j+=1  
    return result

nums = [1, 2, 5, 3, 1, 2]
print(leader(nums))        
                 
            
            
            
            
    
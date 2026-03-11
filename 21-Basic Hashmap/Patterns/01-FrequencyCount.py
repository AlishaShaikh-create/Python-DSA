nums = [1,2,2,3,3,3]
freq={}
count=1
for num in nums:
    if num not in freq:
        freq[num]=count
    else:
        freq[num]+=count
print(freq)            


hashmap={}
count=1
for n in nums:
    if n not in hashmap:
        hashmap[n]=count
    else:
        hashmap[n]+=count
print(hashmap)
result=[]*2
val=0
# for key,value in hashmap:
#     if value>val:
#         val=value
#         result[]
    
        
    
    
    
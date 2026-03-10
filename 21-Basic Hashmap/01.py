# Most Occuring element in the array

arr= [1, 2, 2,2,3,3,4,4,4]
def Most_Occuring(arr):
    hashmap={}
    count=1
    result=0
    for ele in arr:
        if ele not in hashmap:
            hashmap[ele]=count
            
        else:
            hashmap[ele]+=1
    for key ,value in hashmap.items():
        if value>=result:
            result=value
            freq=key
            
    return freq       
    

print(Most_Occuring(arr))
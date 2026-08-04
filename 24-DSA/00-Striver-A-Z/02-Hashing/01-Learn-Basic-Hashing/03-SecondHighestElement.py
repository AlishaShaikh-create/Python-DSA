def findingSecondLargest(nums):
    largest = float('-inf')
    for num in nums:
        if num > largest :
            sec_largest = largest 
            largest = num
        if num > sec_largest and num != largest :
            sec_largest = num 
    return sec_largest
arr = [4, 4, 5, 5, 6, 7]
arr = [1, 2, 2, 3, 3, 3]
print(findingSecondLargest(arr))

def SecondHighestFrequency(nums):
    hashmap ={}
    for num in nums:
        if num in hashmap:
            hashmap[num]+=1
        else :
            hashmap[num] = 1
    largest = float('-inf')  
    ele = 0  
    sec_ele  =0
    sec_largest = float('-inf')    
    for key , value in hashmap.items():
        if value > largest : 
            sec_largest = largest 
            largest = value
            sec_ele = ele 
            ele = key 
        elif value == largest and key < ele: 
            ele = key    
        elif value > sec_largest and value != largest:
            sec_largest = value 
            sec_ele = key
        elif  value == sec_largest and key < sec_ele :
            sec_ele = key
            
    return sec_ele

arr = [4, 4, 5, 5, 6, 7]
arr = [1, 2, 2, 3, 3, 3]
arr = [10, 9 ,7, 7]
arr= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1000,100,10]
print(SecondHighestFrequency(arr))                           
            

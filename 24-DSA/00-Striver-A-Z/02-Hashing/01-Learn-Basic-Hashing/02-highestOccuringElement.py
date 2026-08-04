def highestOccuringElement(nums):
    hashmap = {}
    for num in nums :
        if num in hashmap:
            hashmap[num] +=1
        else :
            hashmap[num] = 1
    max_value = float('-inf')
    ele = float('inf')      
    for key , value in hashmap.items():
        if value >   max_value:
            max_value = value
            ele = key 
        elif  value == max_value and key < ele :
            ele = key 
    return ele 

nums = [1, 2, 2,2, 3, 3, 3]   
nums = [4, 4, 5, 5, 6]
nums = [10000,10000,9999,9999]   
print(highestOccuringElement(nums))

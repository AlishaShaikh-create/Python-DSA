def findMissing(nums):
    nums.sort()
    number = []
    n = len(nums)
    for i in range(n+1):
        number.append(i)
  
    
    for ele in number:
        if ele not in nums:
            return ele 
        
        
  
  
nums = [1, 3, 6, 4, 2, 5]

print(findMissing(nums))     
    
    
      
        

    
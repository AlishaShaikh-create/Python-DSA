def threeSum(nums):
    nums.sort()
    k = 0
    result = []
    while k < len(nums)-2:
        i = k+1
        j = len(nums)-1
        if k > 0 or nums[k] == nums[k-1]:
            k+=1
            continue
            
        while i < j :
            if nums[k] + nums[i] + nums[j] == 0:
                newarr= []
                newarr.append(nums[k])
                newarr.append(nums[i])
                newarr.append(nums[j])
                result.append(newarr)
                i+=1
                j-=1
            elif nums[k] + nums[i] + nums[j] < 0:
                i+=1
            else :
                j-=1  
        k+=1        
    return result          

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))         




                
def fourSum(nums , target):
    nums.sort()
    m = 0
    n = 1
    result = []
    
    
    while m < len(nums)-3:
        while  m > 0 and nums[m] == nums[m-1]:
                m+=1
                continue
        n = m+1
        while n < len(nums)-2:
            while n > 0 and nums[n] == nums[n-1]:
                    n+=1
                    continue
            i=n+1
            j = len(nums)-1
            while i < j:
                s = nums[m] + nums[n] + nums[i] + nums[j]
                if s == target:
                    newarr=[0]*4
                    newarr[0] = nums[m]
                    newarr[1] = nums[n]
                    newarr[2] = nums[i]
                    newarr[3] = nums[j]
                    result.append(newarr)
                    i+=1
                    j-=1 
                    
                    while i < j and nums[i] == nums[i-1]:
                        i+=1
                    while i < j and nums[j] ==  nums[j+1]:
                        j-=1 
                          
                elif s < target :
                    i+=1
                else :
                    j-=1
            n+=1
        m+=1    

    return result    

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))


# majority element
def majorityElement(nums):
    hashmap ={}
    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1
    print(hashmap)

    result  =[]
    k = len(nums)//3
    for key , value in hashmap.items():
        if value > k :
            result.append(key)
    return result

nums = [1, 2, 1, 1, 3, 2] 
nums = [1, 2, 1, 1, 3, 2, 2]      
print(majorityElement(nums))    


# Finding the missing and the repeating number :
def missing_repeating(nums):
    n = len(nums)
    sum_of_nums = n * (n+1)//2
    result = [0]*2
    total = 0
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1
    print(hashmap)    
    for key , value in hashmap.items():
        if value == 2:
            result[0] = key

        total += key

    result[1] = sum_of_nums - total
    return result

nums = [3, 5, 4, 1, 1]  
print(missing_repeating(nums))


# OOPS IN PYTHON 
class Student :
    x = "Alisha"

s = Student()

print(s.x)      

class Person :
    def __init__(self , name , city , age =18 ):
        self.name = name
        self.age = age
        self.city = city
    def printInfo(self):
        print(self.name , self.age , self.city)

p1 = Person("Emily","hyderabad")
print(p1.name )
p1.printInfo()
p2 = Person("Emily","hyderabad",25)
p2.printInfo()
del p1.city
print(p2.city)
print(p1.city)





                
    

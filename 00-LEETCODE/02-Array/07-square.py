def square(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]
    nums.sort()
    print(nums)

nums=[-4,-1,0,3,10]    
square(nums)


def square(nums):
   i=0
   j=len(nums)-1
   while i<=j:
        if abs(nums[i]) >abs(nums[j]):
            temp=abs(nums[j])
            nums[j]=abs(nums[i])
            nums[i]=temp
        nums[j]= nums[j]*nums[j]
        j-=1  
        
   return nums  
 
nums=[-4,-1,0,3,10]    
print(square(nums))

# this code will not execute for all the negative numbers
# [-5,-3,-2,-1]


def square(nums) :
    n=len(nums)
    i=0
    j=n-1
    result=[0]*n
    pos=len(nums)-1
    
    while i<j:
        if abs(nums[i])>abs(nums[j]):
            result[pos] =nums[i]*nums[i]
            i+=1
        else:
            result[pos]=nums[j]*nums[j]
            j-=1
        pos-=1
    return result    
nums=[-4,-1,0,3,10]    
print(square(nums))

nums= [-5,-3,-2,-1]       
print(square(nums))

# time-complexity : 0(n)               
# space-complexity : 0(n)
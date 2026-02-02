# Worst case: O(n²)
# space complexity : O(1)
def remove(nums,val):
   i=0
   while i < len(nums):
       if nums[i]==val:
           nums.pop(i)
       else:
           i+=1    
   return len(nums)        

print(remove( [ 3,2,2,3],2))

  
  
   
# Two pointers approach

# Time-complexity: O(n)
# space-complexity : O(1)
def removeElement(nums,val) :
        write=0
        for read in range(len(nums)):
            if nums[read] !=val:
                nums[write]=nums[read]
                write+=1
        return write           
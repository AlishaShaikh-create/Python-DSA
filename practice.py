# numbers = [2,7,11,15]
# target = 9
numbers =[5,25,75]
target = 100
i=0
j=len(numbers)-1
while i<j:
    sum=numbers[i]+numbers[j]
    if sum==target:
        print([i+1,j+1])
        break
    elif sum < target :
        i+=1
    else:
        j-=1
            
    
    
        


    
           
    
        
        
        
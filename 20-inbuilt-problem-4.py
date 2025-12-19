# Program to remove the unique element form the list
          
def unique(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            if i == j :
                continue
            else:
                if lst[i]==lst[j]:
                    return False
    return True            
                
print(unique([1,2,3,4,5,5]))                
                
         
        


# HALLOW SQUARE:
# ***
# * *
# ***
def hallowSquare(size):
    count=""
    for i in range(1,size+1):
        count=""
        for j in range(1,size+1):
            if i==1 or i==size or j==1 or j==size:
                count+="*"
            else:
                count+=" "    
               
        print(count)    
            
                
        
        
           
        

hallowSquare(3)       
hallowSquare(5)       
            
                
                
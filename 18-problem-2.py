#hallow Rectangle


n=3
for i in range(1,n+1):
    string=""
   
    for j in range(1,n+1):
        
        if i==1 or i==n:
            string+='*'
        else:
            if j==1 or j==n:
                string+='*'
            else:
                string+=" "    
                
    print(string)        
    
n=3
for i in range(n):
   
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")       
        
        
   
def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    result = []

    for i in range(n):
        if i == 0 or i == n - 1 or n <= 2:
            result.append('*' * n)
        else:
            result.append('*' + ' ' * (n - 2) + '*')
            
    return result        

# edge case - if step size is 1 or  2
        
def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    lst=[]
  
    for i in range(0,n):
        string=''
        for j in range(0,n):
            string+="*"
        lst.append(string)
    print(lst)            
generate_square(5)
generate_square(3)
generate_square(1)
# reverted right angle triangle
def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Loop from n down to 1 (inclusive) to create each row
    for i in range(n, 0, -1):
        # Create a row with i '*' characters and append it to the list
        triangle.append('*' * i)
    
    # Return the list of rows
    return triangle

n=3
string=''
for i in range(n,0,-1):
   print('*'*i)
       
    
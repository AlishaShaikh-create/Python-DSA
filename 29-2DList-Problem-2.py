# Rotate triangle by 90 degree

# https://leetcode.com/problems/rotate-image/description/t

def rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix    

matrix = [[5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13, 3, 6, 7],
                 [15, 14, 12, 16]]
print(rotate(matrix));        
        
        
        

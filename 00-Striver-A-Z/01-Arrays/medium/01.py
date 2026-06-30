# Pascal Triangle 
def print_pascal(n):
    triangle = []
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    for row in triangle:
        print(*row)    

print_pascal(5)

# Time-Complexity - O(n)
# space-Complexity - O(n)

# pascal Triangle :
def pascal_1(r,c):
    def ncr(n,r):
        if r > n-r:
            r = n-r
        if r == 1:
            return n 
        for i in range(r):
            res = res *(n-i)
            res = res // (i+1)
        return res
    return ncr(r-1,c-1)    

print(pascal_1(4,2)) 



def rotate_by_90(matrix):
    result =[]
    for j in range(0,len(matrix[0])):
        row = [0]*(len(matrix[0]))
        k =0 
        for i in range(len(matrix)-1,-1,-1):
            row[k] = matrix[i][j]
            k+=1
            
        result.append(row)
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_by_90(matrix))

# Time Complexity : O(n**2)
# Space Complexity : O(n)

# Rotate the element of matrix by 90 degree in place

def rotate_90(matrix):
    n = len(matrix)

    # Transpose of the matrix

    # why j needed to start from i+1 : because we do not need to swap the the diagonal element .

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

    # reverse the row element         
    for i in range(n):
        left = 0
        right = n - 1

        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
    return matrix        



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_90(matrix)
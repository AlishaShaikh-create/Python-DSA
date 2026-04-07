def spiralMatrix(mat):
    if not mat or not mat[0]:
        return []
    
    n = len(mat)
    m = len(mat[0])
    
    ans = []
    top, left = 0, 0
    bottom, right = n - 1, m - 1
    
    while top <= bottom and left <= right:
        
        # Left → Right
        for i in range(left, right + 1):
            ans.append(mat[top][i])
        top += 1
        
        # Top → Bottom
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])
        right -= 1
        
        # Right → Left ✅ FIXED
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])
            bottom -= 1
        
        # Bottom → Top ✅ FIXED
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])
            left += 1
            
    return ans

mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

print(spiralMatrix(mat))
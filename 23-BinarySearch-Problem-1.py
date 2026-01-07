

# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def countNegatives(grid):
    # Implement your solution here
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 0:
                count+=1 
    return count
                
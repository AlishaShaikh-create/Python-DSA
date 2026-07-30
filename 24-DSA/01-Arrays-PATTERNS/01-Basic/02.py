# leaders of the array 
def leaders(nums):
    n = len(nums)
    lead = []
    lead.append(nums[n-1])
    print(lead)
    for i in range(n-2,-1,-1):
        if nums[i] >= lead[-1]:
            lead.append(nums[i])
    lead.reverse()
    print(lead)        

nums = [1, 2, 5, 3, 1, 2]
leaders(nums)   


def rearrangeArray( nums):
    positive = []
    negative = []
    for num in nums:
        if num < 0 :
            negative.append(num)
        else :
            positive.append(num)
    i = 0
    j = 0 
    k = 0
    while i < len(positive) and j < len(negative):
        nums[k] = positive[i]
        nums[k+1] = negative[j]
        i+=1
        j+=1
        k+=2
    return nums
nums = [2, 4, 5, -1, -3, -4]  
print(rearrangeArray(nums))  

# Pascal triangle 
def print_pascal(row):
    ans = []
    ans.append([1])
    for i in range(1,row):
        current  = []
        prev = ans[i-1]
        for j in range(i+1):
            if j == 0 or j == i:
                current.append(1)
            else :
                current.append(prev[j-1]+prev[j])
        ans.append(current)
    print(ans)    

row = 4
print_pascal(row)  

# printing the pascal triangle
def printing_pascal(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(printing_pascal(matrix))        



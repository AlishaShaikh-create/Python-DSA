# Problem 2: Valid Palindrome (LeetCode 125)
Input ="A man, a plan, a canal: Panama"
text  = Input.replace(" ","").lower()
print(text)

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1

        elif not s[right].isalnum():
            right -= 1

        elif s[left].lower() != s[right].lower():
            return False

        else:
            left += 1
            right -= 1

    return True
                          

Input = "A man, a plan, a canal: Panama" 
print(isPalindrome(Input))                 


def sortedSquare(nums):
    result = [0]*len(nums)
    left = 0
    right = len(nums)-1
    k = len(result)-1
    while left < right :
        if abs(nums[left]) < abs(nums[right]):
            result[k] = nums[right]**2
            k-=1
            right -=1
        elif abs(nums[left]) > abs(nums[right]):
            result[k] = nums[left]* nums[left]
            k-=1 
            left +=1
        elif abs(nums[left]) == abs(nums[right]):
            result[k] = nums[right]*nums[right]
            k-=1   
            result[k] = nums[left]* nums[left]
            k-=1
            left +=1
            right -=1
    if left == right :
        result[k] = nums[left]**2        

    return result

nums = [-4,-1,0,3,10]
# nums = [-7,-3,2,3,11]
nums= [-5,-3,-2,-1]
print(sortedSquare(nums))
            

def Container(nums):
    left = 0
    right = len(nums)-1
    max_area = float('-inf')

    while left <= right :
        width = right - left
        height = min(nums[left],nums[right])
        area = width * height
        max_area = max(area , max_area)
        if nums[left] < nums[right]:
            left +=1
        else :
            right -=1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Container(height))            





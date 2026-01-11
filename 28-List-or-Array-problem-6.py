# https://leetcode.com/problems/plus-one/description/

def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    string=""
    lst=[]
    for i in range(0,len(digits)):
        string=string+str(digits[i])
    num=int(string)
    num=num+1 
    string=str(num)
    for i in range(0,len(string)):
        lst.append(int(string[i]))
    return lst    
    
    
digits = [1, 2, 3]    
print(plus_one(digits))
digits = [9, 9, 9]    
print(plus_one(digits))


def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # Start from the last digit
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    # If all digits are 9, the result will be a list of zeros with a 1 at the beginning
    return [1] + digits
 
# Helper function to display the result (for debugging)
def display_result(digits):
    print(plus_one(digits))
 
# Example usage (can be removed)
# digits = [9, 9, 9]
# display_result(digits)  # Output should be [1, 0, 0, 0]
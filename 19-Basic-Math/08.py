# perfect number
# You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.



# A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.


# Example 1

# Input: n = 6

# Output: true

# Explanation: Proper divisors of 6 are 1, 2, 3.

# # 1 + 2 + 3 = 6.


def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
         sum+=i
    return sum==n    

print(perfect(6))
print(perfect(4))
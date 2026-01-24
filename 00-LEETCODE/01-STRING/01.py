# 14. Longest Common Prefix
# Intuition

# This problem asks us to find the longest common prefix shared by all strings in an array. The clever approach is to sort the array lexicographically, then only compare the first and last strings. After sorting, if there's a common prefix, it will be shared by these two extreme strings (and therefore by all strings in between).

# Approach
# We'll use a sort-and-compare strategy:

# Lexicographic sorting: Sort the string array alphabetically
# Extreme comparison: After sorting, first and last strings are most different
# Character-by-character matching: Compare characters at same positions in first and last strings
# Prefix building: Accumulate matching characters into result string
# Early termination: Stop when mismatch found or first string exhausted
# This approach leverages the property that sorted strings preserve prefix relationships.

# Complexity
# Time complexity: O(nlogn⋅m)
# Where n is the number of strings and m is average string length, dominated by sorting operation.

# Space complexity: O(logn)
# For the sorting algorithm's recursion stack (depending on implementation), plus O(m) for the result string.

# # Code

def longestCommonPrefix(strs): 
        strs.sort()
        length=len(strs)
        s=""
        i=0
        while i < len(strs[0]):
            if strs[0][i]==strs[length-1][i]:
                s+=strs[0][i]
            else:
                break
            i+=1
        return s            

print(longestCommonPrefix(["flower","flow","flight"]))

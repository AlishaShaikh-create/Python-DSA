# Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.


def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    start=0
    end=len(lst)-1
    mid=(start+end)//2
    while start<=mid or end>=mid:
        if(lst[start]==lst[end]):
            start=start+1 
            end=end-1
        else:
            return False
    return True  

      
lst = [7, 8, 9, 8, 7]
print(is_palindrome(lst))

lst = [1,2,3,4,5]
print(is_palindrome(lst))


# more easy way to do this
def is_palindrome(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1

    return True
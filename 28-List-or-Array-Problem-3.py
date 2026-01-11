
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
    
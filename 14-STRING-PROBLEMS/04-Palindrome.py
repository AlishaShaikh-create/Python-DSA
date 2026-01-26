# CHECK IF THE STRING IS PALINDROME

def Palindrome(s):
    st=s[::-1]
    s=s.lower()
    if s==st:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"
    
print(Palindrome("hello"))    
print(Palindrome("madam"))    

 
def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string by converting to lowercase and removing non-alphanumeric characters
    normalized_str=""
    for char in s:
        if char.isalnum():
            normalized_str+=char.lower()
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

print(is_palindrome("A man a plan a canal Panama"))
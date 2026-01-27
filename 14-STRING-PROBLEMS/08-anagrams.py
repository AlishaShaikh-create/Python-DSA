# ANAGRAMS

def anagram(s,t):
    if len(s)!=len(t):
        return False
        
    count_s={}
    count_t={}
    for char in s:
        count_s[char]=count_s.get(char,0)+1
    for char in t:
        count_t[char]=count_t.get(char,0)+1 
    
    return count_t==count_s       
    

print(anagram("car","rat"))                

def is_anagram(s, t):
    """
    Function to check if t is an anagram of s without using built-in functions.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # If the lengths of s and t are not equal, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Create two arrays to count character frequencies for both strings
    char_count_s = [0] * 26  # Assuming lowercase a-z characters
    char_count_t = [0] * 26  # Assuming lowercase a-z characters
    
    # Loop through the characters in the first string (s) and count occurrences
    for char in s:
        char_count_s[ord(char) - ord('a')] += 1
    
    # Loop through the characters in the second string (t) and count occurrences
    for char in t:
        char_count_t[ord(char) - ord('a')] += 1
    
    # Compare the character frequency arrays for both strings
    for i in range(26):
        if char_count_s[i] != char_count_t[i]:
            return False  # If there is a mismatch in frequencies, return False
    
    return True  #
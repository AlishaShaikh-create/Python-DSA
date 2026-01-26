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

 
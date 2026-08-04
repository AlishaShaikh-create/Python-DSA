def CheckPalindrome(s):
    
    def HelperFunction(s,i,j):
        if i > j:
            return True
        if s[i] == s[j]:
            return HelperFunction(s,i+1,j-1)
        else :
            return False
    return HelperFunction(s,0,len(s)-1)

s="hannah" 
print(CheckPalindrome(s))   
s="hanna"    
print(CheckPalindrome(s))
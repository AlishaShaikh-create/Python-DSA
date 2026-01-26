# REMOVE THE DUPLICATE LETTERS FROM THE WORDS:
def remove_letter(s):
    words=""
    for i in range(len(s)):
        if s[i] not in words:
            words=words+s[i]
    return words    

print(remove_letter("programming"))    
print(remove_letter("Hello World"))
        
    
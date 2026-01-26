# CONSONENTS COUNT

def constant(s):
    vowels='aeiouAEIOU'
    count=0
    for char in s:
        if ('a'<=char<='z' or 'A' <= char <= 'Z'):
            if char not in vowels:
                count+=1
    return count            
        
print(constant("Hello World!")   )         
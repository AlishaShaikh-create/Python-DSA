# Count the vowels in the string
def countVowels(s):
    
    vowels=['a','e','i','o','u','A','E',"I","O","U"]
    count=0
    for i in range(len(s)):
        if s[i] in vowels:
            count+=1
        
    print(count)   
    
countVowels("Alisha")         
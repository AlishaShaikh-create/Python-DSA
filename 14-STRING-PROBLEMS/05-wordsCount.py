# WORDS COUNT 

def words_count(s):
    count=1
    for char in s:
        if char==" ":
            count+=1
    
    print(count)        

words_count("Hello, World!")            
words_count("Python programming is fun.")

def word_count(s):
    is_word=False
    count=0
    for char in s:
        if not char.isspace():
            if not is_word:
                count+=1
                is_word=True
                
            else :
                is_word=False
                
    print(count)                
       
                
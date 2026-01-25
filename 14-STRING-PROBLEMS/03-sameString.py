# to check if the string are equal or not 
def stringEqual(s,t):
    for i in range(len(s)):
        if s[i] in t:
            return True
        else:
            return False               

print(stringEqual("hello","Hello")   )     
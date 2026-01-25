# REVERSE THE STRING 
## reverse using the slice operator
def reverse(s):
    return s[::-1]

print(reverse("hello"))

## without using the slice operator

def reverse(s):
    count=""
    for i in range(len(s)-1,-1,-1):
        count+=s[i]
    return count    

print(reverse("hello"))        
# pattern

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end='')
        print()
def inverted(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print("*",end="")
        print()    
pattern(3) 
inverted(3-1)           
    
    
    

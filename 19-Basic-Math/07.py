# Amstorng number
def isArmstrong(n):
        count=len(str(n))
        
        copy=n
        add=0
        while copy>0:
            digit=copy%10
            add= add + (digit ** count)
            copy=copy//10
        if ( n == add):
            return True
        else:
            return False   
 
print(isArmstrong(153))        
print(isArmstrong(3))        
            
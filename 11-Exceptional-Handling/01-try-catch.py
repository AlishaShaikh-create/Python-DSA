# Exception : An exception is an event that occurs during program execution which disrupts the normal flow of instructions and can be handled by the program.

# An exception represents a runtime anomaly caused by invalid operations, data, or external conditions, and is propagated through the call stack until handled or the program terminates.

# FileNotFoundError
# ValueError
# TypeError

## Exception try , except and finally


# The Base or the Parent class of the expection is the "Exception"
try: 
    a=b 
except:
    print("b hai hi nahi")    

# NameError is class     
try: 
    a=b 
except NameError as ne:
    print(ne)
    print("b hai hi nahi")       
    
# Zero division error 
try :
    result=1/0
except ZeroDivisionError as ex :
    print(ex)
    print("the number can't be divideb by zero")

try :
    result=1/2
    a=b
except ZeroDivisionError as ex :
    print(ex)
    print("the number can't be divideb by zero")
except Exception as e:
    print(e)    

try:
    num=int(input("Enter the number:"))
    result=10/num
except ValueError:
    print("This is not a valid error")            
except ZeroDivisionError:
    print(" The number cannot be divided by zero")  
except Exception as e:
    print(e)      


#try,except,else block
# Without else, everything inside try is treated as “risky”, even code that logically should not be.

# The else block execute only if the error is not present
try:
    num=int(input("Enter the number:"))
    result=10/num
  
except ValueError:
    print("This is not a valid error")            
except ZeroDivisionError:
    print(" The number cannot be divided by zero")  
except Exception as e:
    print(e)
else :
      print(result)    
     
     
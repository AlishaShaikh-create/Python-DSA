#CUSTOM EXCEPTION
class Error(Exception): #generic class
    pass

class dobException(Error):
    pass
year = int(input("Enter the date-of-birth"))
age=2024-year

try:
    if age<=30 and age>=20:
        print("The age is valid and u can apply for the exam")
    else :
        raise dobException   
except dobException:
    print("sorry , your age should be greater than 20 and less than 30")
         
         
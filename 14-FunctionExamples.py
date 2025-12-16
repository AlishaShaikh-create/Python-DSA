# Temperature Conversion 
def Temp_conversion(temp, unit):
    if unit=='c' or unit =="C":
        print("you need to convert it into the celcuis")
        celcius = (temp-32)*(5/9)
        print("The temperature in celcius is ", celcius)
    elif unit == 'f' or unit == 'F':
        print("you need to convert it into farehhite")
        farenhite= (temp * 9 /5)-32
        print("The temperature in farenhite is ", farenhite)    
    else:
        print("invalid unit")    
 
Temp_conversion(100,'c')        
Temp_conversion(100,'F')        

# Password checker 
# any() it takes iterable like string ,list ,tuple etc and if any one condition satisfied then it gets execute
# islower() -> return the boolean value if the string contain the lower character it return true or else False

# lower() -> convert the string into the lower case

def password_checker(password):
    if len(password) < 8:
        print("The password must contail atleast the 8 digit")
    if not any (char.islower() for char in password):
        print("The password must atleast contain one lower letter")
    if not any(char.isupper() for char in password):
        print("The password must atleast contain one Upper letter")      
    if not any(char in '@#$%^&_*()' for char in password ):
        print("The password must atleast contain the special characters")
    
    else :
        print("The password is strong")    
password_checker("alisjd")
password_checker("@AlishaShaikh_2911")

# Calculate the items in the shopping card
def shopping_cart_items(*agrs):
    sum=0
    for items in agrs:
        sum=sum+items
    return sum

print(shopping_cart_items(1,2,45))


def shopping_cart_items1(cart):
    total_cost=0
    for items in cart:
        total_cost+= items["price"]*items["quantity"]
    return total_cost    
        


cart = [
    {"name": "Apple" , "price":12 , "quantity":12 },
    {"name": "Banana" , "price":6 , "quantity":10 },
    {"name": "oranges" , "price":40 , "quantity":3 }
]
    
    
print(shopping_cart_items1(cart))    


# to check if the string in palendrome or not 
def palindrome(string):
    string=string.lower().replace(" ","")
    if string == string[::-1]:
        return True
    else: 
        return False 
    
print(palindrome("Madam"))    

def is_palindrome(s):
    is_pad=True
    for i in range(len(s)//2):
        if s[i]!= s[-(i+1)]:
            is_pad=False 
            break
    
    if is_pad:
        print("palindrome")
    else:
        print("not palindrome")        
        
is_palindrome("909")       

# Factorial of a number using the recursion
def factorial(n):
    fact=1
    if n==0 or n==1:
        return fact
    else :
        return n*factorial(n-1)

print(factorial(3))        
             
# Validate the email address

def email_validate(email):
    e=False
    for i in email:
        if i=="@":
            e=True
            break
    if e:
        print("Correct email")
    else :
        print("wrong email")        
        
email_validate("alisha@gmail.com")        
                     
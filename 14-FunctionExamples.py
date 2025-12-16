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
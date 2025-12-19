number=[1,2,3,4,15,6]
def greatest_number(number):
    greatest=number[0]
    for i in range(len(number)):
        if greatest>=number[i]:
            pass
        else:
            greatest=number[i]
    return greatest

print(greatest_number(number))        
        
        
    



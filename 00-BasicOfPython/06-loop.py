# 2 primitive types of loop
# for loop
# while loop

i = 1
while i <=10:
    print(i)
    i=i+1
    
# break : to stop execution if the certain conditions are met
print("break keyword")
x=1
while x <=10:
    if x == 3:
        break    
    print(x)
    x+=1
    
# continue : it will stop the current iteration and execute the next one 

print("continue key word")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
 

  
# for loop 
for i in range(0,5):
  print(i)  
  
print("Range btween 1 to 10 and step 2") 
for i in range(1,10,2):
  print(i) 
  
for i in range(10,1,-2):
  print(i)  

 
print("loopin through string")  
string = "Alisha Shaikh"  
for i in string:
  print(i)
  
## calculate the sum of first n natural number using for and while loop

print("sum of first n natural numbers")
n = 10
sum =0 
i=1
while i <= 10:
  sum=sum+n
  i+=1

print("Sum of first n natural number is ", sum)  

sum = 0
for i in range(1,11):
  sum = sum +i

print(sum)  


# Example - 2 Prime numbers

for num in range(1,101):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
    else :
     print(num)
     

for num in range (2,101):
       is_prime=True
       for i in range (2,int(num**0.5)+1):
         if num%i==0:
           is_prime = False
           break
       if is_prime:
         print(num)   

         
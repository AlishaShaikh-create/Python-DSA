# Finding maximum and minimum in the array

def max(lst):
    largest=lst[0]
    for i in range(len(lst)):
        if largest < lst[i]:
            largest=lst[i]
            
    
    return largest

lst=[3, 7, 2, 9, 4]
print(max(lst))   

# Finding the minimum of the array

def minimum(lst):
    minimum=lst[0]
    for i in range(len(lst)):
        if minimum>lst[i]:
            minimum=lst[i]
    
    return minimum

lst=[3, 7, 2, 9, 4]  
print(minimum(lst))      


def reverse(lst):
    length=len(lst)
    new_list=[]
    for i in range(len(lst)):
        new_list.append(lst[length-1-i])
        
    return new_list    

lst=[1,2,3,4,5]
print(reverse(lst))
        
# Finding the sum and average of all the elements

def sum_avg(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    
    print(sum)
    avg=sum/len(lst)
    print(avg)
    
lst=[10, 20, 30, 40]
sum_avg(lst)                

def count_even_odd(lst):
    even_count=0
    odd_count=0
    for i in range(len(lst)):
        if lst[i]%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count

lst=[1, 2, 3, 4, 5, 6]
print(count_even_odd(lst))


# second largest element
def second_largest(lst):
    largest=lst[0]
    second_largest=lst[1]
    for i in range(len(lst)):
        if largest<lst[i]:
            largest=lst[i]
        else:
                
         
    
               
    
# Given a list of integers, write a function to find the sum of all the elements in the list.

def sum(lst):
    sum=0
    for i in range(len(lst)):
        sum=sum+lst[i]
    return sum

lst = [-1, -2, -3, -4]    
print(sum(lst))

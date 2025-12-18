#sum of the element in the list
# think of the edge case if the list is empty then it should return none 


def sum(number):
    sum=0
    if len(number)==0:
        return None
    for i in range(len(number)):
        sum=sum+number[i]
    return sum

print(sum([1,2,3,4,5,6,7]))    
print(sum([]))    
        

    
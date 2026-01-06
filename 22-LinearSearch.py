# linear search
# if element present then return the index or else return -1

l1=[10,23,45,70,11]

def linear_search(l1, target):
    for i in range(len(l1)):
        if l1[i]==target:
           return i
    return -1 
        

print(linear_search(l1,70)  ) 
print(linear_search(l1,700)  ) 



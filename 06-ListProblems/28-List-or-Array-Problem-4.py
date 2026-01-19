#Reverse the list

lst =[1, 2, 3, 4, 5]
lst1=[]
for i in range(len(lst)-1,-1,-1):
    lst1.append(lst[i])
print(lst1)    

# time and space complexity 0(n)

def reverse1(lst):
    left=0
    right=len(lst)-1
    while(left<right):
        lst[left],lst[right] = lst[right],lst[left]
        left+=1
        right-=1
    return lst

lst =[1, 2, 3, 4, 5]
print(reverse1(lst))    

# time = 0(n) space=0(1)

lst =[1, 2, 3, 4, 5]
new_lst=lst[::-1]
print(new_lst)
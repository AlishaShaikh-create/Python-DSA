# library of the python
str="Alisha"
def _length_of_string(str):
    count=0
    for element in str:
        count+=1
    return count

print(_length_of_string(str))    
print(len(str))


# Sorting 
# arr.sort() -> this is only used for the list.
# -> make changes in the same array
# -> print(arr.sort()) this return me the None
arr=[1,5,6,7,4]
arr.sort()
print(arr)

# Sorted 
# arr(sorted) : Used for the literabels like (list ,tuple,dict)
# return the new arr
arr=[1,5,6,7,4]
print(sorted(arr, reverse=True))
print(arr)

# absule value 
arr=[-1,5,-6,7,4]
newarr=sorted(arr , key=lambda x: abs(x))
print(newarr)

# sorted according to the length
# key=function (any function can be written with the key)
fruit_list=['apple','pineapple','kiwi']
print(sorted(fruit_list,key=len)) # ruit_list,key=len

print(sorted(fruit_list,key=len,reverse=True)) #['pineapple', 'apple', 'kiwi']


# max and min
arr=[-15,6,8,7]
print(max(arr,key=lambda x:abs(x))) #-15

# sum
print(sum(arr)) #6

# write the sum of the number from the particular point

arr=[1,2,3]
print(sum(arr,start=10)) # 16

def _sum_method(arr):
    sum=0
    for element in arr:
        sum+=element
    return sum    

print(_sum_method(arr))

# any , all : this is mostly used in the boolean value
# any(): Returns True if at least one element is True in an iterable.
# all(): Returns True only if all elements are True in an iterable.

arr=[True,False,True]
print(any(arr)) #True
print(all(arr)) #False

# Count : to print the occurance of the particular element 

arr=[1,2,1,4,5]
print(arr.count(1)) # 2


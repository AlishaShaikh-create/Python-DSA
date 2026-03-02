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
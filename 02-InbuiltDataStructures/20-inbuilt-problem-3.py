# def remove_duplicates(lst):
#     # Your code goes here
#     for i in range(0, len(lst)):
#         for j in range(0,len(lst)):
#             if i==j:
#                 continue
#             else:
#                 if lst[i]==lst[j]:
#                     lst.pop(j)
#     return lst                

# print(remove_duplicates([1,2,2,3,4,4,5]))

# why this code is not working:
#while using the pop method the existing list element gets shrink and list gets out of range

def duplicate(lst):
    result=[]
    for items in lst:
        if items not in result:
            result.append(items)
    return result         

print(duplicate([1,2,2,3,4,4,5]) )   

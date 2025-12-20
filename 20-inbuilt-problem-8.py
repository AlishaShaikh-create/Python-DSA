def merge_two_sorted_lists(list1, list2):
    # Your code goes here
    list1.extend(list2)
    list1.sort()
    return list1
    
list1 = [1, 3, 5]
list2 = [2, 4, 6]    
print(merge_two_sorted_lists(list1,list2))

print("----------")
# def merge(list3,list4):
#     for i in range(len(list4)):
#         list3.append(list4[i])
#     print(list3)
#     for i in range(len(list3)-1):
#         if list

# list3 = [1, 2, 50]
# list4 = [20, 40, 60] 
# merge(list3,list4)        
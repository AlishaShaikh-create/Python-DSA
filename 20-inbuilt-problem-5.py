#program to reverse the element in the list
def reverse(lst):
    lst.reverse()
    return lst
print(reverse([1,2,3,4,5]))


def reverse_list(lst):
    # Initialize two pointers: one at the beginning, one at the end
    start = 0
    end = len(lst) - 1
    
    # Swap elements until the two pointers meet in the middle
    while start < end:
        # Swap the elements at the start and end pointers
        lst[start], lst[end] = lst[end], lst[start]
        # Move the pointers towards the middle
        start += 1
        end -= 1
    
    # Return the reversed list
    return lst
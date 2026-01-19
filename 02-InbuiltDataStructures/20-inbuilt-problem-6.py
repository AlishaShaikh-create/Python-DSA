def count_even_odd(lst):
    # Your code goes here
    even_count=0
    odd_count=0
    for items in lst:
        if items%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    return tuple((even_count,odd_count))        

print(count_even_odd([1,2,3,4,5,6]))


# Iterators are used for efficient looping and memory managememt .Iterators provide a way to access element of a collection sequentially without exposing the underline structure.

my_list=[1,2,3,4,5]
for i in my_list:
    print(i)
    
print(type(my_list))    

print(my_list)

iterators=iter(my_list)
print(iterators) # <list_iterator object at 0x7fcf25c03400>
print(type(iterators)) # <class 'list_iterator'>

# It uses the lazy loading technique

# To iterate through all the element
#next()-> to print the element present in list

print(next(iterators))
print(next(iterators))
print(next(iterators))
print(next(iterators))

iterators=iter(my_list)
try:
    print(next(iterators))
    print(next(iterators))
    print(next(iterators))
    print(next(iterators))
    print(next(iterators))
    print(next(iterators))
except StopIteration:
    print("End of the list")

        
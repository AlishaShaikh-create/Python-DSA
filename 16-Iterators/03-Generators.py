# Generatos
# generators are simple way to create iterators . They use the "yield" keyword to produce the a series of value lazily, which means they generate the value on the fly and do not store them in memory

# Sub class of iterator

def square(n):
    for i in range(1,n):
        return i**2

print(square(3)) # output = 1


def square(n):
    for i in range(n):
        yield i**2 # -> the yield keyword is used to save and return  the value
        
print(square(3)) # <generator object square at 0x7f217e308fb0>


for i in square(3):
    print(i)        

# output:
# 0
# 1
# 4

a=square(4)
print(a)
print(next(a))
print(next(a))
print(next(a))

def my_generator():
    yield 1
    yield 2
    yield 3
    
gen = my_generator()
print(gen)

print(next(gen)) #1   
print(next(gen)) #2 
print(next(gen)) #3 
# print(next(gen)) # Error : StopIteration  

for val in gen:
    print(val)
    
# output:
# 1
# 2
# 3    

# Practical example : Reading Large File 

# generators are particularly useful for reading large files because they allow you to process one line at a time without loading the entire file into the memory.

def read_large_file(file_path):
    with open(file_path,"r") as file:
        for line in file:
            yield line

file_path='large_file.txt'
for line in read_large_file(file_path):
    print(line.strip())
    
           
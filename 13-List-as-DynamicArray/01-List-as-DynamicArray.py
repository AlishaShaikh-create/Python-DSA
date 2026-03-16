# OOPS -> class -> Custome Data type

# 1.Array was fixed size 
# where as list are dynamic size 

# import sys
# l1=[]
# print("Initial size of l1",sys.getsizeof(l1))

# for i in range(0,17):
#     l1.append(i)
#     print(f"{i} --> {sys.getsizeof(l1)}")

a=1
l1=[]
l1.append(1)

print(id(1))

print(id(a))

print(id(l1[0]))

# 140722372440872
# 140722372440872
# 140722372440872

a=2
print(id(a))

print(id(l1))

x=10000000000000000
y=10000000000000000
print(x==y)
print( x is y)
print(id(x))
print(id(y))
from collections import Counter
arr=Counter([1,2,2,3,2,3,3,4])
print(arr[1]) # 1

print(arr[2]) # 3
print(arr[0]) # 0

print(arr.most_common(1))

print(arr.elements()) # <itertools.chain object at 0x7fc5a38a7520>

print(list(arr.elements())) # [1, 2, 2, 2, 3, 3, 3, 4]

arr.update([1])
print(arr) # Counter({2: 3, 3: 3, 1: 2, 4: 1})

arr.update([3,2,1])
print(arr) #  Counter({2: 4, 3: 4, 1: 3, 4: 1})

# to delete the particular element if the element is not present then it will not return the error
arr.subtract([1,2])
print(arr) # Counter({3: 4, 2: 3, 1: 2, 4: 1})

c1=Counter([1,1,1,2,2,3])
c2=Counter([1,1,2,3,4])
c3=c1-c2
print((c3)) # Counter({1: 1, 2: 1})
print(list(c3)) # [1,2]

# addition
c3=c1+c2
print(list(c3.elements())) # [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# & and taking the common element
c3=c1&c2
print(list(c3.elements())) # [1, 1, 2, 3]





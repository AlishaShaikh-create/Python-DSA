# behind the Scene
lst = [1, 2, 3]

for x in lst:
    print(x)

for x in lst:   # works again!
    print(x)

it = iter([1, 2, 3])

for x in it:
    print(x)

for x in it:   # nothing happens
    print(x)
    
lst=iter([1,2,3])    
print(list(lst)) # output: [1,2,3]
print(list(lst)) # output:[]
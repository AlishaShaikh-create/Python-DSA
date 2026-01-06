# SET : unordered ; immutable ; do not allow duplicate 
# in set you can add or delete the items but u cannot change the items 
# add() : To add one item to the set 
s1={1,2,3}
print(s1)
s1.add(4)
print(s1)

# to add one set to the other set we use the update method

s1={1,2,3}
s2={4,5,6}
s1.update(s2)
print(s1)

#Remove element remove()
s1={1,2,3}
s1.remove(3)
print(s1)
# s1.remove(3) -> raise the error if the element doesnot exist
# print(s1)


#discard() -> does not raise the error if element does not exist
s1={1,2,3}
s1.discard(2)
print(s1)


s1.discard(2)
print(s1)


# JOIN IN SETS

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.


#UNION:
#instead or union () you can even use the or operator |
s1={'a','b','c'}
s2={1,2,3}
s3= s1.union(s2)
print(s3)

s3=s1|s2
print(s3)
# output : {1,2,3,'a' , 'b' ,'c'}
    
#Intersection  & -> gives the common element in both the sets

s1={'a','b','c'}
s2={1,2,'a'}
s3=s1.intersection(s2)
print(s3)



# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
s1={'a','b','c'}
s2={1,2,'a'}
s3= s1.difference(s2)
print(s3)

# Symmetric_difference -> remove the common element and give the remaining element from both the sets
s1={'a','b','c'}
s2={1,2,'a'}

s3=s1.symmetric_difference(s2)
print(s3)
# output: {1, 2, 'b', 'c'}
# SET :
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


#discard()
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

#Intersection  &

s1={'a','b','c'}
s2={1,2,'a'}
s3=s1.intersection(s2)
print(s3)



# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
s1={'a','b','c'}
s2={1,2,'a'}
s3= s1.difference(s2)
print(s3)
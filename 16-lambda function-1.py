# Map function :

# The map function applies a given function to all the items in a input list (or iterable ) and return a map object (an iterable) this is particularly useful for transforming data in a list comprehensively

#Syntax 
# map(function , iterable)


def square(n):
    return n**2

list1=[1,2,3,4,5]

newlist=list(map(square, list1))
print(newlist)


number1=[1,2,3,4,5]
list2=list((map(lambda x:x**2 , number1)))
print(list2)

# map multiple iterables 
n1=[1,2,3]
n2=[4,5,6]
added_number=list(map(lambda x,y:x+y,n1,n2))
print(added_number)


# map to convert string to numbers
string=['1','2','3','4','5']
print(string)
int_numbers=list(map(int,string))
print(int_numbers)
print(type(int_numbers))


words=['apple', 'banana','grapes']
upperwords=list(map(str.upper, words))
print(upperwords)


def get_name(person):
    return person['name']

people=[
    { 'name':"Alisha","roll":'M0'},
    { 'name':"neha","roll":'H0'}
]

name=list((map(get_name, people)))
print(name)
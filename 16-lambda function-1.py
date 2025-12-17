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


# filter function

def even(n):
    if n%2==0:
        return True
    
lst=[1,2,3,4,5,6,7,8,9,10,11,12]
even_number=list(filter(even,lst))  
print(even_number)  



# filter with the lambda function
lst1=[1,2,3,4,5,6,7,8,9,10,11,12]
greater=list(filter(lambda x:x>5 , lst1))
print(greater)


# filter with a lambda function and multiple condition
num=[1,2,3,4,5,6,7,8,9,10,11,12]
even_and_greater=list(filter(lambda x: x>5 and x%2==0, num))
print(even_and_greater)

# filter with dict

people=[
    {"name": "Alisha", "age":24},
    {"name": "Peter", "age":25},
    {"name": "neha", "age":30},
    {"name": "jack", "age":45}
]
def greater_age(person):
    return person['age']>25

age=tuple((filter(greater_age,people)))
print(age)

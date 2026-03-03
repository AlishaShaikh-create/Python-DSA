from collections import defaultdict

dd=defaultdict(int)  # Store the default value as the int 
print(dd) 

# here we did not provide the key to the 'a' but still the default value gets stored as 0
dd['a']
print(dd) # defaultdict(<class 'int'>, {'a': 0})

dd[1]='alisha'
print(dd) # defaultdict(<class 'int'>, {'a': 0, 1: 'alisha'})   

dd['name']='alisha Shaikh'
print(dd) # defaultdict(<class 'int'>, {'a': 0, 1: 'alisha', 'name': 'alisha Shaikh'})

# counting the letters
new_dict=defaultdict(int)
words='apple'
for letter in words:
    new_dict[letter]+=1

print(new_dict)    # defaultdict(<class 'int'>, {'a': 1, 'p': 2, 'l': 1, 'e': 1})

print(dd['xyz']) # 0
# here the default value  in the default dictionary is the int so xyz is not present it will retrun us the 0

# It never raises the key error 
# Always create the default value


# Technically the value we are storing is the list the default so the list operation can also be performed on it

d=defaultdict(list)
d['list']=[1,2,3]
print(d) # defaultdict(<class 'list'>, {'list': [1, 2, 3]})  

d['list'].append(10)
print(d) # defaultdict(<class 'list'>, {'list': [1, 2, 3, 10]}) 

alis=defaultdict(int)
alis['new']=[1,2,3]
alis['new'].append(10)
print(alis) # defaultdict(<class 'int'>, {'new': [1, 2, 3, 10]})  
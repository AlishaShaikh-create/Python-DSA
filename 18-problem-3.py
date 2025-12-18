# Rectangle pattern

# Input: n = 4, m = 5 m -> '*'
# Output: ['*****', '*****', '*****', '*****']

m=2
n=3
lst=[]
for i in range(1,n+1):
    lst.append("*"*m)
print(lst)    

# printing the rectangle
n=3
m=2
for i in range(1,n+1):
    string=''
    for j in range(1,m+1):
        string+="*"
    print(string)    
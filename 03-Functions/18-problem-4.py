# printing the right angle triangle
def traingle(n):  
  return ['*' * i for i in range(1, n + 1)]
print(traingle(3))

n=3
string=''
for i in range(0,n):
  string+='*'
  print(string)
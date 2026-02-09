# Creating my own Custome Iterator :

class My_Iterator:
    def __init__(self,n):
        self.n=n
        self.i=0
    
    def __iter__(self):
        return self # -> this always should return the self 
    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        value = self.i
        self.i+=1
        return value

it1=My_Iterator(3) 
print(it1)

for x in My_Iterator(3):
    print(x)
    
print(next(it1))   
print(next(it1))   
print(next(it1))   
# print(next(it1))   -> raises the exception : Stop iteration
        
            
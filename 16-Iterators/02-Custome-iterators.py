# Creating the custome iterators
class EvenNumber:
    def __iter__(self):
        self.n=2 # -> starting the value with the 2 
        return self
    def __next__(self):
        x=self.n
        self.n+=2
        return x

even=EvenNumber()
print(iter(even))    
print(next(even))    
print(next(even))    
print(next(even))    

# Output: <__main__.EvenNumber object at 0x7fd9b31bf620>
# 2
# 4
# 6


lst=[1,2,3]
it1=iter(lst)
it2=iter(lst)
print(next(it1)) #1
print(next(it1)) #2
print(next(it1)) #3
print(next(it2)) #4
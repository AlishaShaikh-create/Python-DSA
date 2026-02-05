import ctypes

class CustomeArray:
    def __init__(self):
        initialCapacity = 1
        self.size=0
        self.capacity=initialCapacity       
        self.array=self.__create_array(self.capacity)
        
    def __create_array(self,capacity):
        return (capacity*ctypes.py_object)() 
    
    def __resize(self,new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i]=self.array[i]
            
        self.array = new_array
        self.capacity=new_capacity
        
            
    def append(self,items):
        if self.capacity==self.size:
            self.__resize(2*self.capacity)
        
        self.array[self.size]=items
        self.size+=1
        
    def __len__(self):
        return self.size
    
    def __str__(self):
        output=""
        for i in range(self.size):
            output+=str(self.array[i])+','
            
        return '['+ output[:-1]+']'           

myList=CustomeArray()
myList.append(1)
myList.append(2)
print(myList)
print(len(myList))        
        
        
        
        
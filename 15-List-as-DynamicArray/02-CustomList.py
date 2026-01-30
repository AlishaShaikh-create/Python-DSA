import ctypes

class CustomList:
    def __init__(self):
        initialCapacity=1  # Capacity means after doubling of something how much an element can store where as size is the current size of the array
        self.capacity=initialCapacity
        self.size = 0 
        self.array = self.__create_array(self.capacity)
        
    def __create_array(self,capacity):
        #Create a new refrential array with a given capacity
        return (capacity*ctypes.py_object)()
    
    def __resize(self,new_capacity):
        new_array=self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
    
        self.array = new_array # Replace the old array
        self.capacity=new_capacity
        
        
    def append1(self,item):
        if self.size==self.capacity:
            self.__resize(2*self.capacity)
            
        self.array[self.size] = item  
        self.size+=1   
    
    def __len__(self):
        return self.size

myList=CustomList()
myList.append1(1)
myList.append1(2)
print(len(myList))

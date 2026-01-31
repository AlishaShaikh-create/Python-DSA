import ctypes

class CustomList:
    def __init__(self):
        initialCapacity=1  # size → how many elements are currently stored

        #capacity → how many elements can be stored
        
        self.capacity=initialCapacity
        self.size = 0 
        self.array = self.__create_array(self.capacity)
        
    def __create_array(self,capacity):
        #Create a new refrential array with a given capacity
        return (capacity*ctypes.py_object)()
    

  
#Create a new, bigger array "new_array"
# Copy old elements into it
# Throw away the old array
# Start using the new one

# A brand-new array is created
# It has more slots (new_capacity)
# All slots are initially None
# old array: [10, 20]
# new array: [None, None, None, None]

    def __resize(self,new_capacity):
        
        new_array=self.__create_array(new_capacity) # with this statement we are creating a new array 
        
        for i in range(self.size):  # for copying the element of old array into the new array
            new_array[i] = self.array[i]
    
        self.array = new_array # Replace the old array  # self .array points to the new array
        
        # the old array has no reference
        
        self.capacity=new_capacity # updated capacity valye
        
        
    def append1(self,item):
        if self.size==self.capacity:
            self.__resize(2*self.capacity)
            
#  Why 2 * capacity?

# Because:

# Doubling keeps appends fast on average

# Prevents resizing on every insert

# This is how Python lists work internally (conceptually)
            
        self.array[self.size] = item  
        self.size+=1   
    
    def __len__(self):
        return self.size
    
    # printing the list
    def __str__(self):
        output=""
        for i in range(self.size):
            output = output + str(self.array[i])+','
        return '['+output[:-1]+']'  
    
    def pop(self):
        if self.size==0:
            return 'Empty list'
        poped_itme=self.array[self.size-1]
        self.size=self.size-1
        return poped_itme
        
    
      
        
        

myList=CustomList()
myList.append1(1)
myList.append1(2)
print(len(myList))  # 2
print(myList) #[1,2]

print(myList.pop()) #2
print(myList) #[1]

print(myList.pop()) #1
print(myList) #[]

print(myList.pop()) #Empty list
print(myList) #[]


# s="python"
# print(s[:-1])


# x=10
# arrayType=ctypes.py_object(x)
# print(x)

# ctypes.py_object represents a C-type that can hold a reference to a Python object
# 3 * ctypes.py_object creates an array TYPE (blueprint), but does not allocate memory
# () instantiates the array type and allocates memory
# (3 * ctypes.py_object)() creates an actual array object and allocates memory

# A = (3 * ctypes.py_object)()
# print(A)

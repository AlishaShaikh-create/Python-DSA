# importing the package in python 
import math
print(math.sqrt(16))

from math import sqrt,pi
print(sqrt(25))
print(pi)


import numpy as np
print(np.array([1,2,3,4,5]))


# importing the maths which is present in the package
from package.maths import addition
print(addition(2,3))

from package.subpackage.mul import multiplication
print(multiplication(2,3))



# Standard library in python
import array
arr=array.array('i',[1,2,3,4,5])
print(arr)

import random
print(random.randint(0,10))
print(random.choice(['apple','banana', 'grapes']))


# most common package that we use is the os that is mainly use for the file and package handling 

import os
print(os.getcwd())  # -> gives me the current working directory
# output: /mnt/d/Alisha Codes/Python/Python-DSA/01-module


# To create a folder in the python
# if the folder already exist then it gives u an error
# os.mkdir('test_dir') 
# output : A folder name test_dir will be created 


# to create the file in python
# file=open("newFile.txt",'w')
# file.close()

# to copy the file from source to destination
import shutil
shutil.copyfile("newFile.txt","destination.txt")

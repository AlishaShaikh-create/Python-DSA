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
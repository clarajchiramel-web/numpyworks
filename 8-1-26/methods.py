"""
[  4   4   4   4   4]
[  4   1   1   1   4]
[  4   1 100   1   4]
[  4   1   1   1   4]
[  4   4   4   4   4]

"""

import numpy as np
four_array=np.full((5,5),4)
print(four_array)

ones_array=np.ones((3,3),dtype="int16")
ones_array[1,1]=100
print(ones_array)

four_array[1:4,1:4]=ones_array
print(four_array)



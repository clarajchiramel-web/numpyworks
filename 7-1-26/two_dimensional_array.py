"""
1 2 3
4 5 6
7 8 9

"""

import numpy as np
two_dimensinal_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(two_dimensinal_array.ndim)

#size will return total number of elements
print(two_dimensinal_array.size)

#shape will return rows and columns
print(two_dimensinal_array.shape)


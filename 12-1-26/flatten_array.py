"""
FLATTEN
two methods:
1) np.ravel(arr)
2) arr.flatten()

"""

import numpy as np
arr=np.array([
    [10,20],
    [30,40],
    [50,60]
])
new_array=np.ravel(arr)
print(new_array)#[10 20 30 40 50 60]

new_array=arr.flatten()
print(new_array)#[10 20 30 40 50 60]

arr1=np.array([
    [10,15],
    [20,25],
    [30,35]
])
new_array=np.ravel(arr1)
print(new_array)#10 15 20 25 30 35]
 
new_array=arr1.flatten()
print(new_array)#[10 15 20 25 30 35]
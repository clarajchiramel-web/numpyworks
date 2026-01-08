import numpy as np
array=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])

print(array.ndim) #2
print(array.shape) #3,3
print(array.size) #9

#fetch the row
print(array[0]) #[33 31 27]
print(array[2]) #[33 32 34]

#syntax 2 dimensional array
#arr[row,column] (row slicing)
print(array[1:3]) #[[31 30 29]
                  #[33 32 34]]

print(array[0:2]) #[[33 31 27]
                  #[31 30 29]]    

#column slicing
print(array[:,0:2]) #[[33 31]
                    #[31 30]
                    #[33 32]]

print(array[:,1]) #[31 30 32] 

print(array[::2]) #[[33 31 27] (skipping one element in row)
                  #[33 32 34]]    

print(array[2,1]) #32 (second row first colunm value)

print(array[1:3,1:3]) #[[30 29]
                      #[32 34]]

print(array[:,::2]) #[[33 27] (skipping one elemengt in column)
                    #[31 29] 
                    #[33 34]]           




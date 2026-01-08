#array creation methods:
#np.array()
#np.zeros((r,c)) zero array create cheyum
#np.ones((r,c)) one nte array create cheyum
#np.full((r,c),value) specific value add cheyanamengil
#np.random.rand(r,c) no need for brackets
#np.random.randint(low,high,(r,c))for in case of integer

import numpy as np
zeros_array=np.zeros((3,2),dtype="int16")
print(zeros_array)#[[0 0]
                  #[0 0]
                  #[0 0]]

ones_array=np.ones((3,3),dtype="int16")
print(ones_array)#[[1 1 1]
                 #[1 1 1]
                 #[1 1 1]]

five_array=np.full((2,3),5)
print(five_array)#[[5 5 5]
                 #[5 5 5]]

rand_array=np.random.rand(3,2) 
print(rand_array)#[[0.37991548 0.86373215]
                 #[0.29651758 0.72127549]
                 #[0.19774492 0.17818975]] 
                 
rand_int_array=np.random.randint(10,20,(2,2))   
print(rand_int_array)#[[12 14]
                     #[16 17]]    


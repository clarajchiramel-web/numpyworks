import numpy as np
arr=np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])
print(arr.ndim)
print(arr.size)
print(arr.shape)

#display marks of hari
print(arr[1]) #[23 45 45 34 37]

#display maths marks of hari
print(arr[1,0]) #23

#display malayalam marks of all students
print(arr[0:3,0:5]) #[[43 42 45 34 23]
                    #[23 45 45 34 37]
                    #[37 38 39 40 45]]

#display malayalam and cs marks of all students
print(arr[0:3,2:4])  #[[45 34]
                     #[45 34]
                     #[39 40]]   

#display english and malayalam marks of hari and cibin
print(arr[1:3,1:3])  # [[45 45]
                     #[38 39]]         
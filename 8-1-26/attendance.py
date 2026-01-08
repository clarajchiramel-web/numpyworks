import numpy as np
attendance = [
  
  #m  t  w  h  f
  [1, 1, 1, 1, 1], # Student 1
  [1, 0, 1, 1, 1], # Student 2
  [1, 1, 0, 1, 1], # Student 3
  [0, 1, 1, 1, 0], # Student 4
  [1, 1, 1, 0, 1], # Student 5
  [1, 0, 0, 1, 1], # Student 6
  [1, 1, 1, 1, 0], # Student 7
  [0, 1, 1, 0, 1], # Student 8
  [1, 1, 0, 1, 0], # Student 9
  [1, 0, 1, 1, 1]  # Student 10
#   

]
#FUNCTIONS
#sum,max,min,avg,count_nonzero,argmax,median
#axis=0 =>column
#axis=1 =>row

arr=np.array(attendance)
print(arr)

#update
arr[9,1]=1 #[[1 1 1 1 1]
           #[1 0 1 1 1]
           #[1 1 0 1 1]
           #[0 1 1 1 0]
           #[1 1 1 0 1]
           #[1 0 0 1 1]
           #[1 1 1 1 0]
           #[0 1 1 0 1]
           #[1 1 0 1 0]
           #[1 1 1 1 1]]
print(arr)

#studentwise attendance
print(np.sum(arr,axis=1)) #[5 4 4 3 4 3 4 3 3 4]

#daywise attendance
print(np.sum(arr,axis=0)) #[8 7 7 8 7]

#count_nonzero
#studentwise absent count
student_wise_absent_count=np.count_nonzero(arr==0,axis=1)
print(student_wise_absent_count) #[0 1 1 2 1 2 1 2 2 0]

#daywise absence count
daywise_absent_count=np.count_nonzero(arr==0,axis=0)
print(daywise_absent_count) #[2 2 3 2 3]






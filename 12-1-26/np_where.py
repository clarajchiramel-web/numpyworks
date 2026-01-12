#np where(condition,true_value,false_value) it returns index
#mask the conditions 
import numpy as np
array=np.array([19,20,21,17,23,15])
print(np.where(array>=20,"Adult","teen")) #['teen' 'Adult' 'Adult' 'teen' 'Adult' 'teen']



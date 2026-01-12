import numpy as np
array=np.array([-1,2,3,-5,-6])
print(np.where(array>=0,"positive","negative"))#['negative' 'positive' 'positive' 'negative' 'negative']

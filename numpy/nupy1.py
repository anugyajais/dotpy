import numpy as np

a=np.fromiter((i for i in range(1,10,2)),int)
b= np.empty([4],dtype=int)
c=np.arange(1,10)


print(a)
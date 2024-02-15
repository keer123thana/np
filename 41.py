import numpy as np
even1=np.array([2,4,6,8])
even2=even1
even3=np.array([2.0,4.0,6.0,8.0])
even4=even3.astype(int)
even5=even4.copy()
print(even1)
print(even2)
print(even3)
print(even4)
print(even5)

even4[0]=200
print(even4)
print(even5)

even1[0]=2000
print(even1)
print(even2)

#even6=even1.view()
#even7=even1.copy()
#print(even6.base)
#print(even7.base)

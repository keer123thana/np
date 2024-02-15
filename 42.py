import numpy as np
even1=np.array([2,4,6,8,10])
temp1=np.array([[10,20,30],[100,200,300],[1000,2000,3000]])
print(even1.shape)
for i in even1:
    print(i)
for j in temp1:
    for i in j:
        print(i)

import numpy as np
w=np.array([[1,-1,0,0.5]])
x=np.array([[1,-2,0,-1]])
for i,x in enumurate(X):
    net=np.dot(X[i],w)
    if net >=0:
        s=1
    else:
        s=-1
    r=d[-1,-1,1]-s
    delta_w=0.1*r*X[1]
    w=w+delta_w
    print w
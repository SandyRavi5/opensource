import numpy as np
X = np.array([[1,-2,0,-1],[0,1.5,-0.5,-1],[-1,1,0.5,-1],])
print "Input values", X
w = [1,-1,0,0.5]
d = [-1,-1,1]
c = [0.1,0.2,0.3]
for iter in range (1,3):    
    print "Iteration ", iter
    for i,x in enumerate(X):
        net = np.dot(X[i],w)
        if net>=0:
            out = 1
        else:
            out = -1
        r = d[i] - out
        delta_w = c[i]*r*X[i]
        w = w + delta_w
        print "Weights for step ",i, w

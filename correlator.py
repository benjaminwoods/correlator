import numpy as np

import matplotlib.pyplot as plt

def ncross(x,y):
    ndims = len(x.shape)
    _ = [None]*ndims
    for a in range(ndims):
        sl = [0]*ndims
        _[a] = np.empty(x.shape)
        if ndims > 1:
            red = x.shape[0:a]+x.shape[a+1:]
            prod_r=1
            for i in red:
                prod_r *= i
        else:
            prod_r = 1
            _[a] = np.empty(x.shape[0])
        sl[a] = slice(None)
        #Counting in irregular bases!
        j = 1
        for i in range(prod_r):
            _[a][tuple(sl)] = np.correlate(y[tuple(sl)],x[tuple(sl)],mode="same")
            if ndims > 1:
                while True:
                    if j == ndims-a: #if aligned with slice, move on
                        j += 1
                    if j > ndims: #if outside, leave
                        break
                    sl[-j] += 1 #increment
                    if sl[-j] == red[-j+a]: #if at max base
                        sl[-j] %= red[-j+a];
                        j += 1
                    else:
                        break
    return _

def ndiff(x,y):
    ndims = len(x.shape)
    _ = [None]*ndims
    for a in range(ndims):
        sl = [0]*ndims
        _[a] = np.empty(x.shape)
        if ndims > 1:
            red = x.shape[0:a]+x.shape[a+1:]
            prod_r=1
            for i in red:
                prod_r *= i
        else:
            prod_r = 1
            _[a] = np.empty(x.shape[0])
        sl[a] = slice(None)
        j = 1
        for i in range(prod_r):
            _[a][tuple(sl)] = (x[tuple(sl)] - y[tuple(sl)])/x[tuple(sl)]
            if ndims > 1:
                while True:
                    if j == ndims-a: #if aligned with slice, move on
                        j += 1
                    if j > ndims: #if outside, leave
                        break
                    sl[-j] += 1 #increment
                    if sl[-j] == red[-j+a]: #if at max base
                        sl[-j] %= red[-j+a];
                        j += 1
                    else:
                        break
    return _

#Test matrices
a = np.empty((100,100))
b = np.empty((100,100))
c = np.empty((100,100))
d = np.empty((100,100))

t = np.linspace(-1,1,100)
for i in range(100):
    for j in range(100):
        a[i,j] = np.exp(-(t[i]**2+t[j]**2))
        b[i,j] = a[i,j]*(1 + np.random.rand(1))
        c[i,j] = np.exp(-( (t[i] - 0.1)**2 + (t[j]-0.3)**2))
        d[i,j] = c[i,j]*(1 + np.random.rand(1))

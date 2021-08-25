import numpy as np
#AJUSTE LOGARITMICO
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 6, 8])
x = np.log(x)
n = np.size(x)
m = 1
a = np.zeros([m + 1 ,m + 1])
b = np.zeros([1, m + 1])
print(b)
g = np.zeros([1, n])
print(g.shape)
for i in range (0, m + 1):
    for j in range (0, m + 1):
        for k in range (0, n):
            a[i, j] = (a[i, j] + x[k]**(j+i))
    for k in range (0, n):
        b[0, i] = b[0, i] + y[k] * x[k]**i
print(a)
print(b)
d = np.linalg.det(a)
nc = np.linalg.cond(a)
print(d)
print(nc)
c = np.linalg.solve(a, np.transpose(b))
print(c)
for i in range (0, n):
    g[0, i] = c[0,0] + c[1,0] * x[i]

import matplotlib.pyplot as plt
plt.plot(np.exp(x), y, 'ro', np.exp(x).reshape(1, 4), g, 'r')
plt.show()
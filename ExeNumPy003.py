import numpy as np
import matplotlib.pyplot as plt
#INTERPOLAÇÃO POLINOMIAL
def avalia(xx, n, a):
    p = np.zeros([1, y.size])
    for i in range(0,n):
        p[0, i] = p[0, i] + a[i ,0] * xx ** i
    return p
x = np.array([-1, 0, 1])
y = np.array([4, 1, -1]).reshape(x.size,1)
n = x.size
grau = n - 1
v = np.zeros([n, n])
for i in range (0, n):
    for j in range(0, n):
        v[i, j] = x[i]**j
a = np.linalg.solve(v, y)
print (a)
xx = 0.5
px = avalia(xx, n, a)
x1 = np.arange(x[0],x[-1]+0.2, 0.2)
x2 = np.array(x1)
n1 = x2.size
for j in range (0, n1):
    p = avalia(x2[j], n ,a)
    print(p)
plt.plot(x, y, '*')
plt.plot(x1, p, 'r')
plt.show()
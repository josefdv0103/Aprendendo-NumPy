import numpy as np
from numpy.lib.npyio import genfromtxt
#|1 1 1 1 1|
#|1 0 0 0 1|
#|1 0 9 0 1|
#|1 0 0 0 1|
#|1 1 1 1 1|
a = np.full([5,5], 1)
(a)
a[1:4, 1:4] = 0 #ou a[1:-1, 1:-1] = 0
(a)
a[2,2] = 9
(a)
#outra forma
a = np.ones((5, 5))
(a)
b = np.zeros((3, 3))
b[1,1] = 9
(b)
a[1:-1, 1:-1] = b
(a)
#Tomar cuidado em copiar arrays pois o que for modificado em um 
#Irá ser modificado no outro, para evitar isso faz-se 
#a = b.copy() ao invés de a = b
print(genfromtxt('matriz.txt', delimiter=','))
b = np.array(genfromtxt('matriz.txt', delimiter=','))
(b[2:4, 0:2])
(b[[0, 1, 2, 3] ,[1, 2, 3, 4]])
print(b[[0,4,5], 3:])
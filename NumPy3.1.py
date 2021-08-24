import numpy as np
from numpy.lib.npyio import genfromtxt
a = np.array([1,2 ,3, 4])
(a)
#Operações básica de constantes em matrizes
(a+2)
(a-2)
(a*2)
(a/2)
(np.sin(a))
b = np.array([4, 3, 2, 1])
#Operações básicas de matrizes com matrizes
(a+b)
(a*b)#Multiplicação elemento por elemento não é LiCo
#ALGEBRA LINEAR
a = np.ones((2, 3))
(a)
b = np.full((3, 2), 2)
(b)
(np.matmul(a, b))#Multiplicação LiCo
c = np.identity(3)
(np.linalg.det(c))#Determinante
#ESTATÍSTICA
stats = np.array([[1, 2, 3], [4, 5, 6]])
(stats)
(np.min(stats))#Máximo
(np.max(stats))#Mínimo
(np.max(stats, axis = 1))#Máx da segunda matriz
(np.sum(stats, axis = 0))#Soma da primeira matriz
#REORGANIZANDO ARRAYS
antes = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])#(2, 4)
(antes)
depois = antes.reshape(8, 1)#(8, 1)
(depois)
depois2 = antes.reshape(2,2,2)
(depois2)
#Agrupar arrays
#"UMA EM CIMA DA OUTRA"
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.stack([v1, v2]))
(np.stack([v1, v2, v1, v2]))
#"UMA AO LADO DA OUTRA"
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
(np.hstack((v1, v2)))
#Carregar dados através de arquivos
a = np.genfromtxt('matriz.txt', delimiter = ',')
(a)
#BOLEAN MASKING
(a < 2)
(np.any(a > 2, axis = 0))
(np.all(a > 2, axis = 0))
print((a > 1) & (a < 3))

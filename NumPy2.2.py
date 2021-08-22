import numpy as np
#INICIALIZANDO TIPOS DIFERENTES DE ARRAYS
#=========================================
a = np.zeros(shape = (2,2))
#INICIAR MATRIZ INTEIRA COM UM NÚMERO
(np.full((2,2), 99))
#INICIALIZAR MATRIZ NASEADA EM OUTRA E COMPLETA-LA COM UM NÚMERO
(np.full_like(a, 4))
#INICIALIZAR UMA MATRIZ ALEATÓRIA
(np.random.rand(4,2))
#INICIALIZAR UMA MATRIZ ALEATÓRIA COM DIMENSÕES DE OUTRA
(np.random.random_sample(a.shape))
#INICIALIZAR UMA MATRIZ ALETÓRIA (LIMITE DE UM NUMERO INTEIRO)
(np.random.randint(7, size = (1,2)))
#INICIALIZAR UMA MATRIZ ALEATÓRIA (LIMITE ENTRE 2 NÚMEROS INTEIROS)
(np.random.randint(2, 10, size = (2,2)))
#INICIALIZAR UMA MATRIZ IDENTIDADE
(np.identity(5))
#INICIALIZAR MATRIZES COM SEQUENCIA DE NUMEROS REPETIDOS
#[1 1 1 2 2 2 3 3 3]
arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3)
print(r1)
print(20*'-')
#REPETINDO MAS COM MATRIZ 2D (O DUPLO COLCHETE GARANTE ISSO)
#NO FIM ESPECIFICAR O QUE QUER REPETIR LINHAS/COLUNAS
arr = np.array([[1, 2, 3],[4, 5, 6]])
#LINHAS
r1 = np.repeat(arr ,3, axis = 0)
(r1)
#COLUNAS
r1 = np.repeat(arr ,3, axis = 1)
(r1)

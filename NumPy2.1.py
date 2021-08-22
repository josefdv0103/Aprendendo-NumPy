import numpy as np
a = np.array([[3,6,5,4,8,9],[5,0,3,9,7,8]])
print(5*'=-', 'PARA SELECIONAR UM ELEMENTO ESPECÍFICO', 20*'=-')
#O primeiro termo nos colchetes é qual linha você deseja(começa no zero)
#O segundo termo nos colchetes é qual posição do elemento que você quer(começa no zero)
#Se quiser a posição começando pelo ultima use o - começandono -1
(a[0, 5])
(a[0, -1])
print(5*'=-', 'PARA SELECIONAR UMA LINHA EM ESPECÍFICO', 20*'=-')
#Para selecionar uma linha basta escolher a posição da linha  
# e que o segundo termo seja um ':'
(a[0, :])
print(5*'=-', 'PARA SELECIONAR UMA COLUNA EM ESPECÍFICO', 20*'=-')
#Para selecionar uma coluna basta colocar no primeiro termoum ':'
#E logo após colocar a posição da coluna
(a[:, 0])
print(5*'=-', 'PARA SELECIONAR ELEMENTOS EM ESPECÍFICO EM UMA LINHA', 20*'=-')
#Posso selecionar elementos específicos pulando eles em um intervalo
#Selecionar uma linha e logo após dizer a primeira posição, 
#ultima posição e o intervalo 
(a[0, 1:6:2])
(a[0, 1:-1:2])
print(5*'=-', 'PARA SUBSTITUIR ELEMENTOS DAS MATRIZES', 20*'=-')
#Elementos isolados
a[1, 0] = 4
print(f'''Elemento isolado: 
{a}''')
#Linhas
a[0,:] = 0
print(f'''Uma linha: 
{a}''')
#Colunas
a[:, 1] = 1
print(f'''Uma coluna:
{a}''')
print(60*'-')
print('Exemplo 3D')
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(5*'=-', 'PARA SELECIONAR QUALQUER COISA ESPECÍFICO', 20*'=-')
#Para selecionar temos que olhar de fora para dentro começamos 
#selecionando a matriz 2D, logo após a linha e por fim a posição do
#elemento ta linha
(b[1, 1, 0])
(b[1, :, 0])
(b[:, :, 1])
(b[:, 0, :])
print(5*'=-', 'PARA SUBSTITUIR ELEMENTOS DAS MATRIZES', 20*'=-')
#Para substituir usa-se a mesma contrução para selecionar
#Porém igualamos ao valor que desejamos colocar
b[1, :, 0] = 0
print(b)
print(10*'=')
b[0, 0, :] = [2, 0]
print(b)
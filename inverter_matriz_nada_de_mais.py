import numpy as np
from random import randint

# Criando uma matriz 3x3 com NumPy
matriz_np = np.zeros((3, 3))

inidice = 0
# Criando uma matriz 3x3 com NumPy
matriz1 = np.zeros((3, 3))
a = 0

for i in range(9):
    matriz1[inidice, a] = randint(0, 10)
    a += 1
    if a == 3:
        inidice += 1
        a = 0


print(matriz1)




def inverter(matriz):

    chave_inicio = 0
    valor_inicio = 0

    chave_fim = 2
    valor_fim = 2

    for z in range(3):
        primeiro = matriz[chave_inicio, valor_inicio]
        ultimo = matriz[chave_fim, valor_fim]
        matriz[chave_inicio, valor_inicio] = ultimo
        matriz[chave_fim, valor_fim] = primeiro

        valor_inicio += 1
        valor_fim -= 1

        if valor_inicio == 3:
            primeiro = matriz[1, 0]
            ultimo = matriz[1, 2]
            matriz[1, 0] = ultimo
            matriz[1, 2] = primeiro
            print(matriz)


inverter(matriz1)

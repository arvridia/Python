import time
from memory_profiler import profile

start = time.time()

@profile

def encontrar_elemento(matriz, k):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == k:
                return f'O elemento {k} foi encontrado na posição ({i}, {j}).'
    return f'O elemento {k} não foi encontrado na matriz.'

#Exemplo de matriz
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Exemplo a ser procurado
elemento_procurado = 5

resultado = encontrar_elemento(matriz_exemplo, elemento_procurado)
print(resultado)

end = time.time()
print('\nTempo gasto: ')
print(end - start)
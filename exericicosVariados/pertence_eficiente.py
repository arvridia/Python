import time
from memory_profiler import profile

start = time.time()

def busca_binaria(arr, alvo):
    baixo, alto = 0, len(arr) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        valor_meio = arr[meio]

        if valor_meio == alvo:
            return meio  # Elemento encontrado, retorna o índice
        elif valor_meio < alvo:
            baixo = meio + 1  # Descarta a metade inferior
        else:
            alto = meio - 1  # Descarta a metade superior

    return -1  # Elemento não encontrado

@profile

def busca_matriz_ordenada(matriz, k):
    if not matriz or not matriz[0]:
        return f'O elemento {k} não foi encontrado na matriz.'

    linhas, colunas = len(matriz), len(matriz[0])
    i, j = 0, colunas - 1  #Comece na última coluna da primeira linha

    while i < linhas and j >= 0:
        elemento_atual = matriz[i][j]

        if elemento_atual == k:
            return f'O elemento {k} foi encontrado na posição ({i}, {j}).'
        elif elemento_atual > k:
            retorno = busca_binaria(matriz[i], k) #Busca binária
            if retorno == -1:
                return f'O elemento {k} não foi encontrado na matriz.'
            else:
                return f'O elemento {k} foi encontrado na posição ({i}, {retorno}).'
        else:
            i += 1  #Se o elemento atual for menor que k, vá para a próxima linha

    return f'O elemento {k} não foi encontrado na matriz.'

#Exemplo de matriz
matriz_ordenada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Exemplo a ser procurado
elemento_procurado = 5

resultado = busca_matriz_ordenada(matriz_ordenada, elemento_procurado)
print(resultado)

end = time.time()
print('\nTempo gasto: ')
print(end - start)
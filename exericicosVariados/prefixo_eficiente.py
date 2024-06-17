import time
from memory_profiler import profile

start = time.time()

@profile
def prefixo_comum_maximo(vetor):
    if not vetor or not all(vetor):
        return "Sem prefixo comum máximo."

    prefixo = ""
    tamanho_minimo = min(len(s) for s in vetor)

    for i in range(tamanho_minimo):
        #Verifica se todos os caracteres na posição i são iguais
        if all(s[i] == vetor[0][i] for s in vetor):
            prefixo += vetor[0][i]
        else:
            break

    return prefixo

#Exemplo de uso
vetor_strings = ['abcd', 'abxy', 'abcx', 'abzzzzzzz']
resultado = prefixo_comum_maximo(vetor_strings)

print(f'O prefixo comum máximo é: {resultado}')

end = time.time()
print('\nTempo gasto: ')
print(end - start)
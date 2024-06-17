import time
from memory_profiler import profile

start = time.time()

@profile
def maior_prefixo_comum(strings):
    if not strings or not all(strings):
        return "Sem maior prefixo comum."

    tamanho_menor = min(len(s) for s in strings)
    maior_prefixo = strings[0]

    for i in range(1, len(strings)):
        prefixo_atual = ""
        for j in range(min(len(maior_prefixo), len(strings[i]))):
            if maior_prefixo[j] == strings[i][j]:
                prefixo_atual += maior_prefixo[j]
            else:
                break
        maior_prefixo = prefixo_atual

        if not maior_prefixo:
            break  # Não há mais nenhum prefixo comum

    return maior_prefixo

# Exemplo de uso
strings = ['abcd', 'abxy', 'abcx', 'abzzzzzzz']
resultado = maior_prefixo_comum(strings)

print(f'O maior prefixo comum é: {resultado}')

end = time.time()
print('\nTempo gasto: ')
print(end - start)
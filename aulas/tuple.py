"""
Tipo tupla - Uma lista imutável
"""
# ou sem os parenteses
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1]) # imprime o inverso, pq é uma lista entao tambem funciona
print(nomes)
nomes[1] = 'Pedro' # da erro pq é imutavel

"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# retorna o iterator, consigo acessar os valores atraves de um for, pq ele dá o next
# ou posso dar o type coercion pra uma lista ou tupla
lista_enumerada = enumerate(lista)

# esse realiza a mesma coisa que os de baixo, mas mais elegante
# pra cada elemento da lista, que é uma tupla de dois valores
# ele insere cada valor de cada posicao nessas variaveis, em ordem
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice]) # esse lista[indice] printa a msm coisa que o nome, so pra mostrar q é possivel ja que o enumerate nesse caso esta 1:1 com indice

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# o que basicamente esta acontecendo internamente
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
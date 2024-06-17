# listas sao mutaveis, posso alterar o valor de cada pos
# oq nao era possivel com strings
# IMPORTANTE: tentar adicionar e remover so no final e começo
# fazer alteracoes no meio é muito custoso pois tem que mover todo mundo
# suporta valores de varios tipos:
# [int, bool, list, float], na mesma lista
# [] -> falsy
# metodos uteis -> del, append, pop, clear(torna a lista vazia), insert
# lista CRUD -> Create, Read, Update and Delete = lista[i]
lista = [10, 20, 30, 40]
lista[2] = 40
# del deleta uma determinada posicao, mas tem q mover todo mundo da frente pra tras daquela pos
# portanto é mt custoso

del lista[2]
# adiciona no final o valor passado por parametro
lista.append(50)
# remove o ultimo elemento, 50 no caso
# tambem retorna o valor removido, caso seja util saber qual foi
# podemos passar como argumento pro pop um indice pra ele remover aquela pos
lista.pop()
# add na pos 0, o valor 5
lista.insert(0,5)

# o '+' concatena as listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
# lista_c agora é [1,2,3,4,5,6]
# o metodo extend tambem funciona e o codigo fica mais limpo
lista_a.extend(lista_b)
# lista_a agora teve a adicao da lista_b, portanto ela agora é [1,2,3,4,5,6]



"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # com o copy ai vai ter duas listas na memoria mesmo, se for so atribuindo as duas apontam pra msm

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


"""
Introdução ao empacotamento e desempacotamento
"""
# '_' q nem o haskell, nao vai usar a variavel, poe isso
# o '*' é pra indicar pro python pra colocar tudo que sobrar do desempacotamento nessa variavel
# o *resto esta vazio nesse caso e nao tem problema, o valor dele é []
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
# aqui, nome1 tem é o H e o rest é a cauda
nome1, *rest = ['jonas', 'brothers', 'and', 'the six']
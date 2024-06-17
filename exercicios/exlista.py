'''
Printe os valores
da string 
junto com seus
indices
'''


lista = ['maria', 'jose', 'rodolfo']
i = 0
for nome in lista:
    print('[%d] %s'%(i,nome))
    i += 1


# ou 
indices = range(len(lista))
for indice in indices:
    print(f'[{indice}] {lista[indice]}')
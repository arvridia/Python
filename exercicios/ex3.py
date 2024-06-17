# adicionar '*' antes e depois de todas as letras
nome = input('Digite seu nome:\n')
indice = 0
nova_str = ''
while indice < len(nome):
    nova_str += f'*{nome[indice]}'
    indice += 1
nova_str += '*'
print(nova_str)
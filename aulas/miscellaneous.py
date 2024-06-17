#divisao é /, divisao inteira //, modulo %, potenciacao **, multiplicacao *
#nas repeticoes tem break e continue, os dois o cod para quando ler elas, se for break sai do loop se for continue pula pra proxima iteracao

# fstring primeiro tipo de formataçao de string
# essa eh a maneira mais moderna de formatar strings
altura = 1.7800000000000002
variavel = f'Altura: {altura:.2f} m'
peso = 200
variable = 'ABCD'

# padding para ter no minimo 10 espaços, completando com ' ' a esquerda
print(f'{variable: >10}')

# padding para ter no minimo 10 espaços, completando com ' ' a direita
print(f'{variable: <10}')

# padding para ter no minimo 10 espaços, completando com ' ' a esquerda e direita (centro)
print(f'{variable: ^10}')

# padding para ter no minimo 10 espaços, completando com '0' a esquerda
# e 1 casa decimal, utilizando virgula como separador de milhar
# e mostrando o sinal do numero negativo (-) e positivo (+)
# posso substituir o '>' para '=' para o sinal de '+' vir antes de tudo
print(f'{1000.538457358348348:0>+10,.1f}')

# conversao de hexadecimal maiusculo com 8 casas
print(f'O hexadecimal de 1500 é {1500:08X}')



# bom tbm mas menos
# format segundo tipo de formataçao de string
variavel2 = '{nome1:.2f}{nome2}{nome3}sdfsdufh'
print(variavel2.format(
    nome1=altura, nome2=variavel, nome3=peso))

count = 19
nome = input(f'Digite um numero maior que {count} ')

# vem do c, nao tem mt coisa suportada
# interpolacao terceiro tipo de formataçao de string
nome = 'Arthur'
preco = 1000.583445
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print('O hexadecimal de %d é %x' % (15, 15))


#aqui se n for digitada uma senha, é false o input
#e ai senha armazena 'sem senha' pq ela é true, pq é um valor q nao é falsy ( 0, 0.0 e '')
senha = input('Senha:') or 'Sem senha'

if not senha:
    print('Senha não digitada')


nome = 'Arthur'

print('Ar' in nome) # true
print('mar' not in nome) # true
print(f'voce digitou {nome}')


frase = input('Digite uma frase: ')
encontrar = input('Digite uma palavra para encontrar na frase: ')

if encontrar in frase:
    print(f'Encontrou a palavra {encontrar} na frase')
else:
    print(f'Não encontrou a palavra {encontrar} na frase')


# fatiamento de strings
# [inicio:fim:passo]
# se o passo for positivo, ele vai do inicio para o fim
# o fim nao é incluso, ent se quiser que inclui o fim, coloca um a mais
# se o passo for negativo, ele vai do fim para o inicio
nome = 'Arthur'
# A r t h u r
#  0  1  2  3  4  5 ou
# -6 -5 -4 -3 -2 -1
print(nome[0]) # A
print(nome[1]) # r
print(nome[-1]) # r
print(nome[-2]) # u
print(nome[1:4]) # rth
print(nome[1:]) # rthur
print(nome[:4]) # Arth
print(nome[1::2]) # rhr
print(nome[::2]) # Atr
# inverter string (omitiu o inicio e o fim, ent sao considerados 0 e 6 nesse caso)
# porem, como estamos olhando ao contrario, 0 e 6 vira -1 e -7
print(nome[::-1]) # ruhtrA
print(nome[-1:-7:-1]) # mesmo coisa que o de cima, começa de -1 e vai até -7, de um em um
print(nome[::-2]) # rhr
print(len(nome)) # 6

# + em string concatena, * repete aquele numero de vezes
repet = 3
numero = input('digite uma frase: ')
print(
    f'Vou repetir sua frase {repet} vezes:\n'
    f'{numero * repet}'
    )

try:
    # executa td ate encontrar um erro
    # se ocorrer um erro, tipo conversao de 'a' pra inteiro, ele pula pro except e executa oq ta dentro do except
    # mas nao finaliza o programa
    ...
except:
    ...



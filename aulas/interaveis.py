# o while é mais utilizado quando nao sabemos quando o laço vai terminar
# tipo o while true para verificacao de entrada coerente do usuario

# ja o for eh mais utilizado quando sabemos o quanto vai rodar
# se for em uma string vai ser toda a string 

entrada = input('Digite qualquer frase\n')
# letra é uma variavel que acabei de criar
# o for é um iterador, ou seja, ele percorre indice por indice
# 'letra' é o nome que eu dei para esse indice
# portanto para cada indice deve executar o bloco de codigo abaixo
# IMPORTANTE: esse 'indice' o python ja pega o valor direto, portanto letra ja é o valor, nao um indice
for letra in entrada:
    print(letra)


# range + for
# range (inicio, fim, passo)
numeros = range(0,10,1)
# identico ao de cima
numeros = range(10)
# indo para os negativos
numeros = range(0, -10, -1)

print(numeros)
# numeros é um vetor com todos os elementos que o range devolveu
for num in numeros:
    print(num)

# podemos utilizar direto
for num2 in range(10000):
    print(num)

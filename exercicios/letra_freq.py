# letra mais frequente em uma frase digitada

frase = input('Digite qualquer frase:\n')
frase = frase.lower()
i = 0
letras = []
maior = 0
while i < len(frase):
    if frase[i] not in letras:
        letras.append(frase[i])
        if frase.count(frase[i]) > maior:
            maior = frase.count(frase[i]) 
    i += 1
print(maior)
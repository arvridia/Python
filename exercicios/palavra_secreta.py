import os
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
print("Jogo 'Palavra Secreta'\n---------------------------\n")
secret = 'Game'
secret = secret.lower()
user = []
i = 0
count = 0
aux = []
while i < len(secret):
    user += '*'
    i += 1
while True:
    aux = ''
    i = 0
    tentar = input('Digite uma tentativa de letra:\n')
    count += 1
    if len(tentar) > 1 or len(tentar) < 1:
        continue
    while i < len(secret):
        if secret[i] == tentar:
            user[i] = tentar
        i += 1
    for j in user:
        aux += j
    if aux == secret:
        break
    print(aux)
os.system("cls")
print("\nParabéns!!! Jogo concluído\nA palavra era:\n")
print(aux)
print(f"\nVocê realizou {count} tentativas...")



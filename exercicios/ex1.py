'''
Exericício 1
Peça para o usuario digitar seu nome
Peça para o usuario digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} e sua idade é {idade}
        Seu nome tem {tamanho do nome} letras
        Seu nome invertido é {nome invertido}
        Seu nome contem (ou nao) espaços
        A primeira letra do seu nome é {primeira letra}
        A ultima letra do seu nome é {ultima letra}
Se nome ou idade nao forem digitados:
    exiba "Voce deixou campos vazios"
'''

nome = input ('Digite seu nome:\n')
idade = input ('Agora digite sua idade:\n')
if nome and idade:
    print(
        f'Seu nome é {nome} e sua idade é {idade}\n'
        f'Seu nome tem {len(nome)} letras\n'
        f'Seu nome invertido é {nome[::-1]}\n'
        f'A primeira letra do seu nome é {nome[0]}\n'
        f'A ultima letra do seu nome é {nome[-1]}\n'
    )
    if ' ' in nome:
        print('Seu nome contem espaços\n')
    else:
        print('Seu nome nao contem espaços\n')
else:
    print('Voce deixou campos vazios\n')

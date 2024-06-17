






print('Welcome to the Calculator!\n\n-----------------------------\n')
flag = 0
while True:
    print("If you want to quit, insert '[q]uit'\n")
    num1 = input('Insert first number:\n')
    quer_sair = num1.lower() == 'quit' or num1.lower() == 'q'
    if quer_sair:
        flag = 1
        break
    else:
        num1 = int(num1)
    operator = input('Insert operator (+, -, * and /):\n')
    num2 = int(input('Insert second number:\n'))
    if operator == '+':
        result = num1 + num2
        break
    elif operator == '-':
        result = num1 - num2
        break
    elif operator == '*':
        result = num1 * num2
        break
    elif operator == '/':
        result = num1 / num2
        break
    else:
        print('Insert a valid operator!\n')

if flag == 1:
    print('Finalizando calculadora...\n')
else:
    print(f'Total calculation:\n{result}')
    




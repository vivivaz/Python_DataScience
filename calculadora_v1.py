# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def calculadora():
    operacao = int(input('Selecione o número da opção desejada:\n \n 1 - Soma\n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n \nDigite a sua opção: '))
    x = input('Digite o primeiro número: ')
    y = input('Digite o segundo número: ')
    if operacao == 1:
        z = int(x) + int(y)
        resultado = x + ' + ' + y
        print(f'{resultado} = {z}')
    elif operacao == 2:
        z = int(x) - int(y)
        resultado = x + ' - ' + y
        print(f'{resultado} = {z}')
    elif operacao == 3:
        z = int(x) * int(y)
        resultado = x + ' * ' + y
        print(f'{resultado} = {z}')
    elif operacao == 4:
        z = int(x) / int(y)
        resultado = x + ' / ' + y
        print(f'{resultado} = {z}')
    else:
        print('Operação inválida.')


calculadora()
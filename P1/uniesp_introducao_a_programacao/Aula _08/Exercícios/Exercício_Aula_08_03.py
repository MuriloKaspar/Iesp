#Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada.
#Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida. Adição, Subtração, Multiplicacão, Divisão e Potenciação.

from ast import match_case

#Exercicio para construir uma calculadora com +,-,*,/ e **

botao=1000

while botao != 0:
    print('Digite 1 para ADIÇÃO (+):')
    print('Digite 2 para SUBTRAÇÃO (-):')
    print('Digite 3 para MULTIPLICAÇÃO (X):')
    print('Digite 4 para DIVISÂO (:):')
    print('Digite 5 para EXPONENCIAÇÃO (N²):')
    print('Digite 0 para SAIR')
    botao=int(input('Escolha qual operação matemática você quer fazer:'))

    match botao:
        case 1:
            number1=float(input('Agora digite o primeiro número:'))
            number2=float(input('Agora o número que você deseja somar:'))
            resultado=number1+number2
            print(f'{number1} + {number2} = {resultado}')

        case 2:
            number1=float(input('Agora digite o primeiro número:'))
            number2=float(input('Agora o número que você deseja subtrair:'))
            resultado=number1-number2
            print(f'{number1} - {number2} = {resultado}')

        case 3:
            number1=float(input('Agora digite o primeiro número:'))
            number2=float(input('Agora o número que você deseja multiplicar:'))
            resultado=number1*number2
            print(f'{number1} X {number2} = {resultado}')

        case 4:
            number1=float(input('Agora digite o primeiro número:'))
            number2=float(input('Agora o número pelo qual você deseja dividir:'))
            resultado=number1/number2
            print(f'{number1} : {number2} = {resultado}')

        case 5:
            number1=float(input('Agora digite o primeiro número:'))
            number2=float(input('Elevado a que potencia?:'))
            resultado=number1**number2
            print(f'{number1} elevado a {number2}ª potencia = {resultado}')

        case 0:
            print('Ainda bem, não tava afim de calcular mesmo!')

        case _:
            print('Digite um operador matemático válido')
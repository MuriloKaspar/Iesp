#Atividade Avaliativa - Questão 1

print('Equação do 2° grau.')
print('x²-x+1=0, a = x², b = x, c = 1')

a = int(input('De valor à a: '))
b = int(input('De valor à b: '))
c = int(input('De valor à c: '))

print('A formula é (b*b - 4*a*c)')

delta = b*b-4*a*c

print(f'Delta é {delta}')
print('Resultado de x1 e x2')

x = (-b - (delta)**(1/2))/(2*a)
x1 = (-b + (delta)**(1/2))/(2*a)

print(f'x1 = {x1}, x2 = {x}')

#Atividade Avaliativa - Questão 2

print('Calcular a distancia entre dois pontos')
print('Raiz quadrada de (x2 - x1)² + (y2 - y1)²')

x1 = int(input('De valor à x1: '))
x2 = int(input('De valor à x2: '))
y1 = int(input('De valor à y1: '))
y2 = int(input('De valor à y2: '))

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print(f"A distancia entre os pontos é de {d:.2f} metros.")

#Atividade Avaliativa - Questão 3

from ast import match_case

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

#Atividade Avaliativa - Questão 4

print('Digite os respectivos valores de seu peso e altura, descubra seu IMC e como você está classificado =)')
print('Ao digitar os valores utilize . no lugar da , ')
peso=float(input('Digite seu peso (Kg)'))
altura=float(input('Digite sua altura (m)'))
imc=peso/(altura**2)

print(f'seu imc é {imc:,.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Você está no peso normal')

elif imc >=25 and imc < 30:
    print('Você está acima do peso')

else:
    print('Você está Obeso')

#Atividade Avaliativa - Questão 5

lista1=[]
lista2=[]
lista3=[]
lista4=[]

numeros=1000

while numeros >=0:

    numeros=float(input('Digite numeros aleatorios (positivos e negativos):'))
    
    if numeros >=0 and numeros <=25:
        lista1.append(numeros)
        
    elif numeros >=26 and numeros <=50:
        lista2.append(numeros)
        
    elif numeros >=51 and numeros <=75:
        lista3.append(numeros)
        
    elif numeros >=76 and numeros <=100:
        lista4.append(numeros)

    elif numeros > 100:
        numeros

    else:
        print('a quantidade de numeros entre:')
        print(f'0-25 = {len(lista1)}')
        print(f'26-50 = {len(lista2)}')
        print(f'51-75 = {len(lista3)}')
        print(f'76-100 = {len(lista4)}')

#Atividade Avaliativa - Questão 6

from math import factorial

n=int(input('Informe um número inteiro para calcular o seu fatorial: '))
f=factorial(n)
v=n
while v > 0:
    print(f'{v}', end ='')
    print(' x ' if v>1 else ' = ', end ='')
    v-=1
print(f'{f}')
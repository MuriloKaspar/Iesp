#Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado.
#Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

from math import factorial

n=int(input('Informe um número inteiro para calcular o seu fatorial: '))
f=factorial(n)
v=n
while v > 0:
    print(f'{v}', end ='')
    print(' x ' if v>1 else ' = ', end ='')
    v-=1
print(f'{f}')
#Faça um algoritmo para ler um vetor de 30 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.

from random import randint

vetor=[]
qnt=[]

for i in range(30):
    vetor.append(randint(0,20))

print(vetor)

n = int(input('Digite um numero de 0 a 9 para ver quantas vezes ele aparece na lista: '))

for x in vetor:
    if (x == n):
        qnt.append(x)
        
if (len(qnt) == 0):
    print(f'<<<<<< O número {n} não aparece no vetor. >>>>>>')
else:
    print(f'<<<<<< O número {n} aparece no vetor {len(qnt)} vezes. >>>>>>')
# import random

# vetor = []

# for i in range(30):
#     t = random.randint(0, 30)
#     vetor.append(t)

# n = int(input("Digite o número que deseja pesquisar entre 0 e 30: "))

# print(vetor)

# if n in vetor:
#     x = vetor.count(n)
#     print(f"O número {n} apareceu {x} vezes na relação aleatória.")
# else:
#     print(f"O número {n} não apareceu na relação aleatória.")

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
    print(f'O número {n} não aparece no vetor.')
else:
    print(f'O número {n} aparece no vetor {len(qnt)} vezes.')
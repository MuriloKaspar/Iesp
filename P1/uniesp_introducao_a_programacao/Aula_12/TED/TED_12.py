# Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
# Depois:Imprima o resultado da soma de todos os valores da matriz no terminal;
# E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

from random import randint

MA = []
MB = []

for l in range(10):
    linha = []

    for c in range(10):
        linha.append(randint(0, 30))

    MA.append(linha)

for linha_matriz in MA:
    print(linha_matriz)

for linha in MA:
    soma = sum(linha)
    print(soma)
    MB.append(soma * 3)

print(MB)
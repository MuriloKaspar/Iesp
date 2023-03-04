matriz = [
    [[4,5,6],[7,8,9],[10,11,12]],
    [2,3,4],
    [4,8,12]
]

print(matriz[0])
print(matriz[0][1])
print(matriz[0][1][0])

#outro exemplo

matriz = [4,5,6],[7,8,9],[10,11,12]

for linha in matriz:
    for coluna in linha:
        print(coluna)

#exemplo usando nome

matriz = ["Murilo",[10,11,12]]

for linha in matriz:
    for coluna in linha:
        print(coluna)

#usando range e lens
for numero in range(2,10,4):
    print(numero)
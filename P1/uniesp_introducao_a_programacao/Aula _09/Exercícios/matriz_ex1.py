n=0
matriz = [
    [78,90,100,98,7],
    [56,77,93,77,93],
    [10,4,73,77,93],
    [78,90,100,77,93],
    [10,4,73,90,100]
]

for linha in matriz:
    print(linha[n])
    n=n+1

#usando range ## % 2 = resto da divisão por 2
for linha in range(len(matriz)):
    for coluna in range(len(matriz[1])):
        if linha == coluna:
            print(matriz[linha][coluna])
        
        if (matriz[linha][coluna] % 2) == 0:
            print(f"{matriz[linha][coluna]} -> É par!")

        else:
            print(f"{matriz[linha][coluna]} -> É impar!")
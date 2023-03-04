lista_mercado = []

while True:
    op = int(input(" \
                    1 - Adicionar frutas\n \
                    2 - Remover frutas\n \
                    3 - Lista de frutas\n \
                    0 - Sair do programa\n \
                    Digite a opção: "))

    if op == 1:
        #Adicionar objetos a lista
        item = input("Digite um item: ")
        lista_mercado.append(item)

    elif op == 2:
        #Remover objetos da lista
        item = input("Digite o item que será removido: ")
        indice_item = lista_mercado.index(item)
        del lista_mercado[indice_item]

    elif op == 3:
        for item in lista_mercado:
            print(item)

    elif op == 0:
        break
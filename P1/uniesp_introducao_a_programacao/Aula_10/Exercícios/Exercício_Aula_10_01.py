#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

lista_times = []

print("<<<<<<  Adicione o nome de 10 clubes de futebol à lista  >>>>>>")

clube = str(input("Digite o nome de um clube para adicionar a lista: "))
lista_times.append(clube)

while len(lista_times) <= 9:
    clube = str(input("Digite o nome de mais um clube: "))
    if clube in lista_times:
        print("<<< Esse clube já foi adicionado! >>>")
    else:
        lista_times.append(clube)
    
print("<<<<<<  A lista de clubes foi preenchida!  >>>>>>")

pesq = str(input("Digite o nome do clube que deseja procurar: "))

if pesq in lista_times:
    print(f"<<< ACHEI. O clube {pesq} encontra-se na lista. >>>")
else:
    print(f"<<< NÃO ACHEI. O clube {pesq} não foi encontrado na lista. >>>")

#Solução Nº 2

# clubes = []

# for i in range(10):

#     clube = input("Digit o novo clube: ")
#     clubes.append(clube)

# clube_pesquisar = input ("Procure o nome do clube: ")

# for c in clubes:
#     if clube_pesquisar.upper() == str(c).upper():
#         print("Achei!")
#     else:
#         print("Não Achei!")
#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. 
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

qtm = (int(input("Informe quantas de maçãs desejada comprar: ")))

if qtm < 12:
    total = qtm * 1.30
    print(f'O valor total da compra é de {total} reais')
else:
    total = qtm * 1
    print(f'O valor total da compra é de {total} reais')
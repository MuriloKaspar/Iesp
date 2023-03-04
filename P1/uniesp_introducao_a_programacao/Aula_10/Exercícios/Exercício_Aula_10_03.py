#Ler um vetor Q de 20 posições (aceitar somente números positivos). Escrever a seguir:
# a. o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
# b. o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

q=[]

while len(q) <20:
    num=int(input("Digite Numeros Inteiros para adiciona-los na lista:"))
    if num in q:
       print('Numero repetido, digite outro')
    
    elif num < 0:
        print("Digite apenas Numeros Positivos")
        
    else:
        q.append(num)
        


menval=q[0]
maval=q[0]

for valor in q:
    if valor > maval:
        maval=valor
        
print(f'O valor do maior elemento de Q é {maval} e seu índice é {q.index(maval)}')

for valor in q:
    if valor < menval:
        menval=valor

print(f'O valor do menor elemento de Q é {menval} e seu índice é {q.index(menval)}')
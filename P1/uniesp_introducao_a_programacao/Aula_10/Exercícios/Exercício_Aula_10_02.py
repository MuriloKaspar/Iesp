#Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

acumuladora = 0
notas = []
contador = 0

#Criação da lista das notas
for i in range(20):
    notas.append(float(input("Digite uma nota: ")))

#Soma
for nota in notas:
    acumuladora = acumuladora + nota

#Media
media = acumuladora / len(notas)

#contador = contador + 1
for n in notas:
    if n > media:
        contador += 1

print(f"{contador} foram as notas acima da média.")
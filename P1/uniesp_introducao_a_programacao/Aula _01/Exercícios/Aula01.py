# "if", "elif" e "else" estrutura condicional. Criar 2 "if" cria 2 inicios, então é aconselhavel usar um "else" ou "elif", de 
# acordo com a necessidade.
# O ":" equivale a um então no fim do desvio
# "int()" é utilizado para numeros inteiros
# "str()" é uma string, é um conjunto de carateres, texto
# "float()" números com casa fracionada
# "bool()" boolean, true e false, verdadeiro ou falso
# "input()" gera uma string
#  Um "cast" é transformar um tipo de dado em outro. Transformar um str em um int. ex.: nota=int(input("Digite uma nota: "))

# "len" quantos caracteres ou objetos tem em uma lista ou nome
nome = "Klebio"
print(type(nome))
print(len(nome))

lista_a = [1, 2, 5, 6, 9]
print(len(lista_a))

## O que fazer quando queremos realiza uma atividade repetitiva?

gatilho = 0.8
lista_vendedores = [0.8, 0.25, 0.5, 1.2, 1.0]

result_soma = 0

# "for" para lista com objetos encadeados com inicio e fim

for vendedor in lista_vendedores:
    result_soma = result_soma + vendedor

# 0.8 + 0
# 0.25 + 0.8
# 0.5 + 1.05
# 1.2 + 1.55
# 1.0 + 2.75
# Result_soma = 3.75

media = result_soma / len(lista_vendedores)

maior_vendedor = 0
menor_vendedor = 10000

if media >= gatilho:
    print("Campanha válida! Equipe de parabéns!!")
    for vendedor in lista_vendedores:
       
        if vendedor > maior_vendedor:
            maior_vendedor = vendedor
        
        elif vendedor < menor_vendedor:
            menor_vendedor = vendedor

        else:
            print("O vendedor é igual, perdeu a vez!")
else:
    print("A campanha foi um fracasso!")

print("-----------------------------")
print(f"O maior vendedor, vendeu {maior_vendedor}")
print("-----------------------------")


## "range" é um objeto q cria uma lista de numeros

lista_num = list(range(0, 100, 2))
print(lista_num)

# outro exemplo
for num in range (0, 100, 2):
    print(f"Quem é num? -> {num}")
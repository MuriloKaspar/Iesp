# encoding = compatibilidade de linguagem
# "r" = leitura, read
# "\n" pular uma linha
# Tem que estar na mesma pasta

with open ("Aula_13.txt","r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo, "\n")

with open ("Aula_13.txt","r", encoding="utf-8") as arquivo:
    x = 0
    for linha in arquivo:
        print(f"Linha: {x} Conteudo: {linha}", "\n")
        x = x + 1

arquivo_de_linhas = []

with open ("Aula_13.txt","r", encoding="utf-8") as arquivo:
    arquivo_de_linhas = arquivo.readlines()

print (arquivo_de_linhas, "\n")

for linha in arquivo_de_linhas:
    conteudo_linha = linha.split(".")
    print(conteudo_linha)
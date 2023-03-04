# "a" adiciona uma entrada de texto
# "w" sobrescreve o texto existente

nome = "Murilo"

with open ("Aula_13_02.txt","w", encoding="utf-8") as arquivo:
    for line in range(10):
        arquivo.write(f"{line} - Eu me chamo {nome}\n")

nome = "Murilo"

with open ("Aula_13_02.txt","a", encoding="utf-8") as arquivo:
    for line in range(10):
        arquivo.write(f"{line} - Meu nome é {nome}\n")

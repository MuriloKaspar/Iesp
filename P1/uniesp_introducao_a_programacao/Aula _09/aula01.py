# Identificador nome e uma lista de nomes
nomes = ["Messias", "Emanuel", "Miguel", "João"]

# Imprimir a lista
print(nomes)

# Verificar o tipo de dado
type(nomes)

# Acessando um elemento da lista
# nome_da_lista[posição]

nomes[0]

# Lista de frutas
frutas = ["pêra", "uva", "maçã", "kiwi"]

# Alterando o elemento que está na posição 1
frutas[1] = "abacate"

#'''O método insert() ajuda você a adicionar um elemento em qualquer posição desejada, deslocando os elementos seguintes'''

frutas.insert(2, "morango")

#'''A instrução del() pode remover um item da lista
#passando como parâmetro sua posição. Lembre-se, para
#isso você deve conhecer a posição do item na lista.
#Você pode pesquisar o índice (posição) de um item da
#lista com a função index()'''

del frutas[4]

# Vamos descobrir o índice da fruta
indice_fruta = frutas.index("melancia")

# Com o valor do índice, a gente deleta
del frutas[indice_fruta]
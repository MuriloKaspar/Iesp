# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. 
# Ao final, exiba o nome de cada pessoa e seu número favorito.

nfav = {"Murilo": 38, "Marcos": 10, "Andre": 20, "Tony": 7, "Dorgival": 33}

for r,s in nfav.items():
    print(f'O número preferido de {r} é {s}.')
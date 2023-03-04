# Use um dicionário para armazenar informações sobre uma pessoa que você conheça.
# Armazene seu primeiro nome. O sobrenome. A idade e a cidade em que ela vive. 
# Você deverá ter chaves como primeiro_nome, sobrenome, idade, e cidade. 
# Por fim, mostre cada informação armazenada em seu dicionário.


dic={
    'Primeiro_nome': 'Fernando',
    'Sobrenome': 'Braz',
    'Idade': '33',
    'Cidade':'João Pessoa'
}

for info in dic.items():
    print(info)
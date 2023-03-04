#Ler o ano atual e o ano de nascimento de uma pessoa.
#Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = (int(input("Informe o ano atual: ")))
ano_nasc = (int(input("Informe o ano seu ano de nascimento: ")))

if ano_atual - ano_nasc < 16:
    print("Você não pode votar na eleição deste ano!")
elif ano_atual - ano_nasc >= 18 and ano_atual - ano_nasc <=70:
    print("Você deve votar na eleição deste ano!")
else:
    print("O voto é facultativo para você na eleição deste ano!")

#Site utilizado para referencia: https://www.tutorialsteacher.com/python/python-if-elif
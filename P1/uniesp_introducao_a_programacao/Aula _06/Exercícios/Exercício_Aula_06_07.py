#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

cadastro = []

botao = 1000

while botao != 0:
    print("Digite 1 para cadastrar um novo usuário.")
    print("Digite 2 para imprimir todos os usuários.")
    print("Digite 0 para sair")
    botao = int(input("digite a opção desejada: "))

    if botao == 1:
        #entrada dos dados
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o e-mail: ")
        
        #"Folha" de cadastros, só existe dentro do if
        dados = [nome, idade, email]
        
        #Append cria um conjunto de dados com a "Folha" de cadastros
        cadastro.append(dados)
    
    elif botao == 2:
        for p in cadastro:
            print(p)
    elif botao == 0:
        print("Obrigado por acessar este software!")
    else:
        print("digite um número válido!")
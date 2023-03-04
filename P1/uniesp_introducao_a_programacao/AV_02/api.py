# ****************************************************
# ******   Projeto de avaliação Unidade 2       ******
# ******          Turma: SI/SPI - P1B           ******
# ****************************************************
# ******                 ALUNOS:                ******
# ******                                        ******
# ******       Fernando Braz da Silveira        ******
# ******       Jayme Holanda Aguiar             ******
# ******       Murilo Kaspar Deininger Neto     ******
# ****************************************************

import json
from os import system
import requests

CLEAR = 'cls'
CAD = 'locais.txt'
BARRA = '|'
LIMITE = 3
API_KEY = open("api_key.txt", "r").read()

def menu():
    print('\n','-' * 44)
    print('|              GEOPOSICIONAMENTO             |')
    print('', '-' * 44)
    print('|1 - Cadastrar Cidade                        |')
    print('|2 - Cidades Cadastradas                     |')
    print('|3 - Obter informação de uma cidade          |')
    print('|4 - Obter informação das cidades cadastradas|')
    print('|5 - Sair                                    |')
    print('', '-' * 44,'\n')
    
    escop = int(input('Escolha uma das operações: '))
    return escop

def vazio(dado):
    if dado == None or dado == '' or (type(dado) == list and len(dado) == 0) or (type(dado) == list and (len(dado) == 1 and dado[0] == '')):
        return True
    else:
        return False

def pausar():
    print('\n')
    input('Pressione qualquer tecla para continuar')

def cadcid(info):
    try:
        with open(CAD, 'a', encoding='UTF-8') as b_dados:
            b_dados.write(info + '\n')
        print('<< Cidade cadastrada com sucesso! >>')
        
    except (ValueError, TypeError):
        print(f'<< Ocorreu um erro ao cadastrar uma cidade >>')

def lerbdados():
    try:
        with open(CAD, 'r',encoding='UTF-8') as b_dados:
            dados = []
            for linha in b_dados.readlines():
                linha = linha.replace('\n','').split(BARRA)
                dados.append(linha)
        return dados
    
    except FileNotFoundError:
        print(f'<< Banco de dados não encontrada, cadastre uma cidade ou crie o arquivo {CAD} no mesmo diretorio >>')

def callapi(API_KEY,latitude,longitude):
    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}')
    resposta = requests.request("GET", url)
    return resposta.json()

def expocid(nome_cidade,dados):
    try:
        nome_arquivo = nome_cidade + '.json'
        
        with open(nome_arquivo, 'w',encoding='UTF-8') as arquivo:
            dados_json = json.dumps(dados, indent=4)
            arquivo.write(dados_json)
    except (ValueError, TypeError):
        print(f'<< Ocorreu um erro >>')

while True:
    op = menu()
    
    if op <= 0 or op > 5:
        print(f'\n<< Opção inválida: {op} >>')
        print(f'<< Escolha um número de 1 a 5 >>')
        pausar()
        
    if op == 1:
        print('\n','-' * 45)
        print(f'\t  Cadastro de cidades')
        print('-' * 45,'\n')
        nome_cidade = input('Informe o nome da cidade: ')
        lat = input('Informe a latitude: ')
        lon = input('Informe a longitude: ')
        dados = BARRA.join([nome_cidade,lat,lon])
        print('\n')
        cadcid(dados)
        pausar()
        
    elif op == 2:
        print('\n')
        print('-'*45)
        print(f'\t  Listando cidades')
        print('-' * 45,'\n')
        dados = lerbdados()
        contador = 1
        
        if not vazio(dados):
            
            for info in dados:
                print(f'{contador} - {info[0]} | Latitude: {info[1]} | Longitude: {info[2]}')
                contador += 1
                
        else:
            print('-' * 45)
            print('<< Nenhuma cidade cadastrada! >>')
            print('-' * 45)
        pausar()
        
    elif op == 3:
        print('\n')
        print('-' * 45)
        print(f' Obter informações da cidade no API')
        print('-' * 45,'\n')
        dados = lerbdados()
        contador = 1
        linha = 0
        
        if not vazio(dados):
            
            for info in dados:
                
                if linha == LIMITE:
                    print(' ')
                    linha = 0
                print(f'({contador}) - {info[0]}',end='  ')
                contador += 1
                linha += 1

            cidade_id = int(input('\n\n Digite o número da cidade que deseja consultar: '))
                        
            if cidade_id <= 0 or cidade_id > len(dados):
                print(f'<< Opção inválida: {cidade_id} >>')
                
            else:
                print('\n\t << Gerando informações da cidade... >> \n')
                lat = dados[cidade_id - 1][1]
                lon = dados[cidade_id - 1][2]
                cidade = dados[cidade_id - 1][0]

                dados_cidade = callapi(API_KEY,lat,lon)
                expocid(cidade,dados_cidade)
                print(f'<< O arquivo com as informações da cidade foi criado: {cidade}.json >>')
        else:
            print('<< Nenhuma cidade cadastrada >>')
        pausar()
        
    elif op == 4:
        print('\n')
        print('-' * 45)
        print('Obtendo informação das cidades cadastradas')
        print('-' * 45,'\n')
        dados = lerbdados()
        
        if not vazio(dados):
            
            for info in dados:
                cidade = info[0]
                lat = info[1]
                lon = info[2]
                dados_json = callapi(API_KEY,lat,lon)
                expocid(cidade,dados_json)
                print(f'<< Arquivo com as informações de {cidade} criado: {cidade}.json >>\n')
        else:
            print('\n','<< Nenhuma cidade cadastrada >>')
        pausar()
        
    else:
        system(CLEAR)
        print('-' * 45)
        print('Programa Encerrado')
        print('-' * 45)
        break
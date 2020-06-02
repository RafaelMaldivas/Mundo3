# Faça um programa que leia o nome e a média de um aluno
# o programa deverá contem um esquema de cadastro de alunos
# matérias, notas, médias
from pip._vendor.distlib.compat import raw_input
from random import randint
from time import sleep
Lista_Geral = []
Filmes = {}


def exibirMenu():
    print("[ 1 ] Cadastrar")
    print('[ 2 ] Listar Cadastros')
    print('[ 3 ] Excluir')
    print('[ 4 ] Alterar')
    print('[ 5 ] Sair')
    opc = int(input('Escolha uma opção : '))
    return opc


def cadastrar():
    id = randint(1, 1000)
    Filmes['Id'] = id
    Filmes['Titulo'] = raw_input("Digite o título do filme : ").strip().capitalize()
    Filmes['Ano'] = int(input('Digite o ano do filme : '))
    Filmes['Gênero'] = raw_input('Digite o gênero do filme :').strip().capitalize()
    Filmes['Diretor'] = raw_input('Digite o diretor do filme :').strip().capitalize()
    Lista_Geral.append(Filmes.copy())


def listar():
    for e in Lista_Geral:
        print(' - - - - - - - - - - - - - - - - - - ')
        for k, v in e.items():
            print(f'{k} : {v}')
        print(' - - - - - - - - - - - - - - - - - - ')


def excluir():
    id = int(input(" - Digite o número do Id do filme que deseja excluir :"))
    indice = -1
    encontrou = False
    for e in Lista_Geral:
        indice += 1
        for k, v in e.items():
            if id == v:
                encontrou = True
                break
    if encontrou:
        resp = raw_input(f'Tem certeza que deseja deletar {Lista_Geral[indice]}? [S/N]')[0].upper()
        if resp == 'S':
            print('Exclusão Sucedida!!')
            del Lista_Geral[indice]


def alterar():
    id = int(input(" - Digite o número do Id do filme que deseja alterar :"))
    indice = -1
    encontrou = False
    for e in Lista_Geral:
        indice += 1
        for k, v in e.items():
            if id == v:
                encontrou = True
                break
    if encontrou:
        del Lista_Geral[indice]
        Filmes['Id'] = id
        Filmes['Titulo'] = raw_input("Digite o título do filme : ").strip().capitalize()
        Filmes['Ano'] = int(input('Digite o ano do filme : '))
        Filmes['Gênero'] = raw_input('Digite o gênero do filme :').strip().capitalize()
        Filmes['Diretor'] = raw_input('Digite o diretor do filme :').strip().capitalize()
        Lista_Geral.append(Filmes.copy())



while True:
    print("-"*30)
    print(f'{"Locadora 90s":^30}')
    print("-"*30)
    opc = exibirMenu()
    print('-'*30)
    if opc == 4:
        alterar()
    if opc == 1:
        cadastrar()
    if opc == 2:
        listar()
    if opc == 3:
        excluir()
    if opc == 5:
        print('Fechando Programa')
        sleep(1)
        print('. . .')
        sleep(1)
        print('. . . ')
        break

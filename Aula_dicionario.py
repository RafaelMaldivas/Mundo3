from pip._vendor.distlib.compat import raw_input
from random import randint
escola = [[],[],[]]
aluno = {}
notas = {}

def cadastro_aluno():
   print('-'*30)
   aluno['matrícula'] = randint(1, 1000)
   aluno['nome'] = raw_input("Nome : ")
   aluno['idade'] = int(input("Idade : "))
   aluno['ano'] = int(input('ano: '))
   if aluno['ano'] == 1:
       escola[0].append(aluno.copy())
   if aluno['ano'] == 2:
       escola[1].append(aluno.copy())
   if aluno['ano'] == 3:
       escola[2].append(aluno.copy())

def cadastro_notas():
    indice = -1
    nota = []
    print('-' * 30)
    ano = int(input('Para qual ano deseja inserir a nota :'))
    for i in escola[ano-1]:
        print('-'*30)
        for k, v in i.items():
            if k == 'matrícula':
                print(f'{k} : {v}', end='  ')
            if k == 'nome':
                print(f'{k} : {v}')
        print('-'*30)
    matricula = int(input('Para qual matrícula deseja vincular a nota :'))
    local = False
    for k, v in aluno.items():
        if v == matricula:
            local = True
    if local:
        notas['matéria'] = raw_input('Digite o nome da matéria :')
        qtd = int(input('Digite Quantas notas deseja cadastrar :'))
        for i in range(0, qtd):
            notas[f'nota{i+1}'] = float(input(f' - Digite a {i+1}ª nota : '))


while True:
    cadastro_aluno()
    cadastro_notas()
    print(escola)


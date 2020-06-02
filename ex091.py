from random import randint
from time import sleep
dados ={}
aposta = 0
crédito = 100
print('-'*30)
print(f'\033[32m{"Jogo dos Dados":^30}\033[m')
print(f'\033[31m{"Ganhe créditos apostando com 5 jogadores":^30}\033[m')
print('-'*30)
n = 0
perde = ganha = rodada = 0
totperda = totganho = 0
while True:
    print(f'\033[35mCrédito = {crédito}\033[m')
    n = int(input('\033[34m Digite 1 para começar o jogo ou 2 para sair do jogo: > \033[m'))
    if n < 1 or n > 2:
        print('\033[31mNúmero inválido!!!\033[m')

    if n == 1:
        print('-'*30)
        nome = input(' - Digite o seu nome : ').strip().capitalize()
        crédito = 100
        while crédito > 0:
            print(f'\033[32mCrédito = {crédito}\033[m')
            aposta = float(input(' - Digite o valor da aposta R$: '))
            if aposta <= crédito:
                rodada += 1
                print('-'*30)
                d = randint(1, 6)
                dados[f'{nome}'] = d
                for i in range(1, 6):
                    d1 = randint(1, 6)
                    dados[f'jogador{i}'] = d1

                    if d1 > d:
                        totperda += aposta
                        perde += 1
                    elif d1 < d:
                        totganho += aposta
                        ganha += 1
                    elif d1 == d:
                        crédito = crédito
                print('-' * 30)
                sleep(1)
                print(f'\033[1;32m{"Jogando os dados!!":^30}\033[m')
                sleep(1.5)
                for k, v in dados.items():
                    sleep(1.5)
                    print(f' -\033[31m {k:^8} \033[m: dado =\033[32m {v}\033[m')
                print(f'\033[36mRodada {rodada} : {nome} ganhou de {ganha} jogadores e perdeu para {perde} jogadores\033[m')
                print(f'\033[33m - Ganhou um total de R${totganho} e perdeu um total de R${totperda}\033[m')
                if totganho > totperda:
                    print(f'\033[34mLucro de R${totganho-totperda}\033[m')
                    crédito += (totganho - totperda)
                elif totperda > totganho:
                    print(f'\033[31mPrejuízo de R${totperda-totganho}\033[m')
                    crédito -= (totperda - totganho)
                perde = ganha = totperda = totganho = 0
            else:
                print('\033[31mA sua aposta deve ser menor ou igual ao saldo de créditos !!\033[m')
                sleep(0.5)
            if crédito <= 0:
                sleep(1.5)
                print('\033[31mAcabaram seus créditos !!\033[m')
                sleep(1)
                del dados[f'{nome}']


    if n == 2:
        sleep(2)
        print('\033[31m\n\n - Fim de Jogo - \033[m')
        sleep(2)
        break







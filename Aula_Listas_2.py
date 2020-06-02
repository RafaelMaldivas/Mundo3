# nesta aula irei verificar propriedades como lista dentro de lista
# só para relembrar:
# append (adicona dados no final da lista)
# insert(posição da lista, dados a ser adicionado)
# del(deleta lista)
# pop(vaziio elimina ultimo dado da lista);(posição, dado a ser eliminado)
from random import randint

jogador = '\033[1;35;42mX\033[m'
comp = '\033[1;37;41mO\033[m'
vencedor = ''
tabuleiro = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
temp = []
print('**' * 20)
print(f'\033[1;34m{"** Jogo da Velha **":^40}\033[m')
print('**' * 20)
vitória = True
pontos = 0

while vitória:
    if pontos != 0:
        print(f'Pontos : {pontos}')

    # imprimindo tabuleiro
    for i in range(0, 9, 3):
        print(f'            [\033[1;34m{tabuleiro[i]}\033[m]   [\033[1;34m{tabuleiro[i + 1]}\033[m]   [\033[1;34m{tabuleiro[i + 2]}\033[m]')
    # entrando com X
    while True:
        mx = int(input(f'Jogador {jogador} :> Digite o número que quer jogar : '))
        if mx >= 1 and mx <=9:
            mx = mx - 1
            if jogador == tabuleiro[mx] or comp == tabuleiro[mx]:
                print('Número Inválido!!')
            else:
                tabuleiro[mx] = jogador1

                temp.append(mx)
                break
        else:
            print(' - - Número Inválido - - ')
    # condição para ganhar na horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i + 1] == tabuleiro[i + 2]:
            print(f'Jogador {tabuleiro[i]} Venceu!!')
            if tabuleiro[i] == comp:
                pontos -= 1
            elif tabuleiro[i] == jogador:
                pontos += 1
            # imprimindo tabuleiro
            for i in range(0, 9, 3):
                print(f'           [{tabuleiro[i]}]   [{tabuleiro[i + 1]}]   [{tabuleiro[i + 2]}]')
            # condição de continuar com o jogo

            resp = str(input("Deseja continuar ?[s/n] :")).strip().lower()
            if resp == 'n':
                print('\033[1;31m - - Game Over - - \033[m')
                vitória =False
            elif resp == 's':
                temp.clear()
                tabuleiro = [1, 2, 3,
                             4, 5, 6,
                             7, 8, 9]

        # condição para ganhar na vertical
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6]:
            print(f'Jogador {tabuleiro[i]} Venceu!!')
            if tabuleiro[i] == comp:
                pontos -= 1
            elif tabuleiro[i] == jogador:
                pontos += 1
                # imprimindo tabuleiro
            for i in range(0, 9, 3):
                print(f'            [{tabuleiro[i]}]   [{tabuleiro[i + 1]}]   [{tabuleiro[i + 2]}]')
                # condição de continuar com o jogo


            resp = str(input("Deseja continuar ?[s/n] :")).strip().lower()
            if resp == 'n':
                print('\033[1;31m - - Game Over - - \033[m')
                vitória = False

            elif resp == 's':
                temp.clear()
                tabuleiro = [1, 2, 3,
                             4, 5, 6,
                             7, 8, 9]


        # condição para ganhar na diagonal:
    for i in range(0, 3, 2):
        if tabuleiro[0 + i] == tabuleiro[4] == tabuleiro[8 - i]:
            print(f'Jogador {tabuleiro[i]} Venceu!!')
            if tabuleiro[i] == comp:
                pontos -= 1
            elif tabuleiro[i] == jogador:
                pontos += 1
                # imprimindo tabuleiro
            for i in range(0, 9, 3):
                print(f'            [{tabuleiro[i]}]   [{tabuleiro[i + 1]}]   [{tabuleiro[i + 2]}]')
                # condição de continuar com o jogo


            resp = str(input("Deseja continuar ?[s/n] :")).strip().lower()
            if resp == 'n':
                print('\033[1;31m - - Game Over - - \033[m')
                vitória = False

            elif resp == 's':
                temp.clear()
                tabuleiro = [1, 2, 3,
                             4, 5, 6,
                             7, 8, 9]

    # entrando  com O
    while True:
        mo = randint(0, 8)
        if jogador == tabuleiro[mo] or comp == tabuleiro[mo]:
            print('Jogador O - pensando ...')
        else:
            tabuleiro[mo] = comp
            temp.append(mo)
            break

    #condição de empate
    if len(temp) == 9:
        print("Empate")
        # imprimindo tabuleiro
        for i in range(0, 9, 3):
            print(f'            [{tabuleiro[i]}]   [{tabuleiro[i + 1]}]   [{tabuleiro[i + 2]}]')
            # condição de continuar com o jogo

            resp = str(input("Deseja continuar ?[s/n] :")).strip().lower()
            if resp == 'n':
                print('\033[1;31m - - Game Over - - \033[m')
                vitória = False
            elif resp == 's':
                temp.clear()
                tabuleiro = [1, 2, 3,
                             4, 5, 6,
                             7, 8, 9]


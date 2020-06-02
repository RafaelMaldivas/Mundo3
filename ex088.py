#palpites para a Mega Sena
import random
import time
mega = []
sena = []
aposta = []
crédito = 100
while True:
    print('-=-'*15)
    print(f'{"JOGA NA MEGA SENA":^40}')
    print('-=-'*15)
    print(f'Crédito R${crédito},00')
    if len(aposta) > 0:
        print(f'Aposta anterior {aposta}')
    print('Faça a sua aposta:')
    aposta.clear()
    sena.clear()
    for j in range(0, 6):
        while True:

            jogo = int(input(f'Digite o {j+1}º nº da sua aposta : '))
            if jogo <= 60:
                if jogo not in aposta:
                    aposta.append(jogo)
                    break
            else:
                print('Número inválido, Tente novamente!!')
    aposta.sort()
    print(f'A sua aposta é : {aposta}')
    print('Cada aposta vale R$2,00')
    while True:
        sorteio = int(input('Quantos Jogos gostaria de participar com a sua aposta:'))
        if sorteio*2 > crédito:
            print('VocÊ não tem Créditos suficentes para esta aposta!!')
        else:
            break
    cont1 = 1

    while cont1 <= sorteio:
        cont = 0
        while True:
            n = random.randint(1, 60)
            if n not in mega:
                cont += 1
                mega.append(n)
            if cont >= 6:
                break
        mega.sort()
        sena.append(mega[:])
        mega.clear()
        cont1 += 1
    print('-=-'*15)
    valor = 0
    conts = 0
    conta = 0
    for k, v in enumerate(sena):
        time.sleep(0.5)
        print(f'Jogo {k+1}   :   {v}')
        for i in aposta:
            if i in v:
                print(f' [{i}]', end=' ')
                conts += 1
                conta += 1
        time.sleep(0.5)
        print(f'Você acertou um total de {conts} números  ')
        time.sleep(0.5)
        if conts == 0:
            print('Errou Todos!!')
        elif conts <=3:
            print('Acertou uns números, não ficou ricou, mas também não perdeu nada! !! :(')
        elif conts > 3:
            print('VocÊ acertou 4 números ganhou R$100.000,00')
            valor += 100000
        elif conts > 4:
            print('Você acertou 5 números ganhou R$500.000,00')
            valor += 500000
        elif conts == 6:
            print('VocÊ Ganhou a MEGA SENA está Milhonário!!!')
            valor += 1000000
        valor = conta * 2
        conts = 0
    time.sleep(0.5)
    print(f'Total de Jogos = {sorteio}, total de acertos {conta},\nValor total da aposta R${2*sorteio} total arrecadado R${valor}, total de prejuízo R${(2*sorteio)- valor} ')
    crédito = crédito - (sorteio * 2 - valor)
    if crédito == 0:
        print('Acabou seus créditos para aposta!!')
        break
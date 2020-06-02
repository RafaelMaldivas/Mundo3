# dividindo valores em várias listas
import random
acertos = []
lista = []
lista_premio = []
print('-'*40)
print("-"*40)
print( f'{"Jogo da Mega Sena":^40}')
print('-'*40)
print("-"*40)
resp = " "
while True:
    print(f'{"Digite 6 números do 1 ao 60":^40}')
    for i in range(0,6):
        while True:
            num = int(input(f'Digite o {i+1}º número da aposta: '))
            if num > 60:
                print('Número inválido!')
            elif num in lista:
                print('Número Repetido!')
            else:
                lista.append(num)
                break



    for c in range(0,6):
        n = random.randint(1, 60)
        if n not in lista_premio:
            lista_premio.append(n)
    cont = 0
    for x in lista:
        for j in lista_premio:
            if x == j:
                cont += 1
                acertos.append(x)


    print(f'Vc apostou os números {lista}')
    print(f'A lista premiada foi {lista_premio}')
    if cont == 0:
        print('Você não acertou nenhum número!!')
    elif cont == 1:
        print(f'Você acertou o número {acertos} totalizando {cont} acerto')
    elif cont == 3:
        print(f'Você acertou os números {acertos} totalizando {cont} acertos')
        print('Parabéns você ganhou R$5000')
    else:
        print(f'Você acertou os números {acertos} totalizando {cont} acertos')
    while resp not in "SN":
        resp = input('Deseja jogar novamente [S]sim / [N]não').upper()

    if resp == 'N':
        break
    lista.clear()
    lista_premio.clear()
    acertos.clear()


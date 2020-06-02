#maior e menor valores na lista
listagem = []
maior = menor = 0
while True:
    n = int(input('Digite a quantidade de números que quer inserir na lista:'))
    for i in range(0, n):
        listagem.append(int(input(f'Digite o {i+1}º valor: ')))
        if i == 0:
            maior = menor = listagem[i]
        if listagem[i] > maior:
            maior = listagem[i]
        else:
            menor = listagem[i]

    print(f'Os valores na lista são {listagem}')

    print(f'O menor valor é {menor} . . . na posição', end=' ')
    for i, x in enumerate(listagem):
        if x == menor:
          print(f'. . . . {i+1}')

    print(f'\nO maior valor é {maior} na posição', end=' ')
    for i, x in enumerate(listagem):
        if x == maior:
           print(f'. . . . {i+1}')

    resposta = input('Deseja continuar[S/N] :').upper().strip()
    if resposta == 'N':
        break
    if resposta == 'S':
        listagem.clear()





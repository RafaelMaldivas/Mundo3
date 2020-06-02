#valores únicos em uma lista

conjunto = []


while True:
    par = impar = 0
    resposta = ' '
    n = int(input('Digite um número:'))
    if n in conjunto:
        print('Valor Duplicado!!')
    else:
        conjunto.append(n)
        for i in conjunto:
            if i % 2 == 0:
                par += 1
            else:
                impar += 1
        while resposta not in "SN":
            resposta = input('Deseja continuar? [S/N]').upper().strip()
        if resposta == "N":
            print(f'Você digitou os números {sorted(conjunto)}')
            print(f'{par} Números pares\n {impar} Números ímpares')
            break





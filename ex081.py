# extraindo dados de uma lista
lista = []
lpar = []
limpar = []
soma = media = maior = menor = par = impar = 0
while True:

    print('-'*40)
    n = int(input('Digite a quantidade de valores que deseja analisar :'))
    for i in range(0, n):
        while True:
            valor = int(input(f'Digite o {i+1}º valor: '))
            if valor in lista:
                print('valor duplicado!!')
            else:
                break
        soma += valor
        if valor == 12:
            pos = i
        if valor % 2 == 0:
            lpar.append(valor)
        else:
            limpar.append(valor)
        print('-'*30)
        lista.append(valor)
    for c in range(len(lista)):
        if c == 0:
            maior = menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
    media = soma / n
    print('-'*40)
    print(f'Os valores digitados em ordem decrescente : {sorted(lista,reverse=True)}')
    print(f'Os valores digitador em ordem crescente {sorted(lista)}')
    print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
    print(f'Os valores pares foram {lpar}')
    print(f'Os valores ímpares foram {limpar}')
    print(f'A soma dos valores é {soma} e a média é {media:.2f}')
    if 12 in lista:
        print(f'Você digitou o 12 no {pos+1}º número')
    else:
        print('VocÊ não digitou o 12!! :(')


#lista ordenada sem repetições

lista = []
print('-'*40)
while True:
    n = int(input('Quantos números pretende adicionar a lista?'))
    for i in range(0, n):
        while True:
            num = (int(input('Digite um número')))
            if num in lista:
                print('Valor duplicado, tente outro valor!!')
            else:
                break
        if i == 0 or num > lista[-1]:
            lista.append(num)
            print(f'O valor {num} foi adicionado no final da lista!!')

        else:
            cont = 0
            while cont < len(lista):
                if num < lista[cont]:
                    lista.insert(cont, num)
                    print(f'Adicionado na posição {cont} da lista !!')

                    break
                cont += 1
    print('-'*40)
    print(f'Os valores digitados em ordem foram {sorted(lista)}')
    lista.clear()


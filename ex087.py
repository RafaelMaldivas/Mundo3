#análise de Matriz em python

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somapar = maior = smatriz = m = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}] :'))
        smatriz += matriz[l][c]
        if matriz[1][c] == 0:
            maior = matriz[1][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]

        if matriz[l][c] %2 == 0:
            somapar+= matriz[l][c]
        soma += matriz[l][2]
m = smatriz/9
print('=+'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()
print('=+'*20)
print(f'A soma dos valores pares da matriz é [{somapar}]')
print(f'A soma dos valores da 3ª coluna é [{soma}]')
print(f'O maior valor da 2ª linha é [{maior}]')
print(f'A soma de todos os valores da matriz é [{smatriz}] e a média é [{m:.1f}]')
print('=+'*20)
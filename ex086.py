#Matriz em python
print('Multiplicação de matrizes')
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]
matriz2 = [[0,0,0],[0,0,0],[0,0,0]]
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz1[l][c] = int(input(f'Digite o valor [{l} , {c}] da matriz 1'))
print('-=-'*30)
for l in range(0,3):
    for c in range(0,3):
        matriz2[l][c] = int(input(f'Digite o valor [{l} , {c}] da matriz 2'))
print('-=-'*30)
for l in range(0,3):
    for c in range(0,3):
       matriz[l][c] = matriz1[l][c] * matriz2[l][c]
print('-=-'*30)
print(f'O resultado da multiplicação da 2 matriz é:')

for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]}', end=' ')
    print()
print('-=-'*30)
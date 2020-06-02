#exercício sobre lista composta e análise de dados
pessoas = []
geral = []
alto = baixo = 0
maior = menor = 0
resp = ''
while True:
    nome = str(input('Nome : ')).strip().capitalize()
    pessoas.append(nome)
    peso = float(input('Peso : '))
    pessoas.append(peso)
    altura = float(input('Altura:'))
    pessoas.append(altura)
    imc = peso/(altura*altura)
    pessoas.append(imc)
    if len(geral) == 0:
        alto = baixo = pessoas[2]
        maior = menor = pessoas[1]
    else:
        if pessoas[2] < baixo:
            baixo = pessoas[2]
        elif pessoas[2] > alto:
            alto = pessoas[2]
        if pessoas[1] < menor:
            menor = pessoas[1]
        elif pessoas[1] > maior:
            maior = pessoas[1]

    geral.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Continuar Cadastro? [S]sim [N]não')).strip().upper()
    if resp in 'N':
        break
print('-=-'*30)
print(f' - No total vc cadastrou {len(geral)} pessoas')
print(f'A pessoa mais gorda pesa {maior} e se chama',end=' ')
for p in geral:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'A pessoa mais magra pesa {menor} e se chama', end=' ')
for p in geral:
    if p[1] == menor:
        print(f'{p[0]}')
print('-=-'*30)
print(f'A pessoa mais alta mede {alto} e se chama',end=' ')
for p in geral:
    if p[2]==alto:
        print(f'{p[0]}')
print(f'A pessoa mais baixa mede {baixo} e se chama', end=' ')
for p in geral:
    if p[2] == baixo:
        print(f'{p[0]}')
print('-=-'*30)
for p in geral:
    if p[3] < 18:
        print(f'{p[0]} é uma pessoa magra e tem IMC de {p[3]:.1f}')
    if p[3] <= 26:
        print(f'{p[0]} é uma pessoa normal e tem IMC de {p[3]:.1f}')
    if p[3] >26:
        print(f'{p[0]} é uma pessoa gorda e tem IMC de {p[3]:.1f}')
print('-=-'*30)




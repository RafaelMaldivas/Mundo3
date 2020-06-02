ficha = []
temp = []
while True:
    nome = str(input(' Nome : ')).strip().capitalize()
    n = int(input('Quantas notas deseja cadastrar :'))
    nota = media = s =0
    for i in range(0,n):
        nota = float(input(f' Digite a {i+1}ª nota : '))
        s += nota
        temp.append(nota)
    media = s/n
    ficha.append([nome, temp[:], media])
    temp.clear()
    resp = str(input(' Quer continuar ? [S]sim[N]não'))[0].strip().upper()
    if resp in 'N':
        break
print('- -'*30)
print(f'{"Nº :":<8}{"NOME :":<10}{"MÉDIA":>8}')
print('- -'*26)
for i, a in enumerate(ficha):
    print(f'{i:<8}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('- -'*30)
    opc = int(input("Mostrar notal de qual aluno :[0] interrompe"))
    if opc == 999:
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Fim do Programa')
















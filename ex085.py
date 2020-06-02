#listas com pares e ímpares

par = []
impar = []
sp = si = mp = mi = 0
for i in range(0,8):
    while True:
        n = int(input(f'Digite o {i+1}º valor:'))
        if n in par or n in impar:
            print('Número repetido!')
        else:
            break

    if n %2 == 0:
        sp += n
        par.append(n)
        mp = sp/len(par)
    else:
        impar.append(n)
        si += n
        mi = si/len(impar)
print(f'Os valores pares digitados foram {sorted(par)} a média dos valores é {mp:.1f}')
print(f'Os valores ímpares digitados foram {sorted(impar)} a média dos valores é {mi:.1f}')

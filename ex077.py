#contador de vogais em tupla

palavras = ('PANDEMIA', 'CORONA', 'VIRUS',
            'BRASIL', 'PRESIDENTE', 'DESGOVERNO',
            'MORTES', 'CRISE', 'ECONOMIA')

for p in palavras:
    print(f'Na palavra {p} temos as vogais . . . . . ',end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(f'{letra}',end=' ')
    print()

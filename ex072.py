#digite um número de 0 a 20 e mostre-o por extenso

n1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze'
     , 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número de 0 a 20 :'))
        if numero > 20:
            print('Número inválido ! !', end=' ')
        else:
            break
    for pos, n in enumerate(n1):
        if pos == numero:
            print(f'Você digitou o número {n}')
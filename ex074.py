#maior e menor valores em tupla
from random import randint
sorteio = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
maior = menor = 0
print(f'Os Valores Sorteados Foram {sorteio}')
for n in sorteio:
    if n > maior:
        maior = menor = n
    if n < menor:
        menor = n
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
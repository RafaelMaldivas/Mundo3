#digite 4 valores e guarde-os em uma tupla
#quantas vezes aparece o valor 9, em que posição aperece o 3 pela primeira vez, qntd de números pares

tupla = (int(input(f'Digite um número :')), int(input(f'Digite outro número :')), int(input(f'Digite mais um número :')), int(input(f'Digite o último número :')))
print(tupla)
par = 0

for n in tupla:
    if n %2 == 0:
        par += 1
        print(f'{n}',end=' ')

print(f'São os números pares tendo um total de {par} números')
print(f'O número 9 aparece {tupla.count(9)} vezes')
print(f'O número 3 aparece primeiramente na {tupla.index(3)+1}ª posição ')
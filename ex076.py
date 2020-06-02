#criar uma lista ordenada usando tuplas

objects = ('Chocolate', 4.99,
           'Paçoca', 1.55,
           'Doce de Leite', 6.75,
           'Cocada', 2.99,
           'Gelatina', 3.75,
           'CupCake', 6.95
           ,'Pudim de Leite', 4.99)
print('-'*40)
print(f'{"Lista de Preços Doceria da Maria":^40}')
print('-'*40)
for pos in range(len(objects)):
    if pos %2 == 0:
        print(f'{objects[pos]:.<30}',end='')
    if pos %2 == 1:
        print(f'  R$ {objects[pos]:<2}')
print('-'*40)
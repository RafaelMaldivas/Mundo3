#crie uma tupla preenchida com os 15 primeiros colocados da tabela do campeonato brasileiro na ordem de colocação
#mostre os 5 primeiros colocados, os 4 últimos, uma lista com os times em ordem alfabética, em que posição está o time do corinthians

def linha():
    print('-=-'*20)

times = ('Flamengo', 'Cruzeiro', 'Corinthians', 'Fluminense', 'Grêmio',
         'Palmeiras', 'Chapecoense', 'Botafogo', 'Santos', 'Curitiba',
        'Internacional', 'Goiás', 'Juventus', 'Vasco', 'Bahia')

linha()
print('     Tabela Campeonato Brasileiro 2020')
linha()
print()

for pos, clube in enumerate(times):
    print(f'{pos + 1} - - - {clube}')
linha()
print('O Corinthians está na ',times.index('Corinthians') + 1,'ª posição da tabela')
print()
print('     Os 5 primeiros colocados na tabela')
linha()
for pos, clube in enumerate(times):
    if pos <= 4:
        print(f'{pos + 1} - - - {clube}')
linha()
print()
print('     Os 4 últimos na zona de rebaixamento')
for pos, clube in enumerate(times):
    if pos > 10:
        print(f'{pos + 1} - - - {clube}')
linha()
print('     Lista de times em ordem Alfabética')
linha()
for clube in sorted(times):
    print(f'     - {clube}')


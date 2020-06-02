from random import choice
material = ('Pedra', 'Papel', 'Tesoura')
def linhas():
    print('=-='*15)

def vitoria():
    print('-->Vitória<--')
    print('-->Ganhou 1 ponto')
def empate():
    print('-->Empate<--')
def derrota():
    print('-->Derrota<--')
    print('-->Perdeu 1 ponto')

linhas()
print('--> JokenPô <--')
print('--> Se você perder perde 1 ponto')
print('--> Se você ganhar ganha 1 ponto')
print('--> O jogo termina ao atingir:\n6 pontos (vitória)\n0 pontos (derrota)')
pontos = 3
linhas()

while True:
    print(f'Pontos = {pontos}')
    print('Escolha uma opção:')
    for pos, i in enumerate(material):
        print(f'[{pos}] -> {i}')
    print('[3] -> Sair')
    opção = int(input('--->'))
    item = choice(material)
    if opção == 3:
        break
    if opção == 0:
        linhas()
        print(f'Você escolheu {material[0]} e o sistema escolheu {item}')
        if item == 'Pedra':
           empate()
        elif item == 'Papel':
            derrota()
            pontos -= 1
        elif item == 'Tesoura':
            vitoria()
            pontos += 1
        linhas()
    if opção == 1:
        linhas()
        print(f'Você escolheu a opção {material[1]} e o sistema escolheu {item}')
        if item == 'Pedra':
            vitoria()
            pontos += 1
        if item == 'Papel':
            empate()
        if item == 'Tesoura':
            derrota()
            pontos -= 1
        linhas()
    if opção == 2:
        linhas()
        print(f'Você escolheu a opção {material[2]} e o sistema escolheu {item}')
        if item == 'Pedra':
            derrota()
            pontos -= 1
        if item == 'Papel':
            vitoria()
            pontos += 1
        if item == 'Tesoura':
            empate()
        linhas()
    if pontos == 6:
        linhas()
        print('-->Parabéns VocÊ Finalizou o Jogo JoKenPô !!!')
        linhas()
        break
    if pontos == 0:
        linhas()
        print('--> Game Over <--')
        linhas()
        resp = ''
        while True:
            linhas()
            print('Quer Jogar Novamente?', end=' ')
            linhas()
            resp == input('[s]sim / [n]não')
            linhas()

            if resp == 'n':
                break


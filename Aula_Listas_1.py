#testando habilidades em listas com um simples jogo da forca
palavras = ['baleia','morcego','pernilongo','diabetes','jaqueta','gladiador']

import random
random.shuffle(palavras)
palavra = random.choice(palavras)

for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    print('Palavra secreta')
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else " _ "
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    if palavra == 'baleia':
        print('Dica: Maior animal do mundo')
    elif palavra == 'morcego':
        print('Dica: Mamífero Voador')
    elif palavra == 'pernilongo':
        print('Dica: Inseto hematófago')
    elif palavra == 'diabetes':
        print('Dica: Insuficiência de Insulina')
    elif palavra == 'jaqueta':
        print('Dica: Usada no inverno')
    elif palavra == 'gladiador':
        print('Dica: Guerreiro Romano')
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break








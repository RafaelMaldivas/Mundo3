#validando expressões matemáticas

expressão = []
exp = input('Digite sua expressão :')
for simb in exp:
    if simb == '(':
        expressão.append('(')
    elif simb == ')':
        if len(expressão) > 0:
            expressão.pop()
        else:
            expressão.append(')')
            break
if len(expressão) == 0:
    print("Sua Expressão está válida!!")
else:
    print("Sua Expressão está incorreta!! ")
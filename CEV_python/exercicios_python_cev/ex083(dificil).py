expr = str(input('Digite a expressao'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')

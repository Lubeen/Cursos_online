expr = str(input('Digite a expressao'))
pilha = []
cont = 0
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
            cont += 1
        else:
            pilha.append(')')
print(f'{cont}')
if len(pilha) == 0:
    print('Sua expressao esta valida')
else:
    print('Sua expressao esta errada')
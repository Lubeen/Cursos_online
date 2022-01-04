a = float(input('Digite um valor qualquer: '))
b = float(input('Digite outro valor qualquer: '))
if a > b:
    print('O primeiro valor é maior {:.2f}'.format(a))
elif a < b:
    print('O segundo valor é maior {:.2f}'.format(b))
else:
    print('Ambos os valores são iguais')
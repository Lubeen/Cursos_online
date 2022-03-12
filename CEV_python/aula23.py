'''Erros e exceções
NameError = erro de sintaxe
ValueError = Erro de valor
ZeroDivisionError = Divisao por zero
TypeError = Erro de tipo
IndexError = Erro de indice
ModuleNotFoundError = Modulo nao encontrado'''

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__} :(')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado!')
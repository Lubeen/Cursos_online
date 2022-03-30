def tabuada(num):
    for c in range(0,11):
        total = num * c
        print(f'{num} x {c} = {total}')


# Programa principal
tabuada(int(input('Digite um número para ver sua tabuada:')))

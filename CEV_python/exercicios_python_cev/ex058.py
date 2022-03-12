from random import randint
cont = 0
resultado = False
computador = randint(0,10)
while not resultado:
    num = int(input('Pensei em um número de 0 a 10 adivinhe qual é: '))
    if computador == num:
        resultado = True
    else:
        cont += 1
        if computador > num:
            print('mais, tente novamente!')
        elif computador < num:
            print('menos, tente novamente!')
print('Voce acertou só precisou tentar {} vezes'.format(cont))


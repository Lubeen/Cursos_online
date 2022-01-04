'''cont = 0
num = int(input('Digite o numero da tabuada que voce quer ver: '))
while num != int:
    cont = 0
    while cont < 10:
        cont += 1
        resultado = num * cont
        print(f'{num} x {cont} = {resultado}')
    num = int(input('Qual número voce quer ver?'))
print('Fim')'''
while True:
    num = int(input('Digite o numero que voce quer ver: '))
    print('-=' * 20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
print('Fim do programa')


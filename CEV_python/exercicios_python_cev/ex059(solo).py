num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
sair = False

while not sair:
    print(''' 
     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior
     [ 4 ] novos numeros
     [ 5 ] sair do programa''')
    menu = int(input('Digite a opção: '))
    if menu == 1:
        soma = num + num2
        print('A soma de {} e {} é {}'.format(num,num2,soma))
    elif menu == 2:
        mult = num * num2
        print('A multiplicação de {} e {} é {}'.format(num,num2,mult))
    elif menu == 3:
        maior = num
        if num2 > maior:
            maior = num2
        print('O maior número entre {} e {} é {}'.format(num,num2,maior))
    elif menu == 4:
        num = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif menu == 5:
        sair = True
    else:
        print('Opção invalida!, tente novamente')
print('Obrigado por usar meu programa!')

contnum = 0
soma = 0
num = 0
opcao = ''
while opcao != 'N':
    num = int(input('Digite um numero: '))
    contnum += 1
    soma += num
    opcao = input('Quer continuar ? [S/N]').upper().strip()
    if contnum == 1:
        menor = maior = num
    else:
        if menor > num:
            menor = num
        elif maior < num:
            maior = num
media = soma / contnum
print('Voce digitou {} numeros e a soma é {} e a media é {}'.format(contnum,soma, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))

extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    opcao = int(input('Escolha entre 0 e 20: '))
    if 0 <= opcao <= 20:
        break
    print('Tente novamente', end=' ')
print(f'O numero {opcao} por extenso é {extenso[opcao]}')



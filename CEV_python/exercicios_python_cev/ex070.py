soma = maisdemil = cont = menor = 0
nomemenor = ' '
while True:
    cont += 1
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o preco do produto:R$ '))
    soma += valor
    opcao = ' '
    if cont == 1 or valor < menor:
        menor = valor
        nomemenor = nome
    if valor >= 1000:
        maisdemil += 1
    while opcao not in 'SN':
        opcao = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O valor total da compra é R${soma}')
print(f'A quantidade de produtos acima de R$1000,00 é {maisdemil}')
print(f'O preço do produto mais barato é R${menor:.2f} e o seu nome é {nomemenor}')

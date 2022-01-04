produto =float(input('Digite o valor do produto : R$'))
desconto = produto - (produto / 100 * 5)
print('O produto que custa R${:.2f} reais está hoje na promoção de 5% por R${:.2f} reais'.format(produto,desconto))

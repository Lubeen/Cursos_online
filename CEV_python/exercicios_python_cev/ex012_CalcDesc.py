def CalcDesc(preco_produto):
    desconto = preco_produto - (preco_produto / 100 * 5)
    return desconto
    
# Programa Principal
preco_produto = float(input('Digite o valor do produto : R$'))
valor_final = CalcDesc(preco_produto)
print(f'O produto que custa R${preco_produto:.2f} reais está hoje na promoção de 5% por R${valor_final:.2f} reais')
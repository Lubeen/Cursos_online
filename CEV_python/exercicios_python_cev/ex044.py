valor = float(input('digite o valor das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] A Vista dinheiro
[ 2 ] A vista cartão
[ 3 ] 2x no cartão de credito
[ 4 ] 3x ou mais no cartão de crédito''')
opcao =float(input('Qual é a opcao : '))
if opcao == 1:
    desconto = valor - (valor * 15 / 100)
    print('A vista voce ganha 15% de desconto sua compra de {} saiu por {}'.format(valor,desconto))
elif opcao == 2:
    desconto = valor - (valor * 5 / 100)
    print('No cartão voce ganha desconto de 5% sua compra de {} saiu por {}'.format(valor,desconto))
elif opcao == 3:
    print('No cartão até 2x o valor é normal fica {}'.format(valor))
elif opcao == 4:
    parcelas = float(input('Quantas parcelas? '))
    valor_final = valor +(valor * 20 / 100)
    prestacao = valor_final / parcelas
    print('No cartão em 3x ou mais tem juros de 20% o que era de {} ficou por {}'.format(valor,valor_final))
    print('{} reais por {} meses'.format(prestacao,parcelas))
else:print('Opcao invalida de pagamento, tente novamente')
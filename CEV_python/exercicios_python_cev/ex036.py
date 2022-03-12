casa =float(input('Digite o valor da casa  R$ '))
salario = float(input('Digite o seu salario R$'))
anos = float(input('Quantos anos pretende pagar '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos '.format(casa,anos), end='')
print('a prestacao sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado!')

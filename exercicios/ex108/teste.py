import moeda

p = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos R${moeda.moeda(moeda.dimunir(p, 10))}')

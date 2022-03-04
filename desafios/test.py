'''Uma revendedora de carros usados paga a seus funcionários vendedores
um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e
 mais 5% do valor das vendas por ele efetuadas.
 Escrever um algoritmo que leia o número de carros por ele vendidos,
 o valor total de suas vendas, o salário fixo e o
 valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.'''

def Calculo_salario(carros, total, fixo):
    # Mais 5 por causa da comissao fixa
    comissao = ((valor_total / carro_vendido) / 100) * 5 + 5
    salario = salario_fixo + comissao
    return salario


#  Programa principal
carro_vendido = int(input('Quantos carros voce vendeu?'))
valor_total = float(input('Qual o valor total que voce vendeu? R$'))
salario_fixo = float(input('Qual seu salario fixo? R$'))
resposta = Calculo_salario(carro_vendido, valor_total, salario_fixo)
print(f'Seu salario vai ser R${resposta}')
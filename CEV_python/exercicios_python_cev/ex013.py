salario =float(input('Digite o salario do funcionario : R$'))
novo_salario = salario + (salario*15/100)
print('O novo salario do funcionario com aumento de 15% é de R${:.2f} reais' .format(novo_salario))
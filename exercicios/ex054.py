from datetime import date
maior_de_idade = 0
menor_de_idade = 0
idoso = 0
for c in range(1, 7+1):
    ano = int(input(' Digite o ano de nascimento da {}ªpessoa: '.format(c)))
    ano_atual = date.today().year
    maioridade = ano_atual - ano
    if maioridade <= 65:
        maior_de_idade = 1 + maior_de_idade
        # print('voce é de maior')
    elif maioridade <=17:
        menor_de_idade += + 1
        # print('Voce é de menor')
    elif maioridade > 65:
        idoso += +1
        # print('Voce é um idoso com {} anos de idade'.format(maioridade))
print('tem {} pessoas de menor idade'.format(menor_de_idade))
print('tem {} pessoas de maior idade'.format(maior_de_idade))
print('tem {} pessoas idosas '.format(idoso))


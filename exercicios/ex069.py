maioridade = 0
homem = 0
mulher = 0
cont = 0
#sexo = ' '
#resposta = ' '
while True:
    cont += 1
    idade = int(input('Digite a idade: '))
    #sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    #resposta = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
        mulher += 1
    if resposta == 'N':
        break
print(f'Dentre as pessoas cadastradas foram {maioridade} pessoas maiores de idade')
print(f'Dentre as pessoas cadastradas foram {homem} homens ')
print(f'Dentre as pessoas cadastradas foram {mulher} mulheres menor de 20 anos')
print(f'Foram {cont} pessoas cadastradas')

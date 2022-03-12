media = 0
contidade = 0
mais_velho = ''
maior_idade = 0
contmulher = 0
for c in range(1,5):
    print('------ {}° pessoa -------'.format(c) )
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo M/F: ')).strip()
    contidade += idade
    if sexo == 'F':
        if idade <= 20:
            contmulher += 1
    if c == 1 and sexo in 'Mm':
        maior_idade = idade
        mais_velho = nome
    else:
        if idade >= maior_idade and sexo in 'Mm':
            maior_idade = idade
            mais_velho = nome
print('O nome do homem mais velho é {} e sua idade é {}'.format(mais_velho, maior_idade))
media = contidade / 4
print('A media das idades digitadas foi de {} anos de idade'.format(media))
print('A quantidade de mulheres abaixo de 20 anos é {} quantidade'.format(contmulher))



'''Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
- Infantil A: 5 a 7 anos;
- Infantil B: 8 a 10 · anos;
- Juvenil A: 11 a 13 anos;
- Juvenil B: 14 a 17 anos;
- Sênior: maiores de 18 anos.'''

nome = str(input('Qual seu nome? ')).capitalize()
idade = int(input('Qual a sua idade? '))
if idade <= 7:
    print(f'{nome} voce tem {idade} anos e sua classificao é Infantil A!')
elif idade >= 8 and idade <= 10:
    print(f'{nome} voce tem {idade} anos e sua classificao é Infantil B!')
elif idade >= 11 and idade <= 13:
    print(f'{nome} voce tem {idade} anos e sua classificao é Juvenil A!')
elif idade >= 14 and idade <= 17:
    print(f'{nome} voce tem {idade} anos e sua classificao é Juvenil B!')
else:
    print(f'{nome} voce tem {idade} anos e sua classificao é Sênior ')
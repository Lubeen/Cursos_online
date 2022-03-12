from datetime import date
atual = date.today().year
ano = float(input('Digite seu ano de nascimento : '))
idade = atual - ano
if idade < 8:
    print('Sua idade é {} e sua classificação é PRÉ-MIRIM'.format(idade))
elif idade < 10:
    print('Sua idade é {} e sua classificação é MIRIM'.format(idade))
elif idade < 12:
    print('Sua idade é {} e sua classificação é PETIZ'.format(idade))
elif idade < 14:
    print('Sua idade é {} e sua classificação é INFANTIL'.format(idade))
elif idade < 16:
    print('Sua idade é {} e sua classificação é JUVENIL'.format(idade))
elif idade < 19:
    print('Sua idade é {} e sua classificação é JUNIOR'.format(idade))
elif idade < 16:
    print('Sua idade é {} e sua classificação é INFANTO-JUVENIL'.format(idade))
elif idade > 17:
    print('Sua idade é {} e sua classificação é JUNIOR-SENIOR'.format(idade))

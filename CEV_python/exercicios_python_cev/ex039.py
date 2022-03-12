from datetime import date
ano = float(input('Digite o ano do seu nascimento :'))
idade = date.today().year - ano
falta = 18 - idade
if idade >= 18:
    print(' sua idade é {} anos, Parabens voce foi convocado e ja pode servir ao seu PAÍS!'.format(idade))
elif idade < 18:
    print('Voce tem {} anos ainda faltam {} anos para voce servir!'.format(idade,falta))
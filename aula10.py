'''print('Seja bem vindo ao programa de validação para 2° dose da vacina contra covid-19 \n '
      'precisamos saber se voce ja tomou a 1° dose, alem de algumas informações suas')
print('Vamos começar!')
nome = str(input('Digite seu nome :'))
doseum = str(input('{} voce ja tomou a 1° dose? '.format(nome)))
if doseum.upper() == 'SIM' :
    print('Otimo! então, voce está liberado para a 2° dose')
else:print('Poxa, então você pode voltar até dia 23 depois de tomar a 1° dose ')'''
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
s = (n1 + n2) / 2
if s >= 6 :
    print('Sua media foi {}, Parabens você esta aprovado! '.format(s))
else:print('Sua media foi {}, Voce esta reprovado, estude mais!'.format(s))



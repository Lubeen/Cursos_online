import random
from time import sleep
lista = [0,5]
think = random.choice(lista)
num = int(input('Pensei em um número de 0 a 5 adivinhe qual é: '))
print('PROCESSANDO...')
sleep(2)
if num == think:
    print('Parabens voce acertou! o numero era {}'.format(think))

else: print('Errado! pensei no {} tente novamente'.format(think))

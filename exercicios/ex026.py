frase = str(input('Digite uma frase qualquer :')).upper().strip()
print('A letra A aparece {} vezes na frase :'.format(frase.count('A')))
print('A primeira vez que a letra a aparece é no indice {}'.format(frase.find('A')+1))
print('A ultima vez que a letra a aparece é no indice {}'.format(frase.rfind('A')))
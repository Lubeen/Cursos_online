frase = str(input('Digite uma frase :')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
print(junto, end=' ')
print(frase)
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
if junto == inverso:
    print('Voce encontrou um Palíndromo')
else:print('A frase não é um palindromo')
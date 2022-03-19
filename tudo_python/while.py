 #https://www.youtube.com/watch?v=_bqKoPbWeD0&list=PLuhCJtW2i-wLGFkJTN8KGa2sipnmimoDp
 # vamos aprender a usar o while


def principal():
  qtd = int(input('Quantos números a digitar?'))
  contador = 0
  cont_impares = 0
  cont_pares = 0
  cont_primo = 0


  while contador < qtd:
    numero = int(input('Número: '))
    # Se é PAR ou IMPAR
    if numero % 2 == 0:
      cont_pares = cont_pares + 1
    else:
      cont_impares = cont_impares + 1
    # Se é PRIMO
    if primo(numero):
      cont_primo = cont_primo + 1
    contador = contador + 1
  print(f'pares: {cont_pares}')
  print(f'impares {cont_impares}')
  print(f'primos {cont_primo}')


def primo(numero):
    divisores = 0
    inicio = 1

# Descobrindo os divisores
    while inicio <= numero:
      if numero % inicio == 0:
        divisores = divisores + 1
      inicio = inicio + 1
    
    if divisores == 2:
      return True
    else:
      return False

# Programa principal
principal()
print(primo(5))



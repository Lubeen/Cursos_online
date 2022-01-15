'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
 A) A soma de todos os valores pares digitados.
  B) A soma dos valores da terceira coluna.
   C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna += matriz[l][c]
        if l == 1:
            maior = matriz[l][c]
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print(f'matriz na forma padrao de passagem de dados{matriz}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Os valores pares digitados foram {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor do meio digitado foi {maior}')

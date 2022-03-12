'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    resp = 1
    for f in range(n,0,-1):
        if show:
            print(f'{f}', end=' ')
            print(f' x ' if f > 1 else ' = ', end='')
        resp *= f
    return resp


# Programa principal
total = num = int(input('Digite um numero para fatorar: '))
print(fatorial(num, True))
help(fatorial)
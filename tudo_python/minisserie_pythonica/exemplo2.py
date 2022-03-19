# FUNCAO ANONIMA


anonima = lambda param: param + 2 
anonima_plus = lambda param1, param2: param1 + param2


# FUNCAO NORMAL
# X vai ser um parametro posicional

def soma_posional(x, y):
    """x e y são parametros posicionais.    """
    return x + y


def soma_nomeados(x=7, y=7):
    """ 
    X E Y são parametros nomeados.
    na falta de X E Y o valor 7 sera usado"""
    print(f'x: {x} e y:{y}')
    return x + y
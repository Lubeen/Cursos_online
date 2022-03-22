# Funcoes como objeto de primeira classe
# Funcoes podem se comportar como qualquer objeto
from typing import Callable, Dict
from numbers import Number
func = lambda: 'resultado da funcao'
# Funcao dentro de variavel

Dict[str, Callable]

# Funcoes anonimas
'''calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,}'''


def soma(x: Number, y:Number) -> Number: 
    """Soma dois numeros."""
    return x + y


def sub(x: Number, y:Number) -> Number: 
    """Subtrai dois numeros."""
    return x - y


def mult(x: Number, y:Number) -> Number: 
    """multiplica  dois numeros."""
    return x * y


def div(x: Number, y:Number) -> Number: 
    """Dividi dois numeros."""
    return x / y


# funcoes normais
calc_nomeado= {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div, 
}


somas = [
lambda x: x + 2, 
lambda x: x + 1,
lambda x: x + 0
]


def soma_1(x: Number) -> Number:
    """Soma 1 a qualquer x de entrada.
    """
    return x + 1

# Para rodar no terminal com  tupla coloque (soma_1,)[0](10)

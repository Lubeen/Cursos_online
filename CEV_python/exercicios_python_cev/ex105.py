'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
– Quantidade de notas–
 A maior nota–
 A menor nota –
  A média da turma –
   A situação (opcional)'''



def notas(*n, sit=False):
    """Funcao para analisar notas e situacoes de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma."""
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] > 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r



# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
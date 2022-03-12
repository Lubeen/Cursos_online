from Estudos.CEV_python.exercicios_python_cev.ex115.lib.interface import *
from Estudos.CEV_python.exercicios_python_cev.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('Opcao 1')
        # Opcao de listar o conteudo de um arquivo!
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME:'))
        idade = leiaInt('Idade:')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        cabecalho('ERRO! Digite uma opcao válida!')
    sleep(2)



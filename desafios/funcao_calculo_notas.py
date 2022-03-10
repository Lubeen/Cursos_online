'''Faça uma app que solicite as 4 notas de um aluno apresente
o seu nome e sua média e informe se o aluno está aprovado ou reprovado.'''



def nota_final(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 6:
        print(f'{nome} a sua média foi de {media} \nParabens voce está APROVADO!')
        return media
    else:
        print(f'{nome} A sua média foi de {media}\nInfelizmente voce esta REPROVADO!')
        return media


# Programa principal
nome = str(input('Qual seu nome? '))
nota1 = float(input(f'{nome} qual foi sua nota no 1° bimestre? '))
nota2 = float(input(f'{nome} qual foi sua nota no 2° bimestre? '))
nota3 = float(input(f'{nome} qual foi sua nota no 3° bimestre? '))
nota4 = float(input(f'{nome} qual foi sua nota no 4° bimestre? '))
aluno = {'nome':nome,'1 bimestre':nota1,'2 bimestre':nota2,'3 bimestre':nota3,'4 bimestre':nota4}
resultado = nota_final(nota1, nota2, nota3, nota4)



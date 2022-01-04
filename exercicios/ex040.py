nota_a = float(input('Digite a nota do aluno :'))
nota_b = float(input('Digite outra nota :'))
media = (nota_b + nota_a) / 2
if media >= 7:
    print('Parabens voce está aprovado, sua nota é {} '.format(media))
elif media < 6 and media >= 5:
    print('Voce esta de recuperacao, estude mais! sua nota é {} '.format(media))
elif media <=4:
    print('Reprovado, sua nota é {} estude mais!! '.format(media))

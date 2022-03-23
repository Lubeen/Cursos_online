# Média Aritmétic
import statistics
def media_aluno(lista):
    media = statistics.mean([lista])
    if media >= 6:
        return print(f'Parabens sua media é {media} e voce esta APROVADO!')
    else:
        return print(f'Infelizmente sua media foi {media} e voce esta REPROVADO!')



# Programa principal
print('calculo de media aluno')
notas = []
for c in range(1, 5):
    notas = float(input(f'digite a {c}ª nota :'))
media_aluno(notas)


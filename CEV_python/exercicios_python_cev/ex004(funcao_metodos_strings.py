# Métodos de strings
def metodos_de_string(*n):
    dados['alfanumerico'] = n1.isalnum
    dados['padrao ASCI'] = n1.isascii()
    dados['digito'] = n1.isdigit()
    dados['alphanumerico'] = n1.isalpha()
    dados['minusculo'] = n1.islower()
    dados['decimal'] = n1.isdecimal()
    dados['identificador'] = n1.isidentifier()
    dados['numerico'] = n1.isnumeric()
    dados['printavel'] = n1.isprintable()
    dados['espaço'] = n1.isspace()
    dados['capitalized'] = n1.istitle()
    dados['maiusculo'] = n1.isupper()
    return dados

# Programa principal
dados = {}
n1 = input('digite algo:')
tipos = metodos_de_string(n1)

# Mostra pra gente o resultado listado
for key, valor in tipos.items():
    print(f'{key} = {valor}')
print(type(n1))




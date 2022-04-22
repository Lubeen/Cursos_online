"""
Entidades = Container que coloca dados, armazena dados
DER = DIAGRAMA DE ENTIDADES RELACIONAMENTOS
Atributos = cpf, nome, nascimento.. etc sao dados
cardinalidade = Relacionamentos =   muitos para muitos, um para um, um para muitos

no relacionamento de um para um podemos juntar as tabelas em uma tabela só, tem que ver se faz sentido  manter separado, os atributos precisam ser compativeis, mas precisa-se escolher uma entidade dominante
aí voce precisa pegar a chave primaria da entidade secundaria e levar para a entidade dominante


em um para muitos ou muitos para um, voce vai pegar a chave primaria do lado um e joga do lado muitos como chave estrangeira

Em muitos para muitos, o que causa a ligacao entre as tabelas se transforma em uma entidade com atributos, 
então pega a chave primaria de um lado e joga pro meio e pega do outro lado e joga no meio
Ou seja desmembrar esse relacionamento



"""
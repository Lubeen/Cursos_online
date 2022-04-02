#drop database cadastro; para apagar o db
#Constraints significa parametros  ou definicoes que colocamos no db
#Nomes definidos ao redor de crases `` para palavra de definicao
#Campo com chave primaria nao se repete
#auto_increment para executar o auto incremento automaticamente assim ele vai funcionar como um contador e registro ao mesmo tempo
#use cadastro;

# create table pessoas(
# `id` int not null auto_increment,
# `nome` varchar(30) not null,
# `nascimento` date,
# `sexo` enum ('M','F'), 
# `peso` decimal(5,2),
# `altura` decimal (3,2),
# `nacionalidade` varchar(20) default 'Brasil',
# primary key (id)
# )
# default charset = utf8;
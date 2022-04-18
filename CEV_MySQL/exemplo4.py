'''desc pessoas; #comando para descrever o db pessoas

alter table pessoas #comando para alterar a coluna
add column profissao varchar(10)

alter table pessoas
add column profissao varchar(10) after nome; # adicionar apos o nome

select * from pessoas; # comando para selecionar todos os itens de coluna

ALTER TABLE pessoas
add column profissao varchar(10) first # para adicionar a coluna primeiro.

ALTER TABLE pessoas
modify column profissao varchar(20); # para modificar os parametros da coluna.

alter table pessoas
change column profissao prof varchar(20); # para mudar o nome da coluna.

alter table pessoas
change column profissao prof varchar(20) not null default ''; # para mudar o nome da coluna e manter as configuraçoes

alter table pessoas
rename to gafanhotos; # para renomear a tabela

insert into pessoas value
(null, 'Godofredo', '1985-01-01', 'M', 78.5, 1.83, 'Brasil'); # para inserir um registro
#para inserir valores na tabela
'''
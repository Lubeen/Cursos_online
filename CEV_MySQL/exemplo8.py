"""
Obtendo os dados das tabelas
comando select
select * from tabela
order by nome; para ordenar pelo nome

se for order by nome desc; com desc ele irá ordenar pelo nome de baixo pra cima
* para selecionar todas as colunas e linhas

select nome, carga, ano from cursos
order by nome;
para delimitar as colunas por nome, carga, ano e ordenar por nome

select * from cursos
where ano = '2016'
order by nome;
comando para ordenar por linhas

query é uma solicitacao

select nome, ano from cursos
where ano BETWEEN '2014' and '2016';
between para selecionar entre faixas de valores

select nome,descricao, ano from cursos
where ano in (2014,2016)
order by ano;
where IN para selecionar especificamente o que pedir
"""
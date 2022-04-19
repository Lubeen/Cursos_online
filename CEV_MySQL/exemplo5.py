"""
Manipulando registros ou linhas ou tuplas, todos são sinonimos

Registro, linhas e tuplas são diferentes de CAMPOS E COLUNAS

insert into cursos values for add lines in db

para atualizar um registro ou linha ou tupla
update cursos
set nome = 'HTML5'
where idcurso = 1;

para atualizar mais de um registro e limitar a quantidade de modificações ai no caso vai modificar apenas uma linhas ou tupla ou registro
update cursos
set nome = 'Java',carga = '40', ano = '2015'
where idcurso = '5'
limit 1;

O comando update altera as linhas, porém não as exclui
delete from cursos
where idcurso = '10';
para deletar uma linha ou tupla ou registro

para apagar todos os registro o comando é 
TRUNCATE TABLE cursos;

"""
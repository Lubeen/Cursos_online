"""
Relacionando as tabelas

vamos ligar uma tabela na outra

Inno DB é um engine e um mecanismo que pertence a oracle ele permite criar tabelas com algumas caracteristicas especiais como
chave estrangeira, serve MyISAM e XtraDB.

Tem que seguir a Regra ACID
Precisa ser atomica = Ou tudo é feito ou nada é considerado.
Consistente = Se está ok antes de executar, então precisa esta ok apos executar.
Isolamento = Quando tenho duas ou mais transações, as transações precisam ser executadas de forma independente.
Durabilidade = Se voce salvou um dado, voce quer que dure aquele dado armazenado.

Adionando a Foreign key

use cadastro;
desc gafanhotos;
alter table gafanhotos add cursopreferido int;

alter table gafanhotos
add foreign key(cursopreferido)
references cursos(idcurso);

select * from gafanhotos;
select * from cursos;

update gafanhotos set cursopreferido = '6'
where id = '1';

Integridade Referencial

Delete From cursos
where idcurso = '6';
#Não consigo modificar um campo se ele for comprometer a integridade do meu banco

Para juntar duas tabelas Inner join assim ele irá juntar tudo que tem relaçao

select gafanhotos.nome, gafanhotos.cursopreferido, cursos.nome, cursos.ano from gafanhotos as g inner join cursos as c
on cursos.idcurso = gafanhotos.cursopreferido;
#as para apelidar a tabela

select g.nome, c.nome, c.ano from gafanhotos as g left outer join cursos as c
on c.idcurso = g.cursopreferido;
#Left outer ira trazer tudo que tem relaçao com a tabela gafanhotos

select g.nome, c.nome, c.ano from gafanhotos as g right outer join cursos as c
on c.idcurso = g.cursopreferido;
#Right outer ira trazer tudo que tem relaçao com a tabela cursos


"""
"""
Relacionamento de muitos para muitos

Gafanhoto assiste Curso
Gafanhoto <> Assiste <> Curso #assiste se transformou em uma entidade, e os <> serve como ponto de cardinalidade ou seja relacionamento
E então irá pegar as chaves de cada lado para o assiste

Create table assiste_curso (
    id int not null auto_increment,
    data date,
    idgafanhoto int,
    idcurso int,
    primary key(id),
    foreign key(idgafanhoto) references gafanhoto(id),
    foreign key(idcurso) references curso(idcurso)

#Para juntar 3 tabelas ou mais

 insert into gafanhoto_assiste_curso values
(default, '2014-03-01', '1','2');

select * from gafanhoto_assiste_curso;

SELECT 
    c.nome, g.nome
FROM
    gafanhotos g
        JOIN
    gafanhoto_assiste_curso a ON g.id = a.idgafanhoto
        JOIN
    cursos c ON a.idcurso = c.idcurso;

"""
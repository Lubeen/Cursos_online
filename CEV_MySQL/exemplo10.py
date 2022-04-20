"""
Agrupando Registros
select carga from cursos
group by carga;

Agrupando e Agregando
select carga, count(nome) from cursos
group by carga

select totaulas, count(*) from cursos
group by totaulas
order by totaulas;

select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*) desc;

having é ter, ou seja tem que ter 5 anos ou mais, além disso voce só pode 
usar o having do campo que voce agrupou

select carga, count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);
#para selecionar a carga e contar da tabela cursos
onde o ano seja maior que 2015 e agrupar por carga
além disso, precisa necessariamente ser maior que a média de carga da tabela cursos


#IMPORTANTE
WHERE É PARA O SELECT
E HAVING É PARA GROUP BY
"""
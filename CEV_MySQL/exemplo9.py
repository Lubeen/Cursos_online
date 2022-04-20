"""
Obtendo os dados das tabelas

Seleção por nome
select * from cursos
where nome = 'php'; 

Usando o operador like
select * from cursos
where nome like 'p%';
 o % é coringa
like é um operador de comparação

se o % for na frente %a então ele irá colocar o A no final e 
se for a% no final ele irá procurar a letra a no começo , além disso
voce pode colocar %a% para procurar a letra a em qualquer lugar

se quiser procurar tudo que não tiver a, faça
where nome not like '%a%';

e se quiser exigir que tenha alguma coisa no espaço coloque _ underline
where nome like 'ph%p_';

DISTINGUINDO

select distinct carga from cursos;

Funções de agregação
select count(nome) from cursos; # conta quantos nomes tem em cursos
select count(*) from cursos; # nesse caso ele vai contar todos os registros
para agregar quantos dados tem na tabela cursos

select max(totaulas) from cursos; # nesse caso ele irá buscar o maior valor

select min(totaulas) from cursos; # nesse caso ele irá buscar o menor valor

select sum(totaulas) from cursos; # nesse caso ele irá somar todos os valores

select avg(totaulas) from cursos; # nesse caso ele irá calcular a média
"""
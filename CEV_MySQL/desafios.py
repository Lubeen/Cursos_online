"""
exerciocio 1
Uma lista com o nome de todas as gafanhotas:
Resposta: 
select nome, sexo  from gafanhotos
where sexo = 'f';

exercicio 2
Uma lista com os dados de todos aqueles que nasceram entre 1/jan/2000 e 31/dez/2015: ano/mes/dia
Resposta:
select nome, nascimento from gafanhotos
where nascimento between '2000-01-01' and '2015-12-31';

exercicio 3
Uma lista de todos os homens que trabalham como programador:
Resposta:
select * from gafanhotos
where profissao = 'programador' and sexo = 'm';

exercicio 4 
Uma lista com os dados de todas as mulheres que nasceram no brasil e que tem seu nome iniciando com a letra j:
Resposta: 
select * from gafanhotos
where nacionalidade = 'brasil' and sexo = 'f' and nome like 'j%';

exercicio 5
Uma lista com o nome e nacionalidade de todos os homens que tem silva no nome, nao nasceram no brasil e pesam menos de 100kg:
Resposta:
select nome, nacionalidade, sexo, peso from gafanhotos
where sexo = 'm' and not nacionalidade = 'brasil' and peso < '100' and nome like '%silva%'; 

exercicio 6
Qual é a maior altura entre gafanhotos homens que moram no Brasil:
Resposta:
select sexo, nacionalidade, max(altura) from gafanhotos
where sexo = 'm' and nacionalidade = 'brasil';

exercicio 7
Qual a média de peso dos gafanhotos cadastrados:
Resposta:
select avg(peso) from gafanhotos
where sexo = 'm';

exercicio 8
Qual é o menor peso entre as gafanhotos mulheres que nasceram fora do Brasil e entre 01/jan/1990 e 31/dez/2000:
Resposta:
select min(peso) from gafanhotos
where sexo = 'f' and not nacionalidade = 'brasil' and nascimento between '1990-01-01' and '2000-12-31';

exercicio 9
Quantas gafanhotos mulheres tem mais de 1.90 de altura? 
Resposta:
select count(nome) from gafanhotos
where sexo = 'f' and altura > '1.90';

exercicio 10
Uma lista com as profissoes dos gafanhotos e seus respectivos quantitativos:
Resposta:
select profissao, sexo, count(nome) from gafanhotos
where sexo =  'm'
group by profissao;
#Acredito que o metodo count() só funcione com group by, quando tentei com distinct nao deu certo


exercicio 11
Quantos gafanhotos homens e quantas mulheres nasceram após 2005-01-01:
Resposta:
select sexo, count(sexo) from gafanhotos
where nascimento >= '2005-01-01' 
group by sexo;


exercicio 12
Uma lista com os gafanhotos que nasceram fora do Brasil, mostrando o país de origem e o total de pessoas nascidas lá.
Só nos interessam os países que tiverem mais de 3 gafanhotos com essa nacionalidade:
Resposta:
use cadastro;
select nacionalidade, count(nacionalidade) from gafanhotos
where not nacionalidade =  'brasil'
group by nacionalidade
having count(nacionalidade) >= 3;


exercicio 13
Uma lista agrupada pela altura dos gafanhotos, mostrando quantas pessoas pesam mais de 100kg e que estão acima da média de altura 
de todos os cadastrados:
Resposta:
use cadastro;
select altura, count(*) from gafanhotos
where peso > '100'
group by altura
having altura > (select avg(altura) from gafanhotos)
order by count(nome) desc, altura;


"""
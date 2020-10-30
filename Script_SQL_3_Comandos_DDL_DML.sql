/*criação do banco escola*/
create database Faculdade;

use Faculdade;/*conecta com o banco escola*/

create table aluno(
   matricula int auto_increment primary key,
   nome varchar(20) not null,
   sobrenome varchar(20),
   sexo enum('f','m') default 'm', 
   datanasc date, /*'aaaa-mm-dd'*/
   curso varchar(20),
   nota1 decimal(5,2) default 5, 
   nota2 decimal(5,2) default 0
   );
 /*dados da tabela aluno*/
 insert into aluno (nome,sobrenome,datanasc,curso)
 values 
 ('Carlos','Santos','2000-10-10','informatica'),
 ('Pedro','Siqueira','2002-08-10','mecanica'),
 ('Antonio','Cardoso','2002-10-08','informatica');
 
 insert into aluno (nome,sexo,datanasc,curso,nota2)
 values
 ('Debora','f','2000-12-25','informatica',8),
 ('Tania','f','2002-11-15','artes',7.5),
 ('Carmen','f','2001-04-01','mecanica',6);
 
 insert into aluno values
 (null,'Paulo','Ribeiro','m','2000-02-15','mecanica', 7,8.5),
 (null,'Vera','Sampaio','f','2000-05-20', 'informatica', 10, 9),
 (default,'Leonardo','Santos','m','2001-09-07','mecanica', default,3),
 (null,'Elen','Menezes','f','2001-12-25','artes',8,8);

select * from aluno;

select nomealuno as nome from aluno;
alter table aluno change nome nomealuno varchar(30) not null;
alter table aluno add telefone varchar(9) not null after nomealuno;
alter table aluno modify telefone varchar(11) null;

alter table aluno add check (nota1 >= 0 and nota1 <= 10);
alter table aluno modify sexo enum('f','m') default 'f';

insert into aluno (nomealuno, sobrenome, sexo, datanasc, curso, nota1, nota2) 
values
('João', 'Victor', 'm', '2000-05-05', 'informatica', '5', '10'),
('Nany', 'Salvador', 'f', '1998-09-25', 'artes', '10', '8'),
('Julia', 'Salvador', 'f', '2003-11-03', 'informatica', '9', '7');
	

update aluno set nota2 = nota2+0.5 where nota2 < 6;

select nomealuno from aluno where telefone is null or sobrenome is null;

update aluno set sobrenome = 'Santos Silva' where nomealuno = 'Leonardo';
update aluno set sobrenome = 'Salvador Aureliano' where nomealuno = 'Julia';

select * from aluno;

select distinct curso from aluno;
select distinctrow curso from aluno;

select nomealuno from aluno where sexo = 'f' and (curso = 'mecanica' or curso = 'informatica');

select * from aluno where nota1 between 5 and 8;

select nomealuno, sobrenome, telefone from aluno where sobrenome like 'C%';

select * from aluno order by curso asc;

select matricula, nota1, nota2, (nota1 + nota2) / 2 as Media from aluno order by Media desc; 

delete matricula from aluno where matricula = 4;

alter table aluno drop telefone;

select * from aluno where datanasc between '2000-01-01' and '2000-12-31';
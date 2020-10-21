create database Ex1;

use Ex1;

create table aluno(
	matricula int auto_increment primary key,
    nome varchar(60) not null,
    sexo char(1) default 'M',
    curso char(3) default 'ADS',
    nota numeric(5,2) default 0);
    
alter table aluno add faltas int;
alter table aluno drop cpf;
alter table aluno add cpf varchar(16) after nome;
alter table aluno modify cpf varchar(14) not null after nome;
alter table aluno modify nome varchar(40) not null;
alter table aluno modify curso char(3) default 'SEG';
alter table aluno modify n1 numeric(5,2) default '9';
alter table aluno alter n1 set default '5';
alter table aluno add datanasc date not null;
alter table aluno modify cpf char(14) not null unique; 
alter table aluno change nota n1 numeric(5,2) default '5';
rename table aluno to TABALUNO;

	
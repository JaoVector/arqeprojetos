create database if not exists Ex_carros;

use Ex_carros;

create table Marca( 
	id_Marca numeric primary key,
    NomeMarca varchar(14) not null
);

create table Modelo(
	
    id_Modelo numeric,
    id_Marca numeric not null,
    NomeModelo varchar(14) default 'Corsa',
    primary key(id_Modelo, id_Marca),
    foreign key (id_Marca) references Marca(id_Marca)
);


create table Categoria(

	id_Categoria char primary key,
    DescricaoCategoria varchar(5)
);


create table Veiculo(

	placa char(9) primary key,
    cor varchar(8) not null default 'Branca',
    anofabricacao year not null,
    id_Categoria char not null,
    id_Modelo numeric not null,
    id_Marca numeric not null,
    foreign key (id_Categoria) references Categoria(id_Categoria),
    foreign key (id_Modelo, id_Marca) references Modelo(id_Modelo, id_Marca)
);


create table Proprietario(
	
    id_proprietario int auto_increment primary key,
    NomeProprietario varchar(25) not null,
    EnderecoProp varchar(10) not null,
    RG char(10),
    CPF char(11) unique
);


create table Propriedade(
	
    placa char(9) not null,
    id_proprietario int not null,
    datacompra date not null,
	primary key(placa, id_proprietario),
    foreign key (placa) references Veiculo(placa),
    foreign key (id_proprietario) references Proprietario(id_proprietario)
);


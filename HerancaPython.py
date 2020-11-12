# HERANÇA

class Pessoa: # classe principal
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa): # subclasse Cliente recebe a herança de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcio(Pessoa): # subclasse Funcio recebe a herança de Funcio
    def __init__(self, nome, sobrenome, cpf, matri): # recenendo atributos
        super().__init__(nome, sobrenome, cpf) # chamando os atributos da super classe Pessoa
        self.__matri = matri # declerando atributos que não esta na super classe
        
    def nome_completo(self):
        return f'Matricula: {self.__matri} Nome: {self._Pessoa__nome}' # fazendo Overriding
        # sobrescrevendo a função nome completo, usando name mangling para acessar o atributo privado


client = Cliente('joao', 'Victor', '1234', 5000)
fun = Funcio('Douglas', 'Junior', '12312', '5635')

print(client.nome_completo())
print(fun.nome_completo())


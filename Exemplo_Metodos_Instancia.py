# Exemplo de Login com metodos de instancia

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    cont = 0

    @classmethod # decorador utilizado para metodos de classe
    def contas(cls): # primeiro parametro como a classe(cls)
        print(f'{cls.cont} quantidade de usuarios') # a classe e seu atributo respectivamente

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.cont + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.cont = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def user(self):
        print(Usuario.__dict__)


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu email: ')
senha = input('Digite a senha: ')

user1 = Usuario(nome, sobrenome, email, senha)
print('Usuario criado com sucesso')

senha_chek = input('Informe a senha: ')

if user1.senha(senha_chek):
    print('Acesso Permitido')
else:
    print('Acesso negado')

Usuario.contas()
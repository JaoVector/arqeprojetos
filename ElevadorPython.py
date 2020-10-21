from random import *


class Elevador:

    def __init__(self, andares: int, capacidade: int):
        self.__andares, self.__capacidade = andares, capacidade
        self.__elevator, self.__andar = [], []
        self.__limitean: int = 1
        self.__desces: int = self.__andares
        self.__limiteca: int = 0
        self.__pessoa = []

    def iniciar(self):
        if self.__limiteca < self.__capacidade:
            return Elevador.entra(self)
        else:
            return Elevador.sai(self)

    def entra(self):
        if self.__limiteca < self.__capacidade:
            person = input('Pessoa: ')
            self.__pessoa.append(person)
            self.__limiteca += 1
            self.__elevator.append(person)
            p = choice([True, False, True, False])
            if p is True:
                while True:
                    sob = int(input('Digite o Andar para subir: '))
                    if sob <= self.__andares:
                        return Elevador.sobe(self, sob)
            else:
                while True:
                    desc = int(input('Digite o Andar para descer: '))
                    if desc < self.__andares:
                        return Elevador.desce(self, desc)
        else:
            print('Capacidade maxima, Desce gente')
            grup = []
            for n in self.__pessoa:
                person = n
                grup.append(person)
            return Elevador.sai(self, grup)

    def sai(self, grup):
        if self.__limiteca > 1:
            li = [a for a in range(1, len(grup), 1)]
            k = choice(li)
            i = 0
            while i <= k:
                self.__pessoa.pop()
                self.__elevator.pop()
                self.__limiteca -= 1
                i = i + 1
            return Elevador.entra(self)
        else:
            print('Elevador esta vazio')
            return Elevador.entra(self)

    def sobe(self, andar: int):
        if self.__limitean < self.__andares:
            self.__andar.append(andar)
            self.__limitean += 1
            print('Voce subiu')
            return Elevador.entra(self)
        else:
            print('Andar Maximo')
            a = int(input('Digite um andar para descer: '))
            return Elevador.desce(self, a)

    def desce(self, andar: int):
        if andar > 1:
            self.__andar.append(andar)
            self.__limitean -= 1
            print('Voce desceu')
            return Elevador.entra(self)
        else:
            print('Voce esta no Terreo')
            b = int(input('Digite um andar para subir: '))
            return Elevador.sobe(self, b)


var = Elevador(andares=5, capacidade=3)
var.iniciar()

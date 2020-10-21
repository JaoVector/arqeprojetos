
liv = []
lif = []
lil = []


def tchau():
    resp1 = input(str("Deseja Comprar novamente? "))
    if resp1.upper() == "SIM":
        opcoes()
    else:
        print(f"\nSuas Compras \n"
              f"Frutas {lif}\n"
              f"Verduras {liv}\n"
              f"Legumes {lil}\n")
        print('Até mais, volte sempre')


def compraf():
    print('Agora vamos comprar, quandor terminar a compra basta digitar sair')
    a, c = '', 1
    while a != 'sair':
        a = input(f'Digite a Fruta {c}? ')
        if a != 'sair':
            lif.append(a)
            c = c + 1
    return tchau()


def comprav():
    print('Agora vamos comprar, quandor terminar a compra basta digitar sair')
    a, c = '', 1
    while a != 'sair':
        a = input(f'Digite a Verdura {c}? ')
        if a != 'sair':
            liv.append(a)
            c = c + 1
    return tchau()


def compral():
    print('Agora vamos comprar, quandor terminar a compra basta digitar sair')
    a, c = '', 1
    while a != 'sair':
        a = input(f'Digite o Legume {c}? ')
        if a != 'sair':
            lil.append(a)
            c = c + 1
    return tchau()


def mercado(val):
    def menu():
        v = val()
        if v == 1:
            print('Opcoes de Frutas \n')
            print('laranja'',''maca'',''goiaba'',''jenipapo \n')
            a = str(input('Gostaria de Comprar? '))
            if a.upper() == 'NAO':
                tchau()
            else:
                compraf()
        elif v == 2:
            print('Opcoes de Verdeuras \n')
            print('alface'',' 'mandioca'',' 'agriao'',' 'couve-flor \n')
            b = str(input('Gostaria de Comprar? '))

            if b.upper() == 'NAO':
                tchau()
            else:
                comprav()
        else:
            print('Opcoes de Legumes \n')
            print('cenoura'',' 'beterraba'',' 'batata'',' 'batata-doce')
            c = str(input('Gostaria de Comprar? '))
            if c.upper() == 'NAO':
                tchau()
            else:
                compral()
    return menu


@mercado
def opcoes():
    op = int(input('----------------------------- \n'
                   'Essas sao as opcoes do Mercado \n'
                   '1 - Frutas \n'
                   '2 - Verduras \n'
                   '3 - Legumes \n '
                   '--------------------------------\n'
                   'Resp: '))
    return op


def saudacao(val):
    def ola(*args):
        val(*args)
        print('Ola, Bom dia')
        a = str(input('Posso Ajudar? '))
        if a.lower() == 'sim':
            opcoes()
        else:
            tchau()
    return ola


@saudacao
def resp():
    a = input('Type: ')
    return a


resp()

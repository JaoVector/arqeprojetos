# calculadora

def calc(a: float, b: float, funcao):
    return funcao(a, b)


def soma(a, b):
    return a + b


def mult(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


op = int(input('Digite uma das Opções \n'
               '1 - SOMA \n'
               '2 - Multiplicação\n'
               '3 - Subtraçao\n'
               '4 - Divisao\n'
               'Resp: '))

a = float(input('Digite Num1: '))
b = float(input('Digite Num2: '))
if op == 1:
    print(calc(a, b, soma))
elif op == 2:
    print(calc(a, b, mult))
elif op == 3:
    print(calc(a, b, sub))
elif op == 4:
    print(calc(a, b, div))


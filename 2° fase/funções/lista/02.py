import math
A = lambda a,b: a+b

S = lambda a,b: a-b

M = lambda a,b: a*b


def divisao(a,b):
    if b == 0:
        return 'Cálculo impossivel'
    else:
        result = a/b
        return result
    
P = lambda a,b: math.pow(a,b )

while True:
    print("-"*30)
    print('''Escolha uma opção:
          1 - Adicao
          2 - Subtração
          3 - Mutplicação
          4 - Divisão
          5 - Potenciação
          6 - Sair''')
    print("-"*30)
    resposta = int(input("Escolha uma opção: "))

    match resposta:
        case 1:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(A(a,b))
        case 2:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(S(a,b))
        case 3:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(M(a,b))
        case 4:
            a = float(input("Digite o Primeiro número: "))
            b = float(input("Digite o Segundo número: "))
            print(divisao(a,b))
        case 5:
            a = int(input("Digite o Primeiro número: "))
            b = int(input("Digite o Segundo número: "))
            print(P(a,b))
        case 6:
            print("Ja foi tarde")
            break
        case _:
            print("Opção inválida")
         
       
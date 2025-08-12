#15


lista = []
par = []
imapr = []
primo = []

while True:
    print("informações\n1-adicionar\n2-remover\n3-exibir\n4-somente par\n5-somente impares\n6-somente primos")
    op = int(input(" informe a sua opição: "))

    match op:
        case 1:
            num= int(input("informe um numero: "))
            lista.append(num)
            print(lista)
        case 2: 
            print("-----------ATENÇÃO------------")
            print("deseja excluir?\n1-numero")
            r = int(input("informe sua resposta: "))
            if r == 1:
                    lista.remove(num)
        case 3:
              print(lista)
        case 4: 
            if num % 2 == 0:
                par.append(num)
                print(par)
        case 5:
            if num % 2 == 1:
                par.append(imapr)
                print(imapr)
        case 6:
            print("Números primos na lista:")

            for n in lista:
                eh_primo = True
                if n <= 1:
                    eh_primo = False
                else:
                    for i in range(2, int(n**0.5) + 1):
                        if n % i == 0:
                            eh_primo = False
                            break
                if eh_primo:
                    print(n)
                   
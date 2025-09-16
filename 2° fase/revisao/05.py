#05


while True:
    nome = input("informe o nome do produto: ")
    quant = int(input("informe a quantidade: "))
    preco = float(input("informe o preço do produto: "))
    valor = preco*quant
    print(f"o valor final é de: {valor}")
    print("formas de pagamentos:\n1-dinheiro\n2-credito\n3-2x\n4-3x")
    op = int(input("informe a opção escolhida: "))

    match op:
        case 1:
            f = valor-valor*10/100
            print(f"o total a pagar em dinheiro é de: {f}")
        case 2:
            f = valor-valor*5/100
            print(f"o total a pagar no credito é de: {f}")
        case 3:
            f = valor/2
            print(f"o total a pagar em 2x é de: {f}")
        case 4:
            f = valor+valor*5/100
            f = valor/ 3
            print(f"o total a pagar em 3x é de: {f}")
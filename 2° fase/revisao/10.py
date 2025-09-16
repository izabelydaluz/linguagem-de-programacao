#10

litros = float(input("informe o numero de litros vendidos: "))
print("combustiveis:\nA-alcool\nG-gasolina")
op = input("informe sua opção de combustivel: ").upper

valor1 = litros*4.22
valor2 = litros*5.65


match op:
    case "A":
        if litros <= 20:
            valor1 = valor1-valor1*3/100
            print(f"total a pagar{valor1}")
        else:
            valor1 = valor1-valor1*5/100
            print(f"total a pagar{valor1}")

    case "B":
        if litros <= 20:
            valor2 = valor2-valor2*4/100
            print(f"total a pagar{valor2}")
        else:
            valor2 = valor2-valor2*6/100
            print(f"total a pagar{valor2}")
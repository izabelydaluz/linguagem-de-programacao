#12

nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))
valorp = float(input("informe o valor pago no plano: "))

if idade <= 18:
    valor = valorp+valorp*5/100
    print(f"o valor com o reajuste: {valor}")
if idade > 18 and idade<= 35:
    valor = valorp+valorp*10/100
    print(f"o valor com o reajuste: {valor}")
if idade > 36 and idade <= 60:
    valor = valorp+valorp*15/100
    print(f"o valor com o reajuste: {valor}")
if idade > 60:
    valor = valorp+valorp*20/100
    print(f"o valor com o reajuste: {valor}")




# 4.	Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("informe um valor:"))

if valor > 0:
    print(f"{valor} é positivo")

elif valor == 0:
    print(f"{valor} é igual a 0")

else:
    print(f"seu valor{valor} é negativo")
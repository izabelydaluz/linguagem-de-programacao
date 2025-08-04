# 3.	Faça um programa que peça dois números e imprima o maior deles.

valor1 =  float(input("informe o valor 1: "))
valor2 =  float(input("informe o valor 2: "))

if valor1 > valor2:
    print(f"o valor {valor1} é maior que o valor {valor2} valor.")

elif valor1 == valor2 :
    print(f"os valores {valor1} e {valor2} são iguais")

else:
    print(f"o valor{valor2} émaior que o valor {valor1}")

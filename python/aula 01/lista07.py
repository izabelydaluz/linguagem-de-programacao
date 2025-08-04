# 7.	Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento.

nome = (input("informe o nome do produto: "))
n1 = float(input("digite o preço do produto: "))

n2 = 5/100
result = n1*n2
valorfinal = n1 - result

print(f"o preço final do(a) {nome} com desconto é de:{valorfinal}  ")

n3 = 15/100
resul2 = valorfinal*n3 
valorfinal2 = resul2 + valorfinal 

print(f"o preço final do(a) {nome} com desconto é de:{valorfinal2}  ")

# 9.	Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.

nome = input("informe o seu nome:")

n1 = float(input("infome o valor em dinheiro para ser transformado em dolar e euro"))

valor01 = n1/5.41
valor02 = n1/6,58

print(f"o seu valor de: {n1} em dolar é: {valor01} e em euro é: {valor02}")
# Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles. 

lista = []
soma = 0

for v in range(5):
    num = int(input(f"informe o {v + 1}° numero: "))
    lista.append(num)
    soma = soma + num
print(f" seus numeros foram {lista}")
print(f" a soam entre eles é de {soma}")
# 2) Escrever um programa que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos.

lista = []
soma = 0

for v in range(10):
    num = (int(input("informe um numero: ")))
    lista.append(num)
    soma = num + soma
print(f"a soma de todos os numero é de : {soma}")

#mari: 
numeros = 0
cont = 0
while numeros< 10:
    num = (int(input("informe um numero: "))) 
    numeros += 1
    soma += num
print(f"a soma de todos os numeros é: {soma}")
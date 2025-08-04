# 3) Escreva um programa que leia 10 valores inteiros e encontre o maior e o menor deles.

lista = []


for v in range(4):
    num = (int(input("informe um numero: ")))
    lista.append(num)
    maior = max(lista)
    menor =min(lista)
print(maior , menor)

#mari: 

numeros = []
i =1

while(i <= 10):
    numero = int(input(f" informe seu numero {i + 1}° numero: "))
    numeros.append(numero)
    i += 1
print(f"seu valor maximo é {max(numeros)}")
print(f"seu valor minimo é {min(numeros)}")
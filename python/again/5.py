#  Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ímpares no vetor ÍMPAR. Imprima os três vetores. 

lista = []
par = []
impar = []

for v in range(4):
    num = int(input(f" informe o {v + 1}° numero: "))
    lista.append(num)
print(lista)
for num in lista:
   
   if num % 2 == 0 :
       par.append(num)
       print(f" o numero {num} é par")
else:
    impar.append(num)
    print(f"o numero {num} é impar")
#  Escreva um Programa que leia uma lista de 5 números inteiros e mostre-os. 

lista = []

for a in range(5):
 itens = int(input(f"informe o {a + 1}° numero:  "))
 lista.append(itens)
print(lista)
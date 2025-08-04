# Escreva um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa. 

lista = []

for v in range(3):
    num = int(input(f"informe o {v + 1}° numero: "))
    lista.insert(0, num)
print(lista)
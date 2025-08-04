# Escreve um Programa que leia uma lista com 5 itens,  contendo itens repetidos e mostre os itens repetidos.

lista = []
repetidos = []

for v in range(5):
    itens = input(f"informe o {v + 1}° item: ")
    lista.append(itens)
print(lista)

for item in lista:
    if lista.count(itens) > 1 and itens not in repetidos:
        repetidos.append(item)
        
print(f"sua lista: {lista}")
print(f"itens repetidos nela: {repetidos}")
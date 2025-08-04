
'''
carros = {"marca":"chevrolet", "modelo": "onix","ano": 2022}
print(carros)

print(carros["marca"]) #chevrolet
print(carros["modelo"]) #onix

print(carros.get("ano"))#2022 | puxa o valor da chave ano

print(carros.get("cor")) #None (objeto vazio)
#print(carros["cor"]) #erro

print(carros.get("cor", "chave não encontrada"))#resposta padrão caso não aja a chave especifica

print(carros.keys())# traz todas as chaves
print(carros.values())# traz todas os valores
print(carros.items())# retorna todas as chaves e valores



#adicionar novo item ao dicionario
carros["placa"] = "AQX1H54"
print(carros)

#remover um item
carros.pop("placa")#salva caso queira recuperar
print(carros)

del carros["ano"] #deleta para sempre
print(carros)

#verificando se a chave ou valor está no dicionario 
print("marca" in carros)#retorna um bool true caso a chave estiver, ou falso caso a chave não for encontrada

#verificar se determinado valor no dicionario
print("onix" in carros.values())

#iterando(percorendo) sobre um dicionario

#retorna as chaves do meu dicionario
for v in carros:
    print(v)

#retornas os valores
for v in carros.values():
    print(v)

for chave,valor in carros.items():
    print(f"{chave}: {valor}")'''

filmes = [
    {"nome" : "como treinar o seu dragão2", "genero": "fantasia"}, #0
    {"nome" : "por lugares incriveis", "genero": "romance"},       #1
    {"nome" : "o grito", "genero": "terror"}                       #2
]

print(filmes) # mostra a lista toda
print(filmes[0]) #mostra o dicionario inteiro
print(filmes[1]["nome"]) #mostra o valor especifico
print(filmes[1]["genero"])#mostra a chave especifico

print(filmes[2].keys()) #mostra as chaves do item 2
print(filmes[1].values()) #mostra os valores
print(filmes[0].items()) #mostras os 2 em tuplas
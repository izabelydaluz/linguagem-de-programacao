# Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 

idades = []
alturas = []

for v in  range(5):
    idade = int(input("inform sua idade:"))
    idades.append(idade)
    altura = float(input("informe sua altura: "))
    alturas.append(altura)

    media = sum(altura) / len(altura)
    quantidade = 0

for i in range(len(altura)):
    if idades[i] > 13 and alturas[i] < media :
        quantidade = quantidade+ 1

print(f" a media dos alunos é de: {media}")
print(f" a quantidades dos alunos inferiores é de: {quantidade}")